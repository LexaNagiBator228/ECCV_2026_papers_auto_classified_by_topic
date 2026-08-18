import json, re, os, csv, collections
S='/tmp/claude-1000/-home-oleksii-data-eccv-2026/28271e25-e72e-4cc9-ad92-a4f7cb85f073/scratchpad'
OUT='/home/oleksii/data/eccv_2026'
papers=json.load(open(S+'/papers_labeled.json'))

info=collections.defaultdict(dict)
def load(fn):
    p=os.path.join(S,fn)
    if not os.path.exists(p): return []
    rows=[]
    for line in open(p):
        try: rows.append(json.loads(line))
        except Exception: pass
    return rows

for r in load('links.jsonl'):
    i=r['i']
    if r.get('arxiv'): info[i]['arxiv']=r['arxiv']
    if r.get('doi'):   info[i]['doi']=r['doi']
    if r.get('landing'): info[i]['landing']=r['landing']
for r in load('arxiv_extra.jsonl'):
    i=r['i']
    if r.get('arxiv'):
        info[i]['arxiv']=r['arxiv']
        if r.get('summary'): info[i]['summary']=r['summary']
        if r.get('comment'): info[i]['comment']=r['comment']
abs_by_id={r['arxiv']:r for r in load('abstracts.jsonl')}
for i,d in info.items():
    if d.get('arxiv') and not d.get('summary'):
        a=abs_by_id.get(d['arxiv'])
        if a: d['summary']=a.get('summary',''); d['comment']=a.get('comment','')

URL=re.compile(r'https?://[^\s<>"\')\]}]+')
SKIP=re.compile(r'(arxiv\.org|doi\.org|creativecommons|wikipedia|youtube\.com/watch|paperswithcode)', re.I)
CODE=re.compile(r'(github\.com|gitlab\.com|huggingface\.co|bitbucket)', re.I)
def urls_from(d):
    text=' '.join([d.get('summary',''), d.get('comment','')])
    proj=[]; code=[]
    for m in URL.finditer(text):
        u=m.group(0).rstrip('.,;:)]}\'"')
        if SKIP.search(u): continue
        if len(u)<12: continue
        (code if CODE.search(u) else proj).append(u)
    def dedup(x):
        seen=set(); o=[]
        for u in x:
            k=u.rstrip('/').lower()
            if k not in seen: seen.add(k); o.append(u)
        return o
    return dedup(proj)[:2], dedup(code)[:1]

for i,d in info.items():
    p,c = urls_from(d)
    if p: d['project']=p
    if c: d['code']=c

GROUPS=[
 ("Generation & Editing", ["Image Generation & Diffusion Models","Video Generation & World Models",
   "3D Generation & Shape Modeling","Image & Video Editing"]),
 ("Multimodal, Language & Video Understanding", ["Multimodal LLMs & Vision-Language Models",
   "Video Understanding & Temporal Modeling","Retrieval & Cross-Modal Alignment","Document, OCR & Structured Text"]),
 ("3D, Geometry & Imaging", ["3D Reconstruction, Gaussian Splatting & NVS","Depth, Geometry, Matching & Camera Pose",
   "Point Cloud & 3D Perception","Computational Imaging & Novel Sensors","Low-Level Vision & Image Restoration"]),
 ("Recognition & Perception", ["Object Detection & Segmentation","Tracking & Correspondence over Time",
   "Anomaly & Out-of-Distribution Detection","Image Classification & Visual Recognition"]),
 ("Humans, Agents & Autonomy", ["Human Pose, Motion & Avatars","Face, Portrait & Identity",
   "Embodied AI, Robotics & Manipulation","Autonomous Driving"]),
 ("Learning, Efficiency & Trust", ["Representation & Self-Supervised Learning","Transfer, Adaptation & Continual Learning",
   "Efficiency, Compression & Acceleration","Trustworthy AI: Safety, Adversarial & Privacy",
   "Datasets, Benchmarks & Evaluation"]),
 ("Application Domains", ["Medical & Biomedical Imaging","Remote Sensing & Earth Observation",
   "Audio-Visual, Speech & Tactile Sensing"]),
 ("Unclassified", ["Other / Uncategorized"]),
]
by=collections.defaultdict(list)
for i,p in enumerate(papers):
    p['_i']=i; by[p['topic']].append(p)
for k in by: by[k].sort(key=lambda p:p['title'].lower())
def slug(s): return re.sub(r'[^a-z0-9]+','-',s.lower()).strip('-')

nlink=sum(1 for i in range(len(papers)) if info.get(i,{}).get('arxiv'))
nproj=sum(1 for i in range(len(papers)) if info.get(i,{}).get('project'))
ncode=sum(1 for i in range(len(papers)) if info.get(i,{}).get('code'))

def linkline(i):
    d=info.get(i,{}); parts=[]
    if d.get('arxiv'): parts.append(f"[arXiv:{d['arxiv']}](https://arxiv.org/abs/{d['arxiv']})")
    if d.get('code'): parts.append(f"[code]({d['code'][0]})")
    for u in d.get('project',[])[:2]: parts.append(f"[project]({u})")
    if not parts and d.get('doi'): parts.append(f"[doi]({d['doi']})")
    if not parts and d.get('landing'): parts.append(f"[page]({d['landing']})")
    return " · ".join(parts)

PICKS=[
 ("Vulnerability of Privacy-Preserving Visual Localization",
  "The other privacy-vs-localization paper at the venue: attacks that recover imagery from privacy-preserving map representations. Direct companion to #2 - same threat model, different defence target."),
 ("Seeing Through the Weights: Privacy Leakage in Scene Coordinate Regression",
  "An SCR network's weights alone leak the scene it was trained on, so privacy has to be reasoned about at the model level, not only at the map representation."),
 ("BLASt3R: Bundle Adjustment of Any Image Set",
  "Bundle adjustment over unordered image sets, combining multi-view matching with monocular priors - the learned-prior successor to a classic BA pipeline."),
 ("Stable and Scalable Bundle Adjustment of Holistic 3D Structures",
  "Numerical stability and scaling of BA on large holistic structures; relevant when pushing BA past the point where naive solvers degrade."),
 ("Geometry-Preserving in 3D Gaussian Splatting for LiDAR-Camera Extrinsic",
  "Targetless LiDAR-camera extrinsic calibration via a 3DGS geometry-preservation objective."),
 ("RoMa v2: Harder Better Faster Denser Feature Matching",
  "Second generation of the dense feature matcher - the current default front end for relative pose and localization. Code released."),
 ("UniPR-3D: Towards Universal Visual Place Recognition",
  "Visual place recognition on a VGGT-style geometry-grounded transformer, aiming at one VPR model across domains. Code released."),
 ("Learning Global Camera Poses from Noisy View-Graphs",
  "Global SfM rotation/translation averaging made robust to corrupted view-graphs - the failure mode that breaks classical global SfM."),
 ("General Self-Calibration with Varying Intrinsics",
  "Self-calibration when intrinsics drift across a sequence (zoom, autofocus, rolling shutter) instead of staying fixed."),
 ("GEO-Detective: Unveiling Location Privacy Risks in Images",
  "Agentic VLMs geolocating ordinary photos - the attacker-side counterpart to map-privacy work, and evidence that the threat surface now includes off-the-shelf models."),
]

def build_picks(md):
    md.append("## Recommended for you\n")
    md.append("Ten papers picked against an inferred profile: **visual localization and SLAM, "
              "structure-from-motion and bundle adjustment, camera and LiDAR-camera calibration, "
              "feature correspondence, and privacy of localization systems**. The profile was inferred "
              "from the datasets and working directories under `~/data` (nuScenes, Waymo, nuPlan, "
              "Oxford Radar RobotCar, 42dot, Nexar, plus calibration and bundle-adjustment dirs). "
              "Tell me if it is off and I will re-pick.\n")
    for rank,(key,why) in enumerate(PICKS,1):
        hit=None
        for i,p in enumerate(papers):
            if key.lower() in p['title'].lower(): hit=(i,p); break
        if not hit:
            md.append(f"{rank}. *(not found: {key})*\n"); continue
        i,p=hit
        ll=linkline(i)
        md.append(f"{rank}. **{p['title']}**  \n   {p['authors']}  \n   *{why}*  \n   "
                  f"`{p['topic']}`" + (f" - {ll}\n" if ll else " - no preprint found\n"))
    md.append("\n---\n")

md=["# ECCV 2026 Accepted Papers by Topic\n",
 f"**{len(papers)} papers** in {len(by)} topics. Links resolved automatically by title match "
 f"against arXiv and OpenAlex: **{nlink} arXiv preprints found ({100*nlink//len(papers)}%)**, "
 f"{nproj} project pages, {ncode} code repos. Papers with no link have no preprint I could find.\n",
]
md.append("## Contents\n")
for gname,topics in GROUPS:
    md.append(f"**{gname}**\n")
    for t in topics:
        k=sum(1 for p in by[t] if info.get(p['_i'],{}).get('arxiv'))
        md.append(f"- [{t}](#{slug(t)}) — {len(by[t])} ({k} linked)")
    md.append("")
md.append("\n---\n")
build_picks(md)
for gname,topics in GROUPS:
    md.append(f"\n# {gname}\n")
    for t in topics:
        k=sum(1 for p in by[t] if info.get(p['_i'],{}).get('arxiv'))
        md.append(f"\n## {t}\n\n*{len(by[t])} papers · {k} with links*\n")
        for n,p in enumerate(by[t],1):
            ll=linkline(p['_i'])
            md.append(f"{n}. **{p['title']}**  \n   {p['authors']}" + (f"  \n   {ll}" if ll else ""))
open(os.path.join(OUT,'papers_by_topic.md'),'w',encoding='utf-8').write("\n".join(md)+"\n")

tdir=os.path.join(OUT,'topics'); os.makedirs(tdir, exist_ok=True)
idx=0
for gname,topics in GROUPS:
    for t in topics:
        idx+=1
        with open(os.path.join(tdir,f"{idx:02d}_{slug(t)}.txt"),'w',encoding='utf-8') as f:
            k=sum(1 for p in by[t] if info.get(p['_i'],{}).get('arxiv'))
            f.write(f"{t}  ({len(by[t])} papers, {k} with arXiv links)  [{gname}]\n"+"="*76+"\n\n")
            for n,p in enumerate(by[t],1):
                d=info.get(p['_i'],{})
                f.write(f"{n}. {p['title']}\n   {p['authors']}\n")
                if d.get('arxiv'): f.write(f"   arXiv: https://arxiv.org/abs/{d['arxiv']}\n")
                if d.get('code'): f.write(f"   code:  {d['code'][0]}\n")
                for u in d.get('project',[])[:2]: f.write(f"   page:  {u}\n")
                if not d.get('arxiv') and d.get('doi'): f.write(f"   doi:   {d['doi']}\n")
                f.write("\n")

with open(os.path.join(OUT,'papers_by_topic.csv'),'w',newline='',encoding='utf-8') as f:
    w=csv.writer(f); w.writerow(['group','topic','title','authors','arxiv_url','code_url','project_url','doi'])
    for gname,topics in GROUPS:
        for t in topics:
            for p in by[t]:
                d=info.get(p['_i'],{})
                w.writerow([gname,t,p['title'],p['authors'],
                            f"https://arxiv.org/abs/{d['arxiv']}" if d.get('arxiv') else '',
                            (d.get('code') or [''])[0], (d.get('project') or [''])[0], d.get('doi','')])
print(f"papers={len(papers)} arxiv={nlink} project={nproj} code={ncode}")
