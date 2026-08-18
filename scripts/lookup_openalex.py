import json, re, os, sys, time, difflib, threading, queue
import urllib.request, urllib.parse, urllib.error

SCRATCH='/tmp/claude-1000/-home-oleksii-data-eccv-2026/28271e25-e72e-4cc9-ad92-a4f7cb85f073/scratchpad'
papers=json.load(open(SCRATCH+'/papers_labeled.json'))
OUTF=SCRATCH+'/links.jsonl'

done=set()
if os.path.exists(OUTF):
    for line in open(OUTF):
        try: done.add(json.loads(line)['i'])
        except Exception: pass

def norm(s):
    s=re.sub(r'&#x[0-9a-f]+;',' ',s)
    return re.sub(r'[^a-z0-9]+','',s.lower())

def clean_for_query(t):
    t=re.sub(r'&#x[0-9a-f]+;',' ',t)
    t=re.sub(r'[^\w\s-]',' ',t, flags=re.UNICODE)   # commas/colons break filter syntax
    return re.sub(r'\s+',' ',t).strip()

SEL='id,display_name,doi,publication_year,locations,primary_location,open_access'
def fetch(url, tries=4):
    for a in range(tries):
        try:
            req=urllib.request.Request(url, headers={'User-Agent':'eccv-topic-index/1.0'})
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read().decode())
        except urllib.error.HTTPError as e:
            if e.code in (429,500,502,503,504): time.sleep(2*(a+1)+1)
            else: return None
        except Exception:
            time.sleep(1.5*(a+1))
    return None

ARX=re.compile(r'arxiv\.org/abs/([0-9]{4}\.[0-9]{4,5}(v\d+)?)', re.I)
DOIARX=re.compile(r'10\.48550/arxiv\.([0-9]{4}\.[0-9]{4,5})', re.I)

def extract(work):
    arx=None; landing=None; pdf=None
    locs=[l for l in (work.get('locations') or []) if l]
    pl=work.get('primary_location') or {}
    if pl: locs=[pl]+locs
    for l in locs:
        u=l.get('landing_page_url') or ''
        m=ARX.search(u)
        if m and not arx: arx=m.group(1).split('v')[0]
        if not landing and u and 'arxiv.org' not in u: landing=u
        if not pdf and l.get('pdf_url'): pdf=l['pdf_url']
    doi=work.get('doi') or ''
    m=DOIARX.search(doi)
    if m and not arx: arx=m.group(1)
    if doi and '10.48550' in doi: doi=''
    return arx, doi, landing, pdf

q=queue.Queue()
for i,p in enumerate(papers):
    if i not in done: q.put((i,p))
lock=threading.Lock()
out=open(OUTF,'a',buffering=1)
counter={'n':0,'hit':0}

def worker():
    while True:
        try: i,p=q.get_nowait()
        except queue.Empty: return
        title=p['title']; cq=clean_for_query(title)
        rec={'i':i,'title':title,'arxiv':None,'doi':None,'landing':None,'pdf':None,'oa_title':None,'year':None}
        if len(cq)>3:
            url=('https://api.openalex.org/works?filter=title.search:'
                 +urllib.parse.quote(cq)+'&per-page=5&select='+SEL)
            d=fetch(url)
            best=None; bestr=0
            for w in (d or {}).get('results',[]):
                r=difflib.SequenceMatcher(None, norm(title), norm(w.get('display_name') or '')).ratio()
                if r>bestr: bestr, best = r, w
            if best and bestr>=0.92:
                a,doi,landing,pdf=extract(best)
                rec.update(arxiv=a, doi=doi or None, landing=landing, pdf=pdf,
                           oa_title=best.get('display_name'), year=best.get('publication_year'), ratio=round(bestr,3))
        with lock:
            out.write(json.dumps(rec, ensure_ascii=False)+'\n')
            counter['n']+=1
            if rec['arxiv'] or rec['doi'] or rec['landing']: counter['hit']+=1
            if counter['n']%200==0:
                print(f"{counter['n']} done, {counter['hit']} matched", flush=True)
        time.sleep(0.12)

ths=[threading.Thread(target=worker,daemon=True) for _ in range(6)]
[t.start() for t in ths]; [t.join() for t in ths]
print("FINISHED", counter, flush=True)
