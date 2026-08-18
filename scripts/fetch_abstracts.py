"""Fetch arXiv abstracts+comments for matched IDs; extract project/code page URLs."""
import json, re, os, time, urllib.request, urllib.parse
S='/tmp/claude-1000/-home-oleksii-data-eccv-2026/28271e25-e72e-4cc9-ad92-a4f7cb85f073/scratchpad'
ids={}
for fn in ('links.jsonl','arxiv_extra.jsonl'):
    p=os.path.join(S,fn)
    if not os.path.exists(p): continue
    for line in open(p):
        try: r=json.loads(line)
        except Exception: continue
        if r.get('arxiv'): ids[r['i']]=r['arxiv']
have={}
OUT=S+'/abstracts.jsonl'
if os.path.exists(OUT):
    for line in open(OUT):
        try: have[json.loads(line)['arxiv']]=1
        except Exception: pass
todo=sorted({a for a in ids.values() if a not in have})
print("abstracts to fetch:", len(todo), flush=True)
out=open(OUT,'a',buffering=1)
ENTRY=re.compile(r'<entry>(.*?)</entry>', re.S)
B=100
for b in range(0,len(todo),B):
    batch=todo[b:b+B]
    url='https://export.arxiv.org/api/query?id_list='+','.join(batch)+'&max_results=%d'%len(batch)
    xml=''
    for a in range(3):
        try:
            req=urllib.request.Request(url, headers={'User-Agent':'eccv-topic-index/1.0'})
            xml=urllib.request.urlopen(req, timeout=60).read().decode('utf-8','replace'); break
        except Exception: time.sleep(5*(a+1))
    for m in ENTRY.finditer(xml):
        blk=m.group(1)
        idm=re.search(r'<id>http://arxiv\.org/abs/([^<]+)</id>', blk)
        if not idm: continue
        aid=idm.group(1).split('v')[0]
        su=re.search(r'<summary>(.*?)</summary>', blk, re.S)
        co=re.search(r'<arxiv:comment[^>]*>(.*?)</arxiv:comment>', blk, re.S)
        out.write(json.dumps({'arxiv':aid,
            'summary':re.sub(r'\s+',' ',su.group(1)).strip() if su else '',
            'comment':re.sub(r'\s+',' ',co.group(1)).strip() if co else ''}, ensure_ascii=False)+'\n')
    print(f"batch {b//B+1}/{(len(todo)+B-1)//B}", flush=True)
    time.sleep(3.1)
print("DONE", flush=True)
