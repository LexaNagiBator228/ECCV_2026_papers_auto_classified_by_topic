"""Fallback: query arXiv API (OR-batched) for papers OpenAlex didn't match."""
import json, re, os, time, difflib, urllib.request, urllib.parse
S='/tmp/claude-1000/-home-oleksii-data-eccv-2026/28271e25-e72e-4cc9-ad92-a4f7cb85f073/scratchpad'
papers=json.load(open(S+'/papers_labeled.json'))
links={}
for line in open(S+'/links.jsonl'):
    try:
        r=json.loads(line); links[r['i']]=r
    except Exception: pass

def norm(s):
    s=re.sub(r'&#x[0-9a-f]+;',' ',s)
    return re.sub(r'[^a-z0-9]+','',s.lower())

misses=[i for i,p in enumerate(papers) if not (links.get(i) or {}).get('arxiv')]
print("misses to retry:", len(misses), flush=True)

def qterm(title):
    t=re.sub(r'&#x[0-9a-f]+;',' ',title)
    head=t.split(':')[0].strip()
    # use distinctive method name if short & tokenful, else first 8 words of full title
    words=re.findall(r"[A-Za-z0-9][A-Za-z0-9\-]*", head)
    if 1<=len(words)<=4 and any(len(w)>3 for w in words):
        cand=' '.join(words)
    else:
        cand=' '.join(re.findall(r"[A-Za-z0-9][A-Za-z0-9\-]*", t)[:9])
    return cand.replace('"','')

OUT=S+'/arxiv_extra.jsonl'
done=set()
if os.path.exists(OUT):
    for line in open(OUT):
        try: done.add(json.loads(line)['i'])
        except Exception: pass
todo=[i for i in misses if i not in done]
out=open(OUT,'a',buffering=1)
B=12
ENTRY=re.compile(r'<entry>(.*?)</entry>', re.S)
TIT=re.compile(r'<title>(.*?)</title>', re.S)
IDR=re.compile(r'<id>http://arxiv\.org/abs/([^<]+)</id>')

for b in range(0,len(todo),B):
    batch=todo[b:b+B]
    q=' OR '.join('ti:"%s"'%qterm(papers[i]['title']) for i in batch)
    url='https://export.arxiv.org/api/query?search_query='+urllib.parse.quote(q)+'&max_results=80'
    xml=''
    for a in range(3):
        try:
            req=urllib.request.Request(url, headers={'User-Agent':'eccv-topic-index/1.0'})
            xml=urllib.request.urlopen(req, timeout=45).read().decode('utf-8','replace'); break
        except Exception as e:
            time.sleep(4*(a+1))
    cands=[]
    for m in ENTRY.finditer(xml):
        blk=m.group(1)
        t=TIT.search(blk); idm=IDR.search(blk)
        if t and idm:
            cands.append((re.sub(r'\s+',' ',t.group(1)).strip(), idm.group(1).split('v')[0], blk))
    for i in batch:
        best=None; br=0
        nt=norm(papers[i]['title'])
        for t,aid,blk in cands:
            r=difflib.SequenceMatcher(None, nt, norm(t)).ratio()
            if r>br: br,best=r,(t,aid,blk)
        rec={'i':i,'arxiv':None,'ratio':round(br,3)}
        if best and br>=0.92:
            rec['arxiv']=best[1]; rec['arxiv_title']=best[0]
            su=re.search(r'<summary>(.*?)</summary>', best[2], re.S)
            if su: rec['summary']=re.sub(r'\s+',' ',su.group(1)).strip()
            co=re.search(r'<arxiv:comment[^>]*>(.*?)</arxiv:comment>', best[2], re.S)
            if co: rec['comment']=re.sub(r'\s+',' ',co.group(1)).strip()
        out.write(json.dumps(rec, ensure_ascii=False)+'\n')
    print(f"batch {b//B+1}/{(len(todo)+B-1)//B}", flush=True)
    time.sleep(3.1)
print("DONE", flush=True)
