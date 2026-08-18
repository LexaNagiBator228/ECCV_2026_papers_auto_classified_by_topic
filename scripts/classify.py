import json, re, collections
SCRATCH='/tmp/claude-1000/-home-oleksii-data-eccv-2026/28271e25-e72e-4cc9-ad92-a4f7cb85f073/scratchpad'
papers=json.load(open(SCRATCH+'/papers.json'))

TOPICS = [
("Medical & Biomedical Imaging", [
 (r"\bmedical|biomedic|clinical|radiolog|patholog|histolog|\bct\b|\bmri\b|\bfmri\b|x-?ray|ultrasound|endoscop|colonoscop|surg(ery|ical)|tumou?r|lesion|cancer|diagnos|\bwsi\b|whole[- ]slide|retina|fundus|dental|cardiac|electron microscop|microscop|cytolog|polyp|immunohisto|immunostain|staining|nuclei|anatom|patient|disease|prosthe|dermat|blood|protein|molecul|\bdrug\b|\bgene\b|physiolog|\bppg\b|photoplethysmog|\bspo2\b|survival analysis|multiple instance learning|\bmil\b|cell (segmentation|detection|counting|nuclei)|health|gait behavior|biopsy|\becg\b|\beeg\b|brain (decod|signal|activity)|neural decoding", 6),
]),
("Remote Sensing & Earth Observation", [
 (r"remote sensing|satellit|aerial|earth observ|geospatial|multispectral|hyperspectral|\bsar\b|land ?cover|\bcrop\b|agricultur|forest|cadastr|orthophoto|\buav\b|drone|climate|weather|flood|wildfire|precipitation|ionospher|disaster|landslide|facade|building damage|cloud removal|change detection|geo-?contextual|tesselating the earth|plant growth|wildlife", 6),
]),
("Document, OCR & Structured Text", [
 (r"\bocr\b|document (understanding|analysis|parsing|image|layout|ai|generation)|text recognition|scene text|handwrit|table (recognition|structure|understanding|parsing)|chart (understanding|question|reasoning|to)|\bpdf\b|typograph|\bfont\b|layout (analysis|estimation|design|generation)|form understanding|receipt|invoice|formula recognition|slide generation|diagram parsing|graphic (layout|design)|vector graphics|in-image machine translation|tabular", 6),
]),
("Audio-Visual, Speech & Tactile Sensing", [
 (r"\baudio|speech|\bsound\b|music|voice|acoustic|lip[- ]sync|singing|speaker|\basr\b|talking (head|face|portrait)|olfactory|tactile|visuo-?tactile|haptic|mmwave|\brf\b sensing", 6),
]),
("Trustworthy AI: Safety, Adversarial & Privacy", [
 (r"adversarial (attack|example|robust|perturbation|patch|training|defen[cs]e|regulariz|reconstruction|flow)|\battack|\bbackdoor|poison|jailbreak|watermark|deepfake|forgery|face swap|anti[- ]spoof|privacy|private|federated|unlearn|membership inference|copyright|\bnsfw\b|harmful|toxic|safety|guardrail|red[- ]team|fairness|debias|social bias|stereotyp|censor|content moderation|provenance|tamper|hallucinat|trustworth|misinformation|fact[- ]check|forensic|concept (erasure|erasing)|erasing|model stealing|encoder stealing|differentially private|verification|certif|counterfactual", 5),
 (r"interpretab|explainab|\bxai\b|saliency map|concept (bottleneck|circuit)|sparse autoencoder|mechanistic|probing|uncertainty|calibrat|conformal|attribution|evidential|reliab", 4),
]),
("Anomaly & Out-of-Distribution Detection", [
 (r"anomal|out[- ]of[- ]distribution|\bood\b|novelty detection|open[- ]set recognition|defect|outlier|industrial inspection|corrupt", 6),
]),
("Autonomous Driving", [
 (r"autonomous driving|self[- ]driving|\bdriving\b|\bdriver\b|\bbev\b|bird'?s[- ]eye|occupancy (prediction|forecast|network|grid|space)|traffic|\blane\b|vehicle|\bnuscenes|waymo|carla|motion (forecast|planning)|trajectory (prediction|forecast)|\broad\b|intersection|\bv2x\b|collaborative perception|end[- ]to[- ]end driving|vectorized map|\bhd map|map construction|prediction and planning|scenario generation|street", 6),
]),
("Embodied AI, Robotics & Manipulation", [
 (r"robot|manipulat(ion|or) policy|\bvla\b|vision[- ]language[- ]action|embodied|navigation|\bvln\b|grasp|dexterous|end[- ]effector|sim[- ]?to[- ]?real|sim2real|imitation learning|visuomotor|(policy|action) learning|(visuomotor|manipulation|robot) policy|affordance|household|tabletop|locomot|humanoid|teleoper|instruction following|world[- ]action model|planning|agentic|\bagent(s)?\b|\bgui\b|computer use|web agent|tool use", 5),
 (r"reinforcement learning|\brl\b|reward (model|design|shaping)|\bpolicy\b|planning", 3),
]),
("Human Pose, Motion & Avatars", [
 (r"human (pose|mesh|motion|body|avatar|reconstruct|parsing|-object|centric|animation|sensing|prediction|activity|scene)|\bsmpl|\bpose estimation|3d human|motion (generation|synthesis|capture|prior|diffusion|understanding|representation|transfer)|avatar|hand (pose|mesh|object|reconstruct|interaction)|body (mesh|shape|model|proportion)|gesture|\bdance\b|garment|cloth(ing|ed)\b|try[- ]on|gaze|scanpath|eye tracking|action quality|sign language|\bhoi\b|human[- ]object interaction|character animation|skeleton|keypoint|person re[- ]?id|pedestrian|crowd (counting|simulation)|dyadic|social motion|proficiency|skill determination|wearable motion|\bnphm\b|animal (motion|reconstruction)|ego[- ]?exo|human[–-]scene interaction|human videos|humans and objects|fashion", 6),
]),
("Face, Portrait & Identity", [
 (r"\bface\b|\bfaces\b|facial|portrait|head (avatar|reconstruction)|expression recognition|face recognition|identity[- ]preserv|makeup|\bid[- ]preserv|emotion recognition|biometric", 6),
]),
("3D Reconstruction, Gaussian Splatting & NVS", [
 (r"gaussian splat|\bsplat|\b[234]dgs\b|gaussian(s)? (primitive|representation|field|reconstruction|head|volumetric|digital)|\bgaussians\b|\bnerf\b|neural radiance|radiance field|novel view|view synthesis|surface reconstruction|multi[- ]view stereo|\bmvs\b|structure[- ]from[- ]motion|\bsfm\b|photogrammetr|\bsdf\b|isosurface|implicit surface|mesh reconstruction|3d reconstruction|feed[- ]?forward (3d|recon|geometry)|scene (reconstruction|completion|modeling)|neural rendering|differentiable render|relight|inverse rendering|ray tracing|rasteriz|path tracing|\bslam\b|\bnvs\b|light field|reflectance|\bbrdf\b|material (estimation|feature|transfer)|albedo|intrinsic (decomposition|image)|illumination|texturing|neural (field|texture)|implicit neural representation|\binr(s)?\b|4d reconstruction|dynamic (scene|3d|reconstruction)|panoram|omnidirectional|360|volumetric|world reconstruction|geometry (regeneration|transformer|prediction)|active reconstruction|digital twin|tomograph|scene representation|\brendering\b|reconstruct|triplane|non[- ]line[- ]of[- ]sight|\bnlos\b|remesh|mesh (deformation|topology)|physics[- ](informed|in[- ]the[- ]loop|based)|simulation|scene kinematics|environment reconstruction|visibility", 6),
]),
("3D Generation & Shape Modeling", [
 (r"text[- ]to[- ]3d|image[- ]to[- ]3d|3d (generation|generative|asset|shape|content creation|synthesis|modeling|scene generation|coheren)|shape (generation|analysis|correspondence|matching|evolution)|mesh generation|texture (generation|synthesis)|\bcad\b|\bbrep\b|part[- ]level|articulat|procedural|scene (generation|synthesis)|geometry generation|uv map|world generation|amodal 3d|layout estimation|room layout|topological|4d (synthesis|generation|world)", 6),
]),
("Point Cloud & 3D Perception", [
 (r"point cloud|\blidar\b|\bvoxel|3d object detection|3d (detection|segmentation|semantic|classification|question answering|scene graph)|registration|scan(net)?\b|3d perception|sparse convolution|range image|point transformer|\bpoint(s)? (feature|based|rendering)", 6),
]),
("Depth, Geometry, Matching & Camera Pose", [
 (r"depth (estimation|completion|prediction|map|prior|from|ordering|modeling|alignment)|monocular depth|stereo|disparit|optical flow|scene flow|camera (pose|calibration|localization|control|parameter|intrinsic|movement|display)|visual (localization|place recognition)|relocaliz|geo[- ]?local|feature (matching|descriptor)|image (matching|stitching|warping)|correspondenc|homograph|epipolar|\bpnp\b|bundle adjust|metric (depth|geometry)|geometric (foundation|estimation|prior|consensus|misalignment)|6d(of)? pose|object pose|rolling[- ]shutter|fisheye|visual geometry|point-line|local features|dense prediction|spatial (perception|awareness|understanding|intelligence|supersensing|tuning)|geometry[- ]aware|geo-?locat|geolocaliz|cross[- ]view (local|geo)|\blocalization\b|dense (semantic )?matching", 6),
]),
("Object Detection & Segmentation", [
 (r"object detection|segmentation|segment anything|instance segment|semantic segment|panoptic|open[- ]vocabular|referring (expression|segmentation)|matting|camouflag|salient object", 6),
 (r"\bdetection\b|detect(or|ing|ors)\b|segment(ing|er)\b|\bsam\b|salien(t|cy)|counting|scene graph|object[- ]centric|\bentity\b|region (token|proposal)|bounding box|\bmask\b|amodal|dense prediction", 3),
]),
("Video Understanding & Temporal Modeling", [
 (r"video (understanding|question|reasoning|captioning|retrieval|summar|analysis|recognition|classification|segmentation|grounding|temporal|moment|anomaly|highlight|instance|dynamics|intelligence|motion|composition|tokeniz|dense)|action (recognition|detection|localization|segmentation|anticipation|understanding|binding|centric)|temporal (grounding|localization|action|sentence|reasoning|edits|memory|compositional)|moment retrieval|long[- ]form video|egocentric|first[- ]person|movie|streaming video|video[- ]language|video ?llm|activity (recognition|understanding)|instructional video|spatio-?temporal|frame querying|\bvideoqa\b|key frame", 6),
]),
("Tracking & Correspondence over Time", [
 (r"\btracking\b|\btracker\b|multi[- ]object tracking|\bmot\b|point tracking|track any|re[- ]identification|\bsot\b|visual tracking", 6),
]),
("Video Generation & World Models", [
 (r"video (generation|generative|synthesis|diffusion|creation|editing|inpaint|interpolation|prediction|dubbing|control|effect|game)|text[- ]to[- ]video|image[- ]to[- ]video|world model|world (simulat|explor|aware|knowledge)|video[- ]to[- ]video|animat(e|ion|ing)|long video|frame interpolation|\bi2v\b|\bt2v\b|storyboard|storytell|cinemat|film generation|motion transfer|narrative|4d (world|scene)|interactive world|dynamic world", 6),
]),
("Image Generation & Diffusion Models", [
 (r"diffusion|flow matching|rectified flow|normalizing flow|text[- ]to[- ]image|\bt2i\b|image (generation|synthesis|fitting|translation)|\bgan\b|generative (model|adversarial|prior|perception|refinement|ode|synthesis)|autoregressive (generation|image|visual|model|token|prediction)|visual autoregressive|\bvar\b|sampling|classifier[- ]free guidance|\bcfg\b|denoising|noise (schedul|inversion|generation|driven)|latent (diffusion|space|spectral|fusion|decoding|normalizing)|personaliz|subject[- ]driven|concept (learning|customiz|weav|inferring)|dreambooth|controlnet|\blora(s)?\b|customiz|layout[- ]to[- ]image|conditional generation|\bvae(s)?\b|tokenizer|discrete token|masked generative|score[- ]based|consistency model|few[- ]step|one[- ]step generat|compositional generation|visual (generation|synthesis)|multi[- ]instance generation|aesthetic|style[- ]driven|diffusab|\bode\b sampling|flow (model|ensemble|forcing)|\bguidance\b|vectoriz|disentangled concept|synthetic data generation|high[- ]dimensional latent", 5),
]),
("Image & Video Editing", [
 (r"\bediting\b|\bedit(s)?\b|inpaint|outpaint|style transfer|styliz|composit|harmoniz|colori[sz]|drag|instruct(ion)?[- ]based edit|object (removal|insertion|deletion)|virtual try[- ]on|attribute (manipulation|control|token)|semantic control|image[- ]to[- ]image translation|layer(ed|-aware)? (composition|edit)|recapture", 6),
]),
("Multimodal LLMs & Vision-Language Models", [
 (r"\bmllm|\blvlm|\bvlm(s)?\b|\blmm(s)?\b|multimodal large language|large (multimodal|vision[- ]language)|vision[- ]language (model|fusion|alignment|encoder|concept)|\bclip\b|\bllm(s)?\b|large language model|visual instruction|multimodal (reasoning|understanding|model|alignment|learning|network|causality|perception)|chain[- ]of[- ]thought|\bcot\b|visual (reasoning|question answering|thought|reflection|rationale|prompt|analogy|concept|instruction)|\bvqa\b|question answering|captioning|\bcaption|visual token|instruction tuning|in[- ]context learning|prompt (learning|tuning|engineering|discovery)", 6),
 (r"preference (optimization|alignment)|\bdpo\b|\brlhf\b|\bgrpo\b|policy optimization|token (compression|scheduling|selection|arithmetic)|grounding|referring|reasoning|thinking|multi[- ]modal|cross[- ]modal|vision[- ]centric|long[- ]context|language[- ]guided|text[- ]aligned|semantic (flow|relation)", 3),
]),
("Retrieval & Cross-Modal Alignment", [
 (r"\bretrieval\b|re-?ranking|composed image retrieval|text[- ]image (matching|alignment|retrieval)|cross[- ]modal retrieval|image[- ]text (matching|retrieval)|\bcbir\b|universal (embedding|multimodal embedding)|multimodal embedding", 6),
 (r"embedding (space|alignment|field)|representation alignment|optimal transport|semantic alignment", 3),
]),
("Low-Level Vision & Image Restoration", [
 (r"super[- ]resolution|denois|deblur|dehaz|derain|desnow|restoration|enhancement|low[- ]light|underwater|\bhdr\b|tone mapping|demosaic|\bisp\b|\braw\b|image (quality|compression|coding|fusion)|video (compression|coding)|\bcodec\b|neural compression|feature (compression|coding)|artifact removal|jpeg|shadow removal|reflection removal|specular|derain|image signal process|exposure|noise (model|synthesis|generation)|burst|quality assessment|\bmoir|demoir|turbulence|color constancy|chromaticity|white balance|multi[- ]focus|ultra[- ]high[- ]definition|lookup table|bitrate|deconvolution|frequency (decomposition|adaptive|aware)|spectral (reconstruction|imaging)", 6),
 (r"high[- ]resolution|upsampling|\bfusion\b|sharpen", 3),
]),
("Computational Imaging & Novel Sensors", [
 (r"event(-based)? camera|\bevent(s)?\b|spike (camera|modulated)|polariz|photometric stereo|snapshot spectral|lensless|diffuser|structured light|wavefront|interferometry|schlieren|computational (photograph|imaging|mirror)|light transport|\bpsf\b|optics|\blens\b|sensor|in-sensor|imaging system|mueller matrix|neuromorphic|time[- ]of[- ]flight|\btof\b|thermal|infrared|depth from focus|shear[- ]warp|field of view", 6),
]),
("Efficiency, Compression & Acceleration", [
 (r"quantiz|pruning|\bprune|\bkv[- ]cache|knowledge distillation|\bnas\b|neural architecture search|token (merging|reduction|pruning|sparsif)|sparse attention|linear attention|\bmoe\b|mixture[- ]of[- ]experts|memory[- ]efficient|binariz|\bfp8\b|\bint[48]\b|bit[- ]width|low[- ]bitrate|early exit|parameter[- ]efficient|speculative|constant[- ]cost|on[- ]device|edge (device|deploy)|\bmobile\b|acceleration", 6),
 (r"distill|accelerat|lightweight|efficien(t|cy)|low[- ]rank|latency|throughput|real[- ]time|caching|\bfps\b|\bfast\b|scalab|compact|streaming", 3),
]),
("Transfer, Adaptation & Continual Learning", [
 (r"domain (adaptation|generalization|shift|incremental)|test[- ]time (adaptation|training|scaling|augment|geometric)|\btta\b|continual|incremental learning|catastrophic forgetting|lifelong|few[- ]shot|zero[- ]shot|one[- ]shot|meta[- ]learning|transfer learning|fine[- ]tuning|tuning[- ]free|training[- ]free|\bpeft\b|adapter|source[- ]free|unsupervised (adaptation|learning)|semi[- ]supervised|weakly[- ]supervised|self[- ]training|active learning|label[- ]efficient|nois(y|e) label|long[- ]tail|class[- ]imbalance|open[- ]world|generalizab|model (merging|soup)|task arithmetic|dataset (distillation|condens)|data (selection|pruning|curation|augmentation|synthesis|engine|scaling)|partial label|positive[- ]unlabeled|multi[- ]task|missing modalit|covariate shift|category discovery|synthetic[- ]to[- ]real|online adaptation", 5),
 (r"robustness|\brobust\b|distribution shift", 2),
]),
("Representation & Self-Supervised Learning", [
 (r"self[- ]supervis|\bssl\b|contrastive|masked (image|autoencoder|modeling)|\bmae\b|pre[- ]?train|foundation model|representation learning|\bdino|scaling law|jepa|joint[- ]embedding|state space|\bmamba\b|backbone|visual (encoder|encoding|representation)|positional (encoding|embedding)|equivarian|invarian|generalization bound|neural architecture|position(al)? embedding|scale[- ]space|shortcut|error slice|patch (detail|token)", 6),
 (r"representation (transformation|alignment)|feature (learning|extractor|upsampling|space)|emergent|unified (model|framework|architecture|representation|encoding)|architecture|transformer|attention (mechanism|distribution|control)|normalization|optimizer|loss (function|design)|training dynamics|theoretical|manifold|riemannian|clustering|graph neural|\bcnn(s)?\b|\bvit(s)?\b|\bmlp\b|convolution|neural network|deep (network|learning)|slot attention|\blatent\b", 2),
]),
("Image Classification & Visual Recognition", [
 (r"image classification|\bclassification\b|classifier|categoris|categoriz|fine[- ]grained (classification|recognition|visual)|multi[- ]label|metric learning|visual recognition|\brecognition\b", 6),
]),
("Datasets, Benchmarks & Evaluation", [
 (r"benchmark|\bdataset(s)?\b|\bevaluat|\bmetric(s)?\b|\beval\b|test suite|leaderboard|survey|empirical study|analysis of|revisit|rethink|study\b|challenge\b|competition|human (study|level)|user study|annotation|\bbench\b", 4),
]),
]

COMPILED=[(t,[(re.compile(p, re.I), w) for p,w in pats]) for t,pats in TOPICS]

def classify(title):
    scores=[]
    for i,(topic,pats) in enumerate(COMPILED):
        s=0
        for rx,w in pats:
            m=rx.findall(title)
            if m: s += w + (len(m)-1)*0.5
        if s: scores.append((s, -i, topic))
    if not scores: return "Other / Uncategorized", 0
    scores.sort(reverse=True)
    return scores[0][2], round(scores[0][0],1)

out=collections.defaultdict(list)
for p in papers:
    t,s = classify(p['title'])
    p['topic']=t; p['score']=s
    out[t].append(p)
json.dump(papers, open(SCRATCH+'/papers_labeled.json','w'), ensure_ascii=False, indent=0)
order=[t for t,_ in TOPICS]+["Other / Uncategorized"]
for t in order: print(f"{len(out[t]):5d}  {t}")
print("TOTAL", sum(len(v) for v in out.values()))
