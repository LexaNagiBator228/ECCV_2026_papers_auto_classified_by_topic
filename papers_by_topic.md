# ECCV 2026 Accepted Papers by Topic

**2864 papers** in 30 topics. Links resolved automatically by title match against arXiv and OpenAlex: **1725 arXiv preprints found (60%)**, 489 project pages, 406 code repos. Papers with no link have no preprint I could find.

## Contents

**Generation & Editing**

- [Image Generation & Diffusion Models](#image-generation-diffusion-models) — 178 (114 linked)
- [Video Generation & World Models](#video-generation-world-models) — 131 (89 linked)
- [3D Generation & Shape Modeling](#3d-generation-shape-modeling) — 49 (37 linked)
- [Image & Video Editing](#image-video-editing) — 88 (51 linked)

**Multimodal, Language & Video Understanding**

- [Multimodal LLMs & Vision-Language Models](#multimodal-llms-vision-language-models) — 283 (174 linked)
- [Video Understanding & Temporal Modeling](#video-understanding-temporal-modeling) — 104 (59 linked)
- [Retrieval & Cross-Modal Alignment](#retrieval-cross-modal-alignment) — 18 (12 linked)
- [Document, OCR & Structured Text](#document-ocr-structured-text) — 33 (19 linked)

**3D, Geometry & Imaging**

- [3D Reconstruction, Gaussian Splatting & NVS](#3d-reconstruction-gaussian-splatting-nvs) — 313 (178 linked)
- [Depth, Geometry, Matching & Camera Pose](#depth-geometry-matching-camera-pose) — 129 (86 linked)
- [Point Cloud & 3D Perception](#point-cloud-3d-perception) — 57 (31 linked)
- [Computational Imaging & Novel Sensors](#computational-imaging-novel-sensors) — 27 (8 linked)
- [Low-Level Vision & Image Restoration](#low-level-vision-image-restoration) — 100 (63 linked)

**Recognition & Perception**

- [Object Detection & Segmentation](#object-detection-segmentation) — 150 (85 linked)
- [Tracking & Correspondence over Time](#tracking-correspondence-over-time) — 31 (13 linked)
- [Anomaly & Out-of-Distribution Detection](#anomaly-out-of-distribution-detection) — 52 (27 linked)
- [Image Classification & Visual Recognition](#image-classification-visual-recognition) — 15 (8 linked)

**Humans, Agents & Autonomy**

- [Human Pose, Motion & Avatars](#human-pose-motion-avatars) — 181 (102 linked)
- [Face, Portrait & Identity](#face-portrait-identity) — 38 (16 linked)
- [Embodied AI, Robotics & Manipulation](#embodied-ai-robotics-manipulation) — 148 (99 linked)
- [Autonomous Driving](#autonomous-driving) — 81 (57 linked)

**Learning, Efficiency & Trust**

- [Representation & Self-Supervised Learning](#representation-self-supervised-learning) — 82 (53 linked)
- [Transfer, Adaptation & Continual Learning](#transfer-adaptation-continual-learning) — 80 (44 linked)
- [Efficiency, Compression & Acceleration](#efficiency-compression-acceleration) — 103 (62 linked)
- [Trustworthy AI: Safety, Adversarial & Privacy](#trustworthy-ai-safety-adversarial-privacy) — 89 (44 linked)
- [Datasets, Benchmarks & Evaluation](#datasets-benchmarks-evaluation) — 36 (26 linked)

**Application Domains**

- [Medical & Biomedical Imaging](#medical-biomedical-imaging) — 111 (62 linked)
- [Remote Sensing & Earth Observation](#remote-sensing-earth-observation) — 74 (40 linked)
- [Audio-Visual, Speech & Tactile Sensing](#audio-visual-speech-tactile-sensing) — 57 (46 linked)

**Unclassified**

- [Other / Uncategorized](#other-uncategorized) — 26 (20 linked)


---

## Recommended for you

Ten papers picked against an inferred profile: **visual localization and SLAM, structure-from-motion and bundle adjustment, camera and LiDAR-camera calibration, feature correspondence, and privacy of localization systems**. The profile was inferred from the datasets and working directories under `~/data` (nuScenes, Waymo, nuPlan, Oxford Radar RobotCar, 42dot, Nexar, plus calibration and bundle-adjustment dirs). Tell me if it is off and I will re-pick.

1. **Vulnerability of Privacy-Preserving Visual Localization against Diffusion-based Attacks**  
   Maxime Pietrantoni ⋅ Torsten Sattler ⋅ Gabriela Csurka  
   *The other privacy-vs-localization paper at the venue: attacks that recover imagery from privacy-preserving map representations. Direct companion to #2 - same threat model, different defence target.*  
   `Depth, Geometry, Matching & Camera Pose` - no preprint found

2. **Seeing Through the Weights: Privacy Leakage in Scene Coordinate Regression**  
   Oleksii Nasypanyi ⋅ Jaemin Cho ⋅ Utku Ozbulak ⋅ Byungkon Kang ⋅ Francois Rameau  
   *An SCR network's weights alone leak the scene it was trained on, so privacy has to be reasoned about at the model level, not only at the map representation.*  
   `Trustworthy AI: Safety, Adversarial & Privacy` - [arXiv:2606.31164](https://arxiv.org/abs/2606.31164) · [project](https://jaeminch0.github.io/seeing-through-the-weights-privacy-leakage-in-scene-coordinate-regression)

3. **BLASt3R: Bundle Adjustment of Any Image Set with Multi-View Matching and Monocular priors**  
   Vincent Leroy ⋅ Philippe Weinzaepfel ⋅ Lojze Zust ⋅ Yohann Cabon ⋅ Jerome Revaud  
   *Bundle adjustment over unordered image sets, combining multi-view matching with monocular priors - the learned-prior successor to a classic BA pipeline.*  
   `Depth, Geometry, Matching & Camera Pose` - no preprint found

4. **Stable and Scalable Bundle Adjustment of Holistic 3D Structures**  
   Shaohui Liu ⋅ Rémi Pautrat ⋅ Daniel Barath ⋅ Richard Hartley ⋅ Viktor Larsson ⋅ Marc Pollefeys  
   *Numerical stability and scaling of BA on large holistic structures; relevant when pushing BA past the point where naive solvers degrade.*  
   `Depth, Geometry, Matching & Camera Pose` - no preprint found

5. **Geometry-Preserving in 3D Gaussian Splatting for LiDAR-Camera Extrinsic Calibration**  
   Kyoleen Kwak ⋅ Daeho Kim ⋅ Jeong Woon Lee ⋅ Hyoseok Hwang  
   *Targetless LiDAR-camera extrinsic calibration via a 3DGS geometry-preservation objective.*  
   `3D Reconstruction, Gaussian Splatting & NVS` - [arXiv:2606.20103](https://arxiv.org/abs/2606.20103)

6. **RoMa v2: Harder Better Faster Denser Feature Matching**  
   Johan Edstedt ⋅ David Nordström ⋅ Yushan Zhang ⋅ Georg Bökman ⋅ Jonathan Astermark ⋅ Viktor Larsson ⋅ Anders Heyden ⋅ Fredrik Kahl ⋅ Mårten Wadenbäck ⋅ Michael Felsberg  
   *Second generation of the dense feature matcher - the current default front end for relative pose and localization. Code released.*  
   `Depth, Geometry, Matching & Camera Pose` - [arXiv:2511.15706](https://arxiv.org/abs/2511.15706) · [code](https://github.com/Parskatt/romav2)

7. **UniPR-3D: Towards Universal Visual Place Recognition with Visual Geometry Grounded Transformer**  
   Tianchen Deng ⋅ Chen Xun ⋅ Ziming Li ⋅ Hongming Shen ⋅ Shuhao Zhai ⋅ Danwei Wang ⋅ Javier Civera ⋅ Hesheng Wang  
   *Visual place recognition on a VGGT-style geometry-grounded transformer, aiming at one VPR model across domains. Code released.*  
   `Depth, Geometry, Matching & Camera Pose` - [arXiv:2512.21078](https://arxiv.org/abs/2512.21078) · [code](https://github.com/dtc111111/UniPR-3D)

8. **Learning Global Camera Poses from Noisy View-Graphs for Structure from Motion**  
   Fadi Khatib ⋅ Meirav Galun ⋅ Ronen Basri  
   *Global SfM rotation/translation averaging made robust to corrupted view-graphs - the failure mode that breaks classical global SfM.*  
   `3D Reconstruction, Gaussian Splatting & NVS` - no preprint found

9. **General Self-Calibration with Varying Intrinsics**  
   Norio Kosaka ⋅ Timothy Duff ⋅ Tomas Pajdla ⋅ Akihiro Sugimoto  
   *Self-calibration when intrinsics drift across a sequence (zoom, autofocus, rolling shutter) instead of staying fixed.*  
   `Trustworthy AI: Safety, Adversarial & Privacy` - no preprint found

10. **GEO-Detective: Unveiling Location Privacy Risks in Images with LLM Agents**  
   Xinyu Zhang ⋅ Yixin Wu ⋅ Boyang Zhang ⋅ Chenhao Lin ⋅ Chao Shen ⋅ Michael Backes ⋅ Yang Zhang  
   *Agentic VLMs geolocating ordinary photos - the attacker-side counterpart to map-privacy work, and evidence that the threat surface now includes off-the-shelf models.*  
   `Multimodal LLMs & Vision-Language Models` - [arXiv:2511.22441](https://arxiv.org/abs/2511.22441)


---


# Generation & Editing


## Image Generation & Diffusion Models

*178 papers · 114 with links*

1. **AC3S: Adaptive Conditioning for 3D-Aware Synthetic Data Generation**  
   Eric Ji ⋅ Qiran Hu ⋅ Wufei Ma ⋅ Sarthak Jain ⋅ Yingying Li ⋅ Minh Do ⋅ Yaoyao Liu  
   [arXiv:2606.31204](https://arxiv.org/abs/2606.31204) · [project](https://ac3s.cvmlgroup.web.illinois.edu/)
2. **AccelAes: Accelerating Diffusion Transformers for Training-Free Aesthetic-Enhanced Image Generation**  
   Xuanhua Yin ⋅ CHUANZHI XU ⋅ Haoxian Zhou ⋅ Boyu Wei ⋅ Weidong Cai  
   [arXiv:2603.12575](https://arxiv.org/abs/2603.12575) · [code](https://github.com/xuanhuayin/AccelAes)
3. **Accelerated Likelihood Maximization for Diffusion-based Versatile Content Generation**  
   Hyunsoo Lee ⋅ Inwoo Hwang ⋅ Young Min Kim  
   [arXiv:2606.31323](https://arxiv.org/abs/2606.31323) · [project](http://hleephilip.github.io/ALM)
4. **Accelerating Diffusion Models via Equal-Risk Caching**  
   Can Zhang ⋅ Liangshun Zou
5. **Accelerating Diffusion Transformers with Gaussian Process Rectified Feature Cache**  
   Zhirong Shen ⋅ Rui Huang ⋅ Chang Zou ⋅ Shikang Zheng ⋅ Jiacheng Liu ⋅ Peiliang Cai ⋅ zhengyi shi ⋅ Yaosong Du ⋅ Liang Feng ⋅ Xiaobing Tu ⋅ Jinkui Ren ⋅ Xiantao Zhang ⋅ Linfeng Zhang
6. **Achieving Subcategorical Erasure in Text-to-Image Models**  
   Pranav Singh Chib ⋅ Pravendra Singh
7. **Adaptive Noise Covariance Scheduling under Riemannian Metrics for Diffusion Models**  
   Bolin Deng ⋅ Die Hu ⋅ Bin Tan ⋅ Jun Wu
8. **AlignMorph: Tuning-Free Diffusion Image Morphing via Explicit Semantic Transport**  
   Wuyi Liu ⋅ Xu Han ⋅ Yuren Chen ⋅ Yige Mao ⋅ Zishuo Peng ⋅ Xianzhi Li
9. **Analyzing and Improving Training-Free Fast Sampling of Text-to-Image Diffusion Models**  
   Zhenyu Zhou ⋅ Defang Chen ⋅ Siwei Lyu ⋅ Chun Chen ⋅ Can Wang
10. **AnaPFL: When Closed-Form Solutions Meet Generalizationand Personalization in Personalized Federated Learning**  
   Kejia Fan ⋅ Jianheng Tang ⋅ Zhirui Yang ⋅ Feijiang Han ⋅ Yajiang Huang ⋅ Run He ⋅ Jiaxu Li ⋅ Songning Lai ⋅ Anfeng Liu ⋅ Houbing Herbert Song ⋅ Yunhuai Liu ⋅ HUIPING ZHUANG
11. **Anchoring and Steering Diffusion: Enhancing the Faithfulness of Text-to-Image Generation at Inference Time**  
   Xinyi Wang ⋅ Yuyang Huang ⋅ Yalin Su ⋅ Pengcheng Luan ⋅ Tao Zhang ⋅ FEIMING WEI ⋅ Wenxian Yu  
   [arXiv:2607.26647](https://arxiv.org/abs/2607.26647)
12. **ARVAR: Accelerating Visual Autoregressive Model via Attention Retrospect**  
   Jiedong Zhuang ⋅ Lu Lu ⋅ Ming Dai ⋅ Jian Chen ⋅ Qiang Liu ⋅ Haoji Hu
13. **Attention-DP3: Spatially Object-aware 3D Diffusion Policy via Geometry-aligned Attentional Conditioning**  
   Changbo Yan ⋅ Zhongbo Zhang ⋅ Zaibin Zhang ⋅ Yifan Wang ⋅ Lijun Wang ⋅ Huchuan Lu
14. **Autoregressive Image Generation Needs Only a Few Lines of Cached Tokens**  
   Ziran Qin ⋅ Youru Lv ⋅ Mingbao Lin ⋅ Zeren Zhang ⋅ chaofan gan ⋅ Tieyuan Chen ⋅ Liquan Shen ⋅ Junhui Hou ⋅ Chern Hong Lim ⋅ Fei Wen ⋅ Weiyao Lin  
   [arXiv:2512.04857](https://arxiv.org/abs/2512.04857)
15. **Be Tangential to Manifold: Discovering Riemannian Metric for Diffusion Models**  
   Shinnosuke Saito ⋅ Takashi Matsubara  
   [arXiv:2510.05509](https://arxiv.org/abs/2510.05509)
16. **Beyond Aesthetics: Quantifying Information Loss in Turbid Scenes**  
   Vasiliki Ismiroglou ⋅ Tasos Benos ⋅ Malte Pedersen ⋅ Stefan Bengtson ⋅ Thomas B. Moeslund  
   [arXiv:2606.26295](https://arxiv.org/abs/2606.26295) · [project](https://vap.aau.dk/pcd)
17. **Beyond Pixel Mimicry: Disentangled Self-Similarity Rewards for Diverse Subject-Driven Generation**  
   Qian Wang ⋅ Zhenyu Li ⋅ Abdelrahman Eldesokey ⋅ Peter Wonka
18. **Beyond the Black Box: Identifiable Interpretation and Control in Generative Models via Causal Minimality**  
   Lingjing Kong ⋅ Shaoan Xie ⋅ Guangyi Chen ⋅ Yuewen Sun ⋅ Xiangchen Song ⋅ Kun Zhang  
   [arXiv:2512.10720](https://arxiv.org/abs/2512.10720)
19. **CARA: Collision-Aware Resolution Adaptation for Multiresolution Hash Encoding Based Image Fitting**  
   Linfeng Ye ⋅ Zhixiang Chi ⋅ Shayan Mohajer Hamidi ⋅ En-Hui Yang ⋅ Konstantinos Plataniotis
20. **CAST3D: Customizing Arbitrary 2D Assets into 3D World**  
   Yukai Sun ⋅ Hao Qin ⋅ Ming Kong ⋅ Luyuan Chen ⋅ Zhijie Xu ⋅ Jinjian Zhang ⋅ Jie Liu ⋅ Feng Zhang ⋅ Qiang Zhu
21. **CMuon: Accelerating and Stabilizing Diffusion Transformer Training via Chunked Momentum Orthogonalization**  
   Chuyan Chen ⋅ Peng Sun ⋅ Kun Yuan  
   [arXiv:2608.02502](https://arxiv.org/abs/2608.02502)
22. **Co-evolving Representations in Joint Image-Feature Diffusion**  
   Theodoros Kouzelis ⋅ Spyros Gidaris ⋅ Nikos Komodakis
23. **CollectionLoRA: Collecting 50 Effects in 1 LoRA for Deployment**  
   Fangtai Wu ⋅ Hailong Guo ⋅ Shijie Huang ⋅ Jiayi Song ⋅ Yubo Huang ⋅ Mushui Liu ⋅ Zhao Wang ⋅ Yunlong Yu ⋅ Jiaming Liu ⋅ Ruihua Huang
24. **ColorFM: An Optimization-to-Learning Framework for Color Transfer via Flow Matching**  
   Yuhang He ⋅ Kai Zhang ⋅ Xiaoming Li ⋅ Du Chen ⋅ Jian Yang  
   [arXiv:2607.07119](https://arxiv.org/abs/2607.07119)
25. **ConceptWeaver: Weaving Disentangled Concepts with Flow**  
   Jintao Chen ⋅ Aiming Hao ⋅ Xiaoqing Chen ⋅ Chengyu Bai ⋅ Chubin Chen ⋅ Yanxun Li ⋅ Jiahong Wu ⋅ Xiangxiang Chu ⋅ Shanghang Zhang  
   [arXiv:2603.28493](https://arxiv.org/abs/2603.28493)
26. **Cross-Resolution Distribution Matching for Diffusion Distillation**  
   Chen Feiyang ⋅ Hongpeng Pan ⋅ Haonan Xu ⋅ Xinyu Duan ⋅ Zhefeng Wang ⋅ Yang Yang  
   [arXiv:2603.06136](https://arxiv.org/abs/2603.06136)
27. **Cross-Space Distillation: Teaching One-Step Students with Modern Diffusion Teachers**  
   Anh Nguyen ⋅ Ngan Nguyen ⋅ Hong Duc Vu ⋅ Trung Dao ⋅ Viet Nguyen ⋅ Minh Quan Dao ⋅ Kien Nguyen ⋅ Tran Bao Chi Tran ⋅ Phong Nguyen ⋅ Khoi Nguyen ⋅ Cuong Pham ⋅ Dimitris N. Metaxas ⋅ Vishal Patel ⋅ Anh Tran  
   [arXiv:2606.32020](https://arxiv.org/abs/2606.32020)
28. **Ctrl-Z Sampling: Scaling Diffusion Sampling with Controlled Random Zigzag Explorations**  
   Shunqi Mao ⋅ Wei Guo ⋅ Chaoyi Zhang ⋅ Jieting Long ⋅ Ke Xie ⋅ Weidong Cai  
   [arXiv:2506.20294](https://arxiv.org/abs/2506.20294) · [code](https://github.com/ShunqiM/Ctrl-Z-Sampling)
29. **Curvature-Adaptive Consistency Flow Matching: Autonomous Trajectory Optimization via Reinforcement Learning**  
   Songtao Tian ⋅ Guhan Chen ⋅ Bohan Li ⋅ Jingyi Ma ⋅ Zixiong Yu  
   [arXiv:2606.22394](https://arxiv.org/abs/2606.22394)
30. **D2PO: Optimizing Diffusion Samplers via Dynamic Preference**  
   Jinkyu Kim ⋅ Jinyoung Choi ⋅ Bohyung Han  
   [arXiv:2607.06609](https://arxiv.org/abs/2607.06609)
31. **DAPS++: Rethinking Diffusion Inverse Problems with Decoupled Posterior Annealing**  
   Hao Chen ⋅ Renzheng Zhang ⋅ Scott Howard  
   [arXiv:2511.17038](https://arxiv.org/abs/2511.17038)
32. **DARL: Efficient Document-to-Markup Generation via Look-Ahead Diffusion Trajectory Sampling**  
   Wentao Yang ⋅ Yongxin Shi ⋅ Rui Tang ⋅ Peirong Zhang ⋅ Shihang Wu ⋅ Huiguo He ⋅ Zheng Huang ⋅ Dezhi Peng ⋅ Minghui Liao ⋅ Lianwen Jin
33. **Data Circuit Breaker: Identifying Training, Test, and Generated Data in Image Generative Models**  
   Bihe Zhao ⋅ Michel Meintz ⋅ Juangui Xu ⋅ Franziska Boenisch ⋅ Adam Dziedzic
34. **Decoupling Complexity from Scale in Latent Diffusion Model**  
   Tianxiong Zhong ⋅ Xingye Tian ⋅ Xuebo Wang ⋅ Boyuan Jiang ⋅ Xin Tao ⋅ Pengfei Wan  
   [arXiv:2511.16117](https://arxiv.org/abs/2511.16117)
35. **Delving into Latent Spectral Biasing of Video VAEs for Superior Diffusability**  
   Shizhan Liu ⋅ Xinran Deng ⋅ Zhuoyi Yang ⋅ Jiayan Teng ⋅ Xiaotao Gu ⋅ Jie Tang  
   [arXiv:2512.05394](https://arxiv.org/abs/2512.05394) · [code](https://github.com/zai-org/SSVAE)
36. **DiffPro: Joint Timestep and Layer-Wise Precision Optimization for Efficient Diffusion Inference**  
   Farhana Amin ⋅ Sabiha Afroz ⋅ Kanchon Gharami ⋅ Mona Moghadampanah ⋅ Dimitrios Nikolopoulos  
   [arXiv:2511.11446](https://arxiv.org/abs/2511.11446)
37. **DiffRGD: An Inference-Time Diffusion Guidance Through Riemannian Gradient Descent**  
   Jia-Wei Liao ⋅ Li-Xuan Peng ⋅ Mei-Heng Yueh ⋅ Min Sun ⋅ Cheng-Fu Chou ⋅ Jun-Cheng Chen  
   [arXiv:2606.28417](https://arxiv.org/abs/2606.28417) · [project](https://diffrgd.github.io/)
38. **Diffusion Image Generation with Explicitly Modeling of Data Manifold Geometry**  
   Duoduo Xue ⋅ Zhiyu Zhu ⋅ Junhui Hou
39. **Diffusion Integrated Gradients: Controllable Path Generation for Flexible Feature Attribution**  
   Soyeon Kim ⋅ Kyowoon Lee ⋅ Jaesik Choi  
   [arXiv:2606.22314](https://arxiv.org/abs/2606.22314)
40. **Diffusion-SDPO: Safeguarded Direct Preference Optimization for Diffusion Models**  
   Minghao Fu ⋅ Guo-Hua Wang ⋅ Tianyu Cui ⋅ Qing-Guo Chen ⋅ Zhao Xu ⋅ Weihua Luo ⋅ Kaifu Zhang  
   [arXiv:2511.03317](https://arxiv.org/abs/2511.03317) · [code](https://github.com/AIDC-AI/Diffusion-SDPO)
41. **DiffusionVL: Translating Any Autoregressive Models into Diffusion Vision Language Models**  
   Lunbin Zeng ⋅ Jingfeng Yao ⋅ Bencheng Liao ⋅ Hongyuan Tao ⋅ Wenyu Liu ⋅ Xinggang Wang  
   [arXiv:2512.15713](https://arxiv.org/abs/2512.15713) · [code](https://github.com/hustvl/DiffusionVL)
42. **DiTailed: Ensuring Visual Object Consistency in Text-Image-to-Image Flow Matching Models**  
   Francesco Taioli ⋅ Daniel Coelho ⋅ Iaroslav Melekhov ⋅ Roberto Alcover-Couso ⋅ Jose Saiz ⋅ Virginia Arguedas ⋅ Artur Bekasov  
   [arXiv:2607.12539](https://arxiv.org/abs/2607.12539) · [project](https://francescotaioli.github.io/DiTailed/)
43. **DiverseVAR: Balancing Diversity and Quality of Next-Scale Visual Autoregressive Models**  
   Mingue Park ⋅ Prin Phunyaphibarn ⋅ Phillip (Yuseung) Lee ⋅ Minhyuk Sung  
   [arXiv:2511.21415](https://arxiv.org/abs/2511.21415)
44. **Drift-AR: Single-Step Visual Autoregressive Generation via Anti-Symmetric Drifting**  
   zhen zou ⋅ Xiaoxiao Ma ⋅ Mingde Yao ⋅ Jie Huang ⋅ Linjiang Huang ⋅ Feng Zhao  
   [arXiv:2603.28049](https://arxiv.org/abs/2603.28049) · [code](https://github.com/aSleepyTree/Drift-AR)
45. **DriftScope: Measuring The Hidden Effects of Diffusion Model Fine-Tuning**  
   Héctor Laria ⋅ Yiping Han ⋅ Julian Santamaria ⋅ Kai WANG ⋅ Bogdan Raducanu ⋅ Joost Van de Weijer ⋅ Alex Gomez-Villa
46. **DRPO: Disentangling Demographic Bias from Rewards for Fair Diffusion Alignment**  
   YeonGyu Han ⋅ Junah Jung ⋅ Dongheon Lee
47. **DSH-Bench: A Difficulty- and Scenario-Aware Benchmark with Hierarchical Subject Taxonomy for Subject-Driven Text-to-Image Generation**  
   Zhenyu Hu ⋅ Qing Wang ⋅ Cao Te ⋅ Kuo Liao ⋅ Longfei Lu ⋅ Liqun Liu ⋅ Shuang Li ⋅ Hang Chen ⋅ Mengge Xue ⋅ Yuan Chen ⋅ Chao Deng ⋅ Peng Shu ⋅ Huan Yu ⋅ Jie Jiang  
   [arXiv:2603.08090](https://arxiv.org/abs/2603.08090)
48. **Dual Masked Generative Adversarial Transformer for Unsupervised Domain Adaptation**  
   Lei Zhu ⋅ Xinxing Xu ⋅ Jun Zhou ⋅ Qiegen Liu ⋅ Rick Siow Mong Goh ⋅ Yong Liu
49. **Dual-End Consistency Model**  
   linwei dong ⋅ Ruoyu Guo ⋅ Ge Bai ⋅ Zehuan Yuan ⋅ Yawei Luo ⋅ Changqing Zou  
   [arXiv:2602.10764](https://arxiv.org/abs/2602.10764)
50. **DuoFlow: JVP-Free Finite-Difference Mean Flows for One-Step Image Generation**  
   Zeming Li ⋅ Xiangyu Zhang ⋅ Ping Tan ⋅ Heung-Yeung Shum
51. **Dynamic Image Prompt Adapter for Scalable Zero-shot Personalized Text-to-Image Generation**  
   Zhizhong Wang ⋅ Tianyi Chu ⋅ Richard Wang ⋅ Nanyang Wang ⋅ Kehan Li  
   [arXiv:2512.09814](https://arxiv.org/abs/2512.09814)
52. **DynEval: Holistic Evaluations of T2I Generative Models in the Wild**  
   Shyam Marjit ⋅ Dheeraj Baiju ⋅ Anuj Shikarkhane ⋅ Akhil Sakthieswaran ⋅ Sayak Paul ⋅ Anirban Chakraborty  
   [arXiv:2607.11199](https://arxiv.org/abs/2607.11199) · [project](https://vcl-iisc.github.io/dyneval/)
53. **Early Estimation of Language to Latent Alignment in Diffusion Models**  
   VASCO RAMOS ⋅ Regev Cohen ⋅ Idan Szpektor ⋅ Joao Magalhaes  
   [arXiv:2512.08505](https://arxiv.org/abs/2512.08505)
54. **EFlow: Fast Few-Step Video Generator Training from Scratch via Efficient Solution Flow**  
   Dogyun Park ⋅ Yanyu Li ⋅ Sergey Tulyakov ⋅ Anil Kag  
   [arXiv:2603.27086](https://arxiv.org/abs/2603.27086)
55. **ELDiff: When Evidential Learning Meets Text-to-Image Diffusion**  
   Qingtao Pan ⋅ Kai Ye ⋅ Zhihao Dou ⋅ Bing Ji ⋅ Shuo Li  
   [arXiv:2606.20924](https://arxiv.org/abs/2606.20924) · [code](https://github.com/QingtaoPan/ELDiff)
56. **ELT: Elastic Looped Transformers for Visual Generation**  
   Sahil Goyal ⋅ Swayam Agrawal ⋅ Gautham Anil ⋅ Sujoy Paul ⋅ Aditya Kusupati ⋅ Prateek Jain  
   [arXiv:2604.09168](https://arxiv.org/abs/2604.09168)
57. **EMAG: Self-Rectifying Diffusion Sampling with Exponential Moving Average Guidance**  
   ANKIT YADAV ⋅ Huy Ta ⋅ Lingqiao Liu  
   [arXiv:2512.17303](https://arxiv.org/abs/2512.17303)
58. **Entropy-Controlled Flow Matching**  
   Chika Maduabuchi  
   [arXiv:2602.22265](https://arxiv.org/abs/2602.22265)
59. **EruDiff: Refactoring Knowledge in Diffusion Models for Advanced Text-to-Image Synthesis**  
   Xiefan Guo ⋅ Xinzhu Ma ⋅ Haoxiang Ma ⋅ Zihao Zhou ⋅ Di Huang  
   [arXiv:2603.20828](https://arxiv.org/abs/2603.20828) · [code](https://github.com/xiefan-guo/erudiff)
60. **EvoTok: A Unified Image Tokenizer via Residual Latent Evolution for Visual Understanding and Generation**  
   Yan Li ⋅ Ning Liao ⋅ Xiangyu Zhao ⋅ Shaofeng Zhang ⋅ Xiaoxing Wang ⋅ Yifan Yang ⋅ Junchi Yan ⋅ Xue Yang
61. **FairSteer: Cross-Attention Steering Towards a Fairer Text-Guided Image Generation**  
   Tatiana Gaintseva ⋅ Akshit Achara ⋅ Greg Slabaugh ⋅ Jiankang Deng ⋅ Ismail Elezi
62. **Finite Difference Flow Optimization for RL Post-Training of Text-to-Image Models**  
   David McAllister ⋅ Miika Aittala ⋅ Tero Karras ⋅ Janne Hellsten ⋅ Angjoo Kanazawa ⋅ Timo Aila ⋅ Samuli Laine  
   [arXiv:2603.12893](https://arxiv.org/abs/2603.12893) · [code](https://github.com/NVlabs/finite-difference-flow-optimization)
63. **Flash-BoN: Instant Drafts for Inference-Time Scaling in Diffusion Models**  
   Ruchit Rawal ⋅ Reza Shirkavand ⋅ Sayak Paul ⋅ Yuxin Wen ⋅ Heng Huang ⋅ Yizheng Chen ⋅ Tom Goldstein ⋅ Gowthami Somepalli  
   [arXiv:2607.04461](https://arxiv.org/abs/2607.04461)
64. **FlowInOne: Unifying Multimodal Generation as Image-in, Image-out Flow Matching**  
   Junchao Yi ⋅ Rui Zhao ⋅ Jiahao Tang ⋅ Weixian Lei ⋅ Linjie Li ⋅ Qisheng Su ⋅ Zhengyuan Yang ⋅ Lijuan Wang ⋅ Xiaofeng Zhu ⋅ Alex Jinpeng Wang
65. **FlowLess: Controlling Abstract Image Generation**  
   Amir Hertz ⋅ Noah Snavely
66. **From Open Loop to Closed Loop: A Test-Time Iterative Optimization Framework for Reference-Consistent Image Generation**  
   Baixuan Zhao ⋅ Xinyu Zhang ⋅ 华渝 郑 ⋅ Shuaicheng Liu ⋅ Xiongkuo Min ⋅ Guangtao Zhai ⋅ Xiaohong Liu  
   [arXiv:2607.04691](https://arxiv.org/abs/2607.04691) · [code](https://github.com/zzdrill/From-Open-Loop-to-Closed-Loop)
67. **From smooth to sharp: Frequency-Decoupled Latent Optimization for Realistic Image Generation**  
   Tejaswini Medi ⋅ Hsien-Yi Wang ⋅ Arianna Rampini ⋅ Margret Keuper
68. **From Sparse to Dense: Multi-View GRPO for Flow Models via Augmented Condition Space**  
   Jiazi Bu ⋅ Pengyang Ling ⋅ Yujie Zhou ⋅ Yibin Wang ⋅ Yuhang Zang ⋅ Tianyi Wei ⋅ Xiaohang Zhan ⋅ Jiaqi Wang ⋅ Tong Wu ⋅ Xingang Pan ⋅ Dahua Lin  
   [arXiv:2603.12648](https://arxiv.org/abs/2603.12648)
69. **G3AFT: Glance Guided Gradient Aligned Fine-Tuning for Visual Autoregressive Models**  
   Jiayi Zhang ⋅ Xiefan Guo ⋅ Xinzhu Ma ⋅ Di Huang
70. **Generalization and Memorization in Rectified Flow**  
   Mingxing Rao ⋅ Daniel Moyer  
   [arXiv:2603.13421](https://arxiv.org/abs/2603.13421)
71. **Generative Refinement Network for Visual Synthesis**  
   Jian Han ⋅ Jinlai Liu ⋅ Jiahuan Wang ⋅ BINGYUE PENG ⋅ Zehuan Yuan  
   [arXiv:2604.13030](https://arxiv.org/abs/2604.13030) · [code](https://github.com/bytedance/GRN)
72. **GenSP: Consistent Spherical Parameterization via Learning Shape Generative Models**  
   Sai Karthikey Pentapati ⋅ Shashank Gupta ⋅ Rajesh Sureddi ⋅ Yuezhi Yang ⋅ Alan Bovik ⋅ Qixing Huang  
   [arXiv:2607.00492](https://arxiv.org/abs/2607.00492)
73. **GeoCFM: Positive-Only Conditional Flow Matching for Mineral Occurrence Sampling**  
   Moshe Eliasof ⋅ Eldad Haber
74. **Glance: Accelerating Diffusion Models with 1 Sample**  
   Zhuobai Dong ⋅ Rui Zhao ⋅ songjie wu ⋅ Suyang Hou ⋅ Junchao Yi ⋅ Zhengyuan Yang ⋅ Lijuan Wang ⋅ Alex Jinpeng Wang  
   [arXiv:2512.02899](https://arxiv.org/abs/2512.02899)
75. **GR-GRPO: Graph-Diffused Credit for Autoregressive Image RL Alignment**  
   Zheyu Zhang ⋅ Peng-Tao Jiang ⋅ Tianyi Zheng ⋅ Jian Zhang ⋅ Jinwei Chen ⋅ Bo Li
76. **GRAN-TED: Generating Robust, Aligned, and Nuanced Text Embedding for Diffusion Models**  
   Bozhou Li ⋅ Sihan Yang ⋅ Yushuo Guan ⋅ Ruichuan An ⋅ Xinlong Chen ⋅ Yang Shi ⋅ Pengfei Wan ⋅ Wentao Zhang ⋅ Yuanxing Zhang  
   [arXiv:2512.15560](https://arxiv.org/abs/2512.15560) · [project](https://anonymous.4open.science/r/GRAN-TED-4FCC/)
77. **GRE-Diff: Gaussian Room Embeddings for Structured Layout Diffusion**  
   Jing Wang ⋅ Haoran Xiong ⋅ Zihao Yan ⋅ Minglun Gong ⋅ Hui Huang  
   [arXiv:2607.08086](https://arxiv.org/abs/2607.08086)
78. **Hi-DiT: Hybrid Latent-Pixel Diffusion Transformer for Image Generation**  
   Yedong Shen ⋅ Yehao Li ⋅ Yingwei Pan ⋅ Yanyong Zhang ⋅ Ting Yao
79. **Histogram-constrained Image Generation**  
   Haoming Liu ⋅ Yuanhe Guo ⋅ Yijia Cao ⋅ Shenji Wan ⋅ Hongyi Wen  
   [arXiv:2606.31683](https://arxiv.org/abs/2606.31683) · [project](https://maps-research.github.io/hig/)
80. **HO-Flow: Generalizable Hand-Object Interaction Generation with Latent Flow Matching**  
   Zerui Chen ⋅ Rolandos Alexandros Potamias ⋅ Shizhe Chen ⋅ Jiankang Deng ⋅ Cordelia Schmid ⋅ Stefanos Zafeiriou  
   [arXiv:2604.10836](https://arxiv.org/abs/2604.10836) · [project](https://zerchen.github.io/projects/hoflow.html)
81. **HRDiT: Training-Free High-Resolution Image Generation with Off-the-Shelf Diffusion Transformer Models**  
   Yu Xue ⋅ Haoxuan Qu ⋅ ZHUOLING Li ⋅ Hongbin Xu ⋅ Jianxiong Yin ⋅ Simon See ⋅ Hossein Rahmani ⋅ Jun Liu  
   [arXiv:2608.07003](https://arxiv.org/abs/2608.07003) · [code](https://github.com/zylwithxy/HRDiT)
82. **Importance-Aware Low-Rank Distillation of Diffusion Transformers**  
   Denis Zavadski ⋅ Sebastian Heid ⋅ Damjan Kalšan ⋅ Stefan Roth ⋅ Carsten Rother
83. **Improved Immiscible Diffusion: Accelerating Diffusion Training by Reducing Miscibility**  
   Yiheng Li ⋅ Feng Liang ⋅ Dan Kondratyuk ⋅ Masayoshi TOMIZUKA ⋅ Kurt Keutzer ⋅ Chenfeng Xu  
   [arXiv:2505.18521](https://arxiv.org/abs/2505.18521) · [code](https://github.com/yhli123/Immiscible-Diffusion)
84. **InstanceControl: Controllable Complex Image Generation without Instance Labeling**  
   XIAOYU LIU ⋅ Huan Wang ⋅ FAN LI ⋅ Zhixing Wang ⋅ Jiaqi Xu ⋅ Ming LIU ⋅ Wangmeng Zuo
85. **InstantRetouch: Personalized Image Retouching without Test-time Fine-tuning**  
   Temesgen Muruts Weldengus ⋅ Binnan Liu ⋅ Fei Kou ⋅ Youwei Lyu ⋅ Jinwei Chen ⋅ Changqing Zou ⋅ Qingnan Fan
86. **InterCMDM: Block-Causal Diffusion for Autoregressive Human Interaction Generation**  
   Qing Yu ⋅ Kent Fujiwara  
   [arXiv:2607.01743](https://arxiv.org/abs/2607.01743) · [project](https://yu1ut.com/InterCMDM-HP/)
87. **Intermediate Text Representation Guided Text-to-Image Generation for Enhancing One-and-Only Alignment**  
   Soyoun Won ⋅ Aryan Yazdan Parast ⋅ Basim Azam ⋅ Jean Honorio ⋅ NAVEED AKHTAR  
   [arXiv:2606.30262](https://arxiv.org/abs/2606.30262) · [project](https://soyoun-won.github.io/one-and-only-ir-guidance/)
88. **Introspective Attention Modulation for Safe Text-to-Image Generation**  
   Basim Azam ⋅ Hossein Rahmani ⋅ NAVEED AKHTAR  
   [arXiv:2607.14945](https://arxiv.org/abs/2607.14945) · [project](https://basim-azam.github.io/iam/)
89. **ISAC: Training-Free Instance-to-Semantic Attention Control for Multi-Instance Generation**  
   Sanghyun Jo ⋅ Wooyeol Lee ⋅ Ziseok Lee ⋅ Jonghyun Choi ⋅ Jaesik Park ⋅ Kyungsu Kim
90. **JSON: Jigsaw Self-play Optimization for Normalizing Flows**  
   Fengxiang Yang ⋅ Tianyi Zheng ⋅ Jinwei Chen ⋅ Bo Li
91. **Jumping the Landing Phase: Noise Variance Matching Enables Accurate Few-Step Inversion**  
   Yang Luo ⋅ Zhineng Chen ⋅ Ya Gao ⋅ Xieping Gao ⋅ Yu-Gang Jiang
92. **Keep-or-Drop? Adaptive Tokenizer for Compact Video Representation**  
   Yeonkyeong Lee ⋅ Hyunsung Go ⋅ Jongmin Kim ⋅ Lim Sewoong ⋅ Donghoon Lee
93. **LACON: Training Text-to-Image Model from Uncurated Data**  
   Zhiyang Liang ⋅ Ziyu Wan ⋅ Hongyu Liu ⋅ DONG CHEN ⋅ Qiu Shen ⋅ Hao Zhu ⋅ Dongdong Chen  
   [arXiv:2603.26866](https://arxiv.org/abs/2603.26866)
94. **Latent Visual Diffusion Reasoning with Monte Carlo Tree Search**  
   Xirui Teng ⋅ Nan Xi ⋅ Junsong Yuan  
   [arXiv:2606.27988](https://arxiv.org/abs/2606.27988) · [code](https://github.com/XiruiTeng/LVDR_Official.git)
95. **Layout-Conditioned Autoregressive Text-to-Image Generation via Structured Masking**  
   Zirui Zheng ⋅ Takashi Isobe ⋅ Tong Shen ⋅ XU JIA ⋅ Xiaomin Li ⋅ Jianbin Zhao ⋅ Mengmeng Ge ⋅ Baolu Li ⋅ Qinghe Wang ⋅ Haiwen Diao ⋅ Dong Li ⋅ Yunzhi Zhuge ⋅ Dong Zhou ⋅ Huchuan Lu ⋅ Emad Barsoum  
   [arXiv:2509.12046](https://arxiv.org/abs/2509.12046)
96. **Learning on the Manifold: Unlocking Standard Diffusion Transformers with Representation Encoders**  
   Amandeep Kumar ⋅ Vishal Patel  
   [arXiv:2602.10099](https://arxiv.org/abs/2602.10099) · [code](https://github.com/amandpkr/RJF)
97. **Leveraging Cross-Modal Knowledge Transfer for Knowledge-Aware Concept Customization**  
   chenyang zhu ⋅ Hongxiang Li ⋅ Xiu Li ⋅ Long Chen  
   [arXiv:2603.12743](https://arxiv.org/abs/2603.12743) · [project](https://chenyangzhu1.github.io/MoKus/)
98. **LinCa: Accelerating Diffusion Models via Learnable Decomposed Feature Caching**  
   Jinshan Liu ⋅ Haoran Qin ⋅ Xiaobing Tu ⋅ Jiacheng Liu ⋅ Jiahui Hu ⋅ zhengan yan ⋅ Yukun Xie ⋅ Kerui Shen ⋅ Jinkui Ren ⋅ Yuqi Lin ⋅ Xiantao Zhang ⋅ Linfeng Zhang
99. **Logit Refiner: Improving Visual Autoregressive Models via Intra-Scale Dependency Modeling**  
   Meimingwei Li ⋅ Stefan Andreas Baumann ⋅ Felix Krause ⋅ Bjorn Ommer
100. **LUA: Latent Upscaling Adapter for Diffusion-Based Image Synthesis**  
   Aleksandr Razin ⋅ Kazantsev Danil ⋅ Ilya Makarov
101. **Mapping Dark-Matter Clusters via Physics-Guided Diffusion Models**  
   Diego Royo ⋅ Brandon Zhao ⋅ Adolfo Muñoz ⋅ Diego Gutierrez ⋅ Katherine Bouman  
   [arXiv:2603.14503](https://arxiv.org/abs/2603.14503) · [project](https://graphics.unizar.es/projects/DarkMatterMapping)
102. **MARché: Fast Masked Autoregressive Image Generation with Cache-Aware Attention**  
   Chaoyi Jiang ⋅ Sungwoo Kim ⋅ Lei Gao ⋅ Hossein Zarch ⋅ Won Woo Ro ⋅ Murali Annavaram
103. **MetaPoint: Unlocking Precise Spatial Control in Visual Generation**  
   Dewei Zhou ⋅ Xinyu Huang ⋅ Xun Wang ⋅ Ji Xie ⋅ Yabo Zhang ⋅ Liang Li ⋅ Kunchang Li ⋅ Zongxin Yang ⋅ Yi Yang  
   [arXiv:2606.05031](https://arxiv.org/abs/2606.05031)
104. **MMDiff: Extending Diffusion Transformers for Multi-Modal Generation**  
   Yagmur Akarken ⋅ Orest Kupyn ⋅ Christian Rupprecht  
   [arXiv:2606.16673](https://arxiv.org/abs/2606.16673)
105. **Momentum Guidance: Plug-and-Play Guidance for Flow Models**  
   Runlong Liao ⋅ Jian Yu ⋅ Baiyu Su ⋅ Chi Zhang ⋅ Lizhang Chen ⋅ Qiang Liu  
   [arXiv:2602.20360](https://arxiv.org/abs/2602.20360)
106. **MPO: Single-Stream Policy Optimization for Efficient Text-to-Image Alignment**  
   Lishuai Gao ⋅ Jie Hu ⋅ Cong Wei ⋅ Yujie Zhong ⋅ Yibo Zhao ⋅ Zan Gao ⋅ Xiaoming Wei
107. **NaP-Control: Navigating Diffusion Prior for Versatile and Fast Character Control**  
   Chia-Wen Chen ⋅ Yan Wu ⋅ Korrawe Karunratanakul ⋅ Siyu Tang  
   [arXiv:2605.20209](https://arxiv.org/abs/2605.20209) · [project](https://chiawenchen.github.io/nap-control-project/)
108. **Nexus-Vid: Efficient Frequency Bridging with Homogeneous Latent Space for Video Unified Models**  
   Jiazheng Xing ⋅ Hangjie Yuan ⋅ Lingling Cai ⋅ Xinyu Liu ⋅ Yujie Wei ⋅ Fei Du ⋅ Tao Feng ⋅ Hai Ci ⋅ Jiasheng Tang ⋅ Weihua Chen ⋅ Fan Wang ⋅ Yong Liu
109. **NoiseTilt: Noise-Tilted Reverse Kernels for Diffusion Reward Alignment**  
   Jisung Hwang ⋅ Yunhong Min ⋅ Jaihoon Kim ⋅ I-Chao Shen ⋅ Minhyuk Sung  
   [arXiv:2606.18066](https://arxiv.org/abs/2606.18066)
110. **Not All Prediction Targets Keep Training-Free Diffusion Guidance on the Manifold**  
   Yunsung Lee ⋅ Hyeongmin Lee  
   [arXiv:2607.00647](https://arxiv.org/abs/2607.00647) · [code](https://github.com/ManLuML/on-manifold-tfg) · [project](https://manluml.github.io/on-manifold-tfg)
111. **NumColor: Precise Numeric Color Control in Text-to-Image Generation**  
   Muhammad Atif Butt ⋅ Diego Hernández ⋅ Alex Gomez-Villa ⋅ Kai WANG ⋅ Javier Vazquez-Corral ⋅ Joost Van de Weijer  
   [arXiv:2603.13547](https://arxiv.org/abs/2603.13547)
112. **On the Diffusibility of High-Dimensional Latents**  
   Chao Feng ⋅ Zhiyang Xu ⋅ Bowei Chen ⋅ Yuanjun Xiong ⋅ Xiyao Wang ⋅ Jui-Hsien Wang ⋅ Richard Zhang ⋅ Zhe Lin ⋅ Andrew Owens ⋅ Yijun Li
113. **On-Policy Diffusion Reinforcement Learning Meets Off-Policy Quality Anchoring**  
   Zunxu Liu ⋅ Zhaofan Qiu ⋅ Yazhen Xie ⋅ Yingwei Pan ⋅ Ting Yao ⋅ Tao Mei
114. **OneVAE: Joint Discrete and Continuous Optimization Helps Discrete Video VAE Train Better**  
   Yupeng Zhou ⋅ Zhen Li ⋅ Yuming Chen ⋅ Ziheng Ouyang ⋅ Ruoyi Du ⋅ Daquan Zhou ⋅ Bin Fu ⋅ Yihao Liu ⋅ Peng Gao ⋅ Ming-Ming Cheng ⋅ Qibin Hou  
   [arXiv:2508.09857](https://arxiv.org/abs/2508.09857)
115. **OpenSubject: Leveraging Video-Derived Identity and Diversity Priors for Subject-driven Image Generation and Manipulation**  
   Yexin Liu ⋅ Manyuan Zhang ⋅ Yueze Wang ⋅ Hongyu Li ⋅ Dian Zheng ⋅ WEIMING ZHANG ⋅ Changsheng Lu ⋅ Harry Yang  
   [arXiv:2512.08294](https://arxiv.org/abs/2512.08294)
116. **ParaFlow: Parallel Sampling for Flow Matching Models**  
   jianrong Lu ⋅ Bangwei Li ⋅ Haomin Zhang ⋅ Zhuoya Gu ⋅ Yongqing Lu ⋅ Jianhai Chen ⋅ Qinming He
117. **Parsimonious Flow Matching for Efficient Image Generation**  
   Tianjiao Ding ⋅ Ziqing Xu ⋅ Benjamin Haeffele ⋅ Hongkang Li ⋅ Rene Vidal
118. **Personalized Reward Modeling for Text-to-Image Generation**  
   Jeongeun Lee ⋅ Ryang Heo ⋅ Dongha Lee  
   [arXiv:2511.19458](https://arxiv.org/abs/2511.19458)
119. **Phase-Aligned RoPE for Mixed-Resolution Diffusion Transformer**  
   Haoyu Wu ⋅ Jingyi Xu ⋅ Qiaomu Miao ⋅ Dimitris Samaras ⋅ Hieu Le  
   [arXiv:2511.19778](https://arxiv.org/abs/2511.19778) · [project](https://hao-yu-wu.github.io/mixed_res/)
120. **PIPBench: A Profile-Inclusive Framework for Personalized Image Generation Evaluation**  
   Yuhang Wu ⋅ Shuxiang Zhang ⋅ WEE CHING ⋅ Chi Zhang ⋅ Miao Liu  
   [arXiv:2607.06440](https://arxiv.org/abs/2607.06440) · [project](https://wuyuhang05.github.io/PIPBench/)
121. **PixelU: A U-Shaped Transformer for Efficient End-to-End Pixel Diffusion**  
   Zipeng Guo ⋅ Lichen Ma ⋅ Yu He ⋅ Xiaolong Fu ⋅ Jingling Fu ⋅ Junshi Huang ⋅ Yan Li  
   [arXiv:2606.27760](https://arxiv.org/abs/2606.27760)
122. **POET: Preference Optimization for Enhanced Text-to-Image Generation**  
   Ruibo Chen ⋅ Jiacheng Pan ⋅ Heng Huang ⋅ Zhenheng Yang
123. **Policy-Based Tuning of Autoregressive Image Models with Instance- and Distribution-Level Rewards**  
   Orhun Baran ⋅ Melih Kandemir ⋅ Ramazan Gokberk Cinbis  
   [arXiv:2603.23086](https://arxiv.org/abs/2603.23086)
124. **Posterior Augmented Flow Matching**  
   George Stoica ⋅ Sayak Paul ⋅ Matthew Wallingford ⋅ Abhay Nori ⋅ Vivek Ramanujan ⋅ Winson Han ⋅ Ali Farhadi ⋅ Ranjay Krishna ⋅ Judy Hoffman  
   [arXiv:2605.00825](https://arxiv.org/abs/2605.00825) · [code](https://github.com/gstoica27/PAFM.git)
125. **Racing in Volume with Flow Ensembles**  
   Saswat Subhajyoti Mallick ⋅ Riu Cherdchusakulchai ⋅ Marc Olle ⋅ Albert Mosella-Montoro ⋅ Jose Ribeiro-Gomes ⋅ Francisco Vicente Carrasco ⋅ Fernando de la Torre
126. **RankT2I: A Submodular Framework for Discovering Interpretable and Diverse Semantics in Text-to-Image Models**  
   Ritika Allada ⋅ Pinar Yanardag  
   [arXiv:2608.14226](https://arxiv.org/abs/2608.14226)
127. **Rdm: Re-conceptualizing Distribution Matching as a Reward for Diffusion Distillation**  
   Linqian Fan ⋅ Peiqin Sun ⋅ Tiancheng Wen ⋅ Shun Lu ⋅ Chengru Song
128. **RealGen: Photorealistic Text-to-Image Generation via Detector-Guided Rewards**  
   ye junyan ⋅ Leqi Zhu ⋅ Yuncheng Guo ⋅ Dongzhi Jiang ⋅ Zilong Huang ⋅ Yifan Zhang ⋅ Zhiyuan Yan ⋅ Haohuan Fu ⋅ Conghui He ⋅ Weijia Li  
   [arXiv:2512.00473](https://arxiv.org/abs/2512.00473) · [code](https://github.com/yejy53/RealGen)
129. **Recurrent Autoregressive Diffusion: Global Memory Meets Local Attention**  
   Taiye Chen ⋅ Zihan Ding ⋅ Anjian Li ⋅ Christina Zhang ⋅ Zeqi Xiao ⋅ Yisen Wang ⋅ Chi Jin  
   [arXiv:2511.12940](https://arxiv.org/abs/2511.12940) · [project](https://yeyutaihan.github.io/recurrent-autoregressive-diffusion/)
130. **RefDiT: Local Attribute Guidance in Reference-Based Image Generation**  
   Rameshwar Mishra ⋅ Srikrishna Karanam ⋅ Subramanyam Venkata
131. **REGLUE Your Latents with Global and Local Semantics for Entangled Diffusion**  
   Giorgos Petsangourakis ⋅ Christos Sgouropoulos ⋅ Bill Psomas ⋅ Theodoros Giannakopoulos ⋅ Giorgos Sfikas ⋅ Ioannis Kakogeorgiou  
   [arXiv:2512.16636](https://arxiv.org/abs/2512.16636) · [code](https://github.com/giorgospets/reglue)
132. **Reinforcement Learning for Multimodal Diffusion Language Models via Bidimensional Trajectory and Thought Optimization**  
   Bowen Li ⋅ Yinjie Wang ⋅ Yunzhi Zhang ⋅ Junhong Liu ⋅ Yingqing Guo ⋅ Jiajun Wu ⋅ Mengdi Wang ⋅ Ling Yang
133. **ReSWD: ReSTIR‘d, not shaken. Combining Reservoir Sampling and Sliced Wasserstein Distance for Variance Reduction.**  
   Mark Boss ⋅ Andreas Engelhardt ⋅ Simon Donné ⋅ Varun Jampani  
   [arXiv:2510.01061](https://arxiv.org/abs/2510.01061) · [project](https://reservoirswd.github.io/)
134. **Rethinking Cross-Spectral Image Generation via Shared-Specific Representation**  
   Haining Wang ⋅ Na Li ⋅ Huijie Zhao ⋅ Yifan Da ⋅ Yan Wen ⋅ Yi Su ⋅ Yuqiang Fang
135. **RubricRL: Simple Generalizable Rewards for Text-to-Image Generation**  
   Xuelu Feng ⋅ Yunsheng Li ⋅ Ziyu Wan ⋅ Zixuan Gao ⋅ Junsong Yuan ⋅ Dongdong Chen ⋅ Chunming Qiao  
   [arXiv:2511.20651](https://arxiv.org/abs/2511.20651)
136. **Scaling Multi-Reference Image Generation with Dynamic Reward Optimization**  
   Wenwang Huang ⋅ Yusen Fu ⋅ Mengfei Huang ⋅ Junjie Wang ⋅ Yulin Li ⋅ Gan Liu ⋅ Jing Cai ⋅ Yancheng He ⋅ Zhuotao Tian  
   [arXiv:2606.26947](https://arxiv.org/abs/2606.26947)
137. **Scientific Image Synthesis: Benchmarking, Methodologies, and Downstream Utility**  
   honglin lin ⋅ Chonghan Qin ⋅ Zheng Liu ⋅ Qizhi Pei ⋅ Yu Li ⋅ Zhanping Zhong ⋅ Xin Gao ⋅ Wei Li ⋅ Wentao Zhang ⋅ Yanfeng Wang ⋅ Conghui He ⋅ Lijun Wu  
   [arXiv:2601.17027](https://arxiv.org/abs/2601.17027)
138. **Score-Based Matching with Target Guidance for Cryo-EM Denoising**  
   Xiaoqi Wu ⋅ Xueying Zhan ⋅ Wen Li ⋅ Junhao Wu ⋅ Xin Huang ⋅ Ke Ni ⋅ Min Xu  
   [arXiv:2604.17734](https://arxiv.org/abs/2604.17734)
139. **Self-transcendence: Is External Feature Guidance Indispensable for Accelerating Diffusion Transformer Training?**  
   Lingchen Sun ⋅ Rongyuan Wu ⋅ zhengqiang ZHANG ⋅ Ruibin LI ⋅ Yujing Sun ⋅ Shuaizheng LIU ⋅ Yabin Zhang  
   [arXiv:2601.07773](https://arxiv.org/abs/2601.07773) · [code](https://github.com/csslc/Self-Transcendence)
140. **Semantic Browsing: Controllable Diversity for Image Generation**  
   Sara Dorfman ⋅ Maya Vishnevsky ⋅ Omer Dahary ⋅ Or Patashnik ⋅ Danny Cohen-Or  
   [arXiv:2606.23679](https://arxiv.org/abs/2606.23679) · [project](https://saradorfman1.github.io/SemanticBrowsing-webpage/)
141. **Setting the Stage: Text-Driven Scene-Consistent Image Generation**  
   Cong Xie ⋅ Che Wang ⋅ Yan Zhang ⋅ Ruiqi Yu ⋅ Han Zou ⋅ Zheng Pan ⋅ Zhenpeng Zhan  
   [arXiv:2512.12598](https://arxiv.org/abs/2512.12598)
142. **Shared LoRA Subspaces for almost Strict Continual Learning**  
   Prakhar Kaushik ⋅ Ankit Vaidya ⋅ Shravan Sunil Chaudhari ⋅ Rama Chellappa ⋅ Alan Yuille  
   [arXiv:2602.06043](https://arxiv.org/abs/2602.06043)
143. **Short-to-Long Functional Connectivity Transfer via Structure-Aware Latent Diffusion**  
   Ishmael Benjamin Torres Aguilar ⋅ Yufeng Liu ⋅ Zhengwu Zhang
144. **SimFlow: Simplified and End-to-End Training of Latent Normalizing Flows**  
   Qinyu Zhao ⋅ Guangting Zheng ⋅ Tao Yang ⋅ Rui Zhu ⋅ Xingjian Leng ⋅ Stephen Gould ⋅ Liang Zheng  
   [arXiv:2512.04084](https://arxiv.org/abs/2512.04084) · [project](https://qinyu-allen-zhao.github.io/SimFlow/)
145. **Solving Diffusion Inverse Problems with Restart Posterior Sampling**  
   Bilal Ahmed ⋅ Joseph Makin  
   [arXiv:2511.20705](https://arxiv.org/abs/2511.20705)
146. **Source-Agnostic Image Translation Based on Latent Aware Adaptive Masking**  
   Tomislav Dobrički ⋅ Byung-Woo Hong  
   [arXiv:2608.14046](https://arxiv.org/abs/2608.14046) · [code](https://github.com/dtoma95/PM-Edit)
147. **Spanning Tree Autoregressive Visual Generation**  
   Sangkyu Lee ⋅ Changho Lee ⋅ Janghoon Han ⋅ Hosung Song ⋅ Tackgeun You ⋅ Hwasup Lim ⋅ Stanley Jungkyu Choi ⋅ Honglak Lee ⋅ Youngjae Yu  
   [arXiv:2511.17089](https://arxiv.org/abs/2511.17089)
148. **SSDD: Single-Step Diffusion Decoder for Efficient Image Tokenization**  
   Théophane Vallaeys ⋅ Jakob Verbeek ⋅ MATTHIEU CORD  
   [arXiv:2510.04961](https://arxiv.org/abs/2510.04961)
149. **Stochastic Optimal Control Sampling for Diffusion Inverse Problems**  
   zhang jie ⋅ Youmei Qiu ⋅ Hanling Tian ⋅ Jingyuan Zhang ⋅ Xiang Yin ⋅ Xiaolin Huang  
   [arXiv:2606.28785](https://arxiv.org/abs/2606.28785)
150. **Straight-Path Flow Matching for Incomplete Multi-View Clustering**  
   Yiteng Yuan ⋅ Junyan Wang ⋅ Zheyuan Liu ⋅ Hong Jia ⋅ Lei Fan ⋅ Zhulin Tao ⋅ Lianbo Guo  
   [arXiv:2607.06281](https://arxiv.org/abs/2607.06281)
151. **Structural Assessment for Understanding and Guiding Dataset Distillation in Discrete Token Space**  
   Yue Cao ⋅ Jianyang Gu ⋅ Vyacheslav Kungurtsev ⋅ Yu Hu ⋅ Jozsef Hamari ⋅ Zheng Liu ⋅ Mohsen Zardadi  
   [arXiv:2606.21705](https://arxiv.org/abs/2606.21705)
152. **SynCity 3000: Bootstrapping Scene-Scale 3D Diffusion**  
   Paul Engstler ⋅ Iro Laina ⋅ Christian Rupprecht ⋅ Andrea Vedaldi  
   [arXiv:2607.05392](https://arxiv.org/abs/2607.05392) · [project](https://research.paulengstler.com/syncity-3k/)
153. **SynVAR: Synergizing Spatial and Semantic Alignment in Visual Autoregressive Model**  
   Zhennan Chen ⋅ Tianxing Shi ⋅ Pengcheng Xu ⋅ Kepan Nan ⋅ Qian Wang ⋅ Zili Yi ⋅ Jian Yang ⋅ Ying Tai  
   [arXiv:2608.07948](https://arxiv.org/abs/2608.07948)
154. **Test-Time Registers as Global Priors for Tokenized Image Generation**  
   Cheng-Yao Hong ⋅ Yifan Wang ⋅ Yuewei Lin ⋅ Chenyu You  
   [arXiv:2607.16824](https://arxiv.org/abs/2607.16824)
155. **TexTailor: Inference-Time Textual Guidance Tailoring for Multimodal Diffusion Transformers**  
   Binglei Li ⋅ Mengping Yang ⋅ Zhiyu Tan ⋅ Junping Zhang ⋅ Hao Li  
   [arXiv:2601.02211](https://arxiv.org/abs/2601.02211)
156. **The Illusion of High Utility in Safety Alignment of Text-to-Image Diffusion Models**  
   Adeel Yousaf ⋅ Soumik Ghosh ⋅ James Beetham ⋅ Amrit Singh Bedi ⋅ Shah Mubarak  
   [arXiv:2607.00402](https://arxiv.org/abs/2607.00402) · [project](https://adeelyousaf.github.io/SAGE_ECCV26_Project_Page/)
157. **The Map Is Not the Territory: Embedding-Coverage Blacklists for Safe Diffusion Steering**  
   Juyang Bai ⋅ Tong Zhou ⋅ Shaolei Ren ⋅ Xiaolin Xu
158. **Think in Strokes, Not Pixels: Process-Driven Image Generation via Interleaved Reasoning**  
   Lei Zhang ⋅ Junjiao Tian ⋅ Zhipeng Fan ⋅ Kunpeng Li ⋅ Jialiang Wang ⋅ Weifeng Chen ⋅ Markos Georgopoulos ⋅ Felix Juefei-Xu ⋅ Julian McAuley ⋅ Manling Li ⋅ Zecheng He  
   [arXiv:2604.04746](https://arxiv.org/abs/2604.04746)
159. **TIIF-Bench: How Does Your T2I Model Follow Your Instructions?**  
   Xinyu Wei ⋅ Jinrui Zhang ⋅ Zeqing Wang ⋅ Hongyang Wei ⋅ Zhen Guo ⋅ Bairui Li ⋅ Yabin Zhang  
   [arXiv:2506.02161](https://arxiv.org/abs/2506.02161) · [project](https://a113n-w3i.github.io/TIIF_Bench/)
160. **TiltDiff: Tilted Weight-Space Diffusion for Neural Network Generation**  
   En-Ni Chuang ⋅ Hanjuan Huang ⋅ Hao-Jia Song ⋅ Hsing-Kuo Kenneth Pao ⋅ Tyng-Luh Liu
161. **TOPA: Mitigating Concept Dominance in Diffusion Personalization via Target-Oriented Perturbation Augmentation**  
   Jiayou Lu ⋅ Mingzhi Lyu ⋅ Junfeng Huang ⋅ Wai-Kin Adams Kong
162. **Towards Consistent and Efficient Dataset Distillation via Diffusion-Driven Selection**  
   Xinhao Zhong ⋅ Shuoyang Sun ⋅ Zhaoyang Xu ⋅ Xulin Gu ⋅ Bin Chen ⋅ Min Zhang ⋅ Yaowei Wang  
   [arXiv:2412.09959](https://arxiv.org/abs/2412.09959)
163. **Training-Free Refinement of Flow Matching with Divergence-based Sampling**  
   Yeonwoo Cha ⋅ Jaehoon Yoo ⋅ Semin Kim ⋅ Yunseo Park ⋅ Jinhyeon Kwon ⋅ Seunghoon Hong  
   [arXiv:2604.04646](https://arxiv.org/abs/2604.04646) · [project](https://yeonwoo378.github.io/official_fds)
164. **TreeSRNF: Square-Root Normal Fields for Generative Modelling of the Geometric and Structural Variability in Tree-like 3D Objects**  
   Tahmina Khanam ⋅ Hamid Laga ⋅ Mohammed Bennamoun ⋅ Guanjin Wang ⋅ Ferdous Sohel ⋅ Farid Boussaid ⋅ Anuj Srivastava  
   [arXiv:2607.13456](https://arxiv.org/abs/2607.13456)
165. **Trust-Region Noise Search for Black-Box Alignment of Diffusion and Flow Models**  
   Niklas Schweiger ⋅ Karnik Ram ⋅ Daniel Cremers  
   [arXiv:2603.14504](https://arxiv.org/abs/2603.14504)
166. **UltraGen: Efficient Ultra-High-Resolution Image Generation with Hierarchical Local Attention**  
   Yuyao Zhang ⋅ Yu-Wing Tai
167. **UniCSG: Unified High-Fidelity content-constrained style-driven generation via Staged Semantic and Frequency Disentanglement**  
   Jingwei Yang ⋅ Ruoxi Wu ⋅ Wei Shen ⋅ Meng Li ⋅ Yulong Liu ⋅ Huimin She ⋅ Lunxi Yuan  
   [arXiv:2604.17850](https://arxiv.org/abs/2604.17850)
168. **UniGP: Taming Diffusion Transformer for Prior-Preserved Unified Generation and Perception**  
   Qin Guo ⋅ Hao Luo ⋅ Dongxu Yue ⋅ Weixuan Jin ⋅ Xiao Fu ⋅ Fan Wang ⋅ Dan Xu  
   [arXiv:2606.30332](https://arxiv.org/abs/2606.30332)
169. **UNITY: Attention Flow Networks for Adaptive Conditioning in Diffusion**  
   Aryan Das ⋅ Koushik Biswas ⋅ Moloud Abdar ⋅ Vinay Kumar Verma
170. **VC-VAE: Leveraging Video Codecs for Training-Efficient and High-Fidelity Video VAE**  
   Xinxu Ge ⋅ Shang Chai ⋅ Litong Gong ⋅ Zitong Yu ⋅ Xin Liu ⋅ Tiezheng Ge
171. **VD-LoRA: Adaptive Reuse of Low-Rank Directions for Continual Learning**  
   Luqiong Ding ⋅ Jiayao Tan ⋅ Chenggong Ni ⋅ Fuyuan Hu ⋅ Fan Lyu
172. **Vector Scaffolding: Inter-Scale Orchestration for Differentiable Image Vectorization**  
   Jaerin Lee ⋅ KANGGEON LEE ⋅ Kyoung Mu Lee  
   [arXiv:2605.11913](https://arxiv.org/abs/2605.11913)
173. **Vitality-Aware Compression for Efficient Image-to-Shape Diffusion Transformers**  
   Jaeah Lee ⋅ Hyunjin Kim ⋅ Jaewoong Cho ⋅ Gihyun Kwon  
   [arXiv:2607.00382](https://arxiv.org/abs/2607.00382)
174. **When Higher Order Hurts: Pre-Asymptotic Order Collapse in Generative ODE Sampling — A Theory of Discretization–Learning Interaction**  
   Farzad Salajegheh ⋅ Sudhir Mudur
175. **WinTok: A Win-Win Hybrid Tokenizer via Decomposing Visual Understanding and Generation with Transferable Tokens**  
   Yiwei Guo ⋅ Shaobin Zhuang ⋅ Zhipeng Huang ⋅ Canmiao Fu ⋅ Chen Li ⋅ Jing LYU ⋅ Yali Wang  
   [arXiv:2605.18115](https://arxiv.org/abs/2605.18115) · [code](https://github.com/markywg/WinTok)
176. **WorldMesh: Generating Navigable Multi-Room 3D Scenes via Mesh-Conditioned Image Diffusion**  
   Manuel-Andreas Schneider ⋅ Angela Dai  
   [arXiv:2603.22972](https://arxiv.org/abs/2603.22972) · [code](https://github.com/mschneider456/worldmesh) · [project](https://mschneider456.github.io/world-mesh/)
177. **Y-diff: Structure-Texture Decoupled Diffusion Distillation for H&amp;E-to-pCLE Translation**  
   Haodong Wang ⋅ Yan Wen ⋅ Hongen Liao ⋅ Fang Chen ⋅ Tianqi Huang
178. **Zero-Shot Image Personalization from Personas**  
   Harini S I ⋅ Somesh Singh ⋅ Yaman Singla ⋅ David Doermann ⋅ Rajiv Shah

## Video Generation & World Models

*131 papers · 89 with links*

1. **A Benchmark and Multi-Agent System for Instruction-driven Cinematic Video Compilation**  
   Peixuan Zhang ⋅ Chang Zhou ⋅ Ziyuan Zhang ⋅ Hualuo Liu ⋅ Chunjie Zhang ⋅ Jingqi Liu ⋅ Xiaohui Zhou ⋅ Xi Chen ⋅ Shuchen Weng ⋅ Si Li ⋅ Boxin Shi  
   [arXiv:2604.10456](https://arxiv.org/abs/2604.10456)
2. **A Physics-Grounded Benchmark for Multi-Agent Dynamics in World Models**  
   Nuo Chen ⋅ Lulin Liu ⋅ Zihao Li ⋅ Ziyao Zeng ⋅ Zihao Zhu ⋅ Wenyan Cong ⋅ Junyuan Hong ⋅ Yunhao Yang ⋅ Zhengzhong Tu ⋅ Yan Wang ⋅ Boris Ivanovic ⋅ Marco Pavone ⋅ Zhangyang Wang ⋅ Yang Zhou ⋅ Zhiwen Fan  
   [arXiv:2606.28757](https://arxiv.org/abs/2606.28757)
3. **Aligning Anything: Hierarchical Motion Estimation for Video Frame Interpolation**  
   Mengshun Hu ⋅ Zhihang Zhong ⋅ Yansheng Qiu ⋅ Zheng Wang ⋅ Xiao Sun
4. **Aligning Human Sense: Calibrated Distributional Reward Learning for Video Generation**  
   Naixin Zhai ⋅ Weihua Cheng ⋅ Dexu Yu ⋅ Yikai Gu ⋅ Hanwen Du ⋅ Junchen Fu ⋅ Chenxi Huang ⋅ Yingwei Song ⋅ Liyuan Ma ⋅ Yang Ran ⋅ Youhua Li ⋅ Yongxin Ni
5. **Anchored Video Generation: Decoupling Scene Construction and Temporal Synthesis in Text-to-Video Diffusion Models**  
   Mariam Hassan ⋅ Bastien van Delft ⋅ Wuyang Li ⋅ Alexandre ALahi  
   [arXiv:2512.16371](https://arxiv.org/abs/2512.16371)
6. **AnchorWeave: World-Consistent Video Generation with Retrieved Local Spatial Memories**  
   Zun Wang ⋅ Han Lin ⋅ Jaehong Yoon ⋅ Jaemin Cho ⋅ Yue Zhang ⋅ Mohit Bansal  
   [arXiv:2602.14941](https://arxiv.org/abs/2602.14941) · [project](https://zunwang1.github.io/AnchorWeave)
7. **Anti-Prompt: Image Protection against Text-Guided Image-to-Video Generation**  
   Yeonghwan Song ⋅ Chanhui Lee ⋅ Jinsoo Park ⋅ Jeany Son  
   [arXiv:2607.01499](https://arxiv.org/abs/2607.01499)
8. **AnyFlow: Any-Step Video Diffusion Model with On-Policy Flow Map Distillation**  
   Yuchao Gu ⋅ Guian Fang ⋅ Yuxin Jiang ⋅ Weijia Mao ⋅ Song Han ⋅ Han Cai ⋅ Mike Zheng Shou  
   [arXiv:2605.13724](https://arxiv.org/abs/2605.13724) · [project](https://nvlabs.github.io/AnyFlow/)
9. **AR-CoPO: Align Autoregressive Video Generation with Contrastive Policy Optimization**  
   Dailan He ⋅ Guanlin Feng ⋅ Xingtong Ge ⋅ Yi ZHANG ⋅ Bingqi Ma ⋅ Guanglu Song ⋅ Yu Liu ⋅ Hongsheng LI  
   [arXiv:2603.17461](https://arxiv.org/abs/2603.17461)
10. **Benchmarking Scientific Understanding and Reasoning for Video Generation using VideoScience-Bench**  
   Lanxiang Hu ⋅ Abhilash Shankarampeta ⋅ Yixin Huang ⋅ Zilin Dai ⋅ Haoyang Yu ⋅ Yujie Zhao ⋅ Haoqiang Kang ⋅ Daniel Zhao ⋅ Tajana Rosing ⋅ Hao Zhang  
   [arXiv:2512.02942](https://arxiv.org/abs/2512.02942) · [code](https://github.com/hao-ai-lab/VideoScience)
11. **Better Call CineCrew: Consistent Ultra-Long Narrative-to-Film Generation**  
   Jiaben Chen ⋅ Sixun Dong ⋅ Qinhong Zhou ⋅ Raine Ma ⋅ Zhiyang Dou ⋅ Wojciech Matusik ⋅ Chuang Gan
12. **Beyond Dense Futures: World Models as Structured Planners for Robotic Manipulation**  
   Minghao Jin ⋅ Mozheng Liao ⋅ Mingfei Han ⋅ Zhihui Li ⋅ Xiaojun Chang  
   [arXiv:2603.12553](https://arxiv.org/abs/2603.12553)
13. **Counterfactual World Models via Digital Twin-conditioned Video Diffusion**  
   Yiqing Shen ⋅ Aiza Maksutova ⋅ Chenjia Li ⋅ Mathias Unberath  
   [arXiv:2511.17481](https://arxiv.org/abs/2511.17481)
14. **CustomX: Unified Character, Action, and Scene Customization in Video World Models**  
   Yitong Wang ⋅ Fangyun Wei ⋅ Hongyang Zhang ⋅ Bo Dai ⋅ Yan Lu  
   [arXiv:2512.17796](https://arxiv.org/abs/2512.17796) · [project](https://snowflakewang.github.io/CustomX_Page/)
15. **Cycle-World: Mitigating Error Accumulation in Long-term Video World Models via Reverse-Prediction Cycle Consistency**  
   Zihan Su ⋅ Teng Hu ⋅ Jiangning Zhang ⋅ Ruiyan Wang ⋅ Ran Yi ⋅ Lizhuang Ma ⋅ Dacheng Tao  
   [arXiv:2607.11836](https://arxiv.org/abs/2607.11836)
16. **DCARL: A Divide-and-Conquer Framework for Autoregressive Long-Trajectory Video Generation**  
   Junyi Ouyang ⋅ Wenbin Teng ⋅ Gonglin Chen ⋅ Yajie Zhao ⋅ Haiwei Chen  
   [arXiv:2603.24835](https://arxiv.org/abs/2603.24835) · [project](https://junyiouy.github.io/projects/dcarl)
17. **DeforM: Reasoning-Guided Physics-Aware Video Generation via Spatial-Temporal Masking**  
   Yunyi Li ⋅ Yu Qiao ⋅ Yaohui Wang ⋅ Xinyuan Chen
18. **Describe-Then-Act: Proactive Agent Steering via Distilled Language-Action World Models**  
   Massimiliano Pappa ⋅ Luca Romani ⋅ Valentino Sacco ⋅ Alessio Palma ⋅ Stéphane Lathuilière ⋅ Fabio Galasso ⋅ Xavier Alameda-Pineda ⋅ Indro Spinelli  
   [arXiv:2603.23149](https://arxiv.org/abs/2603.23149)
19. **DiffHDR: Re-Exposing LDR Videos with Video Diffusion Models**  
   Zhengming Yu ⋅ Li Ma ⋅ Mingming He ⋅ Leo Isikdogan ⋅ Yuancheng Xu ⋅ Dmitriy Smirnov ⋅ Pablo Salamanca ⋅ Dao Mi ⋅ Pablo Delgado ⋅ Ning Yu ⋅ Julien Philip ⋅ Xin Li ⋅ Wenping Wang ⋅ Paul Debevec  
   [arXiv:2604.06161](https://arxiv.org/abs/2604.06161)
20. **DIVER: Disentangling Camera–Object and Active–Passive Motion for Video Generation**  
   Shaowei Liu ⋅ Xuanchi Ren ⋅ Tianchang Shen ⋅ Huan Ling ⋅ Saurabh Gupta ⋅ Shenlong Wang ⋅ Sanja Fidler ⋅ Jun Gao
21. **Divide and Conquer: Decoupled Representation Alignment for Multimodal World Models**  
   Junyuan Xiao ⋅ Dingkang Liang ⋅ Xin Zhou ⋅ Yixuan Ye ⋅ Tongtong Su ⋅ Guangmo Yi ⋅ Bin Xia ⋅ Qiang Lyu ⋅ Shurui Shi ⋅ Jun Huang ⋅ Jianlou Si ⋅ Wenming Yang
22. **DreamWorld: Geometry-Grounded Video Diffusion for 3D-Consistent World Modeling**  
   Haibo Yang ⋅ Yang Chen ⋅ Yingwei Pan ⋅ Zhineng Chen ⋅ Ting Yao ⋅ Tao Mei
23. **DVG-WM: Disentangled Video Generation Enables Efficient Embodied World Model for Robotic Manipulation**  
   Ziyu Shan ⋅ Zhenyu Wu ⋅ Xiaofeng Wang ⋅ Zheng Zhu ⋅ Ziwei Wang  
   [arXiv:2606.32028](https://arxiv.org/abs/2606.32028)
24. **EcoVideo: Entropy-Orchestrated Video Generation Paradigm in Cloud-Edge Dynamics**  
   Jiayu Chen ⋅ Hengyi Zhang ⋅ Maoliang Li ⋅ Minyu Li ⋅ Zihao Zheng ⋅ Xuanzhe Liu ⋅ Guojie Luo ⋅ Xiang Chen  
   [arXiv:2606.30557](https://arxiv.org/abs/2606.30557) · [code](https://github.com/IF-LAB-PKU/EcoVideo)
25. **End-to-End Training for Autoregressive Video Diffusion via Self-Resampling**  
   Yuwei Guo ⋅ Ceyuan Yang ⋅ Hao He ⋅ Yang Zhao ⋅ Meng Wei ⋅ Zhenheng Yang ⋅ Weilin Huang ⋅ Dahua Lin  
   [arXiv:2512.15702](https://arxiv.org/abs/2512.15702) · [project](https://guoyww.github.io/projects/resampling-forcing/)
26. **Evaluating Reasoning Coherence in Video Generative Models with Text and Visual Hints**  
   Yu Qi ⋅ Xinyi Xu ⋅ Ziyu Guo ⋅ Siyuan Ma ⋅ Renrui Zhang ⋅ Xinyan Chen ⋅ Ruichuan An ⋅ Ruofan Xing ⋅ Jiayi Zhang ⋅ Haojie Huang ⋅ Pheng-Ann Heng ⋅ Jonathan Tremblay ⋅ Lawson Wong  
   [arXiv:2603.20194](https://arxiv.org/abs/2603.20194) · [project](https://video-reasoning-coherence.github.io/)
27. **Event-Driven Video Generation**  
   Chika Maduabuchi ⋅ Jindong Wang  
   [arXiv:2603.13402](https://arxiv.org/abs/2603.13402) · [project](https://evd-project-website.pages.dev)
28. **FlexAM: Flexible Appearance-Motion Decomposition for Versatile Video Generation Control**  
   Mingzhi Sheng ⋅ Zekai Gu ⋅ Peng Li ⋅ Cheng Lin ⋅ Hao-Xiang Guo ⋅ Yingcong Chen ⋅ Yuan Liu  
   [arXiv:2602.13185](https://arxiv.org/abs/2602.13185) · [code](https://github.com/IGL-HKUST/FlexAM)
29. **Following Motion for Sequential Modeling in Video Frame Interpolation**  
   JaeHyun Park ⋅ Nam Ik Cho
30. **FreeSwim: Revisiting Sliding-Window Attention Mechanisms for Training-Free Ultra-High-Resolution Video Generation**  
   Yunfeng Wu ⋅ Jiayi Song ⋅ Zhenxiong Tan ⋅ Zihao He ⋅ Songhua Liu  
   [arXiv:2511.14712](https://arxiv.org/abs/2511.14712) · [code](https://github.com/WillWu111/FreeSwim)
31. **GeCo: Evaluating Geometric Consistency for Video Generation via Motion and Structure**  
   Leslie Gu ⋅ Junhwa Hur ⋅ Charles Herrmann ⋅ Fangneng Zhan ⋅ Todd Zickler ⋅ Deqing Sun ⋅ Hanspeter Pfister  
   [arXiv:2512.22274](https://arxiv.org/abs/2512.22274)
32. **Goku: A Million-Scale Universal Dataset and Benchmark for Instruction-Based Video Editing**  
   Sen Liang ⋅ Cong Wang ⋅ Zhentao Yu ⋅ Fengbin Guan ⋅ zhengguang zhou ⋅ Teng Hu ⋅ youliang zhang ⋅ Yuan Zhou ⋅ Xin Li ⋅ Qinglin Lu ⋅ Zhibo Chen  
   [arXiv:2606.30599](https://arxiv.org/abs/2606.30599) · [project](https://flying-sky999.github.io/Goku.github.io/)
33. **GraphVid: Interactive Graph-Controllable Video Generation**  
   Vedant Shah ⋅ Onkar Susladkar ⋅ Tushar Prakash ⋅ Kiet Nguyen ⋅ Tianjiao (Joey) Yu ⋅ Adheesh Juvekar ⋅ Muntasir Wahed ⋅ Ismini Lourentzou  
   [arXiv:2607.21580](https://arxiv.org/abs/2607.21580)
34. **HiAR: Efficient Autoregressive Long Video Generation via Hierarchical Denoising**  
   Kai Zou ⋅ Dian Zheng ⋅ Hongbo Liu ⋅ Tiankai Hang ⋅ Bin Liu ⋅ Nenghai Yu  
   [arXiv:2603.08703](https://arxiv.org/abs/2603.08703) · [code](https://github.com/Jacky-hate/HiAR) · [project](https://jacky-hate.github.io/HiAR/)
35. **IC-World: In-Context Generation for Shared World Modeling**  
   FAN WU ⋅ Jiacheng Wei ⋅ Ruibo Li ⋅ Yi Xu ⋅ junyou li ⋅ Deheng Ye ⋅ Guosheng Lin  
   [arXiv:2512.02793](https://arxiv.org/abs/2512.02793) · [code](https://github.com/wufan-cse/IC-World)
36. **Inference-time Motion Calibration for Video Generation**  
   Zile Huang ⋅ Ser-Nam Lim
37. **Joint Alignment and Distillation for Video Generation via Sample-Guided Distribution Matching**  
   Jiuzhou Lin ⋅ Fei Zuo ⋅ Huan Ouyang ⋅ Junlong Wu ⋅ Dewen Fan ⋅ Boheng Zhang ⋅ Huaiqing Wang ⋅ Jia Sun ⋅ Fan Yang ⋅ Houde Liu ⋅ Kehai Chen ⋅ Min Zhang ⋅ Tingting Gao ⋅ Han Li
38. **KineBench: Benchmarking Embodied World Models via IDM-Free Kinematic Grounding**  
   Zeyu Liu ⋅ Zhangzhe Zhu ⋅ Yang Zhang ⋅ Chenyou Fan ⋅ Chenjia Bai ⋅ Xuelong Li  
   [arXiv:2607.19876](https://arxiv.org/abs/2607.19876)
39. **LatSearch: Latent Reward-Guided Search for Faster Inference-Time Scaling in Video Diffusion**  
   Zengqun Zhao ⋅ Ziquan Liu ⋅ Yu Cao ⋅ Shaogang Gong ⋅ Zhensong Zhang ⋅ Song Jifei ⋅ Jiankang Deng ⋅ ioannis Patras  
   [arXiv:2603.14526](https://arxiv.org/abs/2603.14526) · [project](https://zengqunzhao.github.io/LatSearch)
40. **Learning to Generate Rigid Body Interactions with Video Diffusion Models**  
   David Orlando Romero Mogrovejo ⋅ Ariana Bermudez ⋅ Viacheslav Iablochnikov ⋅ Hao Li ⋅ Fabio Pizzati ⋅ Ivan Laptev  
   [arXiv:2510.02284](https://arxiv.org/abs/2510.02284) · [project](https://daromog.github.io/KineMask/)
41. **Learning Transferable Dynamics Priors from Action to World Modeling**  
   Ze Huang ⋅ Zhang Jiahui ⋅ Hairuo Liu ⋅ Chenxi Zhang ⋅ Ran Cheng ⋅ Li Zhang  
   [arXiv:2606.29501](https://arxiv.org/abs/2606.29501)
42. **Learning Zero-Shot Subject-Driven Video Generation Using 1% Compute**  
   Daneul Kim ⋅ Jingxu Zhang ⋅ Wonjoon Jin ⋅ Sunghyun Cho ⋅ Qi Dai ⋅ Jaesik Park ⋅ Chong Luo  
   [arXiv:2504.17816](https://arxiv.org/abs/2504.17816) · [project](https://carpedkm.github.io/projects/disentangled_sub/index.html)
43. **LibraGen: Playing a Balance Game in Subject-Driven Video Generation**  
   Jiahao Zhu ⋅ Shanshan Lao ⋅ Lijie Liu ⋅ Gen Li ⋅ Tianhao Qi ⋅ hanwei hanwei ⋅ Bingchuan Li ⋅ FangfangLiu FangfangLiu ⋅ Zhuowei Chen ⋅ Tianxiang Ma ⋅ Qian HE ⋅ Yi Zhou ⋅ Xiaohua Xie  
   [arXiv:2603.13506](https://arxiv.org/abs/2603.13506)
44. **LooseControlVideo: Directorial Video Control using Spatial Blocking**  
   Shariq Farooq Bhat ⋅ Kalyan Sunkavalli ⋅ Niloy Mitra  
   [arXiv:2606.19495](https://arxiv.org/abs/2606.19495) · [project](https://shariqfarooq123.github.io/LooseControlVideo/)
45. **LoT-Pass: Long-term-robust Image Watermarking for Image to Video Generation**  
   Guanjie Wang ⋅ Zehua Ma ⋅ Han Fang ⋅ Weiming Zhang  
   [arXiv:2509.17773](https://arxiv.org/abs/2509.17773) · [code](https://github.com/MrCrims/I2VWM-Robust-Watermarking-for-Image-to-Video-Generation)
46. **MagicPrompt: Ultra-Lightweight Prompt Tuning for Video Generation**  
   Yinhan Zhang ⋅ DINGWEI TAN ⋅ Xianghao Kong ⋅ Yue Ma ⋅ Yeying Jin ⋅ Anyi Rao  
   [arXiv:2607.14595](https://arxiv.org/abs/2607.14595)
47. **Measuring 3D Spatial Geometric Consistency in Dynamic Video Generation**  
   Weijia Dou ⋅ Wenzhao Zheng ⋅ Weiliang Chen ⋅ Yu Zheng ⋅ Jie Zhou ⋅ Jiwen Lu  
   [arXiv:2603.19048](https://arxiv.org/abs/2603.19048) · [code](https://github.com/tj12323/SGC)
48. **MemLearner: Learning to Query Context Memory for Video World Models**  
   Jiwen Yu ⋅ Jianxiong Gao ⋅ Jianhong Bai ⋅ Yiran Qin ⋅ Kaiyi Huang ⋅ Quande Liu ⋅ Xintao Wang ⋅ Pengfei Wan ⋅ Kun Gai ⋅ Xihui Liu  
   [arXiv:2606.31734](https://arxiv.org/abs/2606.31734) · [project](https://yujiwen.github.io/memlearner/)
49. **MemoBench: Benchmarking World Modeling in Dynamically Changing Environments**  
   Haoyu Chen ⋅ Kaichen Zhou ⋅ Hang Hua ⋅ Kaile Zhang ⋅ Jingwen Qian ⋅ Wufei Ma ⋅ Haonan Chen ⋅ Chunjiang Liu ⋅ Yizhou Zhao ⋅ Xiaoyuan Wang ⋅ Weiyue Li ⋅ Alan Yuille ⋅ Paul Pu Liang ⋅ Yilun Du  
   [arXiv:2606.27537](https://arxiv.org/abs/2606.27537)
50. **Memory-V2V: Memory-Augmented Video-to-Video Diffusion for Consistent Multi-Turn Editing**  
   Dohun Lee ⋅ Chun-Hao Huang ⋅ Xuelin Chen ⋅ Jong Chul Ye ⋅ Duygu Ceylan ⋅ Hyeonho Jeong  
   [arXiv:2601.16296](https://arxiv.org/abs/2601.16296) · [project](https://dohunlee1.github.io/MemoryV2V)
51. **MemRoPE: Training-Free Infinite Video Generation via Evolving Memory Tokens**  
   Youngrae Kim ⋅ Qixin Hu ⋅ C.-C. Jay Kuo ⋅ Peter Beerel  
   [arXiv:2603.12513](https://arxiv.org/abs/2603.12513) · [project](https://memrope.github.io)
52. **MoGAN: Improving Motion Quality in Video Diffusion via Few-Step Motion Adversarial Post-Training**  
   Haotian Xue ⋅ Qi Chen ⋅ Zhonghao Wang ⋅ Xun Huang ⋅ Eli Shechtman ⋅ Jinrong Xie ⋅ Yongxin Chen  
   [arXiv:2511.21592](https://arxiv.org/abs/2511.21592) · [project](https://xavihart.github.io/mogan)
53. **Moiré Video Authentication: A Physical Signature Against AI Video Generation**  
   Yuan Qing ⋅ Kunyu Zheng ⋅ Lingxiao Li ⋅ Boqing Gong ⋅ Chang Xiao
54. **MoVA: Learning Asymmetric Dual Projections for Modular Long Video-Text Alignment**  
   Peiyuan Zhu ⋅ Shaoan Xie ⋅ Zijian Li ⋅ Yifan Shen ⋅ Namrata Deka ⋅ Harsh Shrivastava ⋅ Guangyi Chen ⋅ Kun Zhang  
   [arXiv:2607.00858](https://arxiv.org/abs/2607.00858)
55. **MSEditor: Toward Consistent Multi-Shot Video Editing**  
   Kunyu Feng ⋅ Yue Ma ⋅ Bingyuan Wang ⋅ Yuefeng Wang ⋅ Zhiyuan Qin ⋅ Hao Cheng ⋅ Hao Li ⋅ Qifeng Chen ⋅ Zeyu Wang
56. **Multi-scale Mixture of World Models for Embodied Agents in Evolving Environments**  
   Jinwoo Jang ⋅ Daniel Rho ⋅ Sihyung Yoon ⋅ Hyunsuk Cho ⋅ Honguk Woo  
   [arXiv:2607.00457](https://arxiv.org/abs/2607.00457)
57. **NarrativeTrack: Evaluating Entity-Centric Reasoning for Narrative Understanding**  
   Hyeonjeong Ha ⋅ Jinjin Ge ⋅ Bo Feng ⋅ Kaixin Ma ⋅ Gargi Chakraborty  
   [arXiv:2601.01095](https://arxiv.org/abs/2601.01095) · [code](https://github.com/apple/ml-NarrativeTrack)
58. **NoisEasier: Test-Time Noise Optimization for Text-to-Video Generation**  
   Yujiang Pu ⋅ Yu Kong
59. **OctWorld: Long-Range World-Consistent Video Generation with Octree-based 3D Mapping**  
   Zelong Lv ⋅ Sicheng Xu ⋅ Jianfeng Xiang ⋅ Yue Dong ⋅ Ruicheng Wang ⋅ Yu Deng ⋅ Guangzhong Sun ⋅ Jiaolong Yang
60. **OmniHuman: A Large-scale Dataset and Benchmark for Human-Centric Video Generation**  
   Lei Zhu ⋅ xing cai ⋅ Yingjie Chen ⋅ Li YiHeng ⋅ Binxin Yang ⋅ Hao Liu ⋅ Jie Chen ⋅ Chen Li ⋅ Jing LYU  
   [arXiv:2604.18326](https://arxiv.org/abs/2604.18326)
61. **One Video, One World: Turning Monocular Video into Physical 4D Scenes**  
   Junhao Chen ⋅ Boran Zhang ⋅ Mingjin Chen ⋅ Henghaofan Zhang ⋅ Saining Zhang ⋅ Congcong Zhu ⋅ HAO ZHAO ⋅ Ruqi Huang ⋅ Zhihao Li ⋅ Yufei Wang  
   [arXiv:2606.31388](https://arxiv.org/abs/2606.31388) · [project](https://OneVideoOneWorld.github.io/)
62. **OpenVE-3M: A Large-Scale High-Quality Dataset for Instruction-Based Video Editing**  
   Haoyang He ⋅ Jie Wang ⋅ Jiangning Zhang ⋅ Zhucun Xue ⋅ Xingyuan Bu ⋅ Qiangpeng Yang ⋅ Min Zheng ⋅ Lei Xie  
   [arXiv:2512.07826](https://arxiv.org/abs/2512.07826) · [project](https://lewandofskee.github.io/projects/OpenVE)
63. **Optimizing Mesh Animation from Video via Shape Flow Guidance**  
   Jingqiao Xiu ⋅ Yicong Li ⋅ Angela Yao
64. **OSVE: One Step Video Editing with One Step Diffusion Models**  
   Habin Lim ⋅ Gyeong-Moon Park  
   [arXiv:2607.19895](https://arxiv.org/abs/2607.19895) · [code](https://github.com/KU-VGI/OSVE)
65. **Out of Sight, Out of Mind? Evaluating State Evolution in Video World Models**  
   Ziqi Ma ⋅ Mengzhan Liufu ⋅ Georgia Gkioxari  
   [arXiv:2603.13215](https://arxiv.org/abs/2603.13215) · [project](https://glab-caltech.github.io/STEVOBench/) · [project](https://ziqi-ma.github.io/blog/2026/outofsight/)
66. **PackForcing: Short Video Training Suffices for Long Video Sampling and Long Context Inference**  
   Xiaofeng Mao ⋅ Shaohao Rui ⋅ Bo Zheng ⋅ Kaining Ying ⋅ Chuanhao Li ⋅ Mingmin Chi ⋅ Kaipeng Zhang  
   [arXiv:2603.25730](https://arxiv.org/abs/2603.25730) · [code](https://github.com/ShandaAI/PackForcing)
67. **PAI-Studio: Cinematic Video Background Replacement with Camera-Aware Motion**  
   Heyuan Gao ⋅ Bangxun Tang ⋅ Yiren Song ⋅ Guian Fang ⋅ Zijian He ⋅ Jie Yang ⋅ Mike Zheng Shou  
   [arXiv:2606.01399](https://arxiv.org/abs/2606.01399)
68. **Pathwise Test-Time Correction for Autoregressive Long Video Generation**  
   Xunzhi Xiang ⋅ Zixuan Duan ⋅ Guiyu Zhang ⋅ Haiyu Zhang ⋅ Zhe Gao ⋅ Junta Wu ⋅ Shaofeng Zhang ⋅ Tengfei Wang ⋅ Qi Fan ⋅ Chunchao Guo  
   [arXiv:2602.05871](https://arxiv.org/abs/2602.05871)
69. **PeCA: Palette Context Assisted Inference for Test-Time Paint-Bucket Colourisation on Animation Videos**  
   Dongheng Lin ⋅ Jianbo Jiao  
   [arXiv:2608.00903](https://arxiv.org/abs/2608.00903) · [project](https://rathgrith.github.io/PeCA/)
70. **PhyDetEx: Detecting and Explaining the Physical Plausibility of T2V Models**  
   Zeqing Wang ⋅ Keze Wang ⋅ Yabin Zhang  
   [arXiv:2512.01843](https://arxiv.org/abs/2512.01843) · [code](https://github.com/Zeqing-Wang/PhyDetEx)
71. **PhyGDPO: Physics-Aware Groupwise Direct Preference Optimization for Physically Consistent Text-to-Video Generation**  
   Yuanhao Cai ⋅ Kunpeng Li ⋅ Menglin Jia ⋅ Jialiang Wang ⋅ Junzhe Sun ⋅ Feng Liang ⋅ Weifeng Chen ⋅ Felix Juefei-Xu ⋅ Chu Wang ⋅ Ali Thabet ⋅ Xiaoliang Dai ⋅ Xuan JU ⋅ Alan Yuille ⋅ Ji Hou  
   [arXiv:2512.24551](https://arxiv.org/abs/2512.24551) · [code](https://github.com/caiyuanhao1998/Open-PhyGDPO) · [project](https://caiyuanhao1998.github.io/project/PhyGDPO)
72. **PhysAlign: Learning Physical Priors for Dynamical Event-Driven Video Generation via Representation Alignment**  
   Mengxian Li ⋅ Zhan Wang ⋅ Fan Qi ⋅ Changsheng Xu
73. **PhysChoreo: Physics-Controllable Video Generation with Part-Aware Semantic Grounding**  
   Haoze Zhang ⋅ Tianyu Huang ⋅ Zichen Wan ⋅ Xiaowei Jin ⋅ Hongzhi Zhang ⋅ Hui Li ⋅ Wangmeng Zuo  
   [arXiv:2511.20562](https://arxiv.org/abs/2511.20562)
74. **Physics Question Scene Graph: Fine-grained Evaluation of Physical Plausibility in Text-to-Video Generation**  
   Atin Pothiraj ⋅ Jaemin Cho ⋅ Yue Zhang ⋅ Elias Stengel-Eskin ⋅ Mohit Bansal  
   [arXiv:2606.25306](https://arxiv.org/abs/2606.25306) · [code](https://github.com/atinpothiraj/pqsg)
75. **PhysMani: Physics-principled 3D World Model for Dynamic Object Manipulation**  
   Peng Yun ⋅ Shouwang Huang ⋅ Hao Li ⋅ Jinxi Li ⋅ Jianan Wang ⋅ Bo Yang  
   [arXiv:2607.01938](https://arxiv.org/abs/2607.01938) · [code](https://github.com/vLAR-group/PhysMani)
76. **PhysPO: Physics-Aware Local Preference Optimization for Physically Consistent Video Diffusion**  
   Zhuoran Yang ⋅ Yanyong Zhang
77. **PhysRAG: Enhancing Physics-Awareness in Video Generation via Retrieval-Augmented Generation**  
   Kexu Cheng ⋅ Zicheng Liu ⋅ Mingju Gao ⋅ Chunhe Song ⋅ Hao Tang  
   [arXiv:2606.26916](https://arxiv.org/abs/2606.26916) · [code](https://github.com/sediment1024/PhysRAG)
78. **PhysRVG: Physics-Aware Unified Reinforcement Learning for Video Generative Models**  
   Qiyuan Zhang ⋅ Biao Gong ⋅ Shuai Tan ⋅ Zheng Zhang ⋅ Xing Zhu ⋅ Yujun Shen ⋅ Yuyuan Li ⋅ kelu Yao ⋅ Chunhua Shen ⋅ Changqing Zou  
   [arXiv:2601.11087](https://arxiv.org/abs/2601.11087)
79. **Predicting Consequences and Reinforcing Navigation Policies with Latent World Models**  
   Zengmao Wang ⋅ Wei Gao ⋅ Shuhan Shen
80. **Predictive Structure Improves Video Diffusion Dynamics**  
   Mi Luo ⋅ Yujia Chen ⋅ Alex Dimakis ⋅ Kristen Grauman ⋅ Wen-Sheng Chu ⋅ Du Tran
81. **Prompt2Effect: Training-Free LoRA Synthesis for Controllable Video Effects**  
   Xiaomeng Yang ⋅ Yanyu Li ⋅ Gordon Qian ⋅ Ivan Skorokhodov ⋅ Viacheslav Ivanov ⋅ Avalon Vinella ⋅ Xuan Zhang ⋅ Yanzhi Wang ⋅ Sergey Tulyakov ⋅ Anil Kag
82. **QWERTY: Training-Free Motion Control via Query-Warped Video Diffusion Transformers**  
   Kyobin Choo ⋅ Youngmin Kim ⋅ Hyunkyung Han ⋅ Geunrip Park ⋅ Chanyoung Kim ⋅ Sunyoung Jung ⋅ Seong Jae Hwang  
   [arXiv:2607.01869](https://arxiv.org/abs/2607.01869)
83. **RAE-NWM: Navigation World Model in Dense Visual Representation Space**  
   Mingkun Zhang ⋅ wangtian shen ⋅ Fan Zhang ⋅ Haijian Qin ⋅ Zihao Pei ⋅ Ziyang Meng  
   [arXiv:2603.09241](https://arxiv.org/abs/2603.09241) · [code](https://github.com/20robo/raenwm)
84. **RefAlign: Representation Alignment for Reference-to-Video Generation**  
   Lei Wang ⋅ YuXin Song ⋅ Ge Wu ⋅ Haocheng Feng ⋅ Hang Zhou ⋅ Jingdong Wang ⋅ Yaxing Wang ⋅ Jian Yang  
   [arXiv:2603.25743](https://arxiv.org/abs/2603.25743) · [code](https://github.com/gudaochangsheng/RefAlign) · [project](https://gudaochangsheng.github.io/RefAlign-Page/)
85. **Representations Before Pixels: Semantics-Guided Hierarchical Video Prediction**  
   Efstathios Karypidis ⋅ Spyros Gidaris ⋅ Nikos Komodakis  
   [arXiv:2604.11707](https://arxiv.org/abs/2604.11707) · [code](https://github.com/Sta8is/Re2Pix)
86. **Reward Lightning: Fast Video Generation via Homologous Preference Distillation**  
   Jiaxiang Cheng ⋅ bing ma ⋅ Xuhua Ren ⋅ Kai Yu ⋅ Peng Zhang ⋅ Tianxiang Zheng ⋅ Qinglin Lu  
   [arXiv:2607.03960](https://arxiv.org/abs/2607.03960) · [project](https://reward-lightning.github.io)
87. **Ring Forcing: Towards Precise Long-Term Memory for Autoregressive Video Diffusion**  
   Bowen Xue ⋅ Brandon Feng ⋅ Chenguo Lin ⋅ Yuchen Lin ⋅ Yujia Zeng ⋅ lvmin zhang ⋅ Maneesh Agrawala ⋅ Honglei Yan ⋅ Panwang Pan
88. **ROSE: Real-Time Open-World Scene Understanding from Monocular Video via Compact Multimodal 4D Scene Graphs**  
   Ziyue Qiu ⋅ Yong Wang ⋅ Jin Pan
89. **Rotate Your Character: Revisiting Video Diffusion Models for High-Quality 3D Character Generation**  
   Jin Wang ⋅ Jianxiang Lu ⋅ Comi Chen ⋅ Guangzheng Xu ⋅ Haoyu Yang ⋅ Peng Chen ⋅ Na Zhang ⋅ Yifan Xu ⋅ Longhuang Wu ⋅ Shuai Shao ⋅ Qinglin Lu ⋅ Ping Luo  
   [arXiv:2601.05722](https://arxiv.org/abs/2601.05722)
90. **SA-V2V: Training-Free Subject-Aware Video-to-Video Personalization**  
   Soobin Park ⋅ Seohyeon Yoo ⋅ Jiwon Kim ⋅ SeonHwa Kim ⋅ Kyong Hwan Jin ⋅ Eunju Cha
91. **SALT: Self-Consistent Distribution Matching with Cache-Aware Training for Few-Step Video Generation**  
   Xingtong Ge ⋅ Yi ZHANG ⋅ Yushi Huang ⋅ Dailan He ⋅ Xiahong Wang ⋅ Bingqi Ma ⋅ Guanglu Song ⋅ Yu Liu ⋅ Jun Zhang
92. **ScrollScape: Unlocking 32K Image Generation With Video Diffusion Priors**  
   Haodong Yu ⋅ Yabo Zhang ⋅ Donglin Di ⋅ Ruyi Zhang ⋅ Wangmeng Zuo  
   [arXiv:2603.24270](https://arxiv.org/abs/2603.24270)
93. **Semantic Line Diffusion: Character-Consistent Line Art from text-annotated Storyboards**  
   Seo-Yeon Choi ⋅ Kyungsu Lee
94. **SHIFT: Motion Alignment in Video Diffusion Models with Adversarial Hybrid Fine-Tuning**  
   Xi Ye ⋅ Wenjia Yang ⋅ Yangyang Xu ⋅ Xiaoyang Liu ⋅ Duo Su ⋅ Mengfei Xia ⋅ Jun Zhu
95. **ShotStream: Streaming Multi-Shot Video Generation for Interactive Storytelling**  
   Yawen Luo ⋅ Xiaoyu Shi ⋅ Jun-hao Zhuang ⋅ Yutian Chen ⋅ Quande Liu ⋅ Xintao Wang ⋅ Pengfei Wan ⋅ Tianfan Xue  
   [arXiv:2603.25746](https://arxiv.org/abs/2603.25746) · [code](https://github.com/KlingAIResearch/ShotStream) · [project](https://luo0207.github.io/ShotStream/)
96. **SIFT: Self-Imagination Fine-Tuning for Physically Plausible Motion in Video Diffusion Models**  
   Ruoyu Wang ⋅ Jialun Liu ⋅ Huayang Huang ⋅ Haibin Huang ⋅ Jiepeng Wang ⋅ Chi Zhang ⋅ Xuelong Li ⋅ Yu Wu
97. **SPECSIA: Stylization Dataset for Novel-View Enhancement in Drawing-based 3D Animation**  
   Kyuwon Kim ⋅ Sunjae Yoon ⋅ Chang Yoo  
   [arXiv:2607.00525](https://arxiv.org/abs/2607.00525)
98. **Spotlight: Identifying and Localizing Video Generation Errors Using VLMs**  
   Aditya Aravind Chinchure ⋅ Sahithya Ravi ⋅ Pushkar Shukla ⋅ Vered Shwartz ⋅ Leonid Sigal  
   [arXiv:2511.18102](https://arxiv.org/abs/2511.18102)
99. **SSBP: Stage-Specialized Block Pruning for Video Diffusion Models**  
   Mengmeng Ge ⋅ Takashi Isobe ⋅ Dong Zhou ⋅ Dong Li ⋅ Emad Barsoum
100. **STANCE: Controllable Video Generation for Structured Dynamics via Sparse-To-dense ANChored Encoding**  
   ZhiFei Chen ⋅ Tianshuo Xu ⋅ Leyi Wu ⋅ Luozhou Wang ⋅ Dongyu Yan ⋅ Zihan You ⋅ Wenting Luo ⋅ Yingcong Chen
101. **StoryBlender: Inter-Shot Consistent and Editable 3D Storyboard with Spatial-temporal Dynamics**  
   Bingliang Li ⋅ Zhenhong Sun ⋅ Jiaming Bian ⋅ Yuehao Wu ⋅ Yifu Wang ⋅ HONGDONG LI ⋅ Yatao Bian ⋅ Huadong Mo ⋅ Daoyi Dong  
   [arXiv:2604.03315](https://arxiv.org/abs/2604.03315) · [project](https://engineeringai-lab.github.io/StoryBlender/)
102. **StoryTeller: Training-Free Narrative Grounding for Long-Form Audio Description**  
   Seung Hahm ⋅ Minh Dinh ⋅ SouYoung Jin  
   [arXiv:2607.11798](https://arxiv.org/abs/2607.11798)
103. **StreamGVE: Training-Free Video Editing via Few-Step Streaming Video Generation**  
   Guanlong Jiao ⋅ Chenyangguang Zhang ⋅ Jia Xian ⋅ Zewei Zhang ⋅ Renjie Liao
104. **Stylized Video Generation via Decoupled Data Synthesis and Gated Style Token Injection**  
   Xin Wei ⋅ Yijie Fang ⋅ Yanjia Li ⋅ Liangyi Wu ⋅ Qin Yang ⋅ Mingrui Zhu ⋅ Nannan Wang ⋅ Xinbo Gao
105. **Surprise Forcing: What to Remember, When to Skip in Long Video Generation**  
   SHUWEI SHI ⋅ Zhen Li ⋅ Muyao Niu ⋅ Chuanhao Li ⋅ Bo Zheng ⋅ Kaipeng Zhang ⋅ zheng yinqiang  
   [arXiv:2607.18436](https://arxiv.org/abs/2607.18436)
106. **SVG-EAR: Parameter-Free Linear Compensation for Sparse Video Generation via Error-aware Routing**  
   Xuanyi Zhou ⋅ Qiuyang Mang ⋅ Shuo Yang ⋅ Haocheng Xi ⋅ Jintao Zhang ⋅ Huanzhi Mao ⋅ Joseph E Gonzalez ⋅ Kurt Keutzer ⋅ Ion Stoica ⋅ Alvin Cheung  
   [arXiv:2603.08982](https://arxiv.org/abs/2603.08982)
107. **Taming Camera-Controlled Video Generation with Verifiable Geometry Reward**  
   Zhaoqing Wang ⋅ Xiaobo Xia ⋅ Zhuolin Bie ⋅ Jinlin Liu ⋅ Dongdong Yu ⋅ Jiawang Bian ⋅ Changhu Wang  
   [arXiv:2512.02870](https://arxiv.org/abs/2512.02870)
108. **Taming Text-to-Sounding Video Generation via Advanced Modality Condition and Interaction**  
   Kaisi Guan ⋅ Xihua Wang ⋅ Zhengfeng Lai ⋅ Xin Cheng ⋅ Peng Zhang ⋅ Xiaojiang Liu ⋅ Ruihua Song ⋅ Meng Cao  
   [arXiv:2510.03117](https://arxiv.org/abs/2510.03117)
109. **Test Time Training for Long Videos via Frame Forgetting Network**  
   Rajat modi ⋅ Xin Liang ⋅ Sebastian Noel ⋅ Yogesh Rawat
110. **Test-Time Noise Guided Adaptation for Realistic Autoregressive Video Generation**  
   Dimitrios Karageorgiou ⋅ Symeon Papadopoulos ⋅ Ioannis Kompatsiaris ⋅ Efstratios Gavves  
   [arXiv:2607.15849](https://arxiv.org/abs/2607.15849) · [project](https://mever-team.github.io/tango)
111. **Thermo-JEPA: Learning a Geometry-Grounded Thermal World Model via Cross-Modal Privileged Masking**  
   Biwen Yang ⋅ Jin Zhang ⋅ Zhe Cao ⋅ Ruiheng Zhang
112. **TriO: Tri-Modal Unsupervised Occupancy World Model for Anything Perception**  
   Quinlan Sykora ⋅ Sourav Biswas ⋅ Christopher Diehl ⋅ Andrew Cunningham ⋅ Thomas Gilles ⋅ Raquel Urtasun
113. **UniTemp: Unlocking Video Generation in Any Temporal Order via Autoregressive Distillation**  
   Lin Zhang ⋅ Sicheng Mo ⋅ Zefan Cai ⋅ Jinhong Lin ⋅ Zihao Lin ⋅ Jiuxiang Gu ⋅ Krishna Kumar Singh ⋅ Yuheng Li ⋅ Yin Li
114. **VCBench: A Streaming Counting Benchmark for Spatial-Temporal State Maintenance in Long Videos**  
   Pengyiang Liu ⋅ Zhongyue Shi ⋅ Hongye Hao ⋅ Qi Fu ⋅ Xueting BI ⋅ Siwei Zhang ⋅ Xiaoyang Hu ⋅ Zitian Wang ⋅ Linjiang Huang ⋅ Si Liu
115. **VERTIGO: Visual Preference Optimization for Cinematic Camera Generation**  
   Mengtian Li ⋅ Yuwei Lu ⋅ Feifei Li ⋅ Chenqi Gan ⋅ Zhifeng Xie ⋅ Xi WANG  
   [arXiv:2604.02467](https://arxiv.org/abs/2604.02467)
116. **VGEdit: Unlocking Video Generation Priors for Reasoning-Informed Image Editing**  
   Haiquan Lu ⋅ Gongfan Fang ⋅ Xinyin Ma ⋅ Xinchao Wang
117. **VGGRPO: Towards World-Consistent Video Generation with 4D Latent Reward**  
   Zhaochong An ⋅ Orest Kupyn ⋅ Théo Uscidda ⋅ Andrea Colaco ⋅ Karan Ahuja ⋅ Serge Belongie ⋅ Mar Gonzalez Franco ⋅ Marta Gazulla  
   [arXiv:2603.26599](https://arxiv.org/abs/2603.26599) · [project](https://zhaochongan.github.io/projects/VGGRPO)
118. **VGGT-World: Transforming VGGT into an Autoregressive Geometry World Model**  
   Xiangyu Sun ⋅ Shijie Wang ⋅ Fengyi Zhang ⋅ Lin Liu ⋅ Caiyan Jia ⋅ Ziying Song ⋅ Zi Helen Huang ⋅ Yadan Luo  
   [arXiv:2603.12655](https://arxiv.org/abs/2603.12655)
119. **ViBe: Ultra-High-Resolution Video Synthesis Born from Pure Images**  
   Yunfeng Wu ⋅ Hongying Cheng ⋅ Zihao He ⋅ Songhua Liu  
   [arXiv:2603.23326](https://arxiv.org/abs/2603.23326) · [code](https://github.com/WillWu111/ViBe)
120. **Video Generation Models are General-Purpose Vision Learners**  
   Letian Wang ⋅ Chuhan Zhang ⋅ Rishabh Kabra ⋅ Jasper Uijlings ⋅ Steven Waslander ⋅ Andrew ZISSERMAN ⋅ Joao Carreira ⋅ Cristian Sminchisescu ⋅ Kaiming He ⋅ Mykhaylo Andriluka ⋅ Eduard Gabriel Bazavan ⋅ Andrei Zanfir  
   [arXiv:2607.09024](https://arxiv.org/abs/2607.09024) · [project](https://genception.github.io)
121. **Video Generation Models Are Inherent Lighting Estimators**  
   Ziqi Cai ⋅ Shuchen Weng ⋅ Kaiqi Liu ⋅ Zifeng Wang ⋅ Zhiquan Zhang ⋅ Minggui Teng ⋅ Han Jiang ⋅ Boxin Shi  
   [arXiv:2607.04674](https://arxiv.org/abs/2607.04674) · [project](https://caiziqi.com/research/vlite/)
122. **Video Generative Models as Geometry Learner**  
   Haosen Yang ⋅ Song Jifei ⋅ Zhensong Zhang ⋅ Xiatian Zhu ⋅ Jiankang Deng
123. **VideoTIR: Accurate Understanding for Long Videos with Efficient Tool-Integrated Reasoning**  
   Zhe Gao ⋅ Shiyu Shen ⋅ Taifeng Chai ⋅ Weinong Wang ⋅ Haotian Xu ⋅ Xing W ⋅ Wenbin Li ⋅ Qi Fan ⋅ Yang Gao ⋅ Dacheng Tao  
   [arXiv:2603.25021](https://arxiv.org/abs/2603.25021)
124. **VPA-WM: Vision-Priors-Aligned World Models for Robust Visual Reinforcement Learning**  
   Xu Zhang ⋅ Sicong Liu ⋅ Liwei Guo ⋅ Chenjuan Guo ⋅ Bin Yang ⋅ Yang Shu
125. **Walk through Paintings : Ego-centric World models from Internet Priors**  
   Anurag Bagchi ⋅ Zhipeng Bao ⋅ Homanga Bharadhwaj ⋅ Yu-Xiong Wang ⋅ Pavel Tokmakov ⋅ Martial Hebert  
   [arXiv:2601.15284](https://arxiv.org/abs/2601.15284)
126. **WildWorld: A Large-Scale Dataset for Action-Conditioned World Modeling with Explicit State Annotations**  
   Zhen Li ⋅ Zian Meng ⋅ Chuanhao Li ⋅ SHUWEI SHI ⋅ Wenshuo Peng ⋅ Yuwei Wu ⋅ Bo Zheng ⋅ Yunde Jia ⋅ Kaipeng Zhang
127. **World Knowledge in the Weights: Reading Concept Circuits of Vision Transformers**  
   Yanlin Chen ⋅ Tang Li ⋅ Xi Peng
128. **World-in-Loop: Online Correction via Event-Triggered World Models for Robust VLA Policies**  
   Shaoqing Xu ⋅ Fang Li ⋅ Zhi-Xin Yang ⋅ Qimao Chen ⋅ Yuechen Luo ⋅ Zhixiang Duan ⋅ Yifan Yang ⋅ Long Chen
129. **WorldAgents: Can Foundation Image Models be Agents for 3D World Models?**  
   Ziya Erkoç ⋅ Angela Dai ⋅ Matthias Niessner  
   [arXiv:2603.19708](https://arxiv.org/abs/2603.19708) · [project](https://ziyaerkoc.com/worldagents/)
130. **WorldCache: Content-Aware Caching for Accelerated Video World Models**  
   Umair Nawaz ⋅ Ahmed Heakl ⋅ Ufaq Khan ⋅ ABDELRAHMAN YOUSSIEF ⋅ Salman Khan ⋅ Fahad Shahbaz Khan  
   [arXiv:2603.22286](https://arxiv.org/abs/2603.22286) · [project](https://umair1221.github.io/World-Cache/)
131. **Your Data Manifold is Secretly a Reward Model: Shell-LCC for Text-to-Video Generation**  
   Shihao Zhang ⋅ Yunzhi Li ⋅ Yuguang Yan ⋅ Junzhe Zhang ⋅ WEI ZHAO ⋅ Bohan Wang ⋅ Hanwang Zhang  
   [arXiv:2606.30248](https://arxiv.org/abs/2606.30248)

## 3D Generation & Shape Modeling

*49 papers · 37 with links*

1. **2D Features Are All You Need for 3D Shape Understanding**  
   Jinfan Zhou ⋅ Richard Liu ⋅ Itai Lang ⋅ Rana Hanocka  
   [arXiv:2607.27592](https://arxiv.org/abs/2607.27592) · [project](https://threedle.github.io/MeshFM/)
2. **Axolotl3D: a Unified Framework for Faithful 3D Shape Completion**  
   Anita Hu ⋅ Maria Shugrina  
   [arXiv:2607.20660](https://arxiv.org/abs/2607.20660)
3. **Coarse-to-fine Contrast: A Hybrid Self-supervised Method for Non-rigid 3D Shape Matching**  
   Feifan Luo ⋅ Ting Li ⋅ Zhao Li ⋅ Hongyang Chen
4. **DiffGI: Differentiable Geometry Images for High-Fidelity Thin-Shell 3D Generation**  
   Eungjune Shim ⋅ Hansol Lee ⋅ Eunjung Ju  
   [arXiv:2607.13365](https://arxiv.org/abs/2607.13365)
5. **DiTex4D: Direct Text-Driven 4D Generation with Structured Latent Diffusion**  
   Xiaozhe Chen ⋅ Mengqi Rong ⋅ Jian Liu ⋅ Shuhan Shen
6. **DreamCAD: Scaling Multi-modal CAD Generation using Differentiable Parametric Surfaces**  
   Mohammad Sadil Khan ⋅ Muhammad Usama ⋅ Rolandos Alexandros Potamias ⋅ Didier Stricker ⋅ Muhammad Zeshan Afzal ⋅ Jiankang Deng ⋅ Ismail Elezi  
   [arXiv:2603.05607](https://arxiv.org/abs/2603.05607) · [code](https://huggingface.co/datasets/SadilKhan/CADCap-1M)
7. **DreamPartGen: Semantically Grounded Part-Level 3D Generation via Collaborative Latent Denoising**  
   Tianjiao (Joey) Yu ⋅ Xinzhuo Li ⋅ Muntasir Wahed ⋅ Jerry Xiong ⋅ Yifan Shen ⋅ Ying Shen ⋅ Ismini Lourentzou  
   [arXiv:2603.19216](https://arxiv.org/abs/2603.19216)
8. **Dynamic World Generation Made Efficient**  
   Fengrui Tian ⋅ Jinqi Luo ⋅ Uday Kiran Reddy Tadipatri ⋅ Hancheng Min ⋅ Rene Vidal
9. **ESTANet: Efficient Online Error Detection in Procedural Videos via Prediction Inconsistency**  
   Shih-Po Lee ⋅ Reza Ghoddoosian ⋅ Faizan Siddiqui ⋅ Enna Sachdeva ⋅ Behzad Dariush  
   [arXiv:2606.25317](https://arxiv.org/abs/2606.25317)
10. **GaussianGPT: Towards Autoregressive 3D Gaussian Scene Generation**  
   Nicolas von Lützow ⋅ Barbara Roessle ⋅ Katharina Schmid ⋅ Matthias Niessner  
   [arXiv:2603.26661](https://arxiv.org/abs/2603.26661) · [project](https://nicolasvonluetzow.github.io/GaussianGPT/) · [project](https://youtu.be/zVnMHkFzHDg)
11. **GENA3D: Generative Amodal 3D Modeling by Bridging 2D Priors and 3D Coherence**  
   Junwei Zhou ⋅ Yu-Wing Tai  
   [arXiv:2511.21945](https://arxiv.org/abs/2511.21945) · [project](https://colezwhy.github.io/gena3d/)
12. **Geometrically Consistent Multi-View Scene Generation from Freehand Sketches**  
   Ahmed Bourouis ⋅ Savas Ozkan ⋅ Andrea Maracani ⋅ Yi-Zhe Song ⋅ Mete Ozay  
   [arXiv:2604.14302](https://arxiv.org/abs/2604.14302)
13. **Geometry-Aware Single-Image 4D Synthesis via Dense Trajectory Generation**  
   Yanran Zhang ⋅ Ziyi Wang ⋅ Wenzhao Zheng ⋅ Zheng Zhu ⋅ Jie Zhou ⋅ Jiwen Lu  
   [arXiv:2512.05044](https://arxiv.org/abs/2512.05044) · [code](https://github.com/Zhangyr2022/MoGe4D)
14. **GeoWorld: Providing Full-frame Geometry Features to Facilitate 3D Scene Generation**  
   Yuhao Wan ⋅ Lijuan Liu ⋅ Jingzhi Zhou ⋅ Zihan Zhou ⋅ Xuying Zhang ⋅ dongbo zhang ⋅ Shaohui Jiao ⋅ Qibin Hou ⋅ Ming-Ming Cheng  
   [arXiv:2511.23191](https://arxiv.org/abs/2511.23191) · [project](https://peaes.github.io/GeoWorld)
15. **Global Graph-Validated Optimization for VLM-based 3D Indoor Scene Generation**  
   Jialu Huang ⋅ Yingxuan You ⋅ Fei Wang ⋅ Zheng Dang  
   [arXiv:2608.03064](https://arxiv.org/abs/2608.03064)
16. **Hyper-Network Neural Functional Maps for Unsupervised Robust 3D Shape Matching**  
   Dongliang Cao ⋅ Florian Bernard  
   [arXiv:2606.30131](https://arxiv.org/abs/2606.30131)
17. **Inclusive Interactive Collisions for Multi-View Consistent Compositional 3D Generation**  
   Chang Liu ⋅ Mingwen Shao ⋅ Xiang Lv ⋅ Xinyuan Chen ⋅ lingzhuang meng ⋅ Qiao Zhang ⋅ Zhengyi Gong ⋅ Jinghao Hu  
   [arXiv:2606.24206](https://arxiv.org/abs/2606.24206)
18. **Ink3D: Sculpting 3D Assets with Extremely Complex Textures via Video Generative Models**  
   yue han ⋅ Chong Li ⋅ Zhening Liu ⋅ Cong Huang ⋅ Fang Deng ⋅ Yong Liu ⋅ Fangyun Wei ⋅ Yan Lu  
   [arXiv:2607.01222](https://arxiv.org/abs/2607.01222) · [project](https://yuehan99.github.io/Ink3D-TextureGen/)
19. **Interact3D: Compositional 3D Generation of Interactive Objects**  
   Hui Shan ⋅ Keyang Luo ⋅ Ming Li ⋅ Sizhe Zheng ⋅ Yanwei Fu ⋅ Zhen Chen ⋅ Xiangru Huang  
   [arXiv:2603.16085](https://arxiv.org/abs/2603.16085)
20. **Know3D: Prompting 3D Generation with Knowledge from Vision-Language Models**  
   Wenyue Chen ⋅ Wenjue Chen ⋅ Peng Li ⋅ Qinghe Wang ⋅ XU JIA ⋅ Heliang Zheng ⋅ Rongfei Jia ⋅ Yuan Liu ⋅ Ronggang Wang  
   [arXiv:2603.22782](https://arxiv.org/abs/2603.22782) · [project](https://xishuxishu.github.io/Know3D.github.io/)
21. **LaGen: Towards Autoregressive LiDAR Scene Generation**  
   Sizhuo Zhou ⋅ Xiaosong Jia ⋅ Fanrui Zhang ⋅ Junjie Li ⋅ Juyong Zhang ⋅ Yukang Feng ⋅ Jianwen Sun ⋅ Songbur Wong ⋅ Junqi You ⋅ Junchi Yan  
   [arXiv:2511.21256](https://arxiv.org/abs/2511.21256) · [code](https://github.com/szzhou88/LaGen)
22. **Lightweight Online Reinforcement Learning for Block Decomposition of CAD Models**  
   Xitong Luo ⋅ Zhenghan Wu ⋅ Yucong Wang ⋅ Yi Cai
23. **LivingWorld: Interactive 4D World Generation with Environmental Dynamics**  
   Hyeongju Mun ⋅ In-Hwan Jin ⋅ Sohyeong Kim ⋅ Kyeongbo Kong  
   [arXiv:2604.01641](https://arxiv.org/abs/2604.01641)
24. **Map2World: Segment Map Conditioned Text to 3D World Generation**  
   Jaeyoung Chung ⋅ Suyoung Lee ⋅ Jianfeng Xiang ⋅ Jiaolong Yang ⋅ Kyoung Mu Lee  
   [arXiv:2605.00781](https://arxiv.org/abs/2605.00781) · [project](https://robot0321.github.io/Map2World/index.html)
25. **Masked BRep Autoencoder via Hierarchical Graph Transformer**  
   Yifei Li ⋅ Kang Wu ⋅ Wenming Wu ⋅ Xiao-Ming Fu  
   [arXiv:2603.14927](https://arxiv.org/abs/2603.14927)
26. **NaLA: A 3D Native LLM Layout Agent for High-quality 3D Scene Generation**  
   Cheng Wan ⋅ Yongsen Mao ⋅ Wenzheng Wu ⋅ Yuxuan Xie ⋅ Chucheng Xiang ⋅ Runze Wang ⋅ Xiang Zhang ⋅ zhongyuan liu ⋅ Rushi Dai ⋅ Yuan Liu  
   [arXiv:2606.29395](https://arxiv.org/abs/2606.29395) · [code](https://github.com/adamcwan/NaLA-code) · [project](https://adamcwan.github.io/NaLA/)
27. **OneWorld: Taming Scene Generation with 3D Unified Representation Autoencoder**  
   Sensen Gao ⋅ Zhaoqing Wang ⋅ Qihang Cao ⋅ Dongdong Yu ⋅ Changhu Wang ⋅ Tongliang Liu ⋅ Mingming Gong ⋅ Jiawang Bian  
   [arXiv:2603.16099](https://arxiv.org/abs/2603.16099) · [code](https://github.com/SensenGao/OneWorld)
28. **Optimization-Guided Diffusion for Interactive Scene Generation**  
   Shihao Li ⋅ Naisheng Ye ⋅ Tianyu Li ⋅ Kashyap Chitta ⋅ Tuo An ⋅ Peng Su ⋅ Boyang Wang ⋅ Haiou Liu ⋅ Chen Lv ⋅ Hongyang Li  
   [arXiv:2512.07661](https://arxiv.org/abs/2512.07661)
29. **Penetration-Free Compositional 3D Generation via Gaussian Surface Offset**  
   Yilin Shao ⋅ Licheng Jiao ⋅ Lingling Li ⋅ Xu Liu ⋅ Fang Liu ⋅ Wenping Ma ⋅ Long Sun ⋅ Jiaxuan Zhao
30. **Pointer-CAD v2: Plan-Then-Construct CAD Generation with Dimension-Aware Parametric Precision**  
   Dacheng Qi ⋅ Chenyu Wang ⋅ Jingwei Xu ⋅ Yi Ma ⋅ Shenghua Gao  
   [arXiv:2606.29301](https://arxiv.org/abs/2606.29301) · [code](https://github.com/Snitro/Pointer-CAD-v2)
31. **PWM-ArtGen: Part World Model for Articulated Object Generation**  
   Wentao Zheng ⋅ Ancong Wu  
   [arXiv:2607.02045](https://arxiv.org/abs/2607.02045)
32. **Reasoning-Guided Part-Level Visual Grounding via Reinforcement Learning**  
   Kazi Sajeed Mehrab ⋅ Hani Alomari ⋅ Najibul Sarker ⋅ Zaber Abdul Hakim ⋅ Chia-Wei Tang ⋅ Anuj Karpatne ⋅ Chris Thomas  
   [arXiv:2607.15374](https://arxiv.org/abs/2607.15374)
33. **Reflecting Process Expertise in Procedural Material Generation**  
   Kunal Gupta ⋅ Gaurav Joshi ⋅ Yen-Ru Chen ⋅ Seemandhar Jain ⋅ Ishit Mehta ⋅ Manmohan Chandraker  
   [arXiv:2607.13318](https://arxiv.org/abs/2607.13318) · [project](https://materialapprentice.github.io)
34. **Roam2Room: A Unified Floorplan-to-Furnished Framework for Controllable Indoor Scene Generation**  
   Wenbo Li ⋅ Zipeng Qin ⋅ Xiaoliang Ju ⋅ Rongyao Fang ⋅ Hongsheng LI
35. **ROAR-3D: Routing Arbitrary Views for High-Fidelity 3D Generation**  
   Hanxiao Sun ⋅ Mingxin Yang ⋅ Shuhui Yang ⋅ Zebin He ⋅ Xintong Han ⋅ Hongbo Fu ⋅ Chunchao Guo ⋅ Wenhan Luo  
   [arXiv:2605.21121](https://arxiv.org/abs/2605.21121)
36. **RoMan-4D: Learning Robot Arm Manipulation from 4D World Models**  
   Kaichen Zhou ⋅ Yuzhen Chen ⋅ Fangneng Zhan ⋅ Hang Hua ⋅ Grace Chen ⋅ Xinhai Chang ⋅ Ao Qu ⋅ Yilun Du ⋅ Zhuang Liu ⋅ Paul Pu Liang ⋅ Mengyu Wang
37. **Scale3D: Autoregressive Modeling for Large Outdoor Scene Generation**  
   DI QI ⋅ Zheng Sun ⋅ Xuanyang Zhang ⋅ Gang Yu
38. **Scene Generation at Absolute Scale: Utilizing Semantic and Geometric Guidance From Text for Accurate and Interpretable 3D Indoor Scene Generation**  
   Stefan Ainetter ⋅ Thomas Deixelberger ⋅ Edoardo Dominici ⋅ Philipp Drescher ⋅ Konstantinos Vardis ⋅ Markus Steinberger  
   [arXiv:2603.13910](https://arxiv.org/abs/2603.13910)
39. **SceneOrchestra: Efficient Agentic 3D Scene Synthesis via Full Tool-Call Trajectory Generation**  
   Yun He ⋅ Kelin Yu ⋅ Matthias Zwicker  
   [arXiv:2604.19907](https://arxiv.org/abs/2604.19907)
40. **SGMatch: Semantic-Guided Non-Rigid Shape Matching with Flow Regularization**  
   Tianwei Ye ⋅ Xiaoguang Mei ⋅ Yifan Xia ⋅ Fan Fan ⋅ Jun Huang ⋅ Jiayi Ma  
   [arXiv:2603.12937](https://arxiv.org/abs/2603.12937) · [project](https://yetianwei.github.io/SGMatch/)
41. **Sparse auto-regressive modeling for scene generation from multi-view images**  
   Thomas Lucas ⋅ Maxime Pietrantoni ⋅ Wonjune Cho ⋅ Bardienus Duisterhof ⋅ Philippe Weinzaepfel ⋅ Vincent Leroy ⋅ Jerome Revaud
42. **Steering 3D Generations: Preference Alignment via Direct Reward and Preference Optimization**  
   Yuanhang Wang ⋅ Lizhe Qi ⋅ Wenqiang Zhang
43. **SuperVoxelGPT: Adaptive and Ordered 3D Tokenization for Autoregressive Shape Generation**  
   Yuan Li ⋅ Congyi Zhang ⋅ Xifeng Gao ⋅ Xiaohu Guo  
   [arXiv:2605.29655](https://arxiv.org/abs/2605.29655)
44. **TACO-Net: Topological Signatures Triumph in 3D Object Classification**  
   Anirban Ghosh ⋅ Ayan Dutta  
   [arXiv:2509.24802](https://arxiv.org/abs/2509.24802)
45. **Taming LLMs for Codematic Indoor Scene Generation**  
   yixun liang ⋅ Qianyi Wu ⋅ Chuan Fang ⋅ Rui Chen ⋅ Jiahang Liu ⋅ Jianfeng Zhang ⋅ Ping Tan
46. **TopoGAT: Plug-and-Play Topological Graph Attention for Fine-Grained 3D Segmentation**  
   Xinyu Jiang ⋅ Lech Szymanski ⋅ Steven Mills
47. **TORA: Topological Representation Alignment for 3D Shape Assembly**  
   Nahyuk Lee ⋅ Zhiang Chen ⋅ Marc Pollefeys ⋅ Sunghwan Hong  
   [arXiv:2604.04050](https://arxiv.org/abs/2604.04050) · [project](https://nahyuklee.github.io/tora)
48. **Ultra3D: Efficient and High-Fidelity 3D Generation with Part Attention**  
   Yiwen Chen ⋅ Zhihao Li ⋅ Yihao Luo ⋅ Yikai Wang ⋅ Zhang Hu ⋅ Le Li ⋅ Qin Li ⋅ Chi Zhang ⋅ Guosheng Lin  
   [arXiv:2507.17745](https://arxiv.org/abs/2507.17745) · [project](https://buaacyw.github.io/ultra3d/)
49. **WorldFlow3D: Flowing Through 3D Distributions for Unbounded World Generation**  
   Amogh Joshi ⋅ Julian Ost ⋅ Felix Heide  
   [arXiv:2603.29089](https://arxiv.org/abs/2603.29089) · [project](https://light.princeton.edu/worldflow3d)

## Image & Video Editing

*88 papers · 51 with links*

1. **3D-Layout-R1: Structured Reasoning for Language-Instructed Spatial Editing**  
   Haoyu Zhen ⋅ Xiaolong Li ⋅ Yilin Zhao ⋅ Han Zhang ⋅ Sifei Liu ⋅ Kaichun Mo ⋅ Chuang Gan ⋅ Subhashree Radhakrishnan  
   [arXiv:2603.22279](https://arxiv.org/abs/2603.22279)
2. **AGE: Agentic Gaussian Editing in 3D Scenarios**  
   Hao Qin ⋅ Tesi Lin ⋅ Mingwei Wei ⋅ Yukai Sun ⋅ Mengxu Lu ⋅ Ming Kong ⋅ Qiang Zhu
3. **AnyStyle: A Single LoRA is Sufficient for Image-Guided Style Transfer**  
   Yongwen Lai ⋅ Chaoqun Wang  
   [arXiv:2607.04677](https://arxiv.org/abs/2607.04677) · [code](https://github.com/Yvan1001/AnyStyle)
4. **Attention-Logit Steering to Compositional Generalization for Continual VQA**  
   Suyoung Yang
5. **Attribute Token Arithmetic: Disentangled and Continuous Semantic Control for Visual Autoregressive Models**  
   Xindi Yang ⋅ Yicheng Wu ⋅ Cheng Zhang ⋅ Jianfei Cai ⋅ Tien-Tsin Wong
6. **A²-Edit: Precise Reference-Guided Image Editing of Arbitrary Objects and Ambiguous Masks**  
   华渝 郑 ⋅ Guangzhao Li ⋅ Baixuan Zhao ⋅ Siqi Luo ⋅ Hantao Jiang ⋅ Guangtao Zhai ⋅ Xiaohong Liu
7. **Beyond Absolute Scores: Relative Edit-induced Difference for Generalizable Image Aesthetic Assessment**  
   Qifei Jia ⋅ Xintong Yao ⋅ Minghao Li ⋅ Yajie Chai ⋅ Qiming Lu ⋅ Baoyue Shen ⋅ Yasen Zhang ⋅ Runyu Shi ⋅ Ying Huang ⋅ Yue Zhang  
   [arXiv:2606.05778](https://arxiv.org/abs/2606.05778)
8. **Beyond Atomic Layouts: Compositional Design Understanding with Vision-Language Models**  
   Yiyang Huang ⋅ Zhaowen Wang ⋅ Simon Jenni ⋅ Jing Shi ⋅ Yitian Zhang ⋅ Yizhou Wang ⋅ Yun Fu
9. **Beyond Fixed Luminance: Towards Panchromatic and Orthochromatic Image Colorization**  
   Swarnim Maheshwari ⋅ Syed Imam Ali ⋅ Vineeth N Balasubramanian  
   [arXiv:2608.10798](https://arxiv.org/abs/2608.10798)
10. **BeyondMasks: Evaluating Causal and Physical Consistency in Video Object Removal**  
   Yiğit Ekin ⋅ Enes Şanlı ⋅ Aykut Erdem ⋅ Erkut Erdem ⋅ Aysegul Dundar
11. **BlenderFusion: 3D-Grounded Visual Editing and Generative Compositing**  
   Jiacheng Chen ⋅ Ramin Mehran ⋅ Xuhui Jia ⋅ Saining Xie ⋅ Sanghyun Woo  
   [arXiv:2506.17450](https://arxiv.org/abs/2506.17450) · [project](https://blenderfusion.github.io)
12. **BrainFIBRE: A Foundation Model via Information Decomposition for Brain Microstructure**  
   Zijian Dong ⋅ Yi Lin ⋅ Fang Ji ⋅ Jianxiong Zhou ⋅ Eric Kwun Kei NG ⋅ Juan Zhou  
   [arXiv:2607.00573](https://arxiv.org/abs/2607.00573)
13. **CHARTSTYLE-100K: A Large-Scale Dataset for Structured Visualization Style Transfer**  
   Yuwei Yang ⋅ Tianchi Xie ⋅ Jinhong Ni ⋅ Yukai Guo ⋅ Jing Zhang ⋅ Liang Zheng ⋅ Yalong Bai ⋅ YUHUI YUAN
14. **Correlation-Weighted Multi-Reward Optimization for Compositional Generation**  
   Jungmyung Wi ⋅ Hyunsoo Kim ⋅ Donghyun Kim  
   [arXiv:2603.18528](https://arxiv.org/abs/2603.18528) · [code](https://github.com/TheDarkKnight-21th/CMO)
15. **COSY: Compositional 3DGS Synthesis for Disentangled Human Head Editing**  
   Florian Barthel ⋅ Shalini De Mello ⋅ Koki Nagano ⋅ Wieland Morgenstern ⋅ Anna Hilsmann ⋅ Peter Eisert  
   [arXiv:2605.24114](https://arxiv.org/abs/2605.24114)
16. **DARE to Mitigate Hallucination: Dual-path Auto-Regressive-aware Editing**  
   Jaeho Lee ⋅ Jeongeun Lee ⋅ Gyeong-Moon Park
17. **Discrete Noise Inversion for Next-scale Autoregressive Text-based Image Editing**  
   Minh Quan Dao ⋅ Xiaoxiao He ⋅ Ligong Han ⋅ Ngan Nguyen ⋅ Amin Nobari ⋅ Han Zhang ⋅ Faez Ahmed ⋅ Viet Anh Nguyen ⋅ Dimitris N. Metaxas  
   [arXiv:2509.01984](https://arxiv.org/abs/2509.01984)
18. **DreamEdit3D: Personalization of Multi-View Diffusion Models for 3D Editing**  
   Jinxin Ai ⋅ Matthias Niessner ⋅ Ziya Erkoç  
   [arXiv:2605.16990](https://arxiv.org/abs/2605.16990)
19. **Dress-ED: Instruction-Guided Editing for Virtual Try-On and Try-Off**  
   Fulvio Sanguigni ⋅ Davide Lobba ⋅ Bin Ren ⋅ Marcella Cornia ⋅ Nicu Sebe ⋅ Rita Cucchiara  
   [arXiv:2603.22607](https://arxiv.org/abs/2603.22607) · [code](https://github.com/aimagelab/Dress-ED) · [project](https://aimagelab.github.io/Dress-ED/)
20. **EchoStyle: Unlocking High-Fidelity Video Stylization with Reverse Data Synthesis**  
   Huaqiu Li ⋅ Jiahao Wang ⋅ Sijia Cai ⋅ Hualian Sheng ⋅ Bing Deng ⋅ Jieping Ye ⋅ Wenhan Luo  
   [arXiv:2606.25465](https://arxiv.org/abs/2606.25465)
21. **Edit in 2D, Verify in 3D: Reinforcement Learning for Multi-view Consistent Scene Editing**  
   Jiyuan Wang ⋅ Chunyu Lin ⋅ Lei Sun ⋅ Zhi Cao ⋅ Yuyang Yin ⋅ Lang Nie ⋅ Zhenlong Yuan ⋅ Xiangxiang Chu ⋅ Yunchao Wei ⋅ Kang Liao ⋅ Guosheng Lin  
   [arXiv:2603.03143](https://arxiv.org/abs/2603.03143)
22. **Edit3r: Instant 3D Scene Editing from Sparse Unposed Images**  
   Jiageng Liu ⋅ Weijie Lyu ⋅ Xueting Li ⋅ Yejie Guo ⋅ Ming-Hsuan Yang  
   [arXiv:2512.25071](https://arxiv.org/abs/2512.25071) · [project](https://edit3r.github.io/edit3r/)
23. **EditHF-1M: A Million-Scale Rich Human Preference Feedback for Image Editing**  
   Zitong Xu ⋅ Huiyu Duan ⋅ Zhongpeng Ji ⋅ Xinyun Zhang ⋅ Yutao Liu ⋅ Xiongkuo Min ⋅ Ke Gu ⋅ Jian Zhang ⋅ Shusong Xu ⋅ Jinwei Chen ⋅ Bo Li ⋅ Guangtao Zhai  
   [arXiv:2603.14916](https://arxiv.org/abs/2603.14916) · [code](https://github.com/IntMeGroup/EditHF)
24. **Editing Everything Everywhere All at Once**  
   Fabio Quattrini ⋅ Carmine Zaccagnino ⋅ Enis Simsar ⋅ Marta Gazulla ⋅ Rita Cucchiara ⋅ Alessio Tonioni ⋅ Silvia Cascianelli  
   [arXiv:2606.31278](https://arxiv.org/abs/2606.31278)
25. **EditVerse3D: High-Quality 3D Object Editing with Region-Aware Learning**  
   Youtan Yin ⋅ Yanning Zhou ⋅ Jiacheng Wei ⋅ Xiaofeng Yang ⋅ Jun Zhang ⋅ Jiayang Bai ⋅ Jingwen Ye ⋅ Weidong Zhang ⋅ Guosheng Lin  
   [arXiv:2607.07187](https://arxiv.org/abs/2607.07187) · [project](https://editverse3d.github.io)
26. **Enlightening Photographic Style Transfer with a Self-Supervised Photographic Embedding**  
   Chengxuan Zhu ⋅ Jiacong Fang ⋅ Shuchen Weng ⋅ Youwei Lyu ⋅ Jiajun Tang ⋅ Qingnan Fan ⋅ Chao Xu ⋅ Boxin Shi
27. **EraseLoRA: MLLM-Driven Foreground Exclusion and Background Subtype Aggregation for Dataset-Free Object Removal**  
   Sanghyun Jo ⋅ DONGHWAN LEE ⋅ Eunji Jung ⋅ Seong Oh ⋅ Kyungsu Kim  
   [arXiv:2512.21545](https://arxiv.org/abs/2512.21545) · [project](https://shjo-april.github.io/EraseLoRA)
28. **ExpertEdit: Learning Skill-Aware Motion Editing from Expert Videos**  
   Arjun Somayazulu ⋅ Kristen Grauman  
   [arXiv:2604.10466](https://arxiv.org/abs/2604.10466) · [project](https://vision.cs.utexas.edu/projects/expert_edit/)
29. **Fill2SR: Repurposing Inpainting Diffusion Transformers for Real-World Super-Resolution**  
   Xingfu Yi ⋅ Xiaoxue Yu
30. **FineEdit: Fine-Grained Image Edit with Bounding Box Guidance**  
   Haohang Xu ⋅ Lin Liu ⋅ Zhibo Zhang ⋅ Rong Cong ⋅ Xiaopeng Zhang ⋅ Qi Tian  
   [arXiv:2604.10954](https://arxiv.org/abs/2604.10954)
31. **FlexComposer: Unified Video Compositing from Images to Dynamic Footage with Flexible Trajectory Control**  
   Songchun Zhang ⋅ Sitong Guo ⋅ Xianghao Kong ⋅ Pengwei Liu ⋅ Yuwei Guo ⋅ lvmin zhang ⋅ Anyi Rao  
   [arXiv:2607.29627](https://arxiv.org/abs/2607.29627)
32. **Follow-Your-Mind: Towards Inversion-Free Brain-Driven Visual Context Synthesis and Editing**  
   Haodong Jing ⋅ Panqi Yang ⋅ Rongchao Zhang ⋅ Zhipeng Liu ⋅ Yajun Liu ⋅ Xuehai Bai ⋅ Yongqiang Ma ⋅ Nanning Zheng
33. **From Draft to Draft-Free: One-Step Video Object Removal via Privileged Distillation and Fast Planting**  
   Zizhao Chen ⋅ Ping Wei ⋅ Guang Dai ⋅ Jingdong Wang ⋅ Mengmeng Wang  
   [arXiv:2607.14976](https://arxiv.org/abs/2607.14976)
34. **GIDE: Unlocking Diffusion LLMs for Precise Training-Free Image Editing**  
   Zifeng Zhu ⋅ Jiaming Han ⋅ Jiaxiang Zhao ⋅ Minnan Luo ⋅ Xiangyu Yue
35. **GRADE: Benchmarking Discipline-Informed Reasoning in Image Editing**  
   Mingxin Liu ⋅ Ziqian Fan ⋅ Zhaokai Wang ⋅ Leyao Gu ⋅ Zirun Zhu ⋅ YiguoHe YiguoHe ⋅ Yuchen Yang ⋅ Changyao Tian ⋅ Xiangyu Zhao ⋅ Ning Liao ⋅ Shaofeng Zhang ⋅ Qibing Ren ⋅ Zhihang Zhong ⋅ Xuanhe Zhou ⋅ Junchi Yan ⋅ Xue Yang
36. **h-Flow: Flexible Flow-based Image Editing via Doob's h-Transform**  
   ZeHui Guo ⋅ Zhen Wang ⋅ Junwei Shu ⋅ Changbo Wang ⋅ Long Chen ⋅ Yang Li  
   [arXiv:2607.10800](https://arxiv.org/abs/2607.10800)
37. **High-Resolution Artwork Outpainting with Global Blueprint Guidance and Layout Control**  
   Junha Kim ⋅ Hyunjoon Park ⋅ Donghyeon Cho  
   [arXiv:2607.06162](https://arxiv.org/abs/2607.06162)
38. **Improving Image-to-Image Translation via a Rectified Flow Reformulation**  
   Satoshi Iizuka ⋅ Shun Okamoto ⋅ Kazuhiro Fukui  
   [arXiv:2603.20186](https://arxiv.org/abs/2603.20186)
39. **In-context Region-based Drag: Drag Any Region to Any Shape**  
   Jiacheng Sui ⋅ Tianyu Hao ⋅ Bingjie Gao ⋅ Li Niu ⋅ Guangtao Zhai  
   [arXiv:2606.25907](https://arxiv.org/abs/2606.25907) · [code](https://github.com/bcmi/ICRDrag-Region-Drag-Editing)
40. **InnoText: A Unified Model for Visual Text Generation and Editing**  
   Haowei Liu ⋅ Runze He ⋅ Jian Lu ⋅ Ao Ma ⋅ Run Ling ⋅ Ke Cao ⋅ Jiasong Feng ⋅ Wei Feng ⋅ Shuo Lu ⋅ Yexing Xu ⋅ WANG Yun ⋅ Jing Wang ⋅ Zhanjie Zhang  
   [arXiv:2607.22101](https://arxiv.org/abs/2607.22101)
41. **InsertAnywhere: Geometrically Grounded and Optics-Aware Video Object Insertion**  
   Hoiyeong Jin ⋅ Hyojin Jang ⋅ Junha Hyung ⋅ Jeongho Kim ⋅ Kinam Kim ⋅ Dongjin Kim ⋅ Huijin choi ⋅ Hyeonji Kim ⋅ Choo Jaegul  
   [arXiv:2512.17504](https://arxiv.org/abs/2512.17504) · [project](https://myyzzzoooo.github.io/InsertAnywhere/)
42. **InstaEdit: Instant Image Editing via Optimized Noise Prediction**  
   Ning Ma ⋅ Yangrui Shao
43. **InterEdit: Navigating Text-Guided Multi-Human 3D Motion Editing**  
   Yebin Yang ⋅ Di Wen ⋅ Lei Qi ⋅ Weitong Kong ⋅ Junwei Zheng ⋅ Ruiping Liu ⋅ Yufan Chen ⋅ Chengzhi Wu ⋅ Kailun Yang ⋅ Yuqian Fu ⋅ Danda Paudel ⋅ Luc Van Gool ⋅ Kunyu Peng
44. **InverseCrafter: Efficient Video ReCapture as a Latent Domain Inverse Problem**  
   Yeobin Hong ⋅ Suhyeon Lee ⋅ Hyungjin Chung ⋅ Jong Chul Ye  
   [arXiv:2512.05672](https://arxiv.org/abs/2512.05672)
45. **LayerVerse: Finding the Sweet Spot for KV-Injection in Training-Free Image Editing**  
   Mikhail Zhirnov ⋅ Arsen Kuzhamuratov ⋅ Andrey Kuznetsov ⋅ Ivan Oseledets ⋅ Konstantin Sobolev
46. **Learn Once, Edit Anywhere: Visual Direction Transfer for Diffusion Models**  
   Yusuf Dalva ⋅ Hidir Yesiltepe ⋅ Pinar Yanardag  
   [arXiv:2403.19645](https://arxiv.org/abs/2403.19645) · [project](http://vidit-edit.github.io)
47. **Learning to Stylize by Learning to Destylize: A Scalable Paradigm for Supervised Style Transfer**  
   Ye Wang ⋅ Zili Yi ⋅ Yibo Zhang ⋅ Peng Zheng ⋅ Xuping Xie ⋅ Jiang Lin ⋅ Yijun Li ⋅ Yilin Wang ⋅ Rui Ma
48. **MA-VLA: Multi-Arm Vision-Language-Action Model for Collaboration and Compositional Generalization**  
   Zaibin Zhang ⋅ Junlan Xiao ⋅ Zhongbo Zhang ⋅ Yifan Wang ⋅ Li Kang ⋅ Yiran Qin ⋅ Changxing Xia ⋅ Heng Zhou ⋅ Talas Fu ⋅ Enshen Zhou ⋅ Ruimao Zhang ⋅ Zhenfei Yin ⋅ Huchuan Lu ⋅ Lijun Wang
49. **Moebius: 0.2B Lightweight Image Inpainting Framework with 10B-Level Performance**  
   Kangsheng Duan ⋅ Ziyang Xu ⋅ Wenyu Liu ⋅ Xiaohu Ruan ⋅ Xiaoxin Chen ⋅ Xinggang Wang
50. **Multi-History-Step SDE Inversion for Image Editing with Superior Regional Awareness**  
   Haiyan Wei ⋅ Yunlong Wang ⋅ Huaibo Huang ⋅ Zhenan Sun ⋅ Kunbo Zhang
51. **OCTOPUS: Multi‑Agentic Universal Compositional Visual Retrieval**  
   Zhangtao Cheng ⋅ Bozhu Zheng ⋅ Ting Zhong ⋅ Fan Zhou
52. **OmniColor: A Unified Framework for Multi-modal Lineart Colorization**  
   Xulu Zhang ⋅ Haoqian DU ⋅ Xiao-Yong Wei ⋅ Li Qing  
   [arXiv:2603.27531](https://arxiv.org/abs/2603.27531) · [code](https://github.com/zhangxulu1996/OmniColor)
53. **OSOR: One-Step Diffusion Inpainting for Effect-Aware Object Removal**  
   Qinming Zhou ⋅ Chenxi Sun ⋅ Deyang Kong ⋅ Junhao He ⋅ Xiangheng Tang ⋅ Peike Yu ⋅ Haotian Wu ⋅ Leilei Cao ⋅ Linfeng Zhang  
   [arXiv:2606.28094](https://arxiv.org/abs/2606.28094) · [code](https://github.com/Zhouqm-Git/osor)
54. **P-CORE: Self-Supervised Surface Consistency for Point-Based Neural Editing**  
   Yanshu Zhang ⋅ Shichong Peng ⋅ Mehran Aghabozorgi ⋅ Alireza Moazeni ⋅ Ke Li
55. **PhyEditBench: A Real-World Multi-Stage Benchmark for Physics-Aware Image Editing**  
   Shengbin Guo ⋅ Shaokang He ⋅ Chaoyue Meng ⋅ Shengpeng Xiao ⋅ Xunzhi Xiang ⋅ Shaofeng Zhang ⋅ Qi Fan  
   [arXiv:2606.26551](https://arxiv.org/abs/2606.26551) · [code](https://github.com/Previsior/PhyEditBench)
56. **PhysEdit: Physically Consistent Image Editing via Causal Enforcement**  
   Siqi Wan ⋅ Jingwen Chen ⋅ Yehao Li ⋅ Yingwei Pan ⋅ Ting Yao ⋅ Tao Mei
57. **PointGT: Simultaneous Geometric and Textural Editing for Point-Based Representations**  
   Yanshu Zhang ⋅ George Shramko ⋅ Pratul Srinivasan ⋅ Ke Li
58. **PPTArena: A Benchmark for PowerPoint Editing**  
   Michael Ofengenden ⋅ Yunze Man ⋅ Ziqi Pang ⋅ Liang-Yan Gui ⋅ Yu-Xiong Wang  
   [arXiv:2512.03042](https://arxiv.org/abs/2512.03042) · [code](https://github.com/michaelofengend/PPTArena)
59. **PRISM: Latent Composition Consistency for Single-Image Reflection Removal**  
   Junseong Shin ⋅ Tae Hyun Kim
60. **Prototype-Conditioned Imagination for Compositional Zero-Shot Learning**  
   Yifan Zhu ⋅ Haofeng Zhang
61. **Query-Kontext: An Unified Multimodal Model for Image Generation and Editing**  
   YuXin Song ⋅ Wenkai Dong ⋅ Shizun Wang ⋅ Qi Zhang ⋅ Song Xue ⋅ Tao Yuan ⋅ Hu Yang ⋅ Haocheng Feng ⋅ Hang Zhou ⋅ Xinyan Xiao ⋅ Jingdong Wang  
   [arXiv:2509.26641](https://arxiv.org/abs/2509.26641)
62. **RCEdit-500K: Reference Completion for Image-Conditioned Image Editing**  
   Jingxu Zhang ⋅ Daneul Kim ⋅ Yueming Pan ⋅ DONG CHEN ⋅ Kai Qiu ⋅ Yang Liu ⋅ Yifan Yang ⋅ Qi Dai ⋅ Xiaoyan Sun ⋅ Chong Luo
63. **Recolour What Matters: Region-Aware Colour Editing via Token-Level Diffusion**  
   Yuqi Yang ⋅ Dongliang Chang ⋅ Yijia Ling ⋅ Ruoyi Du ⋅ Zhanyu Ma  
   [arXiv:2603.18466](https://arxiv.org/abs/2603.18466) · [project](https://yangyuqi317.github.io/ColourCrafter.github.io/)
64. **ReDesign: Recovering Editable Design Structures from Raster Images via Agentic Decomposition**  
   Jooyeol Yun ⋅ Jintae Park ⋅ Hyesu Lim ⋅ Junha Hyung ⋅ Hyungjin Chung ⋅ Choo Jaegul  
   [arXiv:2607.25565](https://arxiv.org/abs/2607.25565)
65. **Region-Aware Test-Time Scaling for Compositional Image Generation**  
   Mingzhu Shen ⋅ Peng Ye ⋅ Xinyin Ma ⋅ Gongfan Fang ⋅ Christos-Savvas Bouganis ⋅ Yiren Zhao ⋅ Xinchao Wang
66. **SAEdit: Token-Level Control for Continuous Image Editing via Sparse Autoencoder**  
   Ronen Kamenetsky ⋅ Sara Dorfman ⋅ Daniel Garibi ⋅ Roni Paiss ⋅ Or Patashnik ⋅ Danny Cohen-Or  
   [arXiv:2510.05081](https://arxiv.org/abs/2510.05081) · [project](https://ronen94.github.io/SAEdit/)
67. **SAND: Stage-Aware Noise Decomposition for Training-Free Diffusion Guidance**  
   DaeHyun Kim ⋅ Hyo-Jun Lee ⋅ Hanul Kim ⋅ Yeong Jun Koh
68. **Semantically Aligned Gradient-Driven Context-Preserving Image Editing**  
   Chiranjeev Chiranjeev ⋅ Muskan Dosi ⋅ MAYANK VATSA ⋅ RICHA SINGH
69. **SONIC: Spectral Optimization of Noise for Inpainting with Consistency**  
   Seungyeon Baek ⋅ Erqun Dong ⋅ Shadan Namazifard ⋅ Mark J Matthews ⋅ Kwang Moo Yi  
   [arXiv:2511.19985](https://arxiv.org/abs/2511.19985) · [project](https://ubc-vision.github.io/sonic/)
70. **SR-Edit: Region-Aware Image Editing via Self-Refinement**  
   Andong Wang ⋅ Zehua Chen ⋅ Yuxuan Jiang ⋅ Jun Zhu
71. **TanGO: Training-Free 3D Editing via Tangent-Space Guidance and Optimization**  
   Siwoo Lim ⋅ Sunjae Yoon ⋅ Gwanhyeong Koo ⋅ Hyeonseo Yun ⋅ Chang Yoo  
   [arXiv:2607.14927](https://arxiv.org/abs/2607.14927) · [code](https://github.com/siw00-lim/TanGO)
72. **Target-aware Image Editing via Cycle-consistent Constraints**  
   Yanghao Wang ⋅ Zhen Wang ⋅ Long Chen  
   [arXiv:2510.20212](https://arxiv.org/abs/2510.20212)
73. **TASE: Truncation-Aware Semantic Embeddings for 3D Scene Understanding and Editing**  
   Tim-Felix Faasch ⋅ Jochen Kall ⋅ Jens Behley ⋅ Lucas Nunes ⋅ Cyrill Stachniss
74. **The Prism Hypothesis: Harmonizing Semantic and Pixel Representations via Unified Autoencoding**  
   Weichen Fan ⋅ Haiwen Diao ⋅ Quan Wang ⋅ Dahua Lin ⋅ Ziwei Liu  
   [arXiv:2512.19693](https://arxiv.org/abs/2512.19693) · [code](https://github.com/WeichenFan/UAE)
75. **Through Van Gogh’s Eyes: Global Style Transfer with Diffusion Model**  
   Jeongha Lee ⋅ Yujin Kim ⋅ Ghazanfar Ali ⋅ Suhyun Kim ⋅ Jae-In Hwang
76. **Towards In-Context Tone Style Transfer with A Large-Scale Triplet Dataset**  
   Yuhai Deng ⋅ Huimin She ⋅ Wei Shen ⋅ Meng Li ⋅ Ruoxi Wu ⋅ Lunxi Yuan ⋅ Xiang Li  
   [arXiv:2604.16114](https://arxiv.org/abs/2604.16114) · [project](https://dengyuhai.github.io/ICTone_Project/)
77. **Training-Free Multi-Concept Image Editing**  
   Niki Maria Foteinopoulou ⋅ Ignas Budvytis ⋅ Stephan Liwicki  
   [arXiv:2602.20839](https://arxiv.org/abs/2602.20839) · [project](https://nickyfot.github.io/cds/)
78. **Two Birds, One Projection: Harmonizing Safety and Utility in LVLMs via Inference-time Feature Projection**  
   Yewon Han ⋅ Yumin Seol ⋅ Minsoo Jo ⋅ EunGyung Kong ⋅ Taesup Kim  
   [arXiv:2603.14825](https://arxiv.org/abs/2603.14825)
79. **UNet-Twice: A Simple Structured Reference-based Inpainting Framework**  
   Junda Lu ⋅ zhiqiao xu ⋅ Houkun Wu ⋅ Wei Cui ⋅ Bo Huang ⋅ Mingyang Chen ⋅ Bing Li
80. **UniGeo: Unifying Geometric Constraints for Camera-Controllable Image Editing via Video Priors**  
   Hong Jiang ⋅ Wensong Song ⋅ Zongxin Yang ⋅ Ruijie Quan ⋅ Yi Yang
81. **UniREditBench: A Unified Reasoning-based Image Editing Benchmark**  
   Feng Han ⋅ Yibin Wang ⋅ Chenglin Li ⋅ Zheming Liang ⋅ Dianyi Wang ⋅ Yang Jiao ⋅ Zhipeng Wei ⋅ Chao Gong ⋅ Cheng Jin ⋅ Jiaqi Wang  
   [arXiv:2511.01295](https://arxiv.org/abs/2511.01295) · [project](https://maplebb.github.io/UniREditBench)
82. **Universal Image Immunization against Diffusion-based Image Editing via Semantic Injection**  
   Chanhui Lee ⋅ Donggyu Choi ⋅ Seunghyun Shin ⋅ Hae-Gon Jeon ⋅ Jeany Son  
   [arXiv:2602.14679](https://arxiv.org/abs/2602.14679)
83. **V-HOLD: Stabilizing Flow Trajectories to Rethink the Edit–Preservation Trade-off**  
   Gahyeon Kim ⋅ Dong-oh Kang
84. **Versatile Editing of Video Content, Actions, and Dynamics without Training**  
   Vladimir Kulikov ⋅ Roni Paiss ⋅ Andrey Voynov ⋅ Inbar Mosseri ⋅ Tali Dekel ⋅ Tomer Michaeli  
   [arXiv:2603.17989](https://arxiv.org/abs/2603.17989) · [project](https://dynaedit.github.io/)
85. **VLTR: Vision-Language Tool Reasoning for Instruction-Guided Image Editing**  
   Yike Wang ⋅ Yitao Yu ⋅ Shaohua Sun ⋅ Ping Luo
86. **VTEdit-Bench: A Comprehensive Benchmark for Multi-Reference Image Editing Models in Virtual Try-On**  
   XIAOYE LIANG ⋅ Zhiyuan Qu ⋅ Mingye Zou ⋅ Jiaxin Liu ⋅ Lai Jiang ⋅ Mai Xu ⋅ Yiheng Zhu  
   [arXiv:2603.11734](https://arxiv.org/abs/2603.11734)
87. **Wavelet-Guided Semantic Signal Compensation for Inversion-Free Image Editing**  
   Anqi Tang ⋅ Wenhao Sun ⋅ Zhaoqiang Liu  
   [arXiv:2607.02421](https://arxiv.org/abs/2607.02421)
88. **WeEdit: A Dataset, Benchmark and Glyph-Guided Framework for Text-centric Image Editing**  
   Hui Zhang ⋅ Juntao Liu ⋅ Zongkai Liu ⋅ liqiang niu ⋅ Fandong Meng ⋅ Zuxuan Wu ⋅ Yu-Gang Jiang  
   [arXiv:2603.11593](https://arxiv.org/abs/2603.11593)

# Multimodal, Language & Video Understanding


## Multimodal LLMs & Vision-Language Models

*283 papers · 174 with links*

1. **3D-Aware VLMs with Implicit and Explicit Geometries**  
   Wenhao Li ⋅ Xueying Jiang ⋅ Quanhao Qian ⋅ Deli Zhao ⋅ Ran Xu ⋅ Shijian Lu ⋅ Gongjie Zhang  
   [arXiv:2607.21595](https://arxiv.org/abs/2607.21595) · [code](https://github.com/Vegetebird/VLM-IE3D)
2. **3DZip: Spatial-Aware Feature Diversity-Guided Token Compression for 3D Question Answering**  
   Changwoo Baek ⋅ Kyeongbo Kong  
   [arXiv:2608.01185](https://arxiv.org/abs/2608.01185) · [project](https://cvsp-lab.github.io/3DZip)
3. **A Classifier-Agnostic Zero-Shot Adversarial Attack Detection via CLIP**  
   Hodaya Krakover ⋅ Meir Levi ⋅ Eyal Gofer ⋅ Guy Gilboa  
   [arXiv:2606.30342](https://arxiv.org/abs/2606.30342)
4. **AdaBoosting Text Prompts for Vision-Language Models**  
   Seokhee Jin ⋅ Changhwan Sung ⋅ Sunung Mun ⋅ Hoyoung Kim ⋅ Jungseul Ok  
   [arXiv:2607.00684](https://arxiv.org/abs/2607.00684)
5. **ADAPT: Attention Dynamics Alignment with Preference Tuning for Faithful MLLMs**  
   Zhiyuan Yao ⋅ Zheren Fu ⋅ Zhixiao Zheng ⋅ Jiajun Li ⋅ Yi Tu ⋅ Zhendong Mao
6. **AdaThinking-E: One-Token Entropy Regulation for Adaptive Thinking**  
   Zining Wang ⋅ Tongkun Guan ⋅ Boming Chen ⋅ Zhentao Guo ⋅ Jianqiang Liu ⋅ chao jin ⋅ Chen Duan ⋅ Kai zhou ⋅ Pengfei Yan ⋅ Wei Shen ⋅ Xiaokang Yang
7. **AMCI: Unlock the Potential of Large Multimodal Models for Fine-grained Open-world Classification via Adaptive Memory Context Injection**  
   Xiao Liu ⋅ Haiyang Zheng ⋅ Nan Pu ⋅ Wenjing Li ⋅ Nicu Sebe ⋅ Zhun Zhong
8. **An Inverse-Adversarial and Difficulty-Adaptive Robust Vision-Language Model**  
   Ruobing Xu ⋅ Junhao Dong ⋅ Xiaohua Xie
9. **Anchored, Not Graded: How Vision-Language Models Fail at Slant-from-Texture Perception**  
   Qian Zhang ⋅ Michal Golovanevsky ⋅ Fulvio Domini ⋅ James Tompkin  
   [arXiv:2606.06714](https://arxiv.org/abs/2606.06714)
10. **AnchorPrune: Relevance-Anchored Contextual Expansion for Visual Token Pruning**  
   Kyuan Oh ⋅ Bumsoo Kim  
   [arXiv:2607.07033](https://arxiv.org/abs/2607.07033) · [code](https://github.com/MULTI-cau/AnchorPrune)
11. **AnE: Pushing the Reasoning Frontier of Multimodal LLMs via Anchor Evolution**  
   Zehao Wang ⋅ Yihan Zeng ⋅ Zidong Gong ⋅ Yuanfan Guo ⋅ Feng Zhu ⋅ Hongzhi Zhang ⋅ Wei Zhang ⋅ Wangmeng Zuo  
   [arXiv:2605.25571](https://arxiv.org/abs/2605.25571)
12. **AnyGround3D: Towards Grounding Any 3D Object in the Wild via 2D-to-3D Lifting**  
   Yingping Liang ⋅ Wenxuan Guo
13. **Asymmetric Anchoring: Opening the Black Box of MLLMs for Forgery Detection**  
   Zhiqiang Yang ⋅ Renshuai Tao ⋅ Chunjie Zhang ⋅ Zhaoxiang Liu ⋅ Xiaolong Zheng ⋅ Yao Zhao
14. **Attention-based Vision-Language Memory for Spatial Reasoning**  
   Zuntao Liu ⋅ Zuntao Liu ⋅ Taimeng Fu ⋅ Shaoshu Su ⋅ Cherie Ho ⋅ Chen Wang
15. **AutoV: Loss-Oriented Ranking for Visual Prompt Retrieval in LVLMs**  
   Yuan Zhang ⋅ Chun-Kai Fan ⋅ Sicheng Yu ⋅ Junwen Pan ⋅ Tao Huang ⋅ Ming Lu ⋅ Kuan Cheng ⋅ Qi She ⋅ Shanghang Zhang  
   [arXiv:2506.16112](https://arxiv.org/abs/2506.16112)
16. **Background Blurring Matters: Improving Visual Grounding by Merging Text-Irrelevant Tokens**  
   Ruilin Yao ⋅ Shengwu Xiong ⋅ Shanshan Yang ⋅ Tianyu Zou ⋅ Shili Xiong ⋅ Yi Rong
17. **Before Thinking, Learn to Decide: Proactive Routing for Efficient Visual Reasoning**  
   Yinan ZHOU ⋅ Haokun Lin ⋅ Yichen Wu ⋅ Yuxin Chen ⋅ Teng Wang ⋅ Caifeng Shan ⋅ Zhenan Sun ⋅ Chen Ma ⋅ Li Zhu ⋅ Ying Shan  
   [arXiv:2606.30217](https://arxiv.org/abs/2606.30217)
18. **Benchmarking MLLMs on Mistake Recognition and Explanation in Single-Step Components of Cooking**  
   Shun Takashige ⋅ Atsushi Hashimoto ⋅ Shin’ichi Satoh
19. **Beyond Disjoint Tasks: Towards More Natural Continual Learning for Vision-Language Models**  
   Xiang Xu ⋅ Yiyang Su ⋅ Tianchen Zhao ⋅ Zheng Zhang ⋅ Zhuowen Tu ⋅ Anil Jain ⋅ Jonathan Wu
20. **Beyond Final Answers: CRYSTAL Benchmark for Transparent Multimodal Reasoning Evaluation**  
   Wayner Barrios ⋅ SouYoung Jin  
   [arXiv:2603.13099](https://arxiv.org/abs/2603.13099)
21. **Break Visual-Linguistic Asymmetry: Unleashing VLM's Cross-Modal Potential for General Face Forgery Detection**  
   Guilin Pang ⋅ Yiu-ming Cheung ⋅ Ruiqi Li ⋅ Weifeng Su
22. **BrepCoder: A Unified Multimodal Large Language Model for Multi-task B-rep Reasoning**  
   Mingi Kim ⋅ Yongjun Kim ⋅ Jungwoo Kang ⋅ Hyungki Kim  
   [arXiv:2602.22284](https://arxiv.org/abs/2602.22284)
23. **BrepLLM: Enabling Large Language Models to Understand Boundary Representations**  
   Liyuan Deng ⋅ Hao Guo ⋅ Yongkang Dai ⋅ Yunpeng Bai ⋅ Yifan Zhu ⋅ Yuanyuan Gao ⋅ Huaxi Huang ⋅ Yilei Shi  
   [arXiv:2512.16413](https://arxiv.org/abs/2512.16413) · [project](https://user-deng.github.io/BrepLLM/)
24. **Bridging Vision and Language Concepts through Optimal Transport Semantic Flow**  
   Chenyang Zhang ⋅ Anqi Dong ⋅ Guangming Zhu ⋅ Nuoye Xiong ⋅ Siyuan Wang ⋅ Lin Mei ⋅ Liang Zhang  
   [arXiv:2606.26891](https://arxiv.org/abs/2606.26891)
25. **Bridging Visual Representation and Reinforcement Learning from Verifiable Rewards in Large Vision-Language Models**  
   yuhang han ⋅ Yuyang Wu ⋅ Zhengbo Jiao ⋅ Yiyu Wang ⋅ Xuyang Liu ⋅ Shaobo Wang ⋅ Hanlin xu ⋅ Xuming Hu ⋅ Linfeng Zhang  
   [arXiv:2603.27375](https://arxiv.org/abs/2603.27375) · [project](https://kawhiiiileo.github.io/KAWHI_PAGE/)
26. **C3-Bench: A Context-Aware Change Captioning Benchmark**  
   JAEWOO KIM ⋅ Hyeongbeom Kim ⋅ Ue-Hwan Kim  
   [arXiv:2606.25445](https://arxiv.org/abs/2606.25445)
27. **CabinSI: Omni-Cabin Spatial Reasoning through Explicit Visual Cognitive Maps**  
   Mengxue Qu ⋅ Hengrui Hu ⋅ Mingming Ma ⋅ Ming Lei ⋅ Jie Gao ⋅ Henghui Ding ⋅ Yao Zhao ⋅ Kenn wu ⋅ Yunchao Wei
28. **CaPCL: Caption-Preserved Continual Learning for Text-to-Image Retrieval**  
   Naoya Sogi ⋅ Ren Ohkubo ⋅ Takashi Shibata ⋅ Makoto Terao ⋅ Yusuke Hosoya ⋅ Takayuki Okatani
29. **CapFrame: Text-Instructed Viewpoint Grounding in 3D Gaussian Scenes via Geometric Pseudo Labels**  
   Jirong Li ⋅ Satoshi Ikehata ⋅ Shuhei Kurita ⋅ Ikuro Sato
30. **Caption Bottleneck Models**  
   Seref Cagliyan ⋅ Umut Ozdemir ⋅ Merve Tapli ⋅ Emre Akbas  
   [arXiv:2607.00578](https://arxiv.org/abs/2607.00578)
31. **CARE: Causally-Aligned Reasoning Exploration for Medical Large Language Models**  
   Yucheng Zhou ⋅ Peng Luo ⋅ Qianning Wang ⋅ Cheng-zhong Xu ⋅ Shen Jianbing
32. **CASA: Cross-Attention over Self-Attention for Efficient Vision-Language Fusion**  
   Moritz Böhle ⋅ Amelie Royer ⋅ Juliette Marrie ⋅ Edouard Grave ⋅ Patrick Perez  
   [arXiv:2512.19535](https://arxiv.org/abs/2512.19535) · [project](https://kyutai.org/casa)
33. **Ceptor: Vision-Language Model-Infused Diverse Guidance for Detecting Anything**  
   Jinyang Li ⋅ Bin-Bin Gao ⋅ Weifu Fu ⋅ Jingnan Luo ⋅ Hanqiu Deng ⋅ Yue Guo ⋅ Jun Liu ⋅ Yong Liu ⋅ Chengjie Wang ⋅ Wenbing Tao
34. **Chain-of-Visual-Thought: Teaching VLMs to See and Think Better with Continuous Visual Tokens**  
   Yiming Qin ⋅ Bomin Wei ⋅ Jiaxin Ge ⋅ Konstantinos Kallidromitis ⋅ Stephanie Fu ⋅ Trevor Darrell ⋅ XuDong Wang  
   [arXiv:2511.19418](https://arxiv.org/abs/2511.19418) · [project](https://wakalsprojectpage.github.io/covt-website/)
35. **ChronusOmni: Improving Time Awareness of Omni-Modal Large Language Models**  
   Yijing Chen ⋅ Yihan Wu ⋅ Kaisi Guan ⋅ Wenhui Tan ⋅ Yuchen Ren ⋅ Yuyue Wang ⋅ Ruihua Song ⋅ Liyun Ru  
   [arXiv:2512.09841](https://arxiv.org/abs/2512.09841) · [code](https://github.com/YJCX330/Chronus/)
36. **Circuit-MLLM: Topological Logic-Guided Latent-Space Visual Reasoning for Circuit Schematic Understanding**  
   Jinyuan Deng ⋅ Yuqi Jiang ⋅ Wenjing Huang ⋅ Xin Li ⋅ Qi Sun ⋅ Cheng Zhuo
37. **Co-Steer: Cross-Modal Collaborative Steering for Jailbreaking MLLMs**  
   Jingmin Zhu ⋅ Rollin Omari ⋅ Tamas Abraham ⋅ Junae Kim ⋅ Amardeep Kaur ⋅ Trung Le ⋅ Dinh Q Phung ⋅ Qiuhong Ke
38. **CoCo: Code as CoT for Text-to-Image Preview and Rare Concept Generation**  
   Li Haodong ⋅ Chunmei Qing ⋅ Huanyu Zhang ⋅ Dongzhi Jiang ⋅ Yihang Zou ⋅ Hongbo Peng ⋅ Dingming Li ⋅ Yuhong Dai ⋅ ZePeng Lin ⋅ Juanxi Tian ⋅ Yi Zhou ⋅ Siqi Dai  
   [arXiv:2603.08652](https://arxiv.org/abs/2603.08652)
39. **CoLT: Teaching Multi-Modal Models to Think with Chain of Latent Thoughts**  
   Lianyu Hu ⋅ shengqian qin ⋅ Zeqin Liao ⋅ Qing Guo ⋅ Liang Wan ⋅ Wei Feng ⋅ Yang Liu  
   [arXiv:2606.31986](https://arxiv.org/abs/2606.31986) · [code](https://github.com/hulianyuyy/CoLT)
40. **Combating Textual Noise and Redundancy: Entropy-Aware Dense Visual Token Pruning**  
   Xuehui Wang ⋅ Xuankun Yang ⋅ Wei Shen  
   [arXiv:2607.02484](https://arxiv.org/abs/2607.02484)
41. **COMPASS: Grounding Composition-Intent Guidance in Unified Multimodal Models**  
   Ziqi Zhou ⋅ Weize Quan ⋅ Mining Tan ⋅ Zhihan Chen ⋅ Dandan Zheng ⋅ Jingdong Chen ⋅ JUN ZHOU ⋅ Weiming Dong ⋅ Dong-ming Yan
42. **Concept-as-Tree: A Controllable Synthetic Data Framework Makes Stronger Personalized VLMs**  
   Ruichuan An ⋅ Kai Zeng ⋅ Ming Lu ⋅ Sihan Yang ⋅ Renrui Zhang ⋅ Huitong Ji ⋅ Hao Liang ⋅ Wentao Zhang  
   [arXiv:2503.12999](https://arxiv.org/abs/2503.12999)
43. **ConsiSpace: Learning Geometric Consistency Matters for Video Spatial Reasoning**  
   Ting Huang ⋅ zhenyu zhang ⋅ Wenyuan Huang ⋅ Hao Tang ⋅ Jian Yang  
   [arXiv:2607.17599](https://arxiv.org/abs/2607.17599)
44. **Constructing and Interpreting Digital Twin Representations for Visual Reasoning via Large Language Models and Reinforcement Learning**  
   Yiqing Shen ⋅ Mathias Unberath
45. **Context Blindness in DPO: Mitigating Object Hallucination in MLLMs via Context-Calibrated Preference Optimization**  
   Byungoh Ko ⋅ Jinyoung Park ⋅ Jongha Kim ⋅ Jeehye Na ⋅ Jaewon Cho ⋅ Hyunwoo Kim  
   [arXiv:2608.12158](https://arxiv.org/abs/2608.12158) · [code](https://github.com/mlvlab/C2-DPO)
46. **Contrastive-Guided Self-Supervised Latent Visual Reasoning for Hallucination Mitigation**  
   Aoxue Dai ⋅ Ningning Wang
47. **CORE-V: Chain-Of-thought REasoning for Image Editing with Visual Interaction**  
   Tianyang Yan ⋅ Peisen Zhao ⋅ Guanghao Zheng ⋅ Mingxing Xu ⋅ Zhibo Zhang ⋅ Wenrui Dai ⋅ Junni Zou ⋅ Hongkai Xiong ⋅ Xiaopeng Zhang ⋅ Qi Tian
48. **CoverPrune: Coverage-Driven Token Pruning for 3D VLMs via Optimal Transport**  
   Peng Ling ⋅ Yingda Yin ⋅ Lingting Zhu ⋅ Weikai Chen ⋅ Shengju Qian ⋅ Zeyu HU ⋅ Xin Wang ⋅ Wenming Yang  
   [arXiv:2608.13226](https://arxiv.org/abs/2608.13226) · [code](https://github.com/Brucess/CoverPrune)
49. **CrossView: Can Vision-Language Models Reason Across Cameras?**  
   Sahil Shah ⋅ S P Sharan ⋅ Harsh Goel ⋅ Manvik Pasula ⋅ Adithya Hebbalae ⋅ Minkyu Choi ⋅ Sandeep Chinchali  
   [arXiv:2608.15539](https://arxiv.org/abs/2608.15539) · [project](https://utaustin-swarmlab.github.io/CrossView)
50. **CURE: Cumulative Knowledge Reuse for Efficient Device-Server Hybrid Inference in Vision-Language Models**  
   Youngjun Lee ⋅ Doyoung Kim ⋅ Junhyeok Kang ⋅ Hwanjun Song ⋅ Jae-Gil Lee
51. **Curvature-Guided Mixing for MLLM Adaptation**  
   Jinglong Yang ⋅ Jiaxuan He ⋅ Wenjian Huang ⋅ Zhan Zhuang ⋅ Jianguo Zhang  
   [arXiv:2606.24963](https://arxiv.org/abs/2606.24963)
52. **Debiased Textual Prompt Tuning for Enhancing Unknown Class Discovery**  
   Yuxin Fan ⋅ Junbiao Cui ⋅ Changhao Liu ⋅ Xingwang Zhao ⋅ Jiye Liang
53. **DecepGPT: Schema-Driven Deception Detection with Multicultural Datasets and Robust Multimodal Learning**  
   JIAJIAN HUANG ⋅ Dongliang Zhu ⋅ Zitong Yu ⋅ Hui Ma ⋅ Jiayu Zhang ⋅ Chunmei Zhu ⋅ Xiaochun Cao  
   [arXiv:2603.23916](https://arxiv.org/abs/2603.23916)
54. **Decoding Multimodal Causality: End-to-End Multimodal Mediation Pathways Inference**  
   Yulong Li ⋅ Xiwei Liu ⋅ Niranjana Menon ⋅ Yuxuan Zhang ⋅ Jianxu Chen ⋅ Rong Xia ⋅ Haolin Yang ⋅ Peixin Guo ⋅ Yutong Xie ⋅ Imran Razzak
55. **Decompose, Compare, and Decide: Multimodal LLMs are Implicit Few-Shot Learners**  
   Yunhan Wang ⋅ Eshika Khandelwal ⋅ Edson Araujo ⋅ Walid Bousselham ⋅ Nina Shvetsova ⋅ Hilde Kuehne  
   [arXiv:2607.00125](https://arxiv.org/abs/2607.00125) · [code](https://github.com/yunhanwang1105/DeCoDe)
56. **DeCoPatch: Revealing Causal Latent Subspaces in Vision-Language Models for GUI Grounding**  
   Yongkang Zhang ⋅ Linjia Kang ⋅ Zhimin Wang ⋅ Duo Wu ⋅ Zhi Wang
57. **Delineating Knowledge Boundaries for Honest Large Vision-Language Models**  
   Junru Song ⋅ Yimeng Hu ⋅ Yijing Chen ⋅ Huining Li ⋅ Qian Li ⋅ Lizhen Cui ⋅ Yuntao Du  
   [arXiv:2604.26419](https://arxiv.org/abs/2604.26419)
58. **Dense Reward for Multi-View 3D Reasoning with Global Maps and Local Views**  
   Jiho Choi ⋅ Seonho Lee ⋅ Seojeong Park ⋅ Hyunjung Shim  
   [arXiv:2606.23557](https://arxiv.org/abs/2606.23557)
59. **DetPO: In-Context Learning with Multi-Modal LLMs for Few-Shot Object Detection**  
   Gautam Rajendrakumar Gare ⋅ Neehar Peri ⋅ Matvei Popov ⋅ Shruti Jain ⋅ John Galeotti ⋅ Deva Ramanan  
   [arXiv:2603.23455](https://arxiv.org/abs/2603.23455) · [project](https://ggare-cmu.github.io/DetPO/)
60. **DEX-AR: A Dynamic Explainability Method for Autoregressive Vision-Language Models**  
   Walid Bousselham ⋅ Angie Boggust ⋅ Hendrik Strobelt ⋅ Hilde Kuehne  
   [arXiv:2603.06302](https://arxiv.org/abs/2603.06302) · [project](https://walidbousselham.com/DEX-AR)
61. **DH-VLM: Dual-Horizon Cooperative Latent Reasoning for Autonomous Driving**  
   Ziyi Song ⋅ Chen Xia ⋅ Hang Yu ⋅ Sheng Zhou ⋅ Zhisheng Niu  
   [arXiv:2608.09333](https://arxiv.org/abs/2608.09333)
62. **DiaDem: Advancing Dialogue Descriptions in Audiovisual Video Captioning for Multimodal Large Language Models**  
   Xinlong Chen ⋅ Weihong Lin ⋅ Jingyun Hua ⋅ Linli Yao ⋅ Yue Ding ⋅ Bozhou Li ⋅ Bohan Zeng ⋅ Yang Shi ⋅ Qiang Liu ⋅ Yuanxing Zhang ⋅ Pengfei Wan ⋅ Liang Wang  
   [arXiv:2601.19267](https://arxiv.org/abs/2601.19267) · [project](https://diadem-captioner.github.io/)
63. **DICE: Disentangled Instance-Class knowlEdge prompt tuning via SAE for Vision-Language Models**  
   Daeun Lee ⋅ Seungwoo Jang ⋅ Kwangsu Kim
64. **Different Changes Require Different Reasoning: Change-Type-Specialized Experts for Robust Change Captioning**  
   Jiyoung Park ⋅ InJae Oh ⋅ Jung Uk Kim
65. **Diffusion-Based Immersive Visual Reasoning**  
   Yifeng Zhang ⋅ Ming Jiang ⋅ Qi Zhao
66. **Direct Preference Optimization for Perceptual Alignment via Vision-Language Consistency**  
   Seungyeon Lee ⋅ Donggyu Lee
67. **DiscoVL: Unveiling Disentangled Cross-Modal Representation Learning via Orthogonal Adversarial Regularization for Vision-Language Models**  
   Mengping Dong ⋅ Jinbao Li ⋅ Fei Li
68. **Dive into the implicit biases of low-rank vision-language alignment**  
   Mingjia Shi ⋅ Shuo Wang ⋅ Xiaobo Wang ⋅ Sifan Zhou ⋅ Kai Wang ⋅ Tianyu Fu ⋅ Chenxu Zhao ⋅ Anyang Su ⋅ Ping Jiang ⋅ Minghui Wu  
   [arXiv:2607.08194](https://arxiv.org/abs/2607.08194)
69. **Do Not Leave a Gap: Hallucination-Free Object Concealment in Vision-Language Models**  
   Amira Guesmi ⋅ Muhammad Shafique  
   [arXiv:2603.15940](https://arxiv.org/abs/2603.15940)
70. **Do Vision Language Models Recognize Visual Ambiguity?**  
   Huy Ta ⋅ Trang Nguyen ⋅ Townim Chowdhury ⋅ ANKIT YADAV ⋅ Minh-Son To ⋅ Zhibin Liao ⋅ Johan Verjans ⋅ Vu Phan
71. **DoCoG: Mask-based Multi-Type Grounded Chain-of-Thought for Document QA**  
   Sai Madhusudan Gunda ⋅ Jyothi Jinka ⋅ Hrithik Sagar ⋅ Aryan Jain ⋅ Venkata Venna ⋅ Anirudh Srinivasan ⋅ SANTOSH RAVI KIRAN SARVADEVABHATLA
72. **Dual Distribution Estimation for Zero-shot Noisy Test-Time Adaptation with VLMs**  
   Wenjie Zhu ⋅ Yabin Zhang ⋅ Liang Xu ⋅ Xin Jin ⋅ Wenjun Zeng ⋅ Yabin Zhang  
   [arXiv:2606.25758](https://arxiv.org/abs/2606.25758) · [code](https://github.com/ZhuWenjie98/DDE) · [project](https://zhuwenjie98.github.io/DDE-project-page/)
73. **Dual-Generalization-aware Minimization for Continual Fine-Tuning of Vision-Language Models**  
   Yanan Chen ⋅ Tieliang Gong ⋅ Yanle Lyu ⋅ Yuanhong Zhang ⋅ Weizhan Zhang
74. **DualTAP: A Dual-Task Adversarial Protector for Mobile MLLM Agents**  
   Fuyao Zhang ⋅ Jiaming Zhang ⋅ CHE WANG ⋅ Xiongtao Sun ⋅ Yurong Hao ⋅ Guowei Guan ⋅ Wenjie Li ⋅ Longtao Huang ⋅ Wei Lim  
   [arXiv:2511.13248](https://arxiv.org/abs/2511.13248)
75. **EGM: Efficient Visual Grounding Language Models**  
   Guanqi Zhan ⋅ Changye Li ⋅ Zhijian Liu ⋅ Yao Lu ⋅ Yi Wu ⋅ Song Han ⋅ Ligeng Zhu  
   [arXiv:2601.13633](https://arxiv.org/abs/2601.13633)
76. **Eliciting Self-Verification in Multimodal Reasoning Agents with Reinforcement Learning**  
   Vishwas Sathish ⋅ Viresh Ranjan ⋅ Xinliang Zhu ⋅ Arnab Dhua ⋅ Douglas Gray
77. **EmbedCopilot: Evaluating Vision-Language Models for Hardware-Aware Embedded System Development**  
   Dongsheng Yuan ⋅ Yimo Deng ⋅ Huangxun Chen
78. **EndoCoT: Scaling Endogenous Chain-of-Thought Reasoning in Diffusion Models**  
   Xuanlang Dai ⋅ Yujie Zhou ⋅ Long Xing ⋅ Jiazi Bu ⋅ Xilin Wei ⋅ Yuhong Liu ⋅ Beichen Zhang ⋅ Kai Chen ⋅ Yuhang Zang  
   [arXiv:2603.12252](https://arxiv.org/abs/2603.12252) · [project](https://internlm.github.io/EndoCoT/)
79. **Enhancing Alignment for Unified Multimodal Models via Semantically-Grounded Supervision**  
   Jiyeong Kim ⋅ Yerim So ⋅ Hyesong Choi ⋅ Uiwon Hwang ⋅ Dongbo Min  
   [arXiv:2603.19807](https://arxiv.org/abs/2603.19807)
80. **Enhancing Interpretability in CLIP with Optimal Transport-based Submodular Optimization for Ophthalmic Imaging**  
   Sihong Lu ⋅ Jian Yang ⋅ Lei Luo
81. **Entropy-Gradient Grounding: Training-Free Evidence Retrieval in Vision-Language Models**  
   Marcel Gröpl ⋅ Jaewoo Jung ⋅ Seungryong Kim ⋅ Marc Pollefeys ⋅ Sunghwan Hong  
   [arXiv:2604.08456](https://arxiv.org/abs/2604.08456) · [project](https://entropy-gradient-grounding.github.io/)
82. **Error-Driven Scene Editing for 3D Grounding in Large Language Models**  
   Yue Zhang ⋅ Zun Wang ⋅ Han Lin ⋅ Jialu Li ⋅ Jianing Yang ⋅ Yonatan Bitton ⋅ Idan Szpektor ⋅ Mohit Bansal  
   [arXiv:2511.14086](https://arxiv.org/abs/2511.14086) · [code](https://github.com/zhangyuejoslin/Deer-3D)
83. **ESC: Emotional Self-Correction for Reliable Vision-Language Models**  
   Tien-Huy Nguyen ⋅ Nhat Nguyen ⋅ Nhat-Huy Nguyen ⋅ Hung Nguyen ⋅ Huy Nguyen ⋅ Thanh-Huy Nguyen ⋅ Cuong Nguyen ⋅ Hoang Le ⋅ Dat Nguyen ⋅ Phat Huynh ⋅ Min Xu ⋅ Ulas Bagci  
   [arXiv:2607.02089](https://arxiv.org/abs/2607.02089) · [project](https://genai4e.github.io/ESC/) · [project](https://genai4e.github.io/ESC/?)
84. **Explicit Logic Channel for Validation and Enhancement of MLLMs on Zero-Shot Tasks**  
   Mei Chee Leong ⋅ Gu Ying ⋅ Hui Tan ⋅ Liyuan Li ⋅ Nancy Chen  
   [arXiv:2603.11689](https://arxiv.org/abs/2603.11689)
85. **Fast and High-Quality Vision-Language Grounding with Parallel Box Decoding**  
   Shihao Wang ⋅ Shilong Liu ⋅ Yuanguo Kuang ⋅ Xinyu Wei ⋅ Yangzhou Liu ⋅ Zhiqi Li ⋅ Yunze Man ⋅ Guo Chen ⋅ Andrew Tao ⋅ Guilin Liu ⋅ Jan Kautz ⋅ Yabin Zhang ⋅ Zhiding Yu
86. **Finding Highlight Images In Your Albums:From Benchmark To MLLM**  
   Rong Qin ⋅ Congcong Sun ⋅ Yaopeng Dong ⋅ Yanbin Sun ⋅ Chensen Ding ⋅ Chenxi Zhao ⋅ Biao Wang ⋅ Qian Zhang ⋅ Eunil Park ⋅ Chi Man VONG ⋅ Jufeng Yang
87. **FingerCap: Fine-grained Finger-level Hand Motion Captioning**  
   Xin Shen ⋅ Rui Zhu ⋅ Lei Shen ⋅ Zhuojie Wu ⋅ Xinyu Wang ⋅ Kaihao Zhang ⋅ Tianqing Zhu ⋅ Shuchen Wu ⋅ Chenxi Miao ⋅ Weikang Li ⋅ Deguo Xia ⋅ Jizhou Huang ⋅ Xin Yu  
   [arXiv:2511.16951](https://arxiv.org/abs/2511.16951)
88. **FlashVLM: Text-Guided Visual Token Selection for Large Multimodal Models**  
   Kaitong Cai ⋅ jusheng zhang ⋅ Sizhuo Ma ⋅ Bingqian Lu ⋅ Jian Wang ⋅ Keze Wang  
   [arXiv:2512.20561](https://arxiv.org/abs/2512.20561)
89. **Focusing by Contrastive Attention: Enhancing VLMs' Visual Reasoning**  
   Yuyao Ge ⋅ Shenghua Liu ⋅ Yiwei Wang ⋅ Lingrui Mei ⋅ Baolong Bi ⋅ Xuanshan Zhou ⋅ Jiayu Yao ⋅ Jiafeng Guo ⋅ Xueqi Cheng  
   [arXiv:2509.06461](https://arxiv.org/abs/2509.06461)
90. **Fourier Compressor: Frequency-Domain Visual Token Compression for Vision-Language Models**  
   Huanyu Wang ⋅ Jushi Kai ⋅ Haoli Bai ⋅ Lu Hou ⋅ Bo Jiang ⋅ Ziwei He ⋅ Zhouhan Lin  
   [arXiv:2508.06038](https://arxiv.org/abs/2508.06038)
91. **Foveated Reasoning: Stateful, Action-based Visual Focusing for Vision-Language Models**  
   Juhong Min ⋅ Lazar Valkov ⋅ Vitali Petsiuk ⋅ Hossein Souri ⋅ Deen Dayal Mohan  
   [arXiv:2604.21079](https://arxiv.org/abs/2604.21079)
92. **From Illusion to Intention: Visual Rationale Learning for Reliable Evidence Acquisition**  
   Changpeng Wang ⋅ Liu Junhan ⋅ Xi Chen ⋅ Haozhe Wang ⋅ Donglian Qi ⋅ Yunfeng Yan
93. **From Masks to Pixels and Meaning: A New Taxonomy, Benchmark and Metrics for VLM Image Tampering**  
   Xinyi Shang ⋅ Yi Tang ⋅ Jiacheng Cui ⋅ Ahmed Elhagry ⋅ Salwa Al Khatib ⋅ Sondos Bsharat ⋅ Jiacheng Liu ⋅ Xiaohan Zhao ⋅ Jing-Hao Xue ⋅ Hao Li ⋅ Salman Khan ⋅ Zhiqiang Shen  
   [arXiv:2603.20193](https://arxiv.org/abs/2603.20193) · [code](https://github.com/VILA-Lab/PIXAR)
94. **From One-to-One to Many-to-Many: Dynamic Cross-Layer Injection for Deep Vision-Language Fusion**  
   pengpeng Zeng ⋅ Yuyu Guo ⋅ Pengpeng Zeng ⋅ Jingkuan Song ⋅ Peng Di ⋅ Hang Yu ⋅ Lianli Gao  
   [arXiv:2601.10710](https://arxiv.org/abs/2601.10710)
95. **From Reasoning to Pixels: Grounded Medical Multimodal LLMs for VQA and Segmentation**  
   Haowen Gu ⋅ Gensheng Pei ⋅ Junzhu Mao ⋅ Qiong Wang ⋅ Mingwu Ren ⋅ Yazhou Yao
96. **Frozen CLIP Priors for Robust Self-Supervised Poisson Inverse Problems**  
   Laura C. Diaz-Delgado ⋅ Emmanuel Martinez ⋅ Henry Arguello
97. **GAP-MLLM: Geometry-Aligned Pre-training for Activating 3D Spatial Perception in Multimodal Large Language Models**  
   Jiaxin Zhang ⋅ Junjun Jiang ⋅ Haijie LI ⋅ Youyu Chen ⋅ Kui Jiang ⋅ Dave Zhenyu Chen  
   [arXiv:2603.16461](https://arxiv.org/abs/2603.16461) · [project](https://gapmllm.github.io/)
98. **GeMoE: Gating Entropy is All You Need for Uncertainty-aware Adaptive Routing in MoE-based Large Vision-Language Models**  
   Chaoxiang Cai ⋅ Minghe Weng ⋅ Jie Li ⋅ Yibo Jiang ⋅ Longrong Yang ⋅ Zequn Qin ⋅ Xi Li  
   [arXiv:2606.26287](https://arxiv.org/abs/2606.26287)
99. **GenAgent: Scaling Text-to-Image Generation via Agentic Multimodal Reasoning**  
   Kaixun Jiang ⋅ Yuzheng Wang ⋅ Junjie Zhou ⋅ Pandeng Li ⋅ Zhihang Liu ⋅ Chen-Wei Xie ⋅ Zhaoyu Chen ⋅ Yun Zheng ⋅ Wenqiang Zhang  
   [arXiv:2601.18543](https://arxiv.org/abs/2601.18543) · [code](https://github.com/deep-kaixun/GenAgent)
100. **Gender Bias in Vision-Language In-Context Learning**  
   Tong Xiang ⋅ Yuta Nakashima ⋅ Noa Garcia
101. **General Incomplete Multimodal Learning via Dynamic Quality Perception**  
   Xiangyu Meng ⋅ shicai wei  
   [arXiv:2607.06943](https://arxiv.org/abs/2607.06943) · [code](https://github.com/Yu-Five/GIML)
102. **Generalize LMMs to Versatile Visual Modalities via Fabricated Modality Synthesis**  
   YuanShihao YuanShihao ⋅ Yuanze Li ⋅ Ruyi Zhang ⋅ Ming LIU ⋅ Wangmeng Zuo  
   [arXiv:2607.10308](https://arxiv.org/abs/2607.10308) · [code](https://github.com/Hunter-Will/VVM-Tuning)
103. **GenRecal: Generation after Recalibration from Large to Small Vision-Language Models**  
   Byung-Kwan Lee ⋅ Ryo Hachiuma ⋅ Yong Man Ro ⋅ Yu-Chiang Frank Wang ⋅ Yueh-Hua Wu  
   [arXiv:2506.15681](https://arxiv.org/abs/2506.15681) · [project](https://byungkwanlee.github.io/GenRecal-page/)
104. **GEO-Detective: Unveiling Location Privacy Risks in Images with LLM Agents**  
   Xinyu Zhang ⋅ Yixin Wu ⋅ Boyang Zhang ⋅ Chenhao Lin ⋅ Chao Shen ⋅ Michael Backes ⋅ Yang Zhang  
   [arXiv:2511.22441](https://arxiv.org/abs/2511.22441)
105. **Geometry Grounding: Elevating Blind Distortion Correction with 3D Structural Priors**  
   Xiang Li ⋅ Weimin Shi ⋅ Qichuan Geng ⋅ Zhong Zhou
106. **Global-Local Dual Perception for MLLMs in High-Resolution Text-Rich Image Translation**  
   junxin lu ⋅ Tengfei Song ⋅ Zhanglin Wu ⋅ Lipengfei Lipengfei ⋅ Xiaowei Liang ⋅ Hui Yang ⋅ Kun Chen ⋅ NING XIE ⋅ Yunfei Lu ⋅ Jing Zhao ⋅ Shiliang Sun ⋅ Daimeng Wei  
   [arXiv:2602.21956](https://arxiv.org/abs/2602.21956)
107. **Going Deep: Deep Visual Prompting with LoTeP**  
   Zijie Zhao ⋅ Yanru Wu ⋅ Yuji Wang ⋅ Haohua Wang ⋅ Enming Zhang ⋅ Wai Kin Chan ⋅ Yang Li
108. **GradingBench: Evaluating End-to-End Compositional Reasoning of MLLMs for Automated Exam Grading**  
   Yuting Wang ⋅ Zixian Guo ⋅ Weihao You ⋅ Zhilong Ji ⋅ Jinfeng Bai ⋅ Wangmeng Zuo
109. **Ground3D-LMM: Fine-Grained 3D Point Grounding and Spatial Reasoning with LMM**  
   Amol Harsh ⋅ Zongyan Han ⋅ Jean Lahoud ⋅ Ye Liu ⋅ Rao M Anwer ⋅ Hisham Cholakkal ⋅ Salman Khan ⋅ Fahad Shahbaz Khan  
   [arXiv:2607.05493](https://arxiv.org/abs/2607.05493)
110. **GTR: Guide-Then-Refine Token Compression for Training-Free Acceleration of Video-LLMs**  
   Sijin Zhou ⋅ wei feng ⋅ Zhuang Qi ⋅ Zhonghua Wang ⋅ Lie Ju ⋅ Xiang An ⋅ Mehrtash Harandi ⋅ Zongyuan Ge
111. **Guardrail-Agnostic Societal Bias Evaluation in Large Vision-Language Models**  
   Yusuke Hirota ⋅ Michael Boone ⋅ Arun Zachariah ⋅ Jibin Rajan Varghese ⋅ Yu-Chiang Frank Wang ⋅ Boyi Li ⋅ Ryo Hachiuma
112. **HIVE: Understanding Post Hallucination Reasoning in Vision Language Models**  
   Feng He ⋅ Zhenting Wang ⋅ Qifan Wang ⋅ Qiang Guan ⋅ Dongfang Liu ⋅ Ruixiang Tang ⋅ Qiankun Li  
   [arXiv:2607.07507](https://arxiv.org/abs/2607.07507) · [code](https://github.com/hefengcs/HIVE)
113. **Holo-Captioning: A Comprehensive Textual View of 3D Scenes**  
   Kun-Yu Lin ⋅ Chengke Bu ⋅ Zhenguo Li ⋅ Kai Han
114. **HomeGuard: VLM-based Embodied Safeguard for Identifying Contextual Risk in Household Task**  
   Xiaoya Lu ⋅ Yijin Zhou ⋅ Zeren Chen ⋅ Ruocheng Wang ⋅ Bingrui Sima ⋅ Enshen Zhou ⋅ Lu Sheng ⋅ Dongrui Liu ⋅ Jing Shao  
   [arXiv:2603.14367](https://arxiv.org/abs/2603.14367) · [code](https://github.com/AI45Lab/HomeGuard)
115. **How Far Are Video Models from True Multimodal Reasoning?**  
   Xiaotian Zhang ⋅ Jianhui Wei ⋅ Yuan Wang ⋅ Jie Tan ⋅ Yichen Li ⋅ Yan Zhang ⋅ Ziyi Chen ⋅ Daoan Zhang ⋅ DEZHI YU ⋅ Wei Xu ⋅ Songtao Jiang ⋅ Zuozhu Liu  
   [arXiv:2604.19193](https://arxiv.org/abs/2604.19193)
116. **How Far Are Vision-Language Models from Constructing the Real World? A Benchmark for Physical Generative Reasoning**  
   Luyu Yang ⋅ Yutong Dai ⋅ An Yan ⋅ Viraj Prabhu ⋅ Ran Xu ⋅ Zeyuan Chen  
   [arXiv:2603.24866](https://arxiv.org/abs/2603.24866) · [project](https://luluyuyuyang.github.io/dreamhouse)
117. **How to Teach Large Multimodal Models New Skills**  
   Zhen Zhu ⋅ Yiming Gong ⋅ Yao Xiao ⋅ Yaoyao Liu ⋅ Derek Hoiem  
   [arXiv:2510.08564](https://arxiv.org/abs/2510.08564) · [code](https://github.com/jessemelpolio/LMM_CL)
118. **Human-Level Accuracy, Non-Human Strategies: Revealing Model-Human Divergence in Video Physical Reasoning**  
   Fanhong Li ⋅ Shurui Zheng ⋅ Yinzi Yinzi ⋅ Junbo Cui ⋅ Lei Ji ⋅ Jia Liu
119. **HyFL-CLIP: Hyperbolic Fine-Tuning of CLIP for Robust Long-Context Understanding**  
   jiha jang ⋅ Hayeon Kim ⋅ Junghun James Kim ⋅ Chulwon Lee ⋅ Se Young Chun  
   [arXiv:2607.00428](https://arxiv.org/abs/2607.00428) · [project](https://janeyeon.github.io/hyflclip)
120. **HyLaR: Hybrid Latent Reasoning with Decoupled Policy Optimization**  
   Tao Cheng ⋅ Shi-Zhe Chen ⋅ Hao Zhang ⋅ Yixin Qin ⋅ Jinwen Luo ⋅ Zheng Wei  
   [arXiv:2604.20328](https://arxiv.org/abs/2604.20328) · [code](https://github.com/EthenCheng/HyLaR)
121. **ICLAgent: Integrated Circuit Footprint Geometry Labeling via LMM-empowered Multi-Agent Framework**  
   Yida Wang ⋅ Yixin Liu ⋅ Taiting Lu ⋅ Lanqing Yang ⋅ Dian Ding ⋅ Juntao Zhou ⋅ Yifan Yang ⋅ Yi-Chao Chen ⋅ Mahanth Gowda
122. **Identifying and Resolving Pitfalls of Knowledge-Based VQA Benchmarks: Auditing, Repairing, and Augmenting**  
   Qian Ma ⋅ S M Rayeed ⋅ Qiong Wu ⋅ Charles Stewart ⋅ Yao Ma  
   [arXiv:2607.00159](https://arxiv.org/abs/2607.00159) · [code](https://github.com/VAN-QIAN/ECCV26-ARA)
123. **Illuminating Unified Multimodal Model for Free-form Interleaved Text-Image Generation**  
   Chonghuinan Wang ⋅ Zhikai Chen ⋅ Chunwei Wang ⋅ Yecong Wan ⋅ Junwei Yang ⋅ Zhixin Wang ⋅ Wei Zhang ⋅ Jiaqi Xu ⋅ Renjing Pei ⋅ Xiaohe Wu ⋅ FAN LI ⋅ Wangmeng Zuo  
   [arXiv:2606.30054](https://arxiv.org/abs/2606.30054)
124. **Imaginative Perception Tokens Enhance Spatial Reasoning in Multimodal Language Models**  
   Mahtab Bigverdi ⋅ Linjie Li ⋅ Weikai Huang ⋅ Jieyu Zhang ⋅ Tuhin Kundu ⋅ Zelun Luo ⋅ Chris Kim ⋅ Jaemin Cho ⋅ Ranjay Krishna ⋅ Linda Shapiro ⋅ Liu Yiming  
   [arXiv:2606.03988](https://arxiv.org/abs/2606.03988)
125. **Improving Reasoning in Vision-Language Models via Perception Verified Self-Training**  
   Sourabh Sharma ⋅ Sonam Gupta ⋅ Sadbhawna Sadbhawna  
   [arXiv:2606.22158](https://arxiv.org/abs/2606.22158)
126. **Incentivizing Vision Language Models to Search for Long Video Question Answering**  
   Harsh Goel ⋅ S P Sharan ⋅ Sahil Shah ⋅ Minkyu Choi ⋅ Joungbin An ⋅ Kristen Grauman ⋅ Sandeep Chinchali  
   [arXiv:2607.02959](https://arxiv.org/abs/2607.02959) · [project](https://utaustin-swarmlab.github.io/VSeek)
127. **Information-Regularized Attention for Visual-Centric Reasoning**  
   Guohao Sun ⋅ Xiaofang Wang ⋅ Yash Patel ⋅ Mengchen Liu ⋅ Zhiqiang Tao ⋅ Praveen Krishnan  
   [arXiv:2607.00434](https://arxiv.org/abs/2607.00434)
128. **Isotropic Embedding Perturbations for Robust Vision Language Encoders**  
   Hyesong Choi ⋅ Daeun Kim ⋅ Song Park ⋅ Taekyung Kim ⋅ Byeongho Heo ⋅ Sangdoo Yun ⋅ Dongbo Min ⋅ Dongyoon Han
129. **LASER: A Corrective Lens for LVLMs via Visual Attention Preservation and Sink Suppression**  
   Bowen Yuan ⋅ Zijian Wang ⋅ Yadan Luo ⋅ Shijie Wang ⋅ Zi Helen Huang
130. **LatentPilot: Scene-Aware Vision-and-Language Navigation by Dreaming Ahead with Latent Visual Reasoning**  
   HAIHONG HAO ⋅ Lei Chen ⋅ Mingfei Han ⋅ Changlin Li ⋅ Dong An ⋅ Yuqiang Yang ⋅ Zhihui Li ⋅ Xiaojun Chang  
   [arXiv:2603.29165](https://arxiv.org/abs/2603.29165) · [project](https://abdd.top/latentpilot/)
131. **LaViT: Aligning Latent Visual Thoughts for Multi-modal Reasoning**  
   Linquan Wu ⋅ Tianxiang Jiang ⋅ Yifei Dong ⋅ Haoyu Yang ⋅ Fengji Zhang ⋅ Shichang Meng ⋅ AI Xuan ⋅ Linqi Song ⋅ Jacky Keung  
   [arXiv:2601.10129](https://arxiv.org/abs/2601.10129)
132. **Learning Active Perception for Pixel-Space Reasoning via Visual-Intent Stratified GRPO**  
   Mingkang Zhu ⋅ Xi Chen ⋅ Senqiao Yang ⋅ Bei Yu ⋅ Hengshuang ZHAO ⋅ Jiaya Jia
133. **Learning Consistency in Reward Modeling for Multi-Modal Reasoning**  
   Chen Li ⋅ Bolin Ni ⋅ Boxin Zhang ⋅ Ke Ye ⋅ Jinnian Zhang ⋅ Houwen Peng ⋅ Han Hu ⋅ Nanning Zheng
134. **Learning from Primitive: Probing Visual Reasoning of LVLMs via Counting**  
   Liwei Che ⋅ Zhiyu Xue ⋅ Yihao Quan ⋅ Benlin Liu ⋅ Zeru Shi ⋅ Ruixiang Tang ⋅ Ranjay Krishna ⋅ Vladimir Pavlovic
135. **Learning to Deny: Action Denial in Multimodal Large Language Models**  
   Raiyaan Abdullah ⋅ Shehreen Azad ⋅ Yogesh Rawat  
   [arXiv:2606.31187](https://arxiv.org/abs/2606.31187) · [code](https://github.com/raiyaan-abdullah/Learn-to-Deny)
136. **Learning to Mask: Cross-Modal Noise Modulation for Hallucination Mitigation in Multi-modal Large Language Models**  
   Zijian Song ⋅ Chunlei Wang ⋅ Kun He
137. **LEGO-Puzzles: How Good Are MLLMs at Multi-Step Spatial Reasoning?**  
   Kexian Tang ⋅ Junyao Gao ⋅ Yanhong Zeng ⋅ Haodong Duan ⋅ Sun Yanan ⋅ Zhening Xing ⋅ Wenran Liu ⋅ Kai Chen ⋅ Kaifeng Lyu  
   [arXiv:2503.19990](https://arxiv.org/abs/2503.19990)
138. **Less Data, Faster Convergence: Goal-Driven Data Optimization for Multimodal Instruction Tuning**  
   Rujie Wu ⋅ Haozhe Zhao ⋅ Hai Ci ⋅ Yizhou Wang  
   [arXiv:2603.12478](https://arxiv.org/abs/2603.12478) · [code](https://github.com/rujiewu/GDO)
139. **LightFusion: A Light-weighted, Double Fusion Framework for Unified Multimodal Understanding and Generation**  
   Zeyu Wang ⋅ Zilong Chen ⋅ Chenhui Gou ⋅ Feng Li ⋅ Chaorui Deng ⋅ Deyao Zhu ⋅ Kunchang Li ⋅ Weihao Yu ⋅ Haoqin Tu ⋅ Haoqi Fan ⋅ Cihang Xie  
   [arXiv:2510.22946](https://arxiv.org/abs/2510.22946)
140. **LiveK12Bench: Have Large Multimodal Models Truly Conquered High School-level Examinations?**  
   Xiaohan Wang ⋅ Mingze Yin ⋅ Yilin Zhao ⋅ sinbadliu sinbadliu ⋅ Dian Li  
   [arXiv:2605.26781](https://arxiv.org/abs/2605.26781)
141. **LongVQUBench: Benchmarking Long-Term Video Quality Understanding of Vision-Language Models**  
   Arpita Nema ⋅ Hanwei Zhu ⋅ Xi Zhang ⋅ Weisi Lin  
   [arXiv:2607.01086](https://arxiv.org/abs/2607.01086)
142. **Look Less, Think Faster: Joint Token-Compute Adaptation for Multimodal LLMs**  
   Pengcheng Wang ⋅ Zhiquan Wang ⋅ Jayoung Lee ⋅ Zhuoyan Xu ⋅ Ran Xu ⋅ Saurabh Bagchi ⋅ Yin Li ⋅ Somali Chaterji  
   [arXiv:2607.20357](https://arxiv.org/abs/2607.20357) · [project](https://www.schaterji.io/publications/2026/jointtokencompute)
143. **Magic-MM-Embedding: Towards Visual-Token-Efficient Universal Multimodal Embedding with MLLMs**  
   Qi Li ⋅ Yanzhe Zhao ⋅ Yongxin Zhou ⋅ Yameng Wang ⋅ Yandong Yang ⋅ Yuanjia Zhou ⋅ Jinxiang Liu  
   [arXiv:2602.05275](https://arxiv.org/abs/2602.05275)
144. **Make Geometry Matter for Spatial Reasoning**  
   Shihua Zhang ⋅ Qiuhong Shen ⋅ Shizun Wang ⋅ Tianbo Pan ⋅ Xinchao Wang  
   [arXiv:2603.26639](https://arxiv.org/abs/2603.26639) · [project](https://suhzhang.github.io/GeoSR/)
145. **MANGO: Unleashing Image Generation Capability of Unified Multimodal Models**  
   Yi Wang ⋅ Mushui Liu ⋅ Wanggui He ⋅ Hanyang Yuan ⋅ Ziwei Huang ⋅ Guanghao Zhang ⋅ Wenkai Fang ⋅ Haoze Jiang ⋅ Shengxuming Zhang ⋅ Weilong Dai ⋅ Haofei Zhang ⋅ Mingli Song ⋅ Hao Jiang ⋅ Jie Song
146. **MED-LCDS: Multi-Expert-Domain CLIP Classification via Logit Calibration**  
   Zheng Zeng ⋅ Deepak Sridhar ⋅ Nuno Vasconcelos
147. **Metric-Bench: Exploring In-context Spatial Metric Reasoning in VLMs for Indoor Scenes**  
   Yuling Xi ⋅ Haokai Zhang ⋅ Muzhi Zhu ⋅ Hao Zhong ⋅ Zongze Du ⋅ Hengyu Zhao ⋅ Chenchen Jing ⋅ Yufei Yin ⋅ Bin Qin ⋅ Yongjie Yang ⋅ Zhenbo Luo ⋅ Hao Chen ⋅ Chunhua Shen
148. **MindBlock: Probing Spatial Assembly and Structure in Unified Multimodal Models**  
   Baiqiao Yin ⋅ Junhao Liu ⋅ Han Yin ⋅ Heyang Yu ⋅ Tingxuan Zhang ⋅ Zhiheng Li ⋅ Chengzu Li ⋅ Jihan YANG ⋅ Manling Li ⋅ Chen Feng ⋅ Yiming Li
149. **MIRROR: Aligning Semantic Relations from Language to Image via Gromov--Wasserstein**  
   Hong-Han Wang ⋅ Yuntao Wang ⋅ Hu Ding
150. **Mitigate Modality-Asymmetric Forgetting via Stabilizing Visual Representations in CLIP-Based Class-Incremental Learning**  
   Yuanhong Zhang ⋅ Yanan Chen ⋅ Xin Zhang ⋅ Zhaoyang Wang ⋅ Weizhan Zhang ⋅ Muyao Yuan ⋅ Hongjin Niu ⋅ LAN MA ⋅ Yuan Gao ⋅ Joey Tianyi Zhou
151. **MixGRPO: Unlocking Flow-based GRPO Efficiency with Mixed ODE-SDE**  
   Junzhe Li ⋅ Yutao Cui ⋅ Tao Huang ⋅ Chuxuan Zeng ⋅ Weijie Kong ⋅ Yinping Ma ⋅ Chun Fan ⋅ Miles Yang ⋅ Zhao Zhong ⋅ Liefeng Bo  
   [arXiv:2507.21802](https://arxiv.org/abs/2507.21802)
152. **Mixture of Specialized Vision Experts: Unlocking Complementary Visual Insights for Faithful MLLM Reasoning**  
   Yifei Gao ⋅ Liangliang You ⋅ Jiye Xie ⋅ changwei wang ⋅ Kexue Fu ⋅ Jingyi Liu ⋅ Rongtao Xu ⋅ Zhiqiang Kou ⋅ Haoran Xu ⋅ Longxiang Gao ⋅ Yu Zhang
153. **MMBU: A Massive Multi-modal Biomedical Understanding Benchmark to Probe the Perception Capabilities of Vision-Language Models**  
   Alejandro Lozano ⋅ Ryan D'Cunha ⋅ Daniel Jarquin ⋅ Min Sun ⋅ Josiah Aklilu ⋅ James Burgess ⋅ Yuhui Zhang ⋅ Paola Robayo ⋅ Jin Ye ⋅ Ming Hu ⋅ Zhongying Deng ⋅ Junjun He ⋅ Xin Chen ⋅ Yue Yao ⋅ Robert Tibshirani ⋅ Jeffrey Nirschl ⋅ Xiaoxiao Sun ⋅ Serena Yeung-Levy  
   [arXiv:2606.06696](https://arxiv.org/abs/2606.06696)
154. **MMR-Bench: A Comprehensive Benchmark for Multimodal LLM Routing**  
   Hao-Xuan Ma ⋅ Guannan Lai ⋅ Han-Jia Ye  
   [arXiv:2601.17814](https://arxiv.org/abs/2601.17814) · [code](https://github.com/Hunter-Wrynn/MMR-Bench)
155. **MOCHA: Multi-modal Objects-aware Cross-arcHitecture Alignment**  
   Elena Camuffo ⋅ Francesco Barbato ⋅ Mete Ozay ⋅ Simone Milani ⋅ Umberto Michieli  
   [arXiv:2509.14001](https://arxiv.org/abs/2509.14001)
156. **Molmo-Point: Better Pointing for VLMs with Grounding Tokens**  
   Christopher Clark ⋅ Yue Yang ⋅ Jae Sung Park ⋅ Zixian Ma ⋅ Jieyu Zhang ⋅ Rohun Tripathi ⋅ Mohammadreza Salehi ⋅ Sangho Lee ⋅ Ranjay Krishna
157. **MotionAtlas: A High-Quality Dataset and Benchmark for Dense Motion Captioning**  
   Weisong Liu ⋅ Haochen Wang ⋅ Gaokuan Gaokuan ⋅ Yuhao Wang ⋅ Yikang Zhou ⋅ Zhongwei Ren ⋅ Guangcan Mai ⋅ Anran Wang ⋅ Yanwei Li ⋅ Xiangtai Li ⋅ Zhaoxiang Zhang
158. **Multi-dimensional Preference Alignment by Conditioning Reward Itself**  
   JIHO JANG ⋅ Jin-Young Kim ⋅ Kyungjune Baek ⋅ Nojun Kwak  
   [arXiv:2512.10237](https://arxiv.org/abs/2512.10237)
159. **MultihopSpatial: Multi-hop Compositional Spatial Reasoning Benchmark for Vision-Language Model**  
   Youngwan Lee ⋅ Soojin Jang ⋅ Yoorhim Cho ⋅ Seunghwan Lee ⋅ Yong-Ju Lee ⋅ Sung Hwang  
   [arXiv:2603.18892](https://arxiv.org/abs/2603.18892) · [project](https://youngwanlee.github.io/multihopspatial)
160. **Multiple Images Distract Large Multimodal Models via Attention Fragmentation**  
   Tingrui Qiao ⋅ Di Zhao ⋅ Yuzhuo Li ⋅ Bo Pang ⋅ Caroline Walker ⋅ Chris Cunningham ⋅ Yun Sing Koh
161. **MV-STRIDE: Enabling MLLMs to Master Multi-View Spatial Reasoning via Hierarchical Capability Modeling**  
   Jin Xu ⋅ Xiaojian Huang ⋅ zhang zhihong ⋅ Luo Zhuodong ⋅ Xuejin Chen ⋅ Jie Zhao ⋅ Xin Liu ⋅ Wang Xinzhi ⋅ Jiansheng Wei
162. **NaVLM-PVC: Progressive Visual Compression for Efficient Native-Resolution Encoding in MLLMs**  
   Shichu Sun ⋅ Yichen Zhang ⋅ Haolin Song ⋅ Zonghao Guo ⋅ Chi Chen ⋅ Yidan Zhang ⋅ Yuan Yao ⋅ Zhiyuan Liu ⋅ Maosong Sun
163. **Neural Gate: Mitigating Privacy Risks in LVLMs via Neuron-Level Gradient Gating**  
   Xiangkui Cao ⋅ Jie Zhang ⋅ Meina Kan ⋅ Shiguang Shan ⋅ Xilin CHEN  
   [arXiv:2603.12598](https://arxiv.org/abs/2603.12598) · [code](https://github.com/Xiangkui-Cao/Neural-Gate)
164. **OmniFit: Multi-modal 3D Body Fitting via Scale-agnostic Dense Landmark Prediction**  
   Zeyu CAI ⋅ Yuliang Xiu ⋅ renke wang ⋅ Zhijing Shao ⋅ Xiaoben Li ⋅ YU Siyuan ⋅ Chao Xu ⋅ Yang Liu ⋅ Baigui Sun ⋅ Jian Yang ⋅ zhenyu zhang  
   [arXiv:2604.21575](https://arxiv.org/abs/2604.21575) · [project](https://zcai0612.github.io/OmniFit/)
165. **OmniMamba: Efficient and Unified Multimodal Understanding and Generation via State Space Models**  
   Jialv Zou ⋅ Bencheng Liao ⋅ Qian Zhang ⋅ Wenyu Liu ⋅ Xinggang Wang  
   [arXiv:2503.08686](https://arxiv.org/abs/2503.08686) · [code](https://github.com/hustvl/OmniMamba)
166. **OmniSch: A Multimodal PCB Schematic Benchmark For Structured Diagram Visual Reasoning**  
   Taiting Lu ⋅ Kaiyuan Lin ⋅ Yuxin Tian ⋅ Yubo Wang ⋅ Muchuan Wang ⋅ Sharique Khatri ⋅ Akshit Kartik ⋅ Yixi Wang ⋅ Amey Rane ⋅ Yida Wang ⋅ Yifan Yang ⋅ Yi-Chao Chen ⋅ yincheng jin ⋅ Mahanth Gowda  
   [arXiv:2604.00270](https://arxiv.org/abs/2604.00270)
167. **On Locality and Length-Generalization in Visual Reasoning**  
   Pulkit Madan ⋅ Sanjay Haresh ⋅ Reza Ebrahimi ⋅ Apratim Bhattacharyya ⋅ Sunny Panchal ⋅ Roland Memisevic  
   [arXiv:2607.09061](https://arxiv.org/abs/2607.09061)
168. **On Test-Time Scaling for Vision-Language Models**  
   Fawaz Sammani ⋅ Tzoulio Chamiti ⋅ Nikos Deligiannis  
   [arXiv:2606.28864](https://arxiv.org/abs/2606.28864)
169. **Open Your Eyes: Benchmarking the Detection of Fabricated Realities and Weaponized Ethics in VLMs**  
   Amit Pandey ⋅ Aditya Mohan ⋅ Phani Sankar
170. **PACO: Stabilizing Vision Embeddings along Local Paths for Robust Vision-Language Models**  
   Qihang Tang ⋅ Jiacheng Pi ⋅ Zhiguo Yang ⋅ Xu Liu ⋅ Perley Xu ⋅ Wenjie Ruan
171. **PanoGrounder: Bridging 2D and 3D with Panoramic Scene Representations for VLM-based 3D Visual Grounding**  
   Seongmin Jung ⋅ Seongho Choi ⋅ Gunwoo Jeon ⋅ Minsu Cho ⋅ Jongwoo Lim  
   [arXiv:2512.20907](https://arxiv.org/abs/2512.20907)
172. **Parallel Vision Token Scheduling for Fast and Accurate Multimodal LMMs Inference**  
   Wengyi Zhan ⋅ Mingbao Lin ⋅ Zhihang Lin ⋅ Rongrong Ji  
   [arXiv:2511.18875](https://arxiv.org/abs/2511.18875)
173. **Paying More Attention to Visual Tokens in Self-Evolving Large Multimodal Models**  
   Shravan Venkatraman ⋅ Ritesh Thawkar ⋅ Omkar Thawakar ⋅ Rao M Anwer ⋅ Hisham Cholakkal ⋅ Salman Khan ⋅ Fahad Shahbaz Khan  
   [arXiv:2606.27373](https://arxiv.org/abs/2606.27373) · [project](https://mbzuai-oryx.github.io/VISE)
174. **PercepTax: Benchmarking Cross-Property Reasoning in Vision-Language Models**  
   Jonathan Lee ⋅ Xingrui Wang ⋅ Jiawei Peng ⋅ Luoxin Ye ⋅ Zehan Zheng ⋅ Tiezheng Zhang ⋅ Tao Wang ⋅ Wufei Ma ⋅ Siyi Chen ⋅ Yu-Cheng Chou ⋅ Prakhar Kaushik ⋅ Alan Yuille
175. **Personalize Your Large Vision-language Models With In-context Prompt Tuning**  
   Yanshu Li ⋅ Jiaqian Li ⋅ Kuai Yu ⋅ Xi Xiao ⋅ Dongfang Liu ⋅ Tianyang Wang ⋅ Ruixiang Tang  
   [arXiv:2605.31513](https://arxiv.org/abs/2605.31513)
176. **Personalizing MLLMs via Reinforced Multimodal Reference Game**  
   Deepayan Das ⋅ Davide Talon ⋅ Yiming Wang ⋅ Massimiliano Mancini ⋅ Elisa Ricci  
   [arXiv:2606.28845](https://arxiv.org/abs/2606.28845) · [project](https://deepayan137.github.io/papers/conversational-personalization.html)
177. **PhyMAGIC: Physical Motion-Aware Generative Inference with Confidence-guided VLM**  
   Siwei Meng ⋅ Yawei Luo ⋅ Ping Liu  
   [arXiv:2505.16456](https://arxiv.org/abs/2505.16456)
178. **Prefill-Time Interventions against Adversarial Attacks on Large Vision-Language Models**  
   Zhewen Yao ⋅ Yao Zhu ⋅ Shiliang Zhang
179. **ProactiveBench: Benchmarking Proactiveness in Multimodal Large Language Models**  
   Thomas De Min ⋅ Subhankar Roy ⋅ Stéphane Lathuilière ⋅ Elisa Ricci ⋅ Massimiliano Mancini  
   [arXiv:2603.19466](https://arxiv.org/abs/2603.19466)
180. **Probe, Anchor, and Amend: Active Test-Time Adaptation of Vision-Language Models**  
   Jiaqi Lin ⋅ Chaoqi Chen ⋅ Xiasi Wang ⋅ Mingfu Yan ⋅ Jiancheng Huang ⋅ Jianzhuang Liu ⋅ Wenming Yang ⋅ Qingmin Liao
181. **ProLaViT: Learning Progressive Latent Visual Thoughts in Structured Latent Space**  
   Peiming Li ⋅ Yifan Wang ⋅ Xiaotian Zhang ⋅ Zhiyuan Hu ⋅ Shiyu Li ⋅ Zheng Wei ⋅ Yang Tang  
   [arXiv:2607.02907](https://arxiv.org/abs/2607.02907)
182. **ProMSA:Progressive Multimodal Search Agents for Knowledge-Based Visual Question Answering**  
   ZhengXian Wu ⋅ Hangrui Xu ⋅ Kai Shi ⋅ Zhuohong Chen ⋅ Yunyao Yu ⋅ Chuanrui Zhang ⋅ ZIRUI LIAO ⋅ JunYang JunYang ⋅ Zhenyu Yang ⋅ Haonan Lu ⋅ Haoqian Wang
183. **ReasonCLIP-58M: Visually Grounded Commonsense Reasoning Supervision for CLIP**  
   Sicheng Zhang ⋅ Muhammad Muzammal Naseer ⋅ Binzhu Xie ⋅ Naufal Suryanto ⋅ Shi Qiu ⋅ Jamal Bentahar ⋅ NAVEED AKHTAR ⋅ Shah Mubarak  
   [arXiv:2606.26794](https://arxiv.org/abs/2606.26794) · [code](https://github.com/RISys-Lab/ReasonCLIP)
184. **Reasoning Path and Latent State Analysis for Multi-view Visual Spatial Reasoning: A Cognitive Science Perspective**  
   Qiyao Xue ⋅ Haoming Wang ⋅ Weichen Liu ⋅ Shiqi Wang ⋅ Yuyang Wu ⋅ Wei Gao  
   [arXiv:2512.02340](https://arxiv.org/abs/2512.02340) · [code](https://huggingface.co/datasets/Xue0823/ReMindView-Bench)
185. **ReflectCAP: Detailed Image Captioning with Reflective Memory**  
   Kyungmin Min ⋅ Minbeom Kim ⋅ Kang-il Lee ⋅ Seunghyun Yoon ⋅ Kyomin Jung  
   [arXiv:2604.12357](https://arxiv.org/abs/2604.12357)
186. **RegRet: Enhancing Region-Level Retrieval in Large Multimodal Models**  
   Xun Liang ⋅ Honghui Yang ⋅ Weihang Pan ⋅ Boyuan Pan ⋅ Yao Hu ⋅ Binbin Lin ⋅ Deng Cai ⋅ Ruisi Zhao ⋅ Wenxiao Wang
187. **Reinforcing Vision-Language Models for Image Quality Assessment with Grounding Process Rewards**  
   Jingwei Liu ⋅ Hongyan Li ⋅ Bo Liu ⋅ Tianlin Zhang ⋅ Yifei Qian ⋅ Congyang Zhao ⋅ Junhong Liu ⋅ Yang Cai ⋅ Ling Yang
188. **Reliable Reasoning in SVG-LLMs via Multi-Task Multi-Reward Reinforcement Learning**  
   Haomin Wang ⋅ Qi Wei ⋅ Qianli Ma ⋅ Shengyuan Ding ⋅ Jinhui Yin ⋅ Kai Chen ⋅ hongjie Zhang  
   [arXiv:2603.16189](https://arxiv.org/abs/2603.16189)
189. **Residual-Guided Expert Specialization for Incomplete Multimodal Learning**  
   Seunghun Baek ⋅ Jihwan Park ⋅ Jaeyoon Sim ⋅ Minjae Jeong ⋅ Hoseok Lee ⋅ Won Hwa Kim  
   [arXiv:2606.30355](https://arxiv.org/abs/2606.30355)
190. **Rethinking Visual Privacy: A Compositional Privacy Risk Framework for Severity Assessment with VLMs**  
   Efthymios Tsaprazlis ⋅ Tiantian Feng ⋅ Anil Ramakrishna ⋅ Sai Karimireddy ⋅ Rahul Gupta ⋅ Shrikanth Narayanan  
   [arXiv:2603.21573](https://arxiv.org/abs/2603.21573)
191. **Revisiting Parameter Redundancy in Vision-Language-Action Models: Insights from VLM-to-VLA Adaptation**  
   Fengnian Zhang ⋅ Tao Huang ⋅ Siyu Xu ⋅ Zhong Jin ⋅ Chang Xu  
   [arXiv:2606.31382](https://arxiv.org/abs/2606.31382)
192. **RGBT-GroundBench: Visual Grounding Beyond RGB in Complex Real-World Scenarios**  
   Tianyi Zhao ⋅ Jiawen Xi ⋅ Linhui Xiao ⋅ Junnan Li ⋅ Xue Yang ⋅ Maoxun Yuan ⋅ Xingxing Wei  
   [arXiv:2512.24561](https://arxiv.org/abs/2512.24561)
193. **RoadBench: Benchmarking MLLMs on Fine-Grained Spatial Understanding and Reasoning under Urban Road Scenarios**  
   Jun Zhang ⋅ Xin Zhang ⋅ Jie Feng ⋅ Long Chen ⋅ Junhui Wang ⋅ Zhicheng Liu ⋅ Depeng Jin ⋅ Yong Li  
   [arXiv:2511.18011](https://arxiv.org/abs/2511.18011) · [code](https://github.com/tsinghua-fib-lab/RoadBench)
194. **Robobench: A Comprehensive Evaluation Benchmark for Multimodal Large Language Models as Embodied Brain**  
   Yulin Luo ⋅ Chun-Kai Fan ⋅ Menghang Dong ⋅ Jiayu Shi ⋅ Xiangju Mi ⋅ Mengdi Zhao ⋅ Bo-Wen Zhang ⋅ Cheng Chi ⋅ Jiaming Liu ⋅ Gaole Dai ⋅ Rongyu Zhang ⋅ Ruichuan An ⋅ Kun Wu ⋅ Zhengping Che ⋅ shaoxuan Xie ⋅ Guocai Yao ⋅ Zhongxia Zhao ⋅ Pengwei Wang ⋅ Guang Liu ⋅ Zhongyuan Wang ⋅ Tiejun Huang ⋅ Shanghang Zhang  
   [arXiv:2510.17801](https://arxiv.org/abs/2510.17801)
195. **RoboStream: Weaving Spatio-Temporal Reasoning with Memory in Vision-Language Models for Robotics**  
   Yuzhi Huang ⋅ Jie Wu ⋅ Weijue Bu ⋅ Ziyi Xiong ⋅ Gaoyang Jiang ⋅ Ye Li ⋅ Kangye Ji ⋅ Shuzhao Xie ⋅ Yue Huang ⋅ Chenglei Wu ⋅ Jingyan Jiang ⋅ Zhi Wang  
   [arXiv:2603.12939](https://arxiv.org/abs/2603.12939)
196. **RSICCLLM: A Multimodal Large Language Model for Remote Sensing Image Change Captioning**  
   Yelin Wang ⋅ Zijia Song ⋅ Shuo Ye ⋅ Chuanguang Yang ⋅ Miaoyu Wang ⋅ Yong Xu ⋅ Zhulin An ⋅ Yongjun Xu ⋅ Zitong Yu  
   [arXiv:2606.28266](https://arxiv.org/abs/2606.28266) · [code](https://github.com/keaill/RSICCLLM)
197. **Safe Responses Matter: Output-Aware Safety Guardrail Mitigate Over-Refusal in MLLMs**  
   Jiayi Li ⋅ Kun Zhan  
   [arXiv:2607.09697](https://arxiv.org/abs/2607.09697) · [code](https://github.com/kunzhan/OutGuard)
198. **SAFE-EQA: Semantic-Aware Efficient Exploration for Embodied Question Answering**  
   Yijie Tang ⋅ Ke Xia ⋅ Jiazhao Zhang ⋅ Zhinan Yu ⋅ Zhiyuan Yu ⋅ Dezun Dong ⋅ Renjiao Yi ⋅ Chenyang Zhu ⋅ Kai Xu
199. **Same Person, Different Depiction: Counterfactual Evaluation of Vision-Language Models on Individuals with Limb Deficiencies**  
   Heming Du ⋅ Jiaying Ying ⋅ Xin Chen ⋅ Sen Wang ⋅ Xue Li ⋅ Xin Yu
200. **Same Pool, Different Answer: Stable Best-of-N Selection for Vision-Language Models**  
   Pengfei Zheng
201. **SAMPLe: A Sharpness Aware Minimization based Optimizer for Prompt Learning in Vision-Language Models**  
   Hossein Rajoli nowdeh ⋅ Fatemeh Lotfi ⋅ Niloufar Alipour Talemi ⋅ Hossein Kashiani ⋅ Xiaolong Ma ⋅ Fatemeh Afghah
202. **SCoT: Similarity-guided Conflict-aware Task Consolidation for Continual VQA**  
   Anand Patel ⋅ Moloud Abdar ⋅ Biplab Banerjee
203. **SDSA: Shallow-Deep Squeezing Adapter for Vision-Language Models**  
   Hao Wang ⋅ Rui Zhu ⋅ Xiaoxu Li ⋅ Zhanyu Ma ⋅ Jing-Hao Xue
204. **See Only When Needed: Context-Aware Attention Intervention for Hallucination-Free LVLMs**  
   Yuqing Lei ⋅ Wenbo Lyu ⋅ Yingjun Du ⋅ Xiantong Zhen ⋅ Cees Snoek ⋅ Ling Shao
205. **Seeing Isn't Orienting: A Cognitively Grounded Hierarchical Benchmark for Object Orientation in MLLMs**  
   Nazia Tasnim ⋅ Keanu Nichols ⋅ Yuting Yan ⋅ Nicholas Ikechukwu ⋅ Elva Zou ⋅ Deepti Ghadiyaram ⋅ Bryan Plummer
206. **SEERBench: A Spatial Ego-Exo Reasoning Benchmark for MLLMs with a Simple Yet Effective Baseline**  
   Fengyuan Lu ⋅ Jiahe Feng ⋅ Zhengyang Zhou ⋅ Shaofeng Zhang ⋅ Wenbin Li ⋅ Qi Fan ⋅ Yang Gao
207. **Semantic Generative Tuning for Unified Multimodal Models**  
   Songsong Yu ⋅ Yuxin Chen ⋅ Ying Shan ⋅ Yanwei Li  
   [arXiv:2605.18714](https://arxiv.org/abs/2605.18714) · [project](https://song2yu.github.io/SGT/)
208. **ShellMaker: Language-Guided Exterior Completion under Structural Constraints**  
   Ruiqi Xu ⋅ Daniel Aliaga  
   [arXiv:2606.31680](https://arxiv.org/abs/2606.31680) · [project](https://ruiqixu37.github.io/ShellMaker_web/)
209. **Show Me Examples: Inferring Visual Concepts from Image Sets**  
   Nick Stracke ⋅ Kolja Bauer ⋅ Stefan Andreas Baumann ⋅ Miguel Angel Bautista ⋅ Joshua Susskind ⋅ Bjorn Ommer  
   [arXiv:2607.02402](https://arxiv.org/abs/2607.02402) · [code](https://github.com/CompVis/set-learner)
210. **SiGMA: Sign-Guided Merging and Adaptation framework for Multimodal Continual Instruction Tuning**  
   Keonhee Park ⋅ Gunhee Kim
211. **SiPhy: Single-Image Physical Property Reasoning**  
   Hoang Le ⋅ Joonwoo Kwon ⋅ Elkhan Ismayilzada ⋅ Yufei Zhang ⋅ Zijun Cui  
   [arXiv:2607.22355](https://arxiv.org/abs/2607.22355)
212. **SlowBA: An efficiency backdoor attack towards VLM-based GUI agents**  
   Junxian Li ⋅ Tu Lan ⋅ Haozhen Tan ⋅ Yan Meng ⋅ Haojin Zhu  
   [arXiv:2603.08316](https://arxiv.org/abs/2603.08316) · [code](https://github.com/tu-tuing/SlowBA)
213. **Spanning the Visual Analogy Space with a Weight Basis of LoRAs**  
   Hila Manor ⋅ Rinon Gal ⋅ Haggai Maron ⋅ Tomer Michaeli ⋅ Gal Chechik  
   [arXiv:2602.15727](https://arxiv.org/abs/2602.15727) · [project](https://research.nvidia.com/labs/par/lorweb)
214. **SPAR: Semantic-Pixel Self-Alignment and Adaptive Routing for Unified Multimodal Models**  
   Hongxiang Li ⋅ Hongxu chen ⋅ chenyang zhu ⋅ Xiaoshuang Huang ⋅ Jiayin Cai ⋅ Xiaolong Jiang ⋅ Yao Hu ⋅ Long Chen  
   [arXiv:2606.23041](https://arxiv.org/abs/2606.23041)
215. **Spectral Evolution-Guided Token Pruning in Large Multimodal Models**  
   Bin Chen ⋅ Yuxiang Cai ⋅ Yadan Luo ⋅ Yi Zhang ⋅ Jianwei Yin ⋅ Zhi Chen
216. **SPOT-E: Test-Time Entropy Shaping with Visual Spotlights for Frozen VLMs**  
   Bo Yin ⋅ Xiaobin Hu ⋅ Chengming Xu ⋅ Ruolin Shen ⋅ Mo Yang ⋅ Jiangning Zhang ⋅ Peng-Tao Jiang ⋅ Cheng Tan ⋅ Shuicheng Yan  
   [arXiv:2606.20244](https://arxiv.org/abs/2606.20244) · [code](https://github.com/YinBo0927/SPOT-E)
217. **SRUM: Fine-Grained Self-Rewarding for Unified Multimodal Models**  
   Weiyang Jin ⋅ Yuwei Niu ⋅ Jiaqi Liao ⋅ Chengqi Duan ⋅ Aoxue Li ⋅ Shenghua Gao ⋅ Xihui Liu  
   [arXiv:2510.12784](https://arxiv.org/abs/2510.12784) · [project](https://waynejin0918.github.io/srum_web/)
218. **Stabilizing Ultra-Low-Bit Quantization of Multimodal LLMs via Global Bit Allocation**  
   Guilin Li ⋅ Yuexiao Ma ⋅ Yue Zhang ⋅ Xinxiong Wu ⋅ Jiaqi Zhou ⋅ Qingheng Zhang ⋅ Yan Zhang ⋅ Fei Chao ⋅ Xiawu Zheng ⋅ Rongrong Ji
219. **Starve to Perceive: Taming Lazy Perception in VLMs with Constrained Visual Bandwidth**  
   Yuhuan Wu ⋅ Haozhe Wang ⋅ Cong Wei ⋅ Chong Peng ⋅ Fangzhen Lin ⋅ Wenhu Chen  
   [arXiv:2605.18603](https://arxiv.org/abs/2605.18603)
220. **STAT: Soft Tail-dropping for Adaptive Visual Tokenization**  
   Zeyuan Chen ⋅ Kai Zhang ⋅ Zhuowen Tu ⋅ Yuanjun Xiong
221. **Staying VIGILant: Mitigating Visual Laziness in MLLMs via Information-Theoretic Alignment**  
   Xi Xiao ⋅ Chen Liu ⋅ Chih-Ting Liao ⋅ Yunbei Zhang ⋅ Qizhen Lan ⋅ YUXIANG WEI ⋅ Lin Zhao ⋅ Janet Wang ⋅ Jianyang Gu ⋅ Muchao Ye ⋅ Tianyang Wang ⋅ Hao Xu
222. **StochasT: Learning with Stochastic Turn Depth for Visual Instruction Tuning**  
   Yuan Qing ⋅ Chengzhi Mao ⋅ Boqing Gong  
   [arXiv:2607.00465](https://arxiv.org/abs/2607.00465) · [project](https://yuanqing-ai.github.io/StochasT)
223. **SupGRPO: Enhancing GRPO with Matching-based Online SFT for Text Spotting**  
   Xudong Xie ⋅ Yuzhe Li ⋅ Jing Shi ⋅ Zhifei Zhang ⋅ Curtis Wigington ⋅ Zhaowen Wang
224. **SWAN: World-Aware Adaptive Multimodal Networks for Runtime Variations**  
   Jason Wu ⋅ Shir-Kang Jin ⋅ Yuyang Yuan ⋅ Maggie Wigness ⋅ Lance Kaplan ⋅ Hang Qiu ⋅ Mani Srivastava
225. **Syn-GRPO: Self-Evolving Data Synthesis for MLLM Perception Reasoning**  
   Qihan Huang ⋅ Haofei Zhang ⋅ Rong Wei ⋅ Yi Wang ⋅ Rui Tang ⋅ Mingli Song ⋅ Jie Song  
   [arXiv:2511.19343](https://arxiv.org/abs/2511.19343) · [code](https://github.com/hqhQAQ/Syn-GRPO)
226. **SyncLoop: A Multimodal Dual-Loop Framework for Self-Improving Mathematical Reasoning**  
   xiuwei chen ⋅ Wentao Hu ⋅ Hanhui Li ⋅ Yongxin Wang ⋅ Jun Zhou ⋅ Zisheng Chen ⋅ Meng Cao ⋅ Yihan Zeng ⋅ Kui Zhang ⋅ Yu-Jie Yuan ⋅ Jianhua Han ⋅ Hang Xu ⋅ Xiaodan Liang  
   [arXiv:2507.16518](https://arxiv.org/abs/2507.16518)
227. **Synesthesia via Direct Latent Augmentation: Bypassing the Decode-Encode Loop for Cross-Modal Distillation**  
   Cristian Sbrolli ⋅ Nicolas Michel ⋅ Matteo Matteucci ⋅ Toshihiko Yamasaki
228. **T-REN: Learning Text-Aligned Region Tokens Improves Dense Vision-Language Alignment and Scalability**  
   Savya Khosla ⋅ Sethuraman T V ⋅ Aryan Chadha ⋅ Alex Schwing ⋅ Derek Hoiem  
   [arXiv:2604.18573](https://arxiv.org/abs/2604.18573) · [code](https://github.com/savya08/T-REN)
229. **TARS: MinMax Token-Adaptive Preference Strategy for Hallucination Reduction in MLLMs**  
   KEJIA ZHANG ⋅ Keda TAO ⋅ Zhiming Luo ⋅ Chang Liu ⋅ Jiasheng Tang ⋅ Huan Wang  
   [arXiv:2507.21584](https://arxiv.org/abs/2507.21584)
230. **TecoPrompt: Temporal-Conservative Prompt Learning for Vision-Language Models**  
   zeyi shao ⋅ Haowen Hua ⋅ Jiaxin Zhang ⋅ John See ⋅ Zeyd Boukhers ⋅ Cong Yang
231. **Temporal and Cross-modal Alignment for Enhanced Audiovisual Video Captioning**  
   Chen Zhao ⋅ Jiajun Ma ⋅ Qilong Huang ⋅ Tiehan Fan ⋅ Hongyu Li ⋅ Zhuoliang Kang ⋅ Xiaoming Wei ⋅ Jian Yang ⋅ Ying Tai  
   [arXiv:2607.01667](https://arxiv.org/abs/2607.01667)
232. **The Cost of Reasoning: Chain-of-Thought Induces Overconfidence in Vision-Language Models**  
   Robert Welch ⋅ Emir Konuk ⋅ Kevin Smith  
   [arXiv:2603.16728](https://arxiv.org/abs/2603.16728)
233. **Think While Watching: Online Streaming Segment-Level Memory for Multi-Turn Video Reasoning in Multimodal Large Language Models**  
   Lu Wang ⋅ Zhuoran Jin ⋅ Yupu Hao ⋅ Yubo Chen ⋅ Kang Liu ⋅ Yulong Ao ⋅ Jun Zhao  
   [arXiv:2603.11896](https://arxiv.org/abs/2603.11896) · [code](https://github.com/wl666hhh/Think_While_Watching/)
234. **Thinking Ahead: Foresight Intelligence in MLLMs and World Model**  
   Zhantao Gong ⋅ Liaoyuan Fan ⋅ Qing Guo ⋅ Xun Xu ⋅ Xulei Yang ⋅ Shijie Li  
   [arXiv:2511.18735](https://arxiv.org/abs/2511.18735)
235. **Thinking from the Robot’s View: The CoT-HRC Benchmark for Human Intent Reasoning in Embodied Collaboration**  
   Chenxi Deng ⋅ Chao Xu ⋅ JianmingLiu JianmingLiu ⋅ Shaofei Chen
236. **To Adapt or Not to Adapt? Selective Adaptation for Vision-Language Models**  
   Siru Jiang ⋅ Yuwei Liang ⋅ Jian Liang ⋅ Ran He ⋅ Tieniu Tan
237. **ToDRE: Effective Visual Token Pruning via Token Diversity and Task Relevance**  
   Duo Li ⋅ Zuhao Yang ⋅ Xiaoqin Zhang ⋅ Ling Shao ⋅ Shijian Lu  
   [arXiv:2505.18757](https://arxiv.org/abs/2505.18757)
238. **Token-Based Affordance Grounding with Large Vision-Language Models**  
   Seung Il Lee ⋅ Qinqian Lei ⋅ Daguang Xu ⋅ Dong Yang ⋅ Robby T. Tan ⋅ Yixin Chen ⋅ Bo Wang  
   [arXiv:2607.03595](https://arxiv.org/abs/2607.03595)
239. **Toward Interpretable Analysis of Whole-slide Pathology Images via Large Language Model-based Agentic Reasoning**  
   Jingyun Chen ⋅ Linghan Cai ⋅ Zhikang Wang ⋅ Yi Huang ⋅ Songhan Jiang ⋅ Shenjin Huang ⋅ Hongpeng Wang ⋅ Yongbing Zhang  
   [arXiv:2511.17052](https://arxiv.org/abs/2511.17052)
240. **Towards Benign Memory Forgetting for Selective Multimodal Large Language Model Unlearning**  
   Zhen Zeng ⋅ Leijiang Gu ⋅ Zhangling Duan ⋅ Feng Li ⋅ Zenglin Shi ⋅ Cees Snoek ⋅ Meng Wang  
   [arXiv:2511.20196](https://arxiv.org/abs/2511.20196) · [code](https://github.com/zeng-zhen/S-MLLMUn)
241. **Towards Purified Multi-Label Test-Time Adaptation of Vision-Language Models**  
   Yiwen Liang ⋅ Hui Chen ⋅ Yizhe Xiong ⋅ Mengyao Lyu ⋅ Yuhan Cao ⋅ Zijia Lin ⋅ SHUAICHENG NIU ⋅ Sicheng Zhao ⋅ Jungong Han ⋅ Guiguang Ding
242. **Towards Scalable Pre-training of Visual Tokenizers for Generation**  
   Jingfeng Yao ⋅ Yuda Song ⋅ Yucong Zhou ⋅ Xinggang Wang  
   [arXiv:2512.13687](https://arxiv.org/abs/2512.13687) · [code](https://github.com/MiniMax-AI/VTP)
243. **Towards Spatial Trace with Reasoning in Vision-Language Models for Robotics**  
   Enshen Zhou ⋅ Yibo Li ⋅ Jingkun An ⋅ Jiayuan Zhang ⋅ Shanyu Rong ⋅ Mengzhen Liu ⋅ Yi Han ⋅ Yuheng Ji ⋅ Huajie Tan ⋅ Jiawei He ⋅ Pengwei Wang ⋅ Zhongyuan Wang ⋅ Cheng Chi ⋅ Lu Sheng ⋅ Shanghang Zhang  
   [arXiv:2512.13660](https://arxiv.org/abs/2512.13660) · [project](https://zhoues.github.io/RoboTracer)
244. **Training-free Uncertainty Guidance for Complex Visual Tasks with MLLMs**  
   Sanghwan Kim ⋅ Rui Xiao ⋅ Stephan Alaniz ⋅ Yongqin Xian ⋅ Zeynep Akata  
   [arXiv:2510.00705](https://arxiv.org/abs/2510.00705)
245. **Transferability Between Understanding and Generation in Unified Multimodal Models**  
   Jiwon Kang ⋅ Heeji Yoon ⋅ Jaewoo Jung ⋅ Jaewon Min ⋅ Minkyeong Jeon ⋅ Biyeon Hwang ⋅ Sangwon Jung ⋅ Seungryong Kim  
   [arXiv:2607.04423](https://arxiv.org/abs/2607.04423) · [project](https://cvlab-kaist.github.io/UMM_Transferability/)
246. **TruthLens: Object Hallucination Detection via Self-Evaluating Truthfulness Scores in LVLMs**  
   Yanqi Wu ⋅ Runhe Lai ⋅ Xinhua Lu ⋅ Qichao Chen ⋅ Zhiping Zhou ⋅ Jia-Xin Zhuang ⋅ Weijiang Yu ⋅ Ruixuan Wang  
   [arXiv:2608.05616](https://arxiv.org/abs/2608.05616) · [code](https://github.com/wyqstan/TruthLens)
247. **UC-VLM: Consistency-Driven Learning for AI-Generated Image Detection with Vision-Language Large Models**  
   Lei Tan ⋅ Shuwei Li ⋅ Mohan Kankanhalli ⋅ Robby T. Tan  
   [arXiv:2608.15238](https://arxiv.org/abs/2608.15238)
248. **UMO: Unified In-Context Learning Unlocks Motion Foundation Model Priors**  
   Xiaoyan Cong ⋅ Zekun Li ⋅ Zhiyang Dou ⋅ Hongyu Li ⋅ Omid Taheri ⋅ chuan guo ⋅ Abhay Mittal ⋅ Sizhe An ⋅ Taku Komura ⋅ Wojciech Matusik ⋅ Michael Black ⋅ Srinath Sridhar  
   [arXiv:2603.15975](https://arxiv.org/abs/2603.15975) · [project](https://oliver-cong02.github.io/UMO.github.io/)
249. **UniDDT: Unifying Multimodal Understanding and Generation with Decoupled Diffusion Transformer**  
   Shuai Wang ⋅ Liang Li ⋅ Yang Chen ⋅ Ruopeng Gao ⋅ Yao Teng ⋅ Limin Wang  
   [arXiv:2606.16255](https://arxiv.org/abs/2606.16255)
250. **UniReflect: Self-Reflection Tuning for Unified Multimodal Understanding and Generation**  
   Cong Wei ⋅ Zepeng Huang ⋅ Haoxian Tan ⋅ liang shuang ⋅ Lishuai Gao ⋅ Pengfei Yan ⋅ Xiaoming Wei
251. **Unlocking Complex Image Editing via Natively Interleaved Visual Textual CoT with Deep Confidence Reasoning**  
   Zhentao Zou ⋅ Zhengrong Yue ⋅ Kunpeng Du ⋅ Binglei Bao ⋅ Hanting Li ⋅ Haizhen Xie ⋅ Guozheng Xu ⋅ Yue Zhou ⋅ jie hu ⋅ Xue Jiang ⋅ Xinghao Chen
252. **Unlocking Few-Shot Capabilities in LVLMs via Prompt Conditioning and Head Selection**  
   Adhémar de Senneville ⋅ Xavier Bou ⋅ Jérémy Anger ⋅ Rafael Grompone von Gioi ⋅ Gabriele Facciolo  
   [arXiv:2603.24181](https://arxiv.org/abs/2603.24181)
253. **Unsafe by Reciprocity: How Generation–Understanding Coupling Undermines Safety in Unified Multimodal Models**  
   Kaishen Wang ⋅ Heng Huang  
   [arXiv:2603.27332](https://arxiv.org/abs/2603.27332)
254. **UrbanAlign: Post-hoc Semantic Calibration for VLM-Human Preference Alignment**  
   Yecheng Zhang ⋅ RONG ZHAO ⋅ Zhizhou Sha ⋅ Yong Li ⋅ Lei Wang ⋅ Ce Hou ⋅ Wen Ji ⋅ HUANG HAO ⋅ yunshan wan ⋅ Jian Yu ⋅ Junhao Xia ⋅ Yuru Zhang ⋅ Chunlei Shi  
   [arXiv:2602.19442](https://arxiv.org/abs/2602.19442)
255. **V-REX: Benchmarking Exploratory Visual Reasoning via Chain-of-Questions**  
   Chenrui Fan ⋅ Yijun Liang ⋅ Shweta Bhardwaj ⋅ Kwesi Cobbina ⋅ Ming Li ⋅ Tianyi Zhou  
   [arXiv:2512.11995](https://arxiv.org/abs/2512.11995)
256. **VDC-Agent: When Video Detailed Captioners Evolve Themselves via Agentic Self-Reflection**  
   Qiang Wang ⋅ XINYUAN GAO ⋅ SongLin Dong ⋅ Jizhou Han ⋅ Jiangyang Li ⋅ Yuhang He ⋅ Zhiheng Ma ⋅ Yihong Gong  
   [arXiv:2511.19436](https://arxiv.org/abs/2511.19436) · [project](https://vdcagent.github.io)
257. **VERDICT: Training-Free Step-Wise Verification of Multimodal Reasoning via Disagreement-Aware Consensus**  
   Rohit Sinha ⋅ Kunal Tilaganji ⋅ Tanuja Ganu ⋅ Nagarajan Natarajan ⋅ Amit Sharma ⋅ Vineeth N Balasubramanian  
   [arXiv:2608.10665](https://arxiv.org/abs/2608.10665)
258. **Vero: Open Reinforcement Learning Recipes for Visual Reasoning**  
   Gabriel Sarch ⋅ Linrong Cai ⋅ Qunzhong Wang ⋅ Haoyang Wu ⋅ Danqi Chen ⋅ Zhuang Liu
259. **VersaViT: Enhancing MLLM Vision Backbones via Task-Guided Optimization**  
   Yikun Liu ⋅ Yuan Liu ⋅ Shangzhe Di ⋅ Haicheng Wang ⋅ Zhongyin Zhao ⋅ Le Tian ⋅ Zhou Xiao ⋅ Jie Zhou ⋅ Jiangchao Yao ⋅ Yanfeng Wang ⋅ Weidi Xie  
   [arXiv:2602.09934](https://arxiv.org/abs/2602.09934)
260. **Video-Holmes: Can MLLM Think like Holmes for Complex Video Reasoning?**  
   JUNHAO CHENG ⋅ Yuying Ge ⋅ Teng Wang ⋅ Yixiao Ge ⋅ Jing Liao ⋅ Ying Shan  
   [arXiv:2505.21374](https://arxiv.org/abs/2505.21374) · [code](https://github.com/TencentARC/Video-Holmes)
261. **VIEW2SPACE: Studying Multi-View Visual Reasoning from Sparse Observations**  
   Fucai Ke ⋅ Zhixi Cai ⋅ Boying Li ⋅ Long Chen ⋅ Beibei Lin ⋅ Weiqing Wang ⋅ Pari Delir Haghighi ⋅ Gholamreza Haffari ⋅ Hamid Rezatofighi  
   [arXiv:2603.16506](https://arxiv.org/abs/2603.16506)
262. **ViewFusion: Structured Spatial Thinking Chains for Multi-View Reasoning**  
   Xingjian Tao ⋅ Yiwei Wang ⋅ Yujun Cai ⋅ Yifan Song ⋅ Jing Tang  
   [arXiv:2603.06024](https://arxiv.org/abs/2603.06024)
263. **VisCoP: Visual Probing for Video Domain Adaptation of Vision Language Models**  
   Dominick Reilly ⋅ Manish Govind ⋅ Le Xue ⋅ Srijan Das  
   [arXiv:2510.13808](https://arxiv.org/abs/2510.13808) · [code](https://github.com/dominickrei/VisCoP)
264. **Vision-as-Inverse-Graphics Agent via Interleaved Multimodal Reasoning**  
   Shaofeng Yin ⋅ Jiaxin Ge ⋅ Zora Wang ⋅ Xiuyu Li ⋅ Chenyang Wang ⋅ Michael Black ⋅ Trevor Darrell ⋅ Angjoo Kanazawa ⋅ Haiwen Feng  
   [arXiv:2601.11109](https://arxiv.org/abs/2601.11109) · [project](https://fugtemypt123.github.io/VIGA-website/)
265. **VisNec: Measuring and Leveraging Visual Necessity for Multimodal Instruction Tuning**  
   Mingkang Dong ⋅ Hongyi Cai ⋅ jie li ⋅ Sifan Zhou ⋅ Bin Ren ⋅ Kunyu Peng ⋅ Yuqian Fu  
   [arXiv:2603.01195](https://arxiv.org/abs/2603.01195) · [project](https://dmk041218.github.io/VisNec/)
266. **VISOR++ : VISUAL INPUT BASED STEERING FOR LARGE VISION LANGUAGE MODELS**  
   Ravikumar Balakrishnan ⋅ Mansi Phute
267. **VisReason: A Large-Scale Dataset for Visual Chain-of-Thought Reasoning**  
   Lingxiao Li ⋅ Yifan Wang ⋅ Xinyan Gao ⋅ Chen Tang ⋅ Xiangyu Yue ⋅ Chenyu You  
   [arXiv:2511.17731](https://arxiv.org/abs/2511.17731) · [project](https://y-research-sbu.github.io/VisReason/)
268. **VisReflect: Latent Visual Reflection for Fine-Grained Perception in Long Visual Context**  
   Xiaoqian Shen ⋅ Mohamed Elhoseiny  
   [arXiv:2606.30288](https://arxiv.org/abs/2606.30288) · [project](https://xiaoqian-shen.github.io/VisReflect)
269. **Visual Prompt Discovery via Semantic Exploration**  
   Jaechang Kim ⋅ Yotaro Shimose ⋅ Zhao Wang ⋅ Kuang-Da Wang ⋅ Jungseul Ok ⋅ Shingo Takamatsu  
   [arXiv:2603.16250](https://arxiv.org/abs/2603.16250) · [project](https://jaechang.dev/projects/SEVEX/)
270. **VisWordBench: Bridging the Gap in Cross-modal Reasoning for Multimodal Large Language Models**  
   Tianshu Zhang ⋅ Junzhe Chen ⋅ Yean Cheng ⋅ Demin Zhu ⋅ Haoze Zheng ⋅ Lijie Wen
271. **ViTexQA: A Multi-Frame Temporal Perception Dataset for Video Text Question Answering**  
   Zhentao Guo ⋅ Chen Duan ⋅ Tongkun Guan ⋅ Zining Wang ⋅ Kai zhou ⋅ Pengfei Yan  
   [arXiv:2606.24602](https://arxiv.org/abs/2606.24602)
272. **VIVAS: Vitalizing Visual Perception in VLM Pre-training via Vision-language Unified Autoregressive Supervision**  
   Zhehan Kan ⋅ Yubo Zhu ⋅ Xinghua Jiang ⋅ Zhixiang Wei ⋅ Shifeng Liu ⋅ Wei Tong ⋅ Sheng Zhong ⋅ Qingmin Liao ⋅ Wenming Yang ⋅ Xin Li ⋅ Yinsong Liu ⋅ Deqiang Jiang ⋅ Xing Sun
273. **VKnowU: Evaluating Visual Knowledge Understanding in Multimodal LLMs**  
   Tianxiang Jiang ⋅ Sheng Xia ⋅ Yicheng Xu ⋅ Linquan Wu ⋅ Xiangyu Zeng ⋅ Limin Wang ⋅ Yu Qiao ⋅ Yi Wang  
   [arXiv:2511.20272](https://arxiv.org/abs/2511.20272) · [code](https://github.com/OpenGVLab/VKnowU)
274. **VLMSysTrojan: Stealthy System-Aware Backdoor Attacks Against Vision-Language Models**  
   Yezheng Cheng ⋅ Zexin Li ⋅ Jiaqi Wu ⋅ Zhihong Zhang ⋅ Simin Chen
275. **VLZip: Unified Visual and Textual Compression for Interleaved Long-Context Modeling**  
   Yuqi Zhang ⋅ pengpeng Zeng ⋅ Yuyu Guo ⋅ Wenjie Yang ⋅ Lingchen Meng ⋅ Peng Di ⋅ Hang Yu ⋅ Zuxuan Wu ⋅ Yu-Gang Jiang  
   [arXiv:2608.08630](https://arxiv.org/abs/2608.08630) · [code](https://github.com/ShareLab-SII/VLZip)
276. **What CLIP Knows but Cannot Say: Recovering Negation from Frozen Intermediate Features**  
   Chen-yi Lu ⋅ Yueh-Shao Chen ⋅ Somali Chaterji  
   [arXiv:2607.23271](https://arxiv.org/abs/2607.23271) · [project](https://stevencylu.github.io/PeakPatch/)
277. **When Sinks Help or Hurt: Unified Framework for Attention Sink in MLLMs**  
   Jiho Choi ⋅ Jaemin Kim ⋅ JINHWI PARK ⋅ Seunghoon Hong ⋅ Sanghwan Kim
278. **Where to Look Matters: Learning Influential Views for VLM-based 3D Visual Grounding**  
   Tsung-Chih Chiang ⋅ Hsuan-Kung Yang ⋅ Jou-Min Liu ⋅ Ting-Ru Liu ⋅ Chun-Wei Huang ⋅ Quan Kong ⋅ Chun-Yi Lee
279. **Why and When Visual Token Pruning Fails? A Study on Relevant Visual Information Shift in MLLMs Decoding**  
   Jiwan Kim ⋅ Kibum Kim ⋅ Wonjoong Kim ⋅ Byung-Kwan Lee ⋅ Chanyoung Park  
   [arXiv:2604.12358](https://arxiv.org/abs/2604.12358) · [project](https://ptkjw1997.github.io/DSTP-page/)
280. **Why Do Vision Language Models Struggle To Recognize Human Emotions?**  
   Madhav Agarwal ⋅ Sotirios Tsaftaris ⋅ Laura Sevilla ⋅ Steven McDonagh  
   [arXiv:2604.15280](https://arxiv.org/abs/2604.15280)
281. **Why Far Looks Up: Probing Spatial Representation in Vision-Language Models**  
   Cheolhong Min ⋅ Jaeyun Jung ⋅ Daeun Lee ⋅ Hyeonseong Jeon ⋅ Yu Su ⋅ Jonathan Tremblay ⋅ Chan Hee Song ⋅ Jaesik Park  
   [arXiv:2605.30161](https://arxiv.org/abs/2605.30161) · [project](https://cheolhong0916.github.io/whyfarlooksup.github.io/)
282. **X-Stream: Benchmarking MLLMs as Multiplexers for Multi-Stream Understanding**  
   Peiwen Sun ⋅ Xudong LU ⋅ Huadai Liu ⋅ Yang Bo ⋅ Dongming Wu ⋅ Huankang Guan ⋅ Minghong Cai ⋅ Jinpeng Chen ⋅ Xintong Guo ⋅ Shuhan LI ⋅ FANG LIU ⋅ Rui Liu ⋅ Xiangyu Yue
283. **YesTrack: Referring Multi-Object Tracking via MLLM-based Yes/No Reasoning**  
   Quansheng Hu ⋅ Qin Sun ⋅ Qiansen Dai ⋅ Jin Ding ⋅ Wan Zhang ⋅ Xue Zhou ⋅ Jianxiao Zou

## Video Understanding & Temporal Modeling

*104 papers · 59 with links*

1. **ActionParty: Multi-Subject Action Binding in Generative Video Games**  
   Alexander Pondaven ⋅ Ziyi Wu ⋅ Igor Gilitschenski ⋅ Philip Torr ⋅ Sergey Tulyakov ⋅ Fabio Pizzati ⋅ Aliaksandr Siarohin  
   [arXiv:2604.02330](https://arxiv.org/abs/2604.02330) · [project](https://action-party.github.io/)
2. **Adapting MLLMs for Nuanced Video Retrieval**  
   Piyush Nitin Bagad ⋅ Andrew ZISSERMAN  
   [arXiv:2512.13511](https://arxiv.org/abs/2512.13511) · [project](http://bpiyush.github.io/tara-website)
3. **Amplify, Aggregate, and Adjust: VideoMAE-based Holistic-Subtle Aggregation for Micro-Action Recognition**  
   Yan Zhang ⋅ Nan Pu ⋅ Wenjing Li ⋅ Zhun Zhong ⋅ Meng Wang
4. **Anchor Forcing: Anchor Memory and Tri-Region RoPE for Interactive Streaming Video Diffusion**  
   yang yang ⋅ Tianyi Zhang ⋅ Wei Huang ⋅ Jinwei Chen ⋅ Boxi Wu ⋅ Xiaofei He ⋅ Deng Cai ⋅ Bo Li ⋅ Peng-Tao Jiang  
   [arXiv:2603.13405](https://arxiv.org/abs/2603.13405) · [code](https://github.com/vivoCameraResearch/Anchor-Forcing)
5. **Are Video Reasoning Models Ready to Go Outside?**  
   Yangfan He ⋅ Changgyu Boo ⋅ Jaehong Yoon  
   [arXiv:2603.10652](https://arxiv.org/abs/2603.10652) · [project](https://robust-video-reason.github.io/)
6. **AViTS：Adaptive Spatiotemporal Token Selection for Efficient Dynamic-Resolution Generation**  
   Haoran Qin ⋅ zhengan yan ⋅ Shikang Zheng ⋅ Xiaobing Tu ⋅ Jiacheng Liu ⋅ Yuqi Lin ⋅ Chang Zou ⋅ Jinshan Liu ⋅ Peiliang Cai ⋅ Xiantao Zhang ⋅ Jinkui Ren ⋅ Linfeng Zhang
7. **Bayesian Uncertainty Attribution-Guided Fine-Tuning for Open-Set Action Recognition**  
   Shehan Senavirathna ⋅ Hongji Guo ⋅ Qiang Ji
8. **Bridging VideoQA and Video-Guided Agentic Tasks via Generalized Keyframe Extraction**  
   Sunqi Fan ⋅ Qingle Liu ⋅ Runqi Yin ⋅ Meng-Hao Guo ⋅ Shuojin Yang  
   [arXiv:2606.29445](https://arxiv.org/abs/2606.29445) · [code](https://github.com/VG-GUI-TASKER/VG-GUI-TASKER) · [project](https://vg-gui-tasker.github.io/)
9. **Cambrian-P: Pose-Grounded Video Understanding**  
   Jihan YANG ⋅ Zifan Zhao ⋅ Xichen Pan ⋅ Shusheng Yang ⋅ Junyi Zhang ⋅ Hu Xu ⋅ Shang-Wen Li ⋅ Saining Xie  
   [arXiv:2605.22819](https://arxiv.org/abs/2605.22819) · [project](https://cambrian-mllm.github.io/)
10. **Clue Matters: Empower Video Reasoning with Brain-Inspired Latent Clue Learning**  
   Kaixin Zhang ⋅ Xiaohe Li ⋅ Jiahao Li ⋅ Haohua Wu ⋅ Xinyu Zhao ⋅ Zide Fan ⋅ Lei Wang
11. **Continuous Heart Rate Variability Estimation from Egocentric Systems for Skill Assessment**  
   Berken Utku Demirel ⋅ Christian Holz
12. **Controllable Egocentric Video Generation via Occlusion-Aware Sparse 3D Hand Joints**  
   Chenyangguang Zhang ⋅ Botao Ye ⋅ Boqi Chen ⋅ Alexandros Delitzas ⋅ Fangjinhua Wang ⋅ Marc Pollefeys ⋅ Xi Wang  
   [arXiv:2603.11755](https://arxiv.org/abs/2603.11755)
13. **CoSyncDiT: Cognitive Synchronous Diffusion Transformer for Movie Dubbing**  
   Gaoxiang Cong ⋅ Liang Li ⋅ Jiaxin Ye ⋅ Zhedong Zhang ⋅ Hongming Shan ⋅ Yuankai Qi ⋅ Qingming Huang  
   [arXiv:2604.12292](https://arxiv.org/abs/2604.12292)
14. **CTEPM: Continuous-Time Event Process Memory for Long-Video Language Models**  
   Yangyang Liu
15. **CurveStream: Boosting Streaming Video Understanding in MLLMs via Curvature-Aware Hierarchical Visual Memory Management**  
   Chao Wang ⋅ Xudong Tan ⋅ Jianjian Cao ⋅ Kangcong Li ⋅ Tao Chen  
   [arXiv:2603.19571](https://arxiv.org/abs/2603.19571) · [code](https://github.com/streamingvideos/CurveStream)
16. **DART: Difficulty-Adaptive Routing for Zero-Shot Video Temporal Grounding**  
   zhengbo zhang ⋅ Mark Huang ⋅ Zhigang Tu ⋅ Ming-Hsuan Yang
17. **DE2TR: Dual Evidence Detection Transformer for Video Temporal Grounding**  
   Yifan Zhang ⋅ Chengxu Liu ⋅ Yujie Dun ⋅ Xueming Qian
18. **Decoupling Moment from Event for Video Temporal Grounding**  
   Yuda Zou ⋅ Boxiang Zhou ⋅ Xin Zhou ⋅ YIBO CHEN ⋅ Dejia Song ⋅ Xu Tang ⋅ Yao Hu ⋅ Yongchao Xu
19. **Demystifing Video Reasoning**  
   Ruisi Wang ⋅ Zhongang Cai ⋅ Fanyi Pu ⋅ Junxiang Xu ⋅ Wanqi Yin ⋅ Maijunxian Wang ⋅ Ran Ji ⋅ Chenyang Gu ⋅ Bo Li ⋅ Ziqi Huang ⋅ Hokin Deng ⋅ Dahua Lin ⋅ Ziwei Liu ⋅ Lei Yang
20. **DeRA: Decoupled Representation Alignment for Video Tokenization**  
   Pengbo Guo ⋅ Junke Wang ⋅ Zhen Xing ⋅ Chengxu Liu ⋅ Daoguo Dong ⋅ Xueming Qian ⋅ Zuxuan Wu  
   [arXiv:2512.04483](https://arxiv.org/abs/2512.04483)
21. **Discrete Diffusion Bridges for Spatiotemporally Aligned Image Translation and Generation**  
   Xing Xie ⋅ Jiawei Liu ⋅ Shijun Zhou ⋅ Huijie Fan ⋅ Zhi Han ⋅ Yandong Tang ⋅ Liangqiong Qu
22. **Distribution-Alignment Bridge for Uncertainty-Aware Text-to-Video Retrieval**  
   Kyeongmo Chae ⋅ Jihoon Lee ⋅ Sangtae Ahn  
   [arXiv:2607.20984](https://arxiv.org/abs/2607.20984)
23. **DiT as Real-Time Rerenderer: Streaming Video Stylization with Autoregressive Diffusion Transformer**  
   Hengye Lyu ⋅ Zisu Li ⋅ Yue Hong ⋅ Yueting Weng ⋅ Jiaxin Shi ⋅ Hanwang Zhang ⋅ Chen Liang  
   [arXiv:2604.13509](https://arxiv.org/abs/2604.13509)
24. **Egocentric Procedure Parsing**  
   Anubhav Anubhav ⋅ Archit Kambhamettu ⋅ Vatsal Agarwal ⋅ Pulkit Kumar ⋅ Abhinav Shrivastava
25. **EgoCogNav: Cognition-aware Human Egocentric Navigation**  
   Zhiwen Qiu ⋅ Ziang Liu ⋅ Wenqian Niu ⋅ Tapomayukh Bhattacharjee ⋅ Saleh Kalantari  
   [arXiv:2511.17581](https://arxiv.org/abs/2511.17581)
26. **EgoEverything: A Benchmark for Human Behavior–Inspired Long-Context Egocentric Video Understanding in AR Environment**  
   Qiance Tang ⋅ Ziqi Wang ⋅ Jieyu Lin ⋅ Ziyun Li ⋅ Barbara Salvo ⋅ Sai Qian Zhang  
   [arXiv:2604.08342](https://arxiv.org/abs/2604.08342)
27. **EgoPHI: Estimating 3D Hand-Object Contact and Force from Egocentric Vision**  
   Andela Ilic ⋅ Rachel Schuchert ⋅ Yijing Jiang ⋅ Christian Holz
28. **EgoPolice: A Benchmark for Egocentric Video Understanding in High-Stakes Police Body-Worn Camera Footage**  
   Max Saez-Diez ⋅ Jihoon Chung ⋅ Adam D. Wolsky ⋅ Greg Lanzalotto ⋅ Dean Knox ⋅ Jonathan Mummolo ⋅ Brandon Stewart ⋅ Olga Russakovsky  
   [arXiv:2607.06468](https://arxiv.org/abs/2607.06468)
29. **EgoSAT: A Comprehensive Benchmark of Egocentric Streaming Interaction Understanding**  
   Yijia Lei ⋅ Jinzhao Li ⋅ Yichi Zhang ⋅ Jiacheng Hua ⋅ Yin Li ⋅ Miao Liu  
   [arXiv:2606.24422](https://arxiv.org/abs/2606.24422) · [project](https://leiyj23.github.io/EgoSAT/)
30. **EgoSim: Egocentric World Simulator for Embodiment Interaction Generation**  
   Jinkun Hao ⋅ Mingda Jia ⋅ Xudong Xu ⋅ Ruiyan Wang ⋅ Xihui Liu ⋅ Ran Yi ⋅ Lizhuang Ma ⋅ Jiangmiao Pang  
   [arXiv:2604.01001](https://arxiv.org/abs/2604.01001)
31. **EgoTraj: Real-World Egocentric Human Trajectory**  
   Ahmad Yehia ⋅ Abduallah Mohamed ⋅ Tianyi Wang ⋅ Kun Qian ⋅ Jiseop Byeon ⋅ Junfeng Jiao ⋅ Christian Claudel
32. **EgoVITA: Learning to Plan and Verify for Egocentric Video Reasoning**  
   Yogesh Kulkarni ⋅ Pooyan Fazli  
   [arXiv:2511.18242](https://arxiv.org/abs/2511.18242)
33. **Em-Garde: A Propose-Match Framework for Proactive Streaming Video Understanding**  
   Yikai Zheng ⋅ Xin Ding ⋅ Yifan Yang ⋅ Shiqi Jiang ⋅ Hao Wu ⋅ Qianxi Zhang ⋅ Weijun Wang ⋅ Ting Cao ⋅ Yunxin Liu  
   [arXiv:2603.19054](https://arxiv.org/abs/2603.19054)
34. **EventMemAgent: Hierarchical Event-Centric Memory for Online Video Understanding with Adaptive Tool Use**  
   Siwei Wen ⋅ Zhangcheng Wang ⋅ Xingjian Zhang ⋅ Lei Huang ⋅ wenjun wu
35. **EventSTU: Event-Guided Efficient Spatio-Temporal Understanding for Video-LLMs**  
   Wenhao Xu ⋅ Xin Dong ⋅ Yue Li ⋅ Haoyuan Shi ⋅ Yueyi Zhang ⋅ Zhiwei Xiong
36. **Evidence-Backed Video Question Answering**  
   Shijie Wang ⋅ Honglu Zhou ⋅ Ziyang Wang ⋅ Ran Xu ⋅ Caiming Xiong ⋅ Silvio Savarese ⋅ Chen Sun ⋅ Juan Carlos Niebles  
   [arXiv:2607.11862](https://arxiv.org/abs/2607.11862) · [code](https://github.com/SalesforceAIResearch/EVQA)
37. **EXPLORE-Bench: Egocentric Scene Prediction with Long-Horizon Reasoning**  
   Chengjun Yu ⋅ Xuhan Zhu ⋅ Chaoqun Du ⋅ Pengfei Yu ⋅ Wei Zhai ⋅ Yang Cao ⋅ Zheng-Jun Zha  
   [arXiv:2603.09731](https://arxiv.org/abs/2603.09731)
38. **FEEL (Force-Enhanced Egocentric Learning): A Dataset for Physical Action Understanding**  
   Eadom Dessalene ⋅ Botao He ⋅ Michael Maynord ⋅ Yonatan Tussa ⋅ Pavan Mantripragada ⋅ Yianni Karabatis ⋅ Nirupam Roy ⋅ Yiannis Aloimonos  
   [arXiv:2603.15847](https://arxiv.org/abs/2603.15847)
39. **Fine-Grained Text-to-Video Retrieval for Camera-Trap Data**  
   Valentin Gabeff ⋅ Baptiste Maquignaz ⋅ Jiaxian Shan ⋅ Sepideh Mamooler ⋅ Gencer Sumbul ⋅ Blair Costelloe ⋅ Devis TUIA ⋅ Alexander Mathis
40. **FlatLands: Generative Floormap Completion From a Single Egocentric View**  
   Subhransu S. Bhattacharjee ⋅ Dylan Campbell ⋅ Rahul Shome
41. **Frames2Residual: Spatiotemporal Decoupling for Self-Supervised Video Denoising**  
   Mingjie Ji ⋅ Zhan Shi ⋅ Kailai Zhou ⋅ Zixuan Fu ⋅ Xun Cao  
   [arXiv:2603.10417](https://arxiv.org/abs/2603.10417)
42. **From Evaluation to Enhancement: Benchmarking and Improving Think-with-Video Reasoning for Video Generative Models**  
   Meng Luo ⋅ Yicheng Liu ⋅ Jiahao Wang ⋅ Yuanxing Zhang ⋅ Xin Tao ⋅ Pengfei Wan ⋅ Kun Gai ⋅ Hao Fei
43. **From Script to Shot: A Benchmark for Grounding Screenplays in Movies**  
   jungu cho ⋅ Young-Jae Park ⋅ Seong Jong Ha ⋅ Siyeol Kim ⋅ Seungho Park ⋅ Jisu Shin ⋅ Junmyeong Lee ⋅ Chaemin Hwang ⋅ Hyunjun Jung ⋅ Sangeyl Lee ⋅ Hae-Gon Jeon
44. **Gen2Balance: Generative Balancing for Long-Tailed Video Action Recognition**  
   Prajwal Gatti ⋅ Simon Jenni ⋅ Fabian Caba ⋅ Dima Damen  
   [arXiv:2606.22416](https://arxiv.org/abs/2606.22416)
45. **GUIDE: Resolving Domain Bias in GUI Agents through Real-Time Web Video Retrieval and Plug-and-Play Annotation**  
   Rui Xie ⋅ Zhi Gao ⋅ Chenrui Shi ⋅ Zirui Shang ⋅ Lu Chen ⋅ Qing Li  
   [arXiv:2603.26266](https://arxiv.org/abs/2603.26266) · [project](https://sharryXR.github.io/GUIDE/)
46. **GuideMe: Benchmarking Multi-Domain Task Guidance and Intervention in Streaming Video**  
   FANG LIU ⋅ Jinpeng Chen ⋅ Ke Xu ⋅ Yuhao LIU ⋅ Huankang Guan ⋅ Xudong LU ⋅ Yang Bo ⋅ Gerhard P. Hancke ⋅ Rui Liu ⋅ Rynson Lau
47. **H2SVC: Head-aware Heterogeneous Streaming Video Cache for Online Video Understanding**  
   han li ⋅ Xinyi Zhang ⋅ Wenrui Dai ⋅ Yaoming Wang ⋅ Xinyu Peng ⋅ Fan He ⋅ Hang Xu ⋅ Ziyang Zheng ⋅ Chenglin Li ⋅ Junni Zou ⋅ Hongkai Xiong
48. **HAS: Highlight-guided Attention Steering for Multimodal LLM Video Summarization**  
   Rui Chu ⋅ Yingjie Lao  
   [arXiv:2607.17994](https://arxiv.org/abs/2607.17994)
49. **InstrAct: Towards Action-Centric Understanding in Instructional Videos**  
   Zhuoyi Yang ⋅ Jiapeng Yu ⋅ Reuben Tan ⋅ Boyang Li ⋅ Huijuan Xu  
   [arXiv:2604.08762](https://arxiv.org/abs/2604.08762)
50. **Keep It Simple: Multi-Key Episodic Memory Retrieval for Ultra-Long Video Understanding**  
   Yeeun Choi ⋅ Youngbeom Yoo ⋅ Joon-Young Lee ⋅ Hyolim Kang ⋅ Seon Joo Kim  
   [arXiv:2608.07663](https://arxiv.org/abs/2608.07663) · [project](https://choi-yeeun.github.io/MERIT/)
51. **Keeping the Evidence Chain: Semantic Evidence Allocation for Training-Free Token Pruning in Video Temporal Grounding**  
   Jiaqi Li ⋅ Shuntian Zheng ⋅ Yixian Shen ⋅ JIA-HONG HUANG ⋅ Xiaoman Lu ⋅ Minzhe Ni ⋅ Yu Guan  
   [arXiv:2603.05663](https://arxiv.org/abs/2603.05663) · [code](https://github.com/JiaqiLi404/SemVID) · [project](https://jiaqili404.github.io/SemVID)
52. **Layer-Aware Video Composition via Split-then-Merge**  
   Ozgur Kara ⋅ Yujia Chen ⋅ Ming-Hsuan Yang ⋅ James Rehg ⋅ Wen-Sheng Chu ⋅ Du Tran  
   [arXiv:2511.20809](https://arxiv.org/abs/2511.20809) · [project](https://split-then-merge.github.io)
53. **Learning Consistent Temporal Grounding between Related Tasks in Sports Coaching**  
   Arushi Rai ⋅ Adriana Kovashka  
   [arXiv:2603.18453](https://arxiv.org/abs/2603.18453)
54. **Learning Egocentric Cues from Exocentric Video using Privileged Egocentric Supervision**  
   Dominick Reilly ⋅ Manish Govind ⋅ Le Xue ⋅ Srijan Das
55. **LENS: Adaptive Spatio-Temporal Zooming for Keyframe Sampling in Long-Form Videos**  
   Ce Zhang ⋅ Jinxi He ⋅ Yaqi Xie ⋅ Katia Sycara
56. **Linear Scaling Video VLMs for Long Video Understanding**  
   Cristobal Eyzaguirre ⋅ Jiajun Wu ⋅ Juan Carlos Niebles  
   [arXiv:2605.31598](https://arxiv.org/abs/2605.31598)
57. **LiveEdit: Towards Real-Time Diffusion-Based Streaming Video Editing**  
   Xinyu Wang ⋅ Chongbo Zhao ⋅ Fangneng Zhan ⋅ Yue Ma  
   [arXiv:2606.26740](https://arxiv.org/abs/2606.26740) · [project](https://live-edit.github.io)
58. **LogFA: Efficient Feature-Space Data Augmentation for Egocentric Temporal Action Segmentation**  
   Zijia Lu ⋅ Ehsan Elhamifar
59. **MarineEVT: Advancing Event-Centric Marine Video Understanding via Visual Tool Reasoning**  
   Tuan-An To ⋅ Wong Kwan ⋅ Tuan-Anh Vu ⋅ Ziqiang Zheng ⋅ Sai Kit Yeung  
   [arXiv:2607.24064](https://arxiv.org/abs/2607.24064)
60. **Mitigating Modality and Language-Style Gaps for Zero-Shot Video Moment Retrieval**  
   Jihyun Lee ⋅ Cheol-Ho Cho ⋅ Woojin Jun ⋅ Woojin Jeong ⋅ Jae-Pil Heo  
   [arXiv:2607.19027](https://arxiv.org/abs/2607.19027)
61. **MV-Forcing: Long Multi-View Video Generation via 4D-Grounded Spatio-Temporal Self-Forcing**  
   Gal Fiebelman ⋅ Hadar Averbuch-Elor ⋅ Sagie Benaim  
   [arXiv:2607.05376](https://arxiv.org/abs/2607.05376) · [project](https://galfiebelman.github.io/mv-forcing/)
62. **Parallelized Autoregressive Decoding for Omni-Modal Dense Video Captioning**  
   Wenzheng Zeng ⋅ Siyi Jiao ⋅ Chen Gao ⋅ Hwee Tou Ng ⋅ Mike Zheng Shou  
   [arXiv:2607.02963](https://arxiv.org/abs/2607.02963) · [code](https://github.com/showlab/PadCaptioner)
63. **QCA: Query- and Content-Aware Keyframe Selection for Long Video Understanding**  
   Jun Peng ⋅ Baiyang Song ⋅ Jie Li ⋅ Hui Li ⋅ Yiyi Zhou ⋅ Rongrong Ji ⋅ Yonghong Tian  
   [arXiv:2607.00983](https://arxiv.org/abs/2607.00983) · [code](https://github.com/hktk07/QCA)
64. **QSVideo: Query-Conditioned Semantic Temporal Retrieval for Video Understanding**  
   Wei Ao ⋅ Lan Wang ⋅ Vishnu Boddeti  
   [arXiv:2607.04559](https://arxiv.org/abs/2607.04559) · [code](https://github.com/human-analysis/QSVideo)
65. **Reasoning with Memory: A Temporal Granularity-Adaptive Framework for Training-Free Long Video Understanding**  
   Linghao Meng ⋅ Qiankun Li ⋅ Junyuan Mao ⋅ Pujin Liao ⋅ Zhicheng He ⋅ Enbo Zhang ⋅ Kun Wang ⋅ Yang Liu ⋅ Huazhu Fu ⋅ Yueming Jin
66. **Reflect-R1: Evidence-Driven Reflection for Self-Correction in Long Video Understanding**  
   Shuimu Chen ⋅ Yuteng Chen ⋅ Yuanshen Guan ⋅ Zebang Cheng ⋅ Zeyu Zhang ⋅ shengqian qin ⋅ Bin Xia ⋅ Jiaran Li ⋅ Wenming Yang ⋅ Fei Ma  
   [arXiv:2606.27922](https://arxiv.org/abs/2606.27922)
67. **Reinforcing Video Reasoning with Focused Thinking**  
   Jisheng Dang ⋅ Jingze Wu ⋅ Teng Wang ⋅ Xuanhui Lin ⋅ Nannan Zhu ⋅ Hongbo Chen ⋅ WEISHI ZHENG ⋅ Meng Wang ⋅ Tat-Seng Chua  
   [arXiv:2505.24718](https://arxiv.org/abs/2505.24718) · [code](https://github.com/longmalongma/TW-GRPO)
68. **ReQuest: Rethinking-based Question-Aware Frame Selection for Long-Form Video QA**  
   Minkuk Kim ⋅ Suyong Yun ⋅ Young Kim ⋅ Jinyoung Moon ⋅ Jinwoo Choi ⋅ Seong Tae Kim
69. **ReynoldsFlow: Physics-Inspired Spatiotemporal Flow Representation for Video Understanding**  
   Yu-Hsi Chen ⋅ Ching-Kai Lin ⋅ PingKong Huang ⋅ Chin-Tien Wu
70. **S3-Prune: Stability-Aware Token Budgeting for Long-Form Video-Language Models**  
   gilha lee ⋅ Seungil Lee ⋅ Hyun Kim
71. **ScanFocus: A Coarse-to-Fine Framework for Spatio-Temporal Video Grounding**  
   Chen Kai ⋅ Ming Dai ⋅ Wenxuan Cheng ⋅ Wankou Yang  
   [arXiv:2607.13421](https://arxiv.org/abs/2607.13421) · [code](https://github.com/TenMinutes209/ScanFocus)
72. **SE-DETR: Explicit Semantic Exploration for Generalizability and Distinguishability in Video Temporal Grounding**  
   Chengyang Hu ⋅ Guanshuo Wang ⋅ Fufu Yu ⋅ Qiong Jia ⋅ Shouhong Ding ⋅ Lizhuang Ma
73. **Single-Query Person-Centric Bimanual Hand-Object Interaction Detection**  
   Jonghyun Kim ⋅ Junho Roh ⋅ Yubin Yoon ⋅ Jaechul Kim ⋅ Jungho Lee ⋅ Hyotae Lee ⋅ Jongkuk Park ⋅ Taehwan Hwang
74. **Small Vision-Language Models are Smart Compressors for Long Video Understanding**  
   Junjie Fei ⋅ Jun Chen ⋅ Zechun Liu ⋅ Yunyang Xiong ⋅ Chong Zhou ⋅ Wei Wen ⋅ Junlin Han ⋅ Mingchen Zhuge ⋅ Saksham Suri ⋅ Qi Qian ⋅ Shuming Liu ⋅ Lemeng Wu ⋅ Raghuraman Krishnamoorthi ⋅ Vikas Chandra ⋅ Mohamed Elhoseiny ⋅ Chenchen Zhu  
   [arXiv:2604.08120](https://arxiv.org/abs/2604.08120) · [project](https://FeiElysia.github.io/tempo-page/)
75. **SNOW: Spatio-Temporal Scene Understanding with World Knowledge for Open-World Embodied Reasoning**  
   Tin Stribor Sohn ⋅ Maximilian Dillitzer ⋅ Jason Corso ⋅ Johannes Bach ⋅ Eric Sax
76. **Spatial Amsan: A Benchmark for Perception-Grounded Spatial Reasoning and Action Evaluation in Egocentric Manipulation**  
   Changsoo Jung ⋅ Jack Fitzgerald ⋅ Ethan Seefried ⋅ Mariah Bradford ⋅ Nathaniel Blanchard
77. **Spatiotemporal Flux Probing for Single-Photon Videography**  
   Jerry Yan ⋅ Matteo Forlivesi ⋅ Bowen Tan ⋅ Andrew Xie ⋅ Siddharth Somasundaram ⋅ Sotiris Nousias
78. **STAC: Selective Spatiotemporal Aggregation and Compression for Video Reasoning Segmentation**  
   Hesham Syed ⋅ Yun Liu ⋅ Guolei Sun ⋅ Jing Yang ⋅ Henghui Ding ⋅ Xue Geng ⋅ Xudong Jiang  
   [arXiv:2607.02922](https://arxiv.org/abs/2607.02922) · [code](https://github.com/MCG-NKU/nku-video)
79. **STEP: Spatial Thinking and Egocentric Pointing for Embodied Instruction Following**  
   Hanxuan Li ⋅ Bin Fu ⋅ Zeyuan Lin ⋅ Ruiping Wang ⋅ Xilin CHEN
80. **STRIDE: When to Speak Meets Sequence Denoising for Streaming Video Understanding**  
   Junho Kim ⋅ Hosu Lee ⋅ James Rehg ⋅ Minsu Kim ⋅ Yong Man Ro  
   [arXiv:2603.27593](https://arxiv.org/abs/2603.27593) · [project](https://interlive-team.github.io/STRIDE)
81. **STVFocus: Query-guided Spatio-Temporal Visual Focusing for Video LLMs**  
   Taehun Kong ⋅ Minyoung Park ⋅ Sangjun Ahn
82. **SVI-Bench: A Dynamic Microworld for Strategic Video Intelligence**  
   Yulu Pan ⋅ Han Yi ⋅ Seongsu Ha ⋅ Mohaiminul Islam ⋅ Benjamin Zhang ⋅ Lorenzo Torresani ⋅ Gedas Bertasius  
   [arXiv:2605.31529](https://arxiv.org/abs/2605.31529)
83. **Swap the Right Identity: Spatio-Temporal Preference Optimization for Identity Swapping**  
   Hongdeng Shen ⋅ Xiongzheng Li ⋅ Jikang Cheng ⋅ Duo Li ⋅ Yunlong FENG ⋅ Jing Li
84. **Synthetic Visual Genome 2: Extracting Large-scale Spatio-Temporal Scene Graphs from Videos**  
   Ziqi Gao ⋅ Jieyu Zhang ⋅ Wisdom Ikezogwo ⋅ Jae Sung Park ⋅ Tario You ⋅ Daniel Ogbu ⋅ Chenhao Zheng ⋅ Weikai Huang ⋅ Yinuo Yang ⋅ Winson Han ⋅ Quan Kong ⋅ Rajat Saini ⋅ Ranjay Krishna  
   [arXiv:2602.23543](https://arxiv.org/abs/2602.23543)
85. **TAR: Temporal Anchor-Constrained Reasoning for Video Temporal Grounding**  
   Chaohong Guo ⋅ Xun Mo ⋅ Yongwei Nie ⋅ Fei Ma ⋅ Xuemiao Xu ⋅ Chengjiang Long  
   [arXiv:2508.07683](https://arxiv.org/abs/2508.07683)
86. **Tempo-SAM3D: Monocular Video to 4D via Temporal Memory-Guided Generation**  
   Baicheng Li ⋅ Dong Wu ⋅ Yingdian Cao ⋅ Haoxiang Yang ⋅ Yiwen Lu ⋅ Zike Yan ⋅ Hongbin Zha
87. **Thinking in Streaming Video**  
   Zikang Liu ⋅ Longteng Guo ⋅ Handong Li ⋅ Ru Zhen ⋅ Xingjian He ⋅ Ruyi Ji ⋅ Xiaoming Ren ⋅ Yanhao Zhang ⋅ Haonan Lu ⋅ Jing Liu  
   [arXiv:2603.12938](https://arxiv.org/abs/2603.12938) · [code](https://github.com/johncaged/ThinkStream)
88. **Towards Effective Long Video Understanding: Dynamic MAS Construction via Meta-Agent**  
   Jing Huang ⋅ Lidong Zhang ⋅ Yadong Li ⋅ Xingzhong Xu ⋅ Siye Chen ⋅ Jie Liu ⋅ Ming Kong ⋅ Qiang Zhu
89. **Towards Long-Form Spatio-Temporal Video Grounding**  
   Xin Gu ⋅ Bing Fan ⋅ Jiali Yao ⋅ Zhipeng Zhang ⋅ Yan Huang ⋅ Cheng Han ⋅ Heng Fan ⋅ Libo Zhang  
   [arXiv:2602.23294](https://arxiv.org/abs/2602.23294) · [code](https://github.com/HengLan/ART-STVG)
90. **Towards Temporal Compositional Reasoning in Long-Form Sports Videos**  
   Siyu Cao ⋅ Lu Zhang ⋅ Ruizhe Zeng ⋅ Zhi-yong Liu  
   [arXiv:2604.22226](https://arxiv.org/abs/2604.22226)
91. **TRINITY: A Multi-Perspective Benchmark for Personal-Style Video Highlight Detection**  
   Qianqian Chen ⋅ Hyun Bin Kim ⋅ Denzel Wijaya ⋅ Yang Yi ⋅ Bo LIU ⋅ Yangkai Ding
92. **Video Streaming Thinking: VideoLLMs Can Watch and Think Simultaneously**  
   Yiran Guan ⋅ Liang Yin ⋅ Dingkang Liang ⋅ Jianzhong Ju ⋅ Zhenbo Luo ⋅ Jian Luan ⋅ Yuliang Liu ⋅ Xiang Bai  
   [arXiv:2603.12262](https://arxiv.org/abs/2603.12262) · [code](https://github.com/1ranGuan/VST) · [project](https://1ranguan.github.io/VST/)
93. **Video-Oasis: Rethinking Evaluation of Video Understanding**  
   Geuntaek Lim ⋅ Minho Shim ⋅ Sungjune Park ⋅ Jaeyun Lee ⋅ Inwoong Lee ⋅ Taeoh Kim ⋅ Dongyoon Wee ⋅ Yukyung Choi  
   [arXiv:2603.29616](https://arxiv.org/abs/2603.29616) · [code](https://github.com/sejong-rcv/Video-Oasis) · [project](https://limgeuntaekk.github.io/Video-Oasis/)
94. **VideoSearch-R1: Iterative Video Retrieval and Reasoning via Soft Query Refinement**  
   Seohyun Lee ⋅ Seoung Choi ⋅ Dohwan Ko ⋅ Jongha Kim ⋅ Hyunwoo Kim  
   [arXiv:2607.00446](https://arxiv.org/abs/2607.00446)
95. **Vinci2: Providing Proactive Assistance in Continuous Egocentric Videos**  
   Sitong Gong ⋅ Tianyu Yan ⋅ Caixin Kang ⋅ Bo Zheng ⋅ Xiang Ruan ⋅ Huchuan Lu ⋅ Kaipeng Zhang ⋅ Yoichi Sato ⋅ Yifei Huang  
   [arXiv:2607.11523](https://arxiv.org/abs/2607.11523) · [project](https://sitonggong.github.io/EgoServe-page/)
96. **VisionCoach: Reinforcing Grounded Video Reasoning via Visual-Perception Prompting**  
   Daeun Lee ⋅ Shoubin Yu ⋅ Yue Zhang ⋅ Mohit Bansal  
   [arXiv:2603.14659](https://arxiv.org/abs/2603.14659) · [project](https://visioncoach.github.io/)
97. **ViTAL‑X: Video-Text Alignment with Cross‑Modal Temporal Edits**  
   Sethuraman T V ⋅ Savya Khosla ⋅ Onkar Susladkar ⋅ Aditi Tiwari ⋅ Seoung Wug Oh ⋅ Kushal Kafle ⋅ Joon-Young Lee ⋅ Derek Hoiem ⋅ Simon Jenni
98. **Wan-R1: Verifiable-Reinforcement Learning for Generalizable Video Reasoning**  
   Ming Liu ⋅ Yunbei Zhang ⋅ Shilong Liu ⋅ Liwen Wang ⋅ Wensheng Zhang
99. **Wavelet-based Intra-video Counterfactual Reasoning for Video Question Grounding**  
   Jiasheng Yuan ⋅ Wei Wei
100. **What You Ask is What You Ground: Bridging Question Intent to Temporal Evidence for Grounded VideoQA**  
   Jinhwan Seo ⋅ Kyu Han ⋅ Jumin Lee ⋅ Junhyug Noh ⋅ Sung-eui Yoon  
   [arXiv:2608.15708](https://arxiv.org/abs/2608.15708) · [code](https://github.com/jinhseo/GroundFormer) · [project](https://jinhseo.github.io/groundformer/groundformer.html)
101. **When Thinking Hurts: Mitigating Visual Forgetting in Video Reasoning via Frame Repetition**  
   Xiaokun Sun ⋅ Yubo Wang ⋅ Haoyu Cao ⋅ Linli Xu  
   [arXiv:2603.16256](https://arxiv.org/abs/2603.16256)
102. **Where and What: Long-Term Object Tracking in Egocentric Videos**  
   Jacob Chalk ⋅ Saptarshi Sinha ⋅ Dima Damen ⋅ Yannis Kalantidis ⋅ Larlus Diane
103. **Why Can't I Open My Drawer? Mitigating Object-Driven Shortcuts in Zero-Shot Compositional Action Recognition**  
   Geo Ahn ⋅ Inwoong Lee ⋅ Taeoh Kim ⋅ Minho Shim ⋅ Dongyoon Wee ⋅ Jinwoo Choi
104. **WorldWander: Bridging Egocentric and Exocentric Worlds in Video Generation**  
   Quanjian Song ⋅ Yiren Song ⋅ Kelly Peng ⋅ Yuan Gao ⋅ Mike Zheng Shou  
   [arXiv:2511.22098](https://arxiv.org/abs/2511.22098) · [code](https://github.com/showlab/WorldWander)

## Retrieval & Cross-Modal Alignment

*18 papers · 12 with links*

1. **Beyond Categorical Matching: Intra-Class Graded Relevance Estimation for Cross-Modal 3D Retrieval**  
   shunning liu ⋅ YingPeng Zhang ⋅ Jianing Lin ⋅ Yifan Wang ⋅ Yang Zhang ⋅ Chun Yuan
2. **CMDR: Contextual Multimodal Document Retrieval**  
   Ryota Tanaka ⋅ Taku Hasegawa ⋅ Kyosuke Nishida  
   [arXiv:2607.05927](https://arxiv.org/abs/2607.05927) · [project](https://cmdr-bench.github.io/)
3. **CoCo-IR: Conversational Composed Image Retrieval**  
   Shengcao Cao ⋅ Tanmaya Dabral ⋅ Zhongli Ding ⋅ Madhuri Shanbhogue ⋅ Kaifeng Chen ⋅ Zhe Li ⋅ Mojtaba Seyedhosseini ⋅ Liang-Yan Gui ⋅ Yu-Xiong Wang
4. **Controlling Embedding Spaces with Text-Conditioned Transformations**  
   Joseph Fioresi ⋅ Fabian Caba ⋅ Pankaj Nathani ⋅ Shah Mubarak ⋅ Kushal Kafle  
   [arXiv:2607.22919](https://arxiv.org/abs/2607.22919) · [project](https://joefioresi718.github.io/ControlEmbed_webpage/)
5. **ELVA: Exploring Ranking-Driven Universal Multimodal Retrieval**  
   Yuhan Liu ⋅ Pei Fu ⋅ Hang Li ⋅ Yukun Qi ⋅ Chao Jiang ⋅ Jingwen Fu ⋅ Zhen Liu ⋅ Bin Qin ⋅ Zhenbo Luo ⋅ Jian Luan ⋅ Jingmin Xin  
   [arXiv:2606.20280](https://arxiv.org/abs/2606.20280)
6. **Embed-RL: Reinforcement Learning for Reasoning-Driven Multimodal Embeddings**  
   Haonan Jiang ⋅ Yuji Wang ⋅ Yongjie Zhu ⋅ Xin Lu ⋅ Wenyu Qin ⋅ Meng Wang ⋅ Pengfei Wan ⋅ Yansong Tang  
   [arXiv:2602.13823](https://arxiv.org/abs/2602.13823)
7. **FlowCIR: Semantic Transport via Flow Matching for Zero-Shot Composed Image Retrieval**  
   Zhenqi He ⋅ Ziqi Jiang ⋅ Yuanpei Liu ⋅ Yanghao Wang ⋅ Teng Wang ⋅ Long Chen  
   [arXiv:2607.02284](https://arxiv.org/abs/2607.02284)
8. **Generating a Paracosm for Training-Free Zero-Shot Composed Image Retrieval**  
   Tong Wang ⋅ Yunhan Zhao ⋅ Shu Kong  
   [arXiv:2602.00813](https://arxiv.org/abs/2602.00813) · [project](https://leowangtong.github.io/Paracosm/)
9. **HitMem: Hierarchical Temporal 3D Memory with Multi-Modal Context-Aware Retrieval for Dynamic Environments**  
   Ruijie Tang ⋅ Chenye Zou ⋅ Guoquan Wu ⋅ Jun Wei ⋅ Wei Chen ⋅ Jiaxin Zhu
10. **Learning Sample-wise Rank-Aware Interpolation Weights for Composed Visual Data Retrieval**  
   Boseung Jeong ⋅ Taegyu Park ⋅ Donghyeon Kwon ⋅ Hyunsouk Cho ⋅ Suha Kwak
11. **Learning to Compose: Revisiting Proxy Task Design for Zero-Shot Composed Image Retrieval**  
   Jingjing Zhang ⋅ Lei Zhang ⋅ Zheren Fu ⋅ Zhendong Mao  
   [arXiv:2607.00374](https://arxiv.org/abs/2607.00374)
12. **LightSTAR: Efficient Visual Document Retrieval via Lightweight Selection with Vision-Adaptive Refinement**  
   Tongkun Guan ⋅ Haocheng Wang ⋅ Wei Shen ⋅ Xiaokang Yang  
   [arXiv:2606.23539](https://arxiv.org/abs/2606.23539) · [code](https://github.com/bokufa/LightSTAR)
13. **ME-IQA: Memory-Enhanced Image Quality Assessment via Re-Ranking**  
   Kanglong Fan ⋅ Tianhe Wu ⋅ Wen Wen ⋅ Jianzhao Liu ⋅ le yang ⋅ Yabin ZHANG ⋅ Yiting Liao ⋅ Junlin Li ⋅ Li Zhang  
   [arXiv:2603.20785](https://arxiv.org/abs/2603.20785)
14. **MG2-RAG: Multi-Granularity Graph for Multimodal Retrieval-Augmented Generation**  
   Sijun Dai ⋅ Qiang Huang ⋅ Xiaoxing You ⋅ Jun Yu
15. **MultiHaystack: Benchmarking Multimodal Retrieval and Reasoning over 40K Images, Videos, and Documents**  
   Dannong Xu ⋅ zhongyu yang ⋅ Jun Chen ⋅ Yingfang Yuan ⋅ Ming Hu ⋅ Lei Sun ⋅ Luc Van Gool ⋅ Danda Paudel ⋅ Chun-Mei Feng  
   [arXiv:2603.05697](https://arxiv.org/abs/2603.05697)
16. **Representation Alignment for Just Image Transformers is not Easier than You Think**  
   Jaeyo Shin ⋅ Jiwook Kim ⋅ Hyunjung Shim  
   [arXiv:2603.14366](https://arxiv.org/abs/2603.14366) · [code](https://github.com/kaist-cvml/PixelREPA)
17. **TSEmbed: Unlocking Task Scaling in Universal Multimodal Embeddings**  
   Yebo Wu ⋅ Feng Liu ⋅ Ziwei Xie ⋅ Changwang Zhang ⋅ Jun Wang ⋅ Li Li  
   [arXiv:2603.04772](https://arxiv.org/abs/2603.04772)
18. **Unbalanced Optimal Transport for Efficient Visual Document Retrieval**  
   Hoyeon Shin ⋅ Jeongyeon Kim ⋅ Yeong Jun Koh ⋅ Yeoneung Kim ⋅ Hanul Kim

## Document, OCR & Structured Text

*33 papers · 19 with links*

1. **A Scalable Vector Graphics Latent Space**  
   Leonardo Zini ⋅ Elia Frigieri ⋅ Lorenzo Baraldi
2. **Advancing WordArt-Oriented Scene Text Recognition: Datasets and Methods**  
   Xingsong Ye ⋅ Yongkun Du ⋅ Jiaxin Zhang ⋅ Haojie Zhang ⋅ Chong Sun ⋅ Chen Li ⋅ Jing LYU ⋅ Zhineng Chen  
   [arXiv:2606.24484](https://arxiv.org/abs/2606.24484) · [code](https://github.com/YesianRohn/WATER)
3. **BaFCo: A Document Understanding Benchmark for Complex Bangla Form Comprehension**  
   Abu Tyeb Azad ⋅ Ishita Apan ⋅ Fahim Ahmed ⋅ Sumaiya Katha ⋅ Ezharuddin Jubaer ⋅ Armun Alam ⋅ Pranjal Nandi ⋅ Amin Ali ⋅ Aman Chadha ⋅ Md Mofijul Islam ⋅ A K M Mahbubur Rahman  
   [arXiv:2607.05614](https://arxiv.org/abs/2607.05614) · [code](https://huggingface.co/datasets/Mausul/bafco)
4. **Beyond Script Family Boundaries: Towards Unified Open-Set Scene Text Recognition**  
   Chang Liu ⋅ Elisa Smith
5. **Bridging Online and Offline Handwriting via Differentiable Physical Rendering**  
   Seonmi Park ⋅ Seunghyun Shin ⋅ Vihaan Misra ⋅ Dongmin Shin ⋅ Ukcheol Shin ⋅ Jean Oh ⋅ Hae-Gon Jeon  
   [arXiv:2608.03198](https://arxiv.org/abs/2608.03198) · [project](https://seonmip.github.io/onoff)
6. **CubicSplat: Differentiable Vector Graphics via Error-Bounded Forward Relaxation**  
   Chenglong Liu ⋅ Xin Zhang ⋅ Yimeng Zhu ⋅ Liyang He ⋅ Yixiao Ma ⋅ Yu Su ⋅ Zhenya Huang ⋅ Qi Liu
7. **DocLayout-VL: A Foundational Model for Hierarchical, Open-set, and Promptable Document Layout Segmentation**  
   Venkata Venna ⋅ Srihari Bandarupalli ⋅ Anirudh Srinivasan ⋅ R Raghuveer ⋅ Sai Madhusudan Gunda ⋅ SANTOSH RAVI KIRAN SARVADEVABHATLA
8. **Embedding Rotation Invariance for Provable Multi-Oriented Scene Text Recognition**  
   zhibin ma ⋅ Pengwen Dai ⋅ Yi Liu ⋅ Xugong Qin ⋅ Chenyun Yu ⋅ Xiaochun Cao  
   [arXiv:2608.10684](https://arxiv.org/abs/2608.10684)
9. **ET-SAM: Efficient Point Prompt Prediction in SAM for Unified Scene Text Detection and Layout Analysis**  
   Xike Zhang ⋅ Maoyuan Ye ⋅ Juhua Liu ⋅ Bo Du  
   [arXiv:2603.25168](https://arxiv.org/abs/2603.25168)
10. **FontCopilot: Towards Generalist Multimodal Large Language Models for Holistic Chinese Font Engineering**  
   Yu Liu ⋅ Yang Liu ⋅ Ying Gao ⋅ Yang Ding ⋅ Cunrui Wang
11. **GryphOne: Symbol-Aware Masked Diffusion for Structural Refinement in Offline Handwritten Mathematical Expression Recognition**  
   Takaya Kawakatsu ⋅ Ryo Ishiyama  
   [arXiv:2602.03370](https://arxiv.org/abs/2602.03370)
12. **Hierarchical Style Aggregation for Versatile Chinese Handwriting Generation**  
   Jiangpeng Wang ⋅ Fei Gao ⋅ Nannan Wang
13. **i-Design: Step-by-Step Graphic Layout Design with Progressive Aesthetic Policy Optimization**  
   Sohan Patnaik ⋅ Rishabh Jain ⋅ Balaji Krishnamurthy ⋅ Mausoom Sarkar
14. **Invoice Haystack: Benchmarking Document Retrieval and Visual Question Answering Under Strong Visual Homogeneity**  
   Heethanjan Kanagalingam ⋅ Thenukan Pathmanathan ⋅ Mokeeshan Vathanakumar ⋅ Basim Azam ⋅ Sarah Erfani ⋅ NAVEED AKHTAR  
   [arXiv:2606.25343](https://arxiv.org/abs/2606.25343)
15. **iSyncTab: Learning Cross-Modal Feature Sequencing for Image-Tabular Data via Neural Synchrony**  
   Al Zadid Sultan Bin Habib ⋅ Md Younus Ahamed ⋅ Prashnna Gyawali ⋅ Gianfranco Doretto ⋅ Donald Adjeroh
16. **LoGAN: Multilingual Font Localization with Generative Agents**  
   Zhuoning Yuan ⋅ Ta-Ying Cheng ⋅ Benjamin Klein
17. **MEVL-STP: Multi-Encoder and Vision Language Model for Arbitrarily Shaped Scene Text Spotting**  
   Aman Anand ⋅ Partha Pratim Roy ⋅ Palaiahnakote Shivakumara ⋅ Umapada Pal
18. **MinerU-Diffusion: Rethinking Document OCR as Inverse Rendering via Diffusion Decoding**  
   Hejun Dong ⋅ Junbo Niu ⋅ Bin Wang ⋅ Weijun Zeng ⋅ Wentao Zhang ⋅ Conghui He  
   [arXiv:2603.22458](https://arxiv.org/abs/2603.22458)
19. **Mitigating Sycophancy in Multimodal Chart Understanding via Vision-Grounded Verification**  
   Xiaolong Wang ⋅ Zhiwei Lin ⋅ Tai Liu ⋅ Qiang Li ⋅ Jian Sun
20. **Narrative-Driven Paper-to-Slide Generation via ArcDeck**  
   Tarik Can Ozden ⋅ SACHIDANAND VISHNUKUMAR SARMINI ⋅ Furkan Horoz ⋅ Ozgur Kara ⋅ Junho Kim ⋅ James Rehg  
   [arXiv:2604.11969](https://arxiv.org/abs/2604.11969) · [project](https://arcdeck.org/)
21. **P-MTP: Efficient Document Parsing via Multi-Token Prediction with Progressive Depth Scaling**  
   Le Xiang ⋅ Chenxi Zhai ⋅ Shu Wei ⋅ Jingjing Wu ⋅ Qunyi Xie ⋅ Xiao Tan ⋅ KunbinChen KunbinChen ⋅ Wei He  
   [arXiv:2606.24447](https://arxiv.org/abs/2606.24447)
22. **PDF-Omni: Poincaré Dual Disk Distortion Field-based Recurrent Update for Omnidirectional Stereo Matching**  
   Yunseok Yang ⋅ Eunjin Son ⋅ Sang Lee
23. **PolyLayout: Multi-room Manhattan Layout Estimation**  
   Gustav Hanning ⋅ Shaohui Liu ⋅ Rémi Pautrat ⋅ Marc Pollefeys ⋅ Kalle Åström ⋅ Viktor Larsson  
   [arXiv:2608.03323](https://arxiv.org/abs/2608.03323) · [project](https://ghanning.github.io/PolyLayout)
24. **PosterCopilot: Toward Layout Reasoning and Controllable Editing for Professional Graphic Design**  
   Jiazhe Wei ⋅ Ken Li ⋅ Tianyu Lao ⋅ Haofan Wang ⋅ Yueming Lyu ⋅ Liang Wang ⋅ Caifeng Shan ⋅ Chenyang Si  
   [arXiv:2512.04082](https://arxiv.org/abs/2512.04082) · [project](https://postercopilot.github.io/)
25. **Read or Ignore? A Unified Benchmark for Typographic-Attack Robustness and Text Recognition in Vision-Language Models**  
   Futa Waseda ⋅ Shojiro Yamabe ⋅ Daiki Shiono ⋅ Kento Sasaki ⋅ Tsubasa Takahashi  
   [arXiv:2512.11899](https://arxiv.org/abs/2512.11899) · [project](https://turingmotors.github.io/rio-vqa/)
26. **Real5-OmniDocBench: A Full-Scale Physical Reconstruction Benchmark for Robust Document Parsing in the Wild**  
   Cheng Cui ⋅ Changda Zhou ⋅ Tingquan Gao ⋅ Xueqing Wang ⋅ ZIYUE GAO ⋅ Jing Tang ⋅ Yi Liu  
   [arXiv:2603.04205](https://arxiv.org/abs/2603.04205)
27. **Render-in-the-Loop: Vector Graphics Generation via Visual Self-Feedback**  
   Guotao Liang ⋅ Zhangcheng Wang ⋅ Juncheng Hu ⋅ Haitao Zhou ⋅ Ziteng Xue ⋅ Jing Zhang ⋅ Dong Xu ⋅ Qian Yu  
   [arXiv:2604.20730](https://arxiv.org/abs/2604.20730)
28. **RT-DocLayout: Real-Time End-to-End Document Layout Analysis with Reading Order in the Wild**  
   Cheng Cui ⋅ Tingquan Gao ⋅ Xueqing Wang ⋅ Changda Zhou ⋅ Hongen Liu ⋅ Ting Sun ⋅ Yubo Zhang ⋅ Zelun Zhang ⋅ Jiaxuan Liu ⋅ Manhui Lin ⋅ Yue Zhang ⋅ Suyin Liang ⋅ Yiqing Xiang ⋅ Yi Liu  
   [arXiv:2606.23344](https://arxiv.org/abs/2606.23344)
29. **StrucTab: A Structured Optimization Framework for Table Parsing**  
   Gengluo Li ⋅ Shangpin Peng ⋅ Chengquan Zhang ⋅ Binghong Wu ⋅ Hao Feng ⋅ Weinong Wang ⋅ Pengyuan Lyu ⋅ Huawen Shen ⋅ Xingyu Wan ⋅ Zhuotao Tian ⋅ Han Hu ⋅ Can Ma ⋅ Yu ZHOU  
   [arXiv:2606.29905](https://arxiv.org/abs/2606.29905) · [code](https://github.com/VirtualLUOUCAS/StrucTab)
30. **Table-MCR2TR: Merged-Cell-Aware Table Recognition via Reinforced Multimodal Language Models**  
   Bangbang Zhou ⋅ Zhaoqing Zhu ⋅ Feiyu Gao ⋅ Hangdi Xing ⋅ Yadong Qu ⋅ Qi Zheng ⋅ Ming Yan ⋅ Hongtao Xie
31. **This Looks Distinctly Like That: Grounding Interpretable Recognition in Stiefel Geometry against Neural Collapse**  
   Junhao Jia ⋅ Jiaqi Wang ⋅ Yunyou Liu ⋅ Haodong Jing ⋅ Yueyi Wu ⋅ Xian Wu ⋅ Yefeng Zheng  
   [arXiv:2603.08374](https://arxiv.org/abs/2603.08374)
32. **UniRec-0.1B: Unified Text and Formula Recognition with 0.1B Parameters**  
   Yongkun Du ⋅ Zhineng Chen ⋅ Yazhen Xie ⋅ Weikang Bai ⋅ Hao Feng ⋅ Wei Shi ⋅ Yuchen Su ⋅ Can Huang ⋅ Yu-Gang Jiang
33. **UniTranslator: A Unified Multi-modal framework for End-to-end In-Image Machine Translation**  
   Jiahao Lyu ⋅ Pei Fu ⋅ Zhenhang Li ⋅ Shaojie Zhang ⋅ Jiahui Yang ⋅ Yu ZHOU ⋅ Can Ma ⋅ Zhenbo Luo ⋅ Jian Luan  
   [arXiv:2606.24333](https://arxiv.org/abs/2606.24333) · [code](https://github.com/SeerRay-Lab/Unitranslator)

# 3D, Geometry & Imaging


## 3D Reconstruction, Gaussian Splatting & NVS

*313 papers · 178 with links*

1. **2K Retrofit: Entropy-Guided Efficient Sparse Refinement for High-Resolution 3D Geometry Prediction**  
   Tianbao Zhang ⋅ Zhenyu Liang ⋅ Zhenbo Song ⋅ Nana Wang ⋅ Xiaomei Zhang ⋅ Xudong Cai ⋅ Zheng Zhu ⋅ Kejian Wu ⋅ Gang Wang ⋅ Zhaoxin Fan  
   [arXiv:2603.19964](https://arxiv.org/abs/2603.19964)
2. **360Anything: Geometry-Free Lifting of Images and Videos to 360°**  
   Ziyi Wu ⋅ Daniel Watson ⋅ Andrea Tagliasacchi ⋅ David Fleet ⋅ Marcus Brubaker ⋅ Saurabh Saxena  
   [arXiv:2601.16192](https://arxiv.org/abs/2601.16192) · [project](https://360anything.github.io/)
3. **360° Image Perception with MLLMs: A Comprehensive Benchmark and a Training-Free Method**  
   Huyen Thi Thanh Tran ⋅ Van-Quang Nguyen ⋅ Farros Alferro ⋅ Kang-Jun Liu ⋅ Takayuki Okatani  
   [arXiv:2603.16179](https://arxiv.org/abs/2603.16179)
4. **3D Gaussian Splatting Compression with Object Scalability**  
   Ruixiang Xue ⋅ Tong Chen ⋅ Zhan Ma
5. **3D Gaussian Texture for Real-time Mesoscale Appearance Synthesis and Rendering**  
   Xiang Chen ⋅ Jia Li ⋅ Lu Wang ⋅ Beibei Wang
6. **3D-ReGen: A Unified 3D Geometry Regeneration Framework**  
   Geon Yeong Park ⋅ Roman Shapovalov ⋅ Rakesh Ranjan ⋅ Jong Chul Ye ⋅ Andrea Vedaldi ⋅ Thu Nguyen-Phuoc
7. **3DGS3: Joint Super Sampling and Frame Interpolation for Real-Time Large-Scale 3DGS Rendering**  
   Yibo Zhao ⋅ Fan Gao ⋅ Youcheng Cai ⋅ Ligang Liu
8. **4D-VGGT: A SpatioTemporal Foundation Model for Dynamic Scene Geometry Estimation**  
   Haonan Wang ⋅ Hanyu Zhou ⋅ Haoyue Liu ⋅ Luxin Yan
9. **4DGS360: 360° Gaussian Reconstruction of Dynamic Objects from a Single Video**  
   Jae Won Jang ⋅ Yeonjin Chang ⋅ Wonsik Shin ⋅ Juhwan Cho ⋅ Nojun Kwak  
   [arXiv:2603.21618](https://arxiv.org/abs/2603.21618) · [project](https://jaewon040.github.io/4dgs360/)
10. **Active View Selection with Perturbed Gaussian Ensemble for Tomographic Reconstruction**  
   Yulun Wu ⋅ Ruyi Zha ⋅ Wei Cao ⋅ Yingying Li ⋅ Yuanhao Cai ⋅ Yaoyao Liu  
   [arXiv:2603.06852](https://arxiv.org/abs/2603.06852) · [project](https://perturbed-gaussian-ensemble.cvmlgroup.web.illinois.edu/)
11. **ActiveStructure: Plane Scene Graph-Guided Active 3D Gaussian Splatting**  
   Yingzhao Li ⋅ Yan Li ⋅ Yanjie Liu ⋅ Hanyu Zhou ⋅ lijun zhao ⋅ Gim Hee Lee
12. **AdaptiveSplat: Texture Aware Controllable 3D Gaussian Allocation for Feed-Forward Reconstruction**  
   Badrinath Singhal ⋅ Srihari G ⋅ Sreehari Iyer ⋅ Ankit Dhiman ⋅ Venkatesh Babu Radhakrishnan
13. **AHOY! Animatable Humans under Occlusion from YouTube Videos with Gaussian Splatting and Video Diffusion Priors**  
   Aymen Mir ⋅ Riza Alp Guler ⋅ Xiangjun Tang ⋅ Peter Wonka ⋅ Gerard Pons-Moll  
   [arXiv:2603.17975](https://arxiv.org/abs/2603.17975) · [project](https://miraymen.github.io/ahoy/)
14. **AirSplat: Alignment and Rating for Robust Feed-Forward 3D Gaussian Splatting**  
   Minh-Quan Bui ⋅ Jaeho Moon ⋅ Munchurl Kim  
   [arXiv:2603.25129](https://arxiv.org/abs/2603.25129) · [project](https://kaist-viclab.github.io/airsplat-site)
15. **AnchorSplat: Fast and Structure Consistent Detail Synthesis for Gaussian Splatting**  
   Dexu Zhu ⋅ Jiangnan Shao ⋅ Xiaofeng Wang ⋅ Junxian Duan ⋅ Jie Cao ⋅ Zheng Zhu ⋅ Huaibo Huang  
   [arXiv:2607.01290](https://arxiv.org/abs/2607.01290) · [code](https://github.com/zhude233/AnchorSplat)
16. **AnyView: Synthesizing Any Novel View in Dynamic Scenes**  
   Basile Van Hoorick ⋅ Dian Chen ⋅ Shun Iwase ⋅ Pavel Tokmakov ⋅ Muhammad Zubair Irshad ⋅ Igor Vasiljevic ⋅ Swati Gupta ⋅ Fangzhou Cheng ⋅ Sergey Zakharov ⋅ Vitor Guizilini  
   [arXiv:2601.16982](https://arxiv.org/abs/2601.16982) · [project](https://tri-ml.github.io/AnyView/)
17. **Argus: Metric Panoramic 3D Reconstruction for Indoor Scenes**  
   Xi Li ⋅ Linyuan Li ⋅ Yan Wu ⋅ Tong Rao ⋅ Kai Zhang ⋅ Xinchen Hui ⋅ Cihui Pan  
   [arXiv:2606.30047](https://arxiv.org/abs/2606.30047) · [project](https://argus-paper.realsee.ai)
18. **Articulat3D: Reconstructing Articulated Digital Twins From Monocular Videos with Geometric and Motion Constraints**  
   Lijun Guo ⋅ Haoyu Zhao ⋅ Xingyue Zhao ⋅ Rong Fu ⋅ Linghao Zhuang ⋅ Siteng Huang ⋅ Zhongyu Li ⋅ Hua Zou  
   [arXiv:2603.11606](https://arxiv.org/abs/2603.11606) · [project](https://maxwell-zhao.github.io/Articulat3D/)
19. **Articulated Object Reconstruction from Rest-State Observation**  
   Daeun Lee ⋅ Jaeah Lee ⋅ Woosung Kim ⋅ Haebeom Jung ⋅ Jaesik Park  
   [arXiv:2607.27749](https://arxiv.org/abs/2607.27749)
20. **Auto3R: Automated 3D Reconstruction and Scanning via Data-driven Uncertainty Quantification**  
   Chentao Shen ⋅ Sizhe Zheng ⋅ Bingqian Wu ⋅ Yaohua Feng ⋅ Yuanchen Fei ⋅ Mingyu Mei ⋅ Hanwen Jiang ⋅ Xiangru Huang  
   [arXiv:2512.04528](https://arxiv.org/abs/2512.04528) · [project](https://tomatoma00.github.io/auto3r.github.io)
21. **AVSplat:Dense-View Feed-Forward 3D Gaussian Splatting with Assist-View Preconditioning**  
   MUYU XU ⋅ Fangneng Zhan ⋅ Yu Wei ⋅ Hanspeter Pfister ⋅ Shijian Lu
22. **Beyond Inpainting: Unleash 3D Understanding for Stable Camera-Controlled Video Re-rendering**  
   Dongyu Chen ⋅ Yixin Guo ⋅ Shuojin Yang ⋅ Tai-Jiang Mu ⋅ Shimin Hu
23. **BioMTBee: Biologically Constrained Multi-View Template-Based 3D Reconstruction of Bumblebee**  
   Yi Zhang ⋅ Minchen Ye ⋅ Nenggan Zheng
24. **Boba: Batched Simulation for Physics-Based Gaussian Digital Twins**  
   Yihan Pang ⋅ Hanxiao Jiang ⋅ Sushant Kondguli ⋅ Sarita Adve ⋅ Shenlong Wang
25. **Bootstrapping Articulated 3D Reconstruction from 2D Image Collections**  
   Jakub Zadrozny ⋅ Oisin Mac Aodha ⋅ Hakan Bilen  
   [arXiv:2607.03891](https://arxiv.org/abs/2607.03891) · [project](https://jakubzadrozny.github.io/bat3r/)
26. **Calibrated Harmonic Overlaid Implicit Neural Representations for Multi-Dimensional Data**  
   Honghang Chen ⋅ XIUJUN ZHANG ⋅ Xiaoli Sun ⋅ MINGQING XIAO  
   [arXiv:2606.26763](https://arxiv.org/abs/2606.26763) · [code](https://github.com/chorl0229/CHOIR)
27. **CAM3R: Camera-Agnostic Model for 3D Reconstruction**  
   Namitha Guruprasad ⋅ Abhay Kumar Yadav ⋅ Cheng Peng ⋅ Rama Chellappa  
   [arXiv:2603.22631](https://arxiv.org/abs/2603.22631)
28. **Capacity-Controlled Multi-View Stylization of 3D Gaussian Splatting**  
   Zhihao Wen ⋅ Yixin Yang ⋅ Bojian Wu ⋅ Yang Zhou ⋅ Dani Lischinski ⋅ Danny Cohen-Or ⋅ Hui Huang  
   [arXiv:2606.26754](https://arxiv.org/abs/2606.26754) · [project](https://vcc2310.github.io/SceneStyler/)
29. **CasaMaestro: Multi-View Panoramas for House-Scale 3D Reconstruction**  
   Yuzhou Ji ⋅ Xiaotian Yang ⋅ Zhipeng Zhang  
   [arXiv:2606.31086](https://arxiv.org/abs/2606.31086)
30. **City-Level 3D Surface Reconstruction with Viewpoint Orientation Partitioning and Scene Completion**  
   Liang Han ⋅ Wenyuan Zhang ⋅ Junsheng Zhou ⋅ Yushen Liu ⋅ Zhizhong Han  
   [arXiv:2607.03771](https://arxiv.org/abs/2607.03771) · [project](https://hanl2010.github.io/VOP-GS)
31. **Closing the Capacity–Convergence Gap: Globally Optimal Configuration of Implicit Neural Representations**  
   Sipeng Chen ⋅ Yan Zhang ⋅ Shibo Li
32. **CoIn: Comprehensive 2D-3D Inpainting with Gaussian Splatting Guidance**  
   Hana Kim ⋅ Minje Kim ⋅ Tae-Kyun Kim
33. **Complex-Valued 2D Gaussian Representation for Computer-Generated Holography**  
   Yicheng Zhan ⋅ Xiangjun Gao ⋅ Long Quan ⋅ Kaan Akşit  
   [arXiv:2511.15022](https://arxiv.org/abs/2511.15022)
34. **Confidence-Based Mesh Extraction from 3D Gaussians**  
   Lukas Radl ⋅ Felix Windisch ⋅ Andreas Kurz ⋅ Thomas Köhler ⋅ Michael Steiner ⋅ Markus Steinberger  
   [arXiv:2603.24725](https://arxiv.org/abs/2603.24725) · [project](https://r4dl.github.io/CoMe/)
35. **Consistent Feature Transport for Image Relighting**  
   Bohan Zhang ⋅ huanweiliang huanweiliang ⋅ Yuhan He ⋅ Hongteng Xu ⋅ Xiaochao Qu ⋅ Luoqi Liu ⋅ Dixin Luo ⋅ Ting Liu  
   [arXiv:2607.17833](https://arxiv.org/abs/2607.17833) · [code](https://github.com/Dixin-Lab/CFT)
36. **ControlHair: Synergizing Physics Simulator and Video Diffusion for Controllable Dynamic Hair Rendering**  
   Weikai Lin ⋅ Haoxiang Li ⋅ Yuhao Zhu  
   [arXiv:2509.21541](https://arxiv.org/abs/2509.21541) · [project](https://linwk20.github.io/controlhair-web)
37. **Cube-Splat: High-Fidelity 360° Gaussian Splatting SLAM via Cubemap Factorization and Adjoint-Consistent Optimization**  
   Xiangfei Guo ⋅ Hao Shi ⋅ Yufan Zhang ⋅ Zhonghua Yi ⋅ maoyongqi maoyongqi ⋅ Xiaoting Yin ⋅ Kaiwei Wang
38. **D-Rex : Diffusion Rendering for Relightable Expressive Avatars**  
   Timo Teufel ⋅ xilong zhou ⋅ Umar Iqbal ⋅ Jan Kautz ⋅ Marc Habermann ⋅ Vladislav Golyanik ⋅ Christian Theobalt  
   [arXiv:2604.27871](https://arxiv.org/abs/2604.27871) · [project](https://vcai.mpi-inf.mpg.de/projects/DRex/)
39. **DANTE-W: Diffuse Albedo Neural Texturing in the Wild**  
   Guangyu Wang ⋅ Tianheng Lu ⋅ Ruqi Huang ⋅ Lu Fang  
   [arXiv:2606.30677](https://arxiv.org/abs/2606.30677)
40. **DASAM3D: A Unified Foundation Model for Enhanced 3D Scene Reconstruction and Segmentation**  
   RONNY XAVIER VELASTEGUI SANDOVAL ⋅ Max Pfingsthorn ⋅ Sezer Karaoglu ⋅ Theo Gevers
41. **Decoupled Illumination Priors for Spatially Controllable Multi-View Indoor Scene Relighting**  
   Chenjian Gao ⋅ Linning Xu ⋅ Tianfan Xue  
   [arXiv:2607.08879](https://arxiv.org/abs/2607.08879) · [project](https://cjeen.github.io/lumepalette)
42. **DefenseSplat: Enhancing the Robustness of 3D Gaussian Splatting via Frequency-Aware Filtering**  
   Yiran Qiao ⋅ Yiren Lu ⋅ Yunlai Zhou ⋅ Rui Yang ⋅ Linlin Hou ⋅ Yu Yin ⋅ Jing Ma  
   [arXiv:2602.19323](https://arxiv.org/abs/2602.19323)
43. **Deformable Triangle Splatting: Flexible Primitives for Real-Time Radiance Field Rendering**  
   Oriol Jiménez-Ayguadé ⋅ Antonio Agudo  
   [arXiv:2607.22446](https://arxiv.org/abs/2607.22446) · [project](https://orioljim1.github.io/detris)
44. **Denoising the Deep Sky: Physics-Based CCD Noise Formation for Astronomical Imaging**  
   Shuhong Liu ⋅ Xining Ge ⋅ Ziying Gu ⋅ Quanfeng Xu ⋅ Ziteng Cui ⋅ Lin Gu ⋅ Xuangeng Chu ⋅ Jun Liu ⋅ Dong Li ⋅ Tatsuya Harada  
   [arXiv:2601.23276](https://arxiv.org/abs/2601.23276)
45. **Dense Dynamic Scene Reconstruction and Camera Pose Estimation from Multi-View Videos**  
   Shuo Sun ⋅ Unal Artan ⋅ Malcolm Mielle ⋅ Achim Lilienthal ⋅ Martin Magnusson  
   [arXiv:2603.12064](https://arxiv.org/abs/2603.12064)
46. **DF3DV-1K: A Large-Scale Dataset and Benchmark for Distractor-Free Novel View Synthesis**  
   Cheng-You Lu ⋅ Yi-Shan Hung ⋅ Wei Chi ⋅ Hao Ping Wang ⋅ Charlie Tsai ⋅ Yu-Cheng Chang ⋅ Yu-Lun Liu ⋅ Thomas Do ⋅ Chin-teng Lin  
   [arXiv:2604.13416](https://arxiv.org/abs/2604.13416) · [project](https://johnnylu305.github.io/df3dv1k_web/)
47. **Differentiable Polarized Path Tracing**  
   Pramod Rao ⋅ Jérémy Riviere ⋅ xilong zhou ⋅ Abhijeet Ghosh ⋅ Abhimitra Meka ⋅ Thabo Beeler ⋅ Marc Habermann ⋅ Christian Theobalt ⋅ Delio Vicini  
   [arXiv:2607.13265](https://arxiv.org/abs/2607.13265) · [project](https://vcai.mpi-inf.mpg.de/projects/DPPT/)
48. **Diffusion-Based Material Regularization for Physics-Based Inverse Rendering**  
   Jingwang Ling ⋅ Lifan Wu ⋅ Feng Xu ⋅ Shuang Zhao  
   [arXiv:2606.31065](https://arxiv.org/abs/2606.31065) · [project](https://gerwang.github.io/diffusion-regularized-inverse-rendering/)
49. **DINO-SLAM: DINO-Informed RGB-D SLAM for Neural Implicit and Explicit Representations**  
   ZIREN GONG ⋅ Xiaohan Li ⋅ Fabio Tosi ⋅ Youmin Zhang ⋅ Stefano Mattoccia ⋅ Jun Wu ⋅ Matteo Poggi  
   [arXiv:2507.19474](https://arxiv.org/abs/2507.19474)
50. **Director: Instance-aware Gaussian Splatting for Dynamic Scene Modeling and Understanding**  
   Yuheng Jiang ⋅ Yiwen Cai ⋅ Zihao Wang ⋅ Yize Wu ⋅ Sicheng Li ⋅ Zhuo Su ⋅ Lan Xu ⋅ Shaohui Jiao  
   [arXiv:2604.01678](https://arxiv.org/abs/2604.01678) · [project](https://caiyw2023.github.io/Director/)
51. **DLGStream: Dynamic Language-embedded Guassian Splatting for Open-vocabulary Enabled Free-viewpoint Video Streaming**  
   ZHIHUI KE ⋅ Yvyang Liu ⋅ Xiaobo Zhou ⋅ Tie Qiu  
   [arXiv:2606.28840](https://arxiv.org/abs/2606.28840) · [code](https://github.com/kkkzh/DLGStream)
52. **Do Flat Minima Improve Sparse Novel View Synthesis?**  
   Youngsik Yun ⋅ Dongjun Gu ⋅ Youngjung Uh  
   [arXiv:2511.17918](https://arxiv.org/abs/2511.17918) · [project](https://bbangsik13.github.io/FASR)
53. **Don’t Mask Out the Background! Natural-Light Photometric Stereo via Illumination Reconstruction**  
   Taiga Hashida ⋅ Hiroaki Santo ⋅ Fumio Okura
54. **DPGS: A Diffusion-Prior Guided Framework for Large-Scale 3D Gaussian Splatting Reconstruction**  
   Shidong Zhang ⋅ shuaixin li ⋅ Juntong Qi ⋅ Haoxin Zhang ⋅ Xiao zhang ⋅ Xiaozhou Zhu ⋅ Wen Yao
55. **DR-GS: Physically-Based Deformable and Relightable 2D Gaussians**  
   Jiaxin LI ⋅ Tong Wu ⋅ Yi Wei ⋅ Tailin Wu ⋅ Li Zhang  
   [arXiv:2606.29379](https://arxiv.org/abs/2606.29379)
56. **Drop-In Perceptual Optimization for 3D Gaussian Splatting**  
   Ezgi Ozyilkan ⋅ Zhiqi Chen ⋅ Oren Rippel ⋅ Jona Ballé ⋅ Kedar Tatwawadi  
   [arXiv:2603.23297](https://arxiv.org/abs/2603.23297) · [project](https://apple.github.io/ml-perceptual-3dgs)
57. **DualDiff3D: Dual Structure-Appearance Diffusion Priors for Reliability-Enhanced 3D Gaussian Splatting**  
   Qian Wang ⋅ Yu Wang ⋅ Weiqi Li ⋅ Xinhua Cheng ⋅ Xiandong MENG ⋅ Ronggang Wang ⋅ Jian Zhang
58. **Dynamic Inverse Rendering for Enhanced Material-Lighting Decomposition**  
   Raza Yunus ⋅ Benjamin Ummenhofer ⋅ Jan Eric Lenssen ⋅ Eddy Ilg  
   [arXiv:2607.09329](https://arxiv.org/abs/2607.09329) · [project](https://razayunus.github.io/DIR)
59. **Dynamic-Robust Photometric–Semantic Reconstruction for Open-Vocabulary 3D Scene Understanding**  
   Boyu xxx ⋅ Li Yang ⋅ Yan Xu ⋅ Wei Liu ⋅ Nian Liu ⋅ Sikui Zhang ⋅ Yan Wang ⋅ Chunfeng Yuan ⋅ Weiming Hu
60. **D²R²OSR: Degradation-Disentangled Representation for Real-World Omnidirectional Image Super-Resolution**  
   Hongyu An ⋅ Xinfeng Zhang ⋅ Xu Fan ⋅ Shijie Zhao ⋅ Li Zhang ⋅ Ruiqin Xiong
61. **E3VS-Bench: A Benchmark for Viewpoint-Dependent Active Perception in 3D Gaussian Splatting Scenes**  
   Koya Sakamoto ⋅ Taiki Miyanishi ⋅ Daichi Azuma ⋅ Shuhei Kurita ⋅ Shu Morikuni ⋅ Naoya Chiba ⋅ Motoaki Kawanabe ⋅ Yusuke Iwasawa ⋅ Yutaka Matsuo  
   [arXiv:2604.17969](https://arxiv.org/abs/2604.17969) · [project](https://k0uya.github.io/e3vs-proj/)
62. **EDM:Event-guided Diffusion Model for Video Shadow Detection in Complex Dynamic Scenes**  
   boyang gao ⋅ jiayi guo ⋅ Ziyu Wang ⋅ Yingbin Cui ⋅ Zhan Tu
63. **EGGS: Explicitly Granular 3D Gaussian Splatting via Luma-Aware and Volume-Preserving Attribute Factorization**  
   InGyu Jeong ⋅ Hyunmin Jung
64. **Enhancing Embodied Reasoning and Grounding by Novel View Synthesis**  
   Yu-Ji Kim ⋅ Dahye Lee ⋅ Kim Jun-Seong ⋅ Nam Hyeon-Woo ⋅ GeonU Kim ⋅ Yongjin Kwon ⋅ Yu-Chiang Frank Wang ⋅ Jaesung Choe ⋅ Tae-Hyun Oh
65. **Event-driven Motion Deblurring via Trajectory-based Kernel Reconstruction**  
   Zhiwei Zhong ⋅ Peilin CHEN ⋅ Wei Dong ⋅ Bo Li ⋅ Anmin Liu ⋅ Shiqi Wang
66. **FaCT-GS: Fast and Scalable CT Reconstruction with Gaussian Splatting**  
   Pawel Pieta ⋅ Rasmus Juul Pedersen ⋅ Sina Borgi ⋅ Jakob Jørgensen ⋅ Jens Wenzel Andreasen ⋅ Vedrana Dahl  
   [arXiv:2604.01844](https://arxiv.org/abs/2604.01844) · [code](https://github.com/PaPieta/fact-gs)
67. **Fast and Compact 3D Gaussian Splatting with Polarized Opacity Prior**  
   Zi-Ming Wang ⋅ Kevin Duan ⋅ Ko Wei Huang ⋅ Akihiro Sugimoto ⋅ Shang-Hong Lai
68. **FillGS: Filling Observation Gaps in 4D Gaussian Splatting via Viewpoint-Time Selection and Generative Refinement**  
   Takashi Otonari ⋅ Toshihiko Yamasaki  
   [arXiv:2607.29284](https://arxiv.org/abs/2607.29284)
69. **FILT3R: Latent State Adaptive Kalman Filter for Streaming 3D Reconstruction**  
   Seonghyun Jin ⋅ Jong Chul Ye  
   [arXiv:2603.18493](https://arxiv.org/abs/2603.18493) · [code](https://github.com/jinotter3/FILT3R)
70. **FixAnything: 3D-Consistent Rendering Refinement via Video Generative Priors**  
   Khiem Vuong ⋅ Deva Ramanan ⋅ Srinivasa G. Narasimhan
71. **Flash-Refine: Frustum-Guided Local Incremental Learning for Efficient 3D Gaussian Splatting Completion**  
   Nuocheng Ji ⋅ Hanyang Zhuang ⋅ Chunxiang Wang ⋅ Ming Yang
72. **FLEG: Feed-Forward Language Embedded Gaussian Splatting from Any Views via Compact Semantic Representation**  
   Qijian Tian ⋅ Xin Tan ⋅ Jiayu Ying ⋅ Xuhong Wang ⋅ Yuan Xie ⋅ Lizhuang Ma  
   [arXiv:2512.17541](https://arxiv.org/abs/2512.17541) · [project](https://fangzhou2000.github.io/projects/fleg)
73. **Flow4R: Unifying 4D Reconstruction and Tracking with Scene Flow**  
   Shenhan Qian ⋅ Ganlin Zhang ⋅ Elliott (Shangzhe) Wu ⋅ Daniel Cremers  
   [arXiv:2602.14021](https://arxiv.org/abs/2602.14021) · [project](https://shenhanqian.github.io/flow4r)
74. **Fourier Splatting: Generalized Fourier encoded primitives for scalable radiance fields**  
   Mihnea Jurca ⋅ Bert hauwermeiren ⋅ Adrian Munteanu  
   [arXiv:2603.19834](https://arxiv.org/abs/2603.19834)
75. **Free-Range Gaussians: Non-Grid-Aligned Generative 3D Gaussian Reconstruction**  
   Akhmedkhan Shabanov ⋅ Peter Hedman ⋅ Ethan Weber ⋅ Zhengqin Li ⋅ Denys Rozumnyi ⋅ Gael Le Lan ⋅ Naina Dhingra ⋅ Lei Luo ⋅ Andrea Vedaldi ⋅ Christian Richardt ⋅ Andrea Tagliasacchi ⋅ Bo Zhu ⋅ Numair Khan  
   [arXiv:2604.04874](https://arxiv.org/abs/2604.04874) · [project](https://free-range-gaussians.github.io)
76. **From Blobs to Spokes: High-Fidelity Surface Reconstruction via Oriented Gaussians**  
   Diego Gomez ⋅ Antoine Guedon ⋅ Nissim Maruani ⋅ Bingchen Gong ⋅ Maks Ovsjanikov  
   [arXiv:2604.07337](https://arxiv.org/abs/2604.07337) · [project](http://diego1401.github.io/BlobsToSpokesWebsite/index.html)
77. **From Local to Global: A Progressive Reconstruction Network for Diffractive Snapshot Spectral Imaging**  
   Zhengyue Zhuge ⋅ Shiqi Chen ⋅ Chi Zhang ⋅ Jiahui Xu ⋅ Tianchen Qiu ⋅ Dingchuan Yu ⋅ Yueting Chen
78. **From Reconstruction to Decision: A Post-Encoder Plug-in Adapter for Curvilinear Segmentation**  
   Qin Lei ⋅ Jiang Zhong ⋅ Xin Xiao ⋅ ymyang ymyang ⋅ Hao Wu  
   [arXiv:2606.23486](https://arxiv.org/abs/2606.23486)
79. **F⁴Splat: Feed-Forward Predictive Densification for Feed-Forward 3D Gaussian Splatting**  
   Injae Kim ⋅ Chaehyeon Kim ⋅ Minseong Bae ⋅ Minseok Joo ⋅ Hyunwoo Kim
80. **GaINeR: Geometry-Aware Implicit Neural Representation for Image Editing**  
   Weronika Jakubowska ⋅ Mikołaj Zieliński ⋅ Rafał Tobiasz ⋅ Krzysztof Byrski ⋅ Maciej Zieba ⋅ Dominik Belter ⋅ Przemysław Spurek
81. **GAINS: Gaussian-based Inverse Rendering from Sparse Multi-View Captures**  
   Patrick Noras ⋅ Jun Myeong Choi ⋅ Didier Stricker ⋅ Pieter Peers ⋅ Roni Sengupta
82. **GARDEN: Gravity-Aligned Reconstruction of Disentangled ENvironments from RGB images**  
   Jiahao Sun ⋅ Dingkun Wei ⋅ Zehong Shen ⋅ Hongyu Zhou ⋅ Yujun Shen ⋅ Liang Li
83. **Gaussian Volumetric Representation for Efficient Shear–Warp Visualization**  
   Mayuri Mathur ⋅ Ojaswa Sharma  
   [arXiv:2607.25377](https://arxiv.org/abs/2607.25377)
84. **GaussianLens: Localized High-Resolution Reconstruction via On-Demand Gaussian Densification**  
   Yijia Weng ⋅ Zhicheng Wang ⋅ Songyou Peng ⋅ Saining Xie ⋅ Howard Zhou ⋅ Leonidas Guibas  
   [arXiv:2509.25603](https://arxiv.org/abs/2509.25603)
85. **Gaussians on Fire: High-Frequency Reconstruction of Flames**  
   Jakob Nazarenus ⋅ Dominik Michels ⋅ Wojciech Palubicki ⋅ Simin Kou ⋅ Fang-Lue Zhang ⋅ Soren Pirk ⋅ Reinhard Koch  
   [arXiv:2511.22459](https://arxiv.org/abs/2511.22459)
86. **Generalizable Neural Reconstruction of High-Fidelity Surfaces via Sparse Volumetric Representations**  
   Aoxiang Fan ⋅ Corentin Dumery ⋅ Nicolas Talabot ⋅ Ming Xu ⋅ Hieu Le ⋅ Pascal Fua
87. **Geometric Context Transformer for Streaming 3D Reconstruction**  
   Lin-Zhuo Chen ⋅ Jian Gao ⋅ Shangzhan Zhang ⋅ Yihang Chen ⋅ Nan Xue ⋅ Jianyuan Wang ⋅ Christian Rupprecht ⋅ Xun Cao ⋅ Xing Zhu ⋅ Yujun Shen ⋅ Yao Yao ⋅ YINGHAO XU  
   [arXiv:2604.14141](https://arxiv.org/abs/2604.14141) · [code](https://github.com/robbyant/lingbot-map) · [project](https://technology.robbyant.com/lingbot-map)
88. **Geometric Foundation Model Distillation for Efficient Lunar 3D Reconstruction**  
   Clémentine Grethen  
   [arXiv:2607.01851](https://arxiv.org/abs/2607.01851) · [project](https://clementinegrethen.github.io/publications/ECCV.html)
89. **Geometric Probing for Isotropic Optimization Manifold in Sparse-View 3D Gaussian Splatting**  
   Yunlong Zhao ⋅ Xiaoheng Deng ⋅ Hongyan Xu ⋅ Yichao Cao ⋅ Keke Huang ⋅ Shuo Yang ⋅ Xiangjian He ⋅ Lei Fan ⋅ Zhuohua Qiu ⋅ Xiu Su
90. **Geometry-Aware Style Transfer in 3D Gaussian Splatting**  
   Min Hyeok Bang ⋅ Jun Hyeong Kim ⋅ Seung-Wook Kim ⋅ Se-Ho Lee  
   [arXiv:2606.24144](https://arxiv.org/abs/2606.24144) · [code](https://github.com/oweixx/gast)
91. **Geometry-Preserving in 3D Gaussian Splatting for LiDAR-Camera Extrinsic Calibration**  
   Kyoleen Kwak ⋅ Daeho Kim ⋅ Jeong Woon Lee ⋅ Hyoseok Hwang  
   [arXiv:2606.20103](https://arxiv.org/abs/2606.20103)
92. **Geometry-Propagated Gaussian Splatting for Aerial Sparse Novel View Synthesis**  
   Yijing Wang ⋅ Xu Tang ⋅ Jingjing Ma ⋅ Xiangrong Zhang
93. **GeoNVS: Geometry Grounded Video Diffusion for Novel View Synthesis**  
   Minjun Kang ⋅ Inkyu Shin ⋅ Taeyeop Lee ⋅ Myungchul Kim ⋅ In Kweon ⋅ KUK-JIN YOON  
   [arXiv:2603.14965](https://arxiv.org/abs/2603.14965) · [project](https://sites.google.com/view/minjun-kang/geonvs-eccv26)
94. **GLARE: Towards Generalizable Detection of Latent Diffusion Images with Global-Local Reconstruction Error**  
   Jiangtao Yan ⋅ Jiazhen Ji ⋅ Zhongyu Zhang ⋅ Yuge Huang ⋅ Wenbin Wang ⋅ Shouhong Ding
95. **GlassGS: Geometry and Concept-Aware 3D Gaussian Splatting for Reflective Enclosures**  
   Mingxuan Cui ⋅ Yunrui Zhu ⋅ Wuqi Wang ⋅ Di Lin ⋅ Jianhua Zhang ⋅ Jie Zhang ⋅ Ming-Ming Cheng ⋅ Shengyong Chen ⋅ Qing Guo
96. **Global Pose Control for Generative View Synthesis in Normalized Object Coordinate Space**  
   Zhibing Li ⋅ Amogh Gupta ⋅ Behnoosh Parsa ⋅ Dan Casas  
   [arXiv:2607.02712](https://arxiv.org/abs/2607.02712) · [project](https://lizb6626.github.io/GlobalNVS/)
97. **GlobalSplat: Efficient Feed-Forward 3D Gaussian Splatting via Global Scene Tokens**  
   Roni Itkin ⋅ Noam Issachar ⋅ Yehonatan Keypur ⋅ Xingyu Chen ⋅ Anpei Chen ⋅ Sagie Benaim  
   [arXiv:2604.15284](https://arxiv.org/abs/2604.15284) · [project](https://r-itk.github.io/globalsplat/)
98. **GMODiff: One-Step Gain Map Refinement with Diffusion Priors for Efficient HDR Reconstruction**  
   Tao Hu ⋅ Weiyu Zhou ⋅ Yanjie Tu ⋅ Wei Dong ⋅ Peng Wu ⋅ Qingsen Yan ⋅ Yanning Zhang  
   [arXiv:2512.16357](https://arxiv.org/abs/2512.16357) · [code](https://github.com/gbymat/GMODiff)
99. **GO-Renderer: Generative Object Rendering with 3D-aware Controllable Video Diffusion Models**  
   Zekai Gu ⋅ Shuoxuan Feng ⋅ Yansong Wang ⋅ Hanzhuo Huang ⋅ Zhongshuo Du ⋅ Chengfeng Zhao ⋅ Chengwei Ren ⋅ Peng Wang ⋅ Yuan Liu  
   [arXiv:2603.23246](https://arxiv.org/abs/2603.23246) · [project](https://igl-hkust.github.io/GO-Renderer)
100. **GRF-Recon: Global Ray-Field Optimization for Long-Sequence Feed-forward Reconstruction**  
   Enpeng Li ⋅ Yunzhou Zhang ⋅ Zhiyao Zhang ⋅ Dexuan Lyu ⋅ Chenyu Wang ⋅ Chiyuan Cui ⋅ Cheng Cheng
101. **Grounding World Simulation Models in a Real-World Metropolis**  
   Junyoung Seo ⋅ Hyunwook Choi ⋅ Minkyung Kwon ⋅ Jinhyeok Choi ⋅ Siyoon Jin ⋅ Gayoung Lee ⋅ Junho Kim ⋅ JoungBin Lee ⋅ Geonmo Gu ⋅ Dongyoon Han ⋅ Sangdoo Yun ⋅ Seungryong Kim ⋅ Jin-Hwa Kim  
   [arXiv:2603.15583](https://arxiv.org/abs/2603.15583) · [project](https://seoul-world-model.github.io/)
102. **Habitat-GS: A High-Fidelity Navigation Simulator with Dynamic Gaussian Splatting**  
   Ziyuan Xia ⋅ Jingyi Xu ⋅ Chong Cui ⋅ Yuanhong Yu ⋅ Jiazhao Zhang ⋅ Qingsong Yan ⋅ Ni Tao ⋅ Junbo Chen ⋅ Xiaowei Zhou ⋅ Hujun Bao ⋅ Ruizhen Hu ⋅ Sida Peng  
   [arXiv:2604.12626](https://arxiv.org/abs/2604.12626) · [project](https://zju3dv.github.io/habitat-gs/)
103. **HandSCS: Structural Coordinate Space for Animatable Hand Gaussian Splatting**  
   Yilan Dong ⋅ Wenqing WANG ⋅ Qing Wang ⋅ Jiahao Yang ⋅ Haohe Liu ⋅ Xiatian Zhu ⋅ Greg Slabaugh ⋅ Shanxin Yuan  
   [arXiv:2503.14736](https://arxiv.org/abs/2503.14736)
104. **Heat Kernel Textures -- the Geodesic Gaussians That Do Not Splat**  
   Simone Foti ⋅ Caner Korkmaz ⋅ Stefanos Zafeiriou ⋅ Tolga Birdal
105. **High-speed Imaging through Turbulence with Event-based Light Fields**  
   Yu-Hsiang Huang ⋅ Levi Burner ⋅ Sachin Shah ⋅ Ziyuan Qu ⋅ Adithya Pediredla ⋅ Christopher Metzler  
   [arXiv:2603.14023](https://arxiv.org/abs/2603.14023)
106. **Holo360D: A Large-Scale Real-World Dataset with Continuous Trajectories for Advancing Panoramic 3D Reconstruction and Beyond**  
   Jing OU ⋅ Zidong Cao ⋅ Yinrui Ren ⋅ Zhuoxiao Li ⋅ Jinjing Zhu ⋅ Tongyan Hua ⋅ Shuai Zhang ⋅ Hui Xiong ⋅ Wufan Zhao  
   [arXiv:2604.22482](https://arxiv.org/abs/2604.22482) · [code](https://github.com/Jou719/Holo360D)
107. **HoloTetSphere: Unified TetSphere Mesh Reconstruction for Physical Simulations**  
   Yaqiao Dai ⋅ Renjiao Yi ⋅ Zhirui Gao ⋅ Wei Chen ⋅ Kai Xu ⋅ Chenyang Zhu  
   [arXiv:2607.08398](https://arxiv.org/abs/2607.08398)
108. **HorizonRelight: Relighting Long-horizon Videos Consistently via Diffusion Transformers**  
   Jing Yang ⋅ Mayoore Jaiswal ⋅ Zian Wang ⋅ Xiao Zeng ⋅ Yajie Zhao ⋅ Jianyuan Min ⋅ Rochelle Pereira  
   [arXiv:2606.29095](https://arxiv.org/abs/2606.29095) · [project](https://research.nvidia.com/labs/sil/projects/horizonrelight/)
109. **HSImul3R: Physics-in-the-Loop Reconstruction of Simulation-Ready Human–Scene Interactions**  
   Yukang Cao ⋅ Haozhe Xie ⋅ Fangzhou Hong ⋅ Long Zhuo ⋅ Zhaoxi Chen ⋅ Liang Pan ⋅ Ziwei Liu  
   [arXiv:2603.15612](https://arxiv.org/abs/2603.15612) · [project](https://yukangcao.github.io/HSImul3R/)
110. **Implicit Neural Representation Facilitates Unified Universal Vision Encoding**  
   Matthew Gwilliam ⋅ Xiao Wang ⋅ Xuefeng Hu ⋅ Zhenheng Yang  
   [arXiv:2601.14256](https://arxiv.org/abs/2601.14256) · [code](https://github.com/tiktok/huvr)
111. **Implicit Neural Representation for Spherical Harmonics Reconstruction of Motion-Corrupted Fetal Diffusion MRI**  
   Wenxuan Wu ⋅ Irina Grigorescu ⋅ Ruowen Qu ⋅ Jo Hajnal ⋅ J-Donald Tournier ⋅ Maria Deprez
112. **Improving Sparse-View 3DGS Generalization via Flat Minima Optimization**  
   Kangmin Seo ⋅ Sangeek Hyun ⋅ MinKyu Lee ⋅ Jae-Pil Heo  
   [arXiv:2607.00885](https://arxiv.org/abs/2607.00885) · [project](https://kangrnin.github.io/FlatMinGS)
113. **InceptionGS: Generative Bootstrapping for Large-Scale Gaussian Splatting under Unstructured View Sampling**  
   Tianheng Lu ⋅ Guangyu Wang ⋅ Ruqi Huang ⋅ Lu Fang
114. **Incremental Online Scene Reconstruction by 3D Gaussian Triangulation**  
   Yanjin Zhu ⋅ Shaofan Liu ⋅ Jianke Zhu  
   [arXiv:2607.10690](https://arxiv.org/abs/2607.10690)
115. **IndoorSplat: Enhanced Indoor Scene Reconstruction with Structured 2D Gaussian Splatting**  
   Min Shi ⋅ Tao Yang ⋅ Xigang Zhao ⋅ Qi Wang ⋅ Dengming Zhu ⋅ Zhaoxin Li
116. **InSpace: Structure-Aware 3D Indoor Scene Generation from a Single 360° Image**  
   Gwanhyeong Koo ⋅ Hyunsu Kim ⋅ Youngji Kim ⋅ Taejae Lee ⋅ Siwoo Lim ⋅ Sunjae Yoon ⋅ Suyong Yeon ⋅ Chang Yoo  
   [arXiv:2607.03990](https://arxiv.org/abs/2607.03990) · [project](https://kookie12.github.io/InSpace-Project-Page/)
117. **InstantHDR: Single-forward Gaussian Splatting for High Dynamic Range 3D Reconstruction**  
   Dingqiang Ye ⋅ Jiacong Xu ⋅ Jianglu Ping ⋅ Yuxiang Guo ⋅ Chao Fan ⋅ Vishal Patel  
   [arXiv:2603.11298](https://arxiv.org/abs/2603.11298)
118. **InstaPano: Zero-shot Instance Layout Controlled Panorama Generation Via Global Attention Fusion**  
   Zejian Li ⋅ Rui Huang ⋅ Lefan Hou ⋅ Pei Chen ⋅ Heyuan Xu ⋅ Shengyuan Zhang ⋅ Kewen Zhu ⋅ Huanghuang Deng ⋅ Li Liu ⋅ Lingyun Sun
119. **InstGS: Shared-Template Gaussian Instancing for Object-Redundancy-Free Rendering**  
   Zi'ang Lu ⋅ Qian Zhang ⋅ Kang Du ⋅ Dong Liang ⋅ John Li ⋅ Xinyao Wei ⋅ Zeyu Wang ⋅ Jinyuan Jia
120. **Integrated Forward–Inverse Network for Reconstruction for Lensless Image Reconstruction**  
   Donggeon Bae ⋅ Jaewoo Jung ⋅ Yong Guk Kang ⋅ Kyung Chul Lee ⋅ Taeyoung Kim ⋅ Jongho Kim ⋅ Sangjun Byun ⋅ Joonsik Park ⋅ Seung Ah Lee
121. **Interaction-Aware 4D Gaussian Splatting for Dynamic Hand-Object Interaction Reconstruction**  
   Hao Tian ⋅ Chenyangguang Zhang ⋅ Rui Liu ⋅ Wen Shen ⋅ Xiaolin Qin  
   [arXiv:2511.14540](https://arxiv.org/abs/2511.14540)
122. **Iterative Perceptual Alignment for VLMs via Deterministic Reconstruction Feedback**  
   Xiaorui Chen ⋅ Hanzhong Guo ⋅ Nizhe Cai ⋅ Jieliang Luo
123. **KineticGS: Momentum-driven Coherent 4D Gaussian Splatting for Monocular Dynamic Scene Reconstruction**  
   Yunqing Wang ⋅ Baoyao Yang ⋅ SI-QI LIU ⋅ CHONG YIN ⋅ Yihua Shao ⋅ Hao Tang
124. **KISS-GS: 3D Gaussian Splatting Compression Kept Simple**  
   Wieland Morgenstern ⋅ Friedrich Elias Branschke ⋅ Florian Fleischmann ⋅ Adrian Szatmari ⋅ Paul Schlack ⋅ Florian Barthel ⋅ Anna Hilsmann ⋅ Peter Eisert
125. **Large-Scale High-Quality 3D Gaussian Head Reconstruction from Multi-View Captures**  
   Evan Ntavelis ⋅ Sean Wu ⋅ Mohamad Shahbazi ⋅ Fabio Maninchedda ⋅ Dmitry Kostiaev ⋅ Artem Sevastopolsky ⋅ Mehak Gupta ⋅ Vittorio Megaro ⋅ Trevor Phillips ⋅ Thomas Etterlin ⋅ Jeronimo Bayer ⋅ Simon Schaefer ⋅ Matthias Vestner ⋅ Shridhar Ravikumar ⋅ Christian Zimmermann ⋅ Alejandro Blumentals ⋅ Reinhard Knothe ⋅ Mathias Deschler ⋅ Alexey Artemov ⋅ Stefan Brugger ⋅ Peter Kaufmann ⋅ Sebastian Martin ⋅ Brian Amberg ⋅ Tom Runia  
   [arXiv:2605.04035](https://arxiv.org/abs/2605.04035) · [project](https://apple.github.io/ml-headsup/)
126. **Large-Scale Light Field Synthesis from Videos Enables Geometrically Consistent Bokeh Editing**  
   Haoming Cai ⋅ Zhoutong Zhang ⋅ Christopher Metzler ⋅ Shumian Xin
127. **Latent Fusion: Decoding Consolidated 3D Geometry from Feed-forward Geometry Transformer Latents**  
   Laura Fink ⋅ Linus Franke ⋅ George Kopanas ⋅ Marc Stamminger ⋅ Peter Hedman
128. **Learning Global Camera Poses from Noisy View-Graphs for Structure from Motion**  
   Fadi Khatib ⋅ Meirav Galun ⋅ Ronen Basri
129. **Learning Implicit Constitutive Laws for Dynamic 3D Gaussian Splatting from Monocular Videos**  
   Xiaoyang Liu ⋅ Kai Han
130. **Learning Physics-based Forward Model Corrections in Unrolled Networks for Diffuser-based Imaging**  
   Yoko Sogabe ⋅ Shiori Sugimoto ⋅ Shoichiro Saito ⋅ Masaki Kitahara
131. **Learning Spectral and Polarimetric Clues for One-to-Multimodal Novel View Synthesis**  
   Federico Lincetto ⋅ Gianluca Agresti ⋅ Mattia Rossi ⋅ Piergiorgio Sartor ⋅ Pietro Zanuttigh  
   [arXiv:2607.02372](https://arxiv.org/abs/2607.02372) · [project](https://medialab.dei.unipd.it/paper_data/SPoILeR/)
132. **Learning Video Dynamics with Predictive Differentiable Rendering**  
   Yujin Tang ⋅ Tian Zhou ⋅ Xin Lin ⋅ Cheng Tan ⋅ Yifan Hu ⋅ Rong Jin ⋅ SouYoung Jin ⋅ Liang Sun  
   [arXiv:2606.31050](https://arxiv.org/abs/2606.31050)
133. **LEGO: Leveled Language Gaussian Splatting**  
   Yuning Peng ⋅ Haiping Wang ⋅ Yuan Liu ⋅ Yipeng Lu ⋅ Zhen Dong ⋅ Bisheng Yang  
   [arXiv:2608.10057](https://arxiv.org/abs/2608.10057) · [project](https://pz0826.github.io/LEGO-Webpage/)
134. **LensStyle: Learning the Optical Aesthetics for Controllable Stylized Lens Effect Rendering**  
   Yachuan Huang ⋅ Liwen Xiao ⋅ Liao Shen ⋅ Qiwen Wang ⋅ Huiqiang Sun ⋅ Zhiyu Pan ⋅ Zhiguo Cao
135. **LiDAR-EVS: Enhance Extrapolated View Synthesis for 3D Gaussian Splatting with Pseudo-LiDAR Supervision**  
   Yiming Huang ⋅ Xin Kang ⋅ Sipeng Zhang ⋅ Hongliang Ren ⋅ Weihua Zhang ⋅ Junjie Lai  
   [arXiv:2603.14763](https://arxiv.org/abs/2603.14763)
136. **LiFlow: Flow Matching for 3D LiDAR Scene Completion**  
   Andrea Matteazzi ⋅ Dietmar Tutsch  
   [arXiv:2602.02232](https://arxiv.org/abs/2602.02232) · [code](https://github.com/matteandre/LiFlow)
137. **LIIFusion: Coarse-to-fine Framework for Generative MEF via Implicit Neural Representation**  
   Sangmin Han ⋅ Jinho Kim ⋅ Jinwoo Kim ⋅ Dongyoung Kim ⋅ Seon Joo Kim
138. **Linear Fusion MultiDiffusion for Fast Training-Free Spherical Panorama Generation**  
   Akio Hayakawa ⋅ Yusuke Mukuta ⋅ Tatsuya Harada
139. **LiteGS: a high-performance framework to train 3dgs in subminutes via system and algorithm codesign**  
   Kaimin Liao ⋅ Hua Wang ⋅ Zhi Chen ⋅ Luchao Wang ⋅ Yaohua Tang  
   [arXiv:2503.01199](https://arxiv.org/abs/2503.01199)
140. **LoGeR: Long-Context Geometric Reconstruction with Hybrid Memory**  
   Junyi Zhang ⋅ Charles Herrmann ⋅ Junhwa Hur ⋅ Chen Sun ⋅ Ming-Hsuan Yang ⋅ Forrester Cole ⋅ Trevor Darrell ⋅ Deqing Sun  
   [arXiv:2603.03269](https://arxiv.org/abs/2603.03269) · [project](https://LoGeR-project.github.io/)
141. **LSRM: High-Fidelity Object-Centric Reconstruction via Scaled Context Windows**  
   Zhengqin Li ⋅ Cheng Zhang ⋅ Jakob Engel ⋅ Dong Zhao  
   [arXiv:2604.05182](https://arxiv.org/abs/2604.05182)
142. **LumiDepth: Stable Monocular Depth in Multi-Illumination Scenes**  
   Anqi Cheng ⋅ Zhiyuan Yang ⋅ Tianjiao Li ⋅ Haiyue Zhu ⋅ Kezhi Mao
143. **LumiTokens: 3D Relighting via Token-Space Lighting Transformation**  
   Yiwen Chen ⋅ Matheus Gadelha ⋅ Huaizu Jiang
144. **MAC-Splat: Multi-Attribute Consistency for High-Fidelity Sparse-View Reconstruction**  
   Jinqian Yang ⋅ Yichen Wu ⋅ Wanhua Li ⋅ Haokun Lin ⋅ Renzhen Wang ⋅ Xiangchu Feng ⋅ Xixi Jia  
   [arXiv:2607.10792](https://arxiv.org/abs/2607.10792)
145. **MAGiSt3R: Multi-Agent Feed-forward 3D Reconstruction from Monocular RGB Videos**  
   ZIREN GONG ⋅ Xiaohan Li ⋅ Fabio Tosi ⋅ Ninghui Xu ⋅ Stefano Mattoccia ⋅ Jianfei Cai ⋅ Matteo Poggi  
   [arXiv:2607.15211](https://arxiv.org/abs/2607.15211)
146. **MagnetGS-Mesh: High-Quality Multi-Object Mesh Reconstruction via Adaptive Surface Optimization**  
   Min-Su Park ⋅ Yeonho Han ⋅ Uijoon Jeong ⋅ Jun-Hyeong Park ⋅ Eun-Seok Ryu
147. **MambaRaw: Selective State Space Modeling for Efficient 4K RAW Image Reconstruction**  
   Peize Li ⋅ Fanhu Zeng ⋅ Tongda Xu ⋅ XINJIE ZHANG ⋅ Xingtong Ge ⋅ Haotian Zhang ⋅ Xingguo Xu ⋅ Yan Wang  
   [arXiv:2606.24479](https://arxiv.org/abs/2606.24479) · [code](https://github.com/Peizeli1/MambaRaw)
148. **Manifold-Aware Spectral Compaction: A Graph Signal Processing Perspective on Online Gaussian Reduction for 3DGS SLAM**  
   Jiayi Tian ⋅ Jiaze Wang ⋅ Tian Xia ⋅ Wenzhe zhao ⋅ Pengju Ren
149. **MaterialFlow: Attribute-Disentangled Material Transfer via Trajectory-Aware Velocity Modulation**  
   Sung-Lin Tsai ⋅ Bo-Kai Ruan ⋅ Yu-Hsuan Chen ⋅ Wen-Huang Cheng ⋅ Hong-Han Shuai
150. **Matryoshka Gaussian Splatting**  
   Zhilin Guo ⋅ Boqiao Zhang ⋅ Hakan Aktas ⋅ Kyle Fogarty ⋅ Jeffrey Hu ⋅ Nursena Aslan ⋅ Wenzhao Li ⋅ Canberk Baykal ⋅ Albert Miao ⋅ Josef Bengtson ⋅ Chenliang Zhou ⋅ Weihao Xia ⋅ Cristina Vasconcelos ⋅ Cengiz Oztireli  
   [arXiv:2603.19234](https://arxiv.org/abs/2603.19234) · [project](https://zhilinguo.github.io/MGS)
151. **MedGSSR: Generalizable Medical Image Super-Resolution 3D Reconstruction via Hierarchical Feed-forward Gaussian Splatting**  
   Chengkai Wang ⋅ Luoyu Hong ⋅ Yiting Zhao ⋅ Jiamin Wang ⋅ Xiang Feng ⋅ Feiwei Qin ⋅ Zhenzhong Kuang ⋅ Xuefei Yin ⋅ Ali Bashashati ⋅ Yanming Zhu
152. **MeGAS: Thermomechanical Dynamic Gaussian Splatting for Thermophysical Scene Editing**  
   Zesong Yang ⋅ Yuanhang Lei ⋅ Yihang Chen ⋅ Jiaer Huang ⋅ liyuan cui ⋅ Boming Zhao ⋅ Peter Yichen Chen ⋅ Hujun Bao ⋅ Zhaopeng Cui  
   [arXiv:2606.23455](https://arxiv.org/abs/2606.23455) · [project](http://zju3dv.github.io/MeGAS)
153. **MessyKitchens: Contact-rich object-level 3D scene reconstruction**  
   Junaid Ahmed Ansari ⋅ Ran Ding ⋅ Fabio Pizzati ⋅ Ivan Laptev  
   [arXiv:2603.16868](https://arxiv.org/abs/2603.16868) · [project](https://messykitchens.github.io/)
154. **MetaView: Monocular Novel View Synthesis with Scale-Aware Implicit Geometry Priors**  
   Yufei Cai ⋅ Xuesong Niu ⋅ Guosheng Lin ⋅ Hao LU ⋅ Kai Wu ⋅ Kun Gai  
   [arXiv:2607.12000](https://arxiv.org/abs/2607.12000) · [code](https://github.com/KlingAIResearch/MetaView)
155. **Minute4D: Training High-Fidelity 4D Gaussian Splatting in One Minute**  
   BINJIAN XIE ⋅ Chenhui Shi ⋅ Pengju Zhang ⋅ Yihong Wu
156. **MLP Splatting: Object-Centric Neural Fields**  
   Shinjeong Kim ⋅ Yuzhou Cheng ⋅ Xin Kong ⋅ Paul Kelly ⋅ Andrew Davison  
   [arXiv:2606.03877](https://arxiv.org/abs/2606.03877) · [project](https://shinjeongkim.com/mlp-splatting)
157. **mmIR: Frequency-Space Inverse Rendering for 3D Millimeter-Wave Radar ADC Synthesis**  
   Adnan Armouti ⋅ Yixuan Gao ⋅ Rajalakshmi Nandakumar
158. **MoBa-GS: Learning a Spatially-Varying Motion Basis over a Dynamic Canonical Space for 4D Reconstruction**  
   Guan Yuan Tan ⋅ Arghya Pal ⋅ Sailaja Rajanala ⋅ Raphaël Phan ⋅ Chee-Ming Ting
159. **MoCam: Unified Novel View Synthesis via Structured Denoising Dynamics**  
   Haofeng Liu ⋅ Yang Zhou ⋅ Ziheng Wang ⋅ Zhengbo Xu ⋅ Zhan Peng ⋅ Jie Ma ⋅ Jun Liang ⋅ Shengfeng He ⋅ Jing Li  
   [arXiv:2605.12119](https://arxiv.org/abs/2605.12119) · [project](https://orange-3dv-team.github.io/MoCam)
160. **Modeling and Compensating Phase Error in High-speed 3D Reconstruction**  
   Yuchong Chen ⋅ Jian Yu ⋅ Pengcheng Yao ⋅ Shaoyan Gai ⋅ Feipeng Da
161. **MonoArt: Progressive Structural Reasoning for Monocular Articulated 3D Reconstruction**  
   Haitian Li ⋅ Haozhe Xie ⋅ Junxiang Xu ⋅ Beichen Wen ⋅ Fangzhou Hong ⋅ Ziwei Liu  
   [arXiv:2603.19231](https://arxiv.org/abs/2603.19231) · [project](https://lihaitian.com/MonoArt)
162. **Monte Carlo Energy Aggregation for Mobile 3D Gaussian Splatting**  
   Xiaobiao Du ⋅ YuAn Wang ⋅ Hao Li ⋅ Bosheng Wang ⋅ Xun Sun ⋅ Xin Yu  
   [arXiv:2606.30017](https://arxiv.org/abs/2606.30017) · [project](https://xiaobiaodu.github.io/flux-gs-project/)
163. **MotionAnymesh: Physics-Grounded Articulation for Simulation-Ready Digital Twins**  
   WenBo Xu ⋅ Liu Liu ⋅ li zhang ⋅ Dan Guo ⋅ Ruonan Liu  
   [arXiv:2603.12936](https://arxiv.org/abs/2603.12936)
164. **MotionEditGS: Editing Motion and Appearance of 4D Scenes from Monocular Video via Semantically Anchored Gaussians**  
   Daehyun We ⋅ Youngho Yoon ⋅ Jiyong Boo ⋅ KUK-JIN YOON
165. **MotionSplicer: Part-Based Motion Editing for 4D Volumetric Videos**  
   Chaerin Min ⋅ Praccho Muna-McQuay ⋅ Tao Lu ⋅ James Tompkin ⋅ Srinath Sridhar
166. **MSVS-VAE: Multi-Scale Anchored VecSet for High-Fidelity 3D Reconstruction**  
   Dehao Hao ⋅ Kaiyi Zhang ⋅ Tanghui Jia ⋅ Xiangjun Gao ⋅ Dongyu Yan ⋅ Weikai Chen ⋅ Zeyu HU ⋅ Lingting Zhu ⋅ Yingda Yin ⋅ Runze Zhang ⋅ Li Yuan ⋅ Xin Wang ⋅ Long Quan  
   [arXiv:2607.24436](https://arxiv.org/abs/2607.24436)
167. **Multi4D: High-Fidelity Dynamic Gaussian Splatting via Multi-Level Competitive Allocation**  
   Rui Wang ⋅ Quentin Lohmeyer ⋅ Siyu Tang ⋅ Mirko Meboldt  
   [arXiv:2606.22197](https://arxiv.org/abs/2606.22197) · [project](https://batfacewayne.github.io/Multi4D.io/)
168. **MVFusion-GS: Motion-Variance Guided Temporal Attention for High-Quality Dynamic Gaussian Splatting**  
   Jianwei Hu ⋅ Tingxuan Huang ⋅ Hengyu Zhou ⋅ Ningna Wang ⋅ Xiaohu Guo ⋅ Jinshan Lai ⋅ Bin Wang  
   [arXiv:2607.01578](https://arxiv.org/abs/2607.01578)
169. **MVGS: Multi-view Regulated Gaussian Splatting for Novel View Synthesis**  
   Xiaobiao Du ⋅ Yida Wang ⋅ Xin Yu  
   [arXiv:2410.02103](https://arxiv.org/abs/2410.02103) · [project](https://xiaobiaodu.github.io/mvgs-project/)
170. **NanoGS: Training-Free and Lightweight Gaussian Splat Simplification**  
   Butian Xiong ⋅ Rong Liu ⋅ Tiantian Zhou ⋅ Meida Chen ⋅ Zhiwen Fan ⋅ Andrew Feng
171. **NEOMAP: Novel-View Synthesis via Noise Initialization by Manifold Alternating Projection**  
   Jinxi Li ⋅ Tianyi Zhang ⋅ Yafei YANG ⋅ Zihui Zhang ⋅ Peng Huang ⋅ Koon Lin ⋅ Bo Yang
172. **NeuIDO: Neural Intrinsic Dynamics Operator for Physics-Informed 4D World Models**  
   Jiajing Lin ⋅ Xin Zhang ⋅ Jianhua Sun
173. **Neural Harmonic Textures for High-Quality Primitive Based Neural Reconstruction**  
   Jorge Condor ⋅ Nicolas Moënne-Loccoz ⋅ Merlin Nimier-David ⋅ Piotr Didyk ⋅ Zan Gojcic ⋅ Qi Wu  
   [arXiv:2604.01204](https://arxiv.org/abs/2604.01204)
174. **NeuralGarSim: Geometry-agnostic Garment Simulation with Neural Fields**  
   Arihant Gaur ⋅ Navami Kairanda ⋅ Christian Theobalt ⋅ Vladislav Golyanik
175. **Nexels: Neurally-Textured Surfels for Real-Time Novel View Synthesis with Sparse Primitives**  
   Victor Rong ⋅ Jan Held ⋅ Victor Chu ⋅ Daniel Rebain ⋅ Marc Van Droogenbroeck ⋅ Kyros Kutulakos ⋅ Andrea Tagliasacchi ⋅ David Lindell  
   [arXiv:2512.13796](https://arxiv.org/abs/2512.13796) · [project](https://lessvrong.com/cs/nexels)
176. **Novel View Synthesis as Video Completion**  
   Qi Wu ⋅ Khiem Vuong ⋅ Minsik Jeon ⋅ Srinivasa G. Narasimhan ⋅ Deva Ramanan  
   [arXiv:2604.08500](https://arxiv.org/abs/2604.08500) · [project](https://frame-crafter.github.io/)
177. **NURBS Splatting: A Unified Differentiable Rendering Framework for Vector Graphics**  
   Jingye Qiu ⋅ Shizhe Zhou  
   [arXiv:2606.31764](https://arxiv.org/abs/2606.31764)
178. **OmniCoT: A Benchmark for Global and Multi-Step Panoramic Reasoning**  
   Haocong He ⋅ Chenfei Liao ⋅ Zichen Wen ⋅ Zihao Dongfang ⋅ Xu Zheng ⋅ Bin Ren ⋅ Chang Su ⋅ Zixin Zhang ⋅ Harold Haodong Chen ⋅ Hongfei Zhang ⋅ Weijia Li ⋅ Kailun Yang ⋅ Conghui He ⋅ Xuming Hu ⋅ Nicu Sebe ⋅ Linfeng Zhang  
   [arXiv:2606.30378](https://arxiv.org/abs/2606.30378)
179. **OmniLife360: A Benchmark for 3D Reconstruction from In-the-Wild 360° Captures**  
   Zonglin Zhao ⋅ Bowen Zhang ⋅ Yatai Li ⋅ Chao.Liang Chao.Liang ⋅ Zhipeng Zhang
180. **OmniRen: Neural Rendering wih Heterogeneous Scene Primitives**  
   Chong Zeng ⋅ Yue Dong ⋅ Pieter Peers ⋅ lvmin zhang ⋅ Maneesh Agrawala
181. **OmniStream: Mastering Perception, Reconstruction and Action in Continuous Streams**  
   Yibin Yan ⋅ Jilan Xu ⋅ Shangzhe Di ⋅ Haoning Wu ⋅ Weidi Xie  
   [arXiv:2603.12265](https://arxiv.org/abs/2603.12265) · [project](https://go2heart.github.io/omnistream/)
182. **OmniX: Any-view and Any-time 4D reconstruction via Feed-forward Trajectory Fields**  
   Yanqin Jiang ⋅ Tengfei Wang ⋅ Zhenwei Wang ⋅ Chenjie Cao ⋅ Junta Wu ⋅ Wenhan Luo ⋅ Weiming Hu ⋅ Jin Gao ⋅ Chunchao Guo  
   [arXiv:2607.10840](https://arxiv.org/abs/2607.10840) · [project](https://omnix4d.github.io/)
183. **OmniX: From Unified Panoramic Generation and Perception To Graphics-Ready 3D Scenes**  
   Yukun Huang ⋅ Jiwen Yu ⋅ Yanning Zhou ⋅ Jianan Wang ⋅ Xintao Wang ⋅ Pengfei Wan ⋅ Xihui Liu  
   [arXiv:2510.26800](https://arxiv.org/abs/2510.26800) · [project](https://yukun-huang.github.io/OmniX/)
184. **On Geometric Understanding and Learned Priors in Feed-forward 3D Reconstruction Models**  
   Jelena Bratulić ⋅ Sudhanshu Mittal ⋅ Thomas Brox ⋅ Christian Rupprecht  
   [arXiv:2512.11508](https://arxiv.org/abs/2512.11508)
185. **One4D: Unified 4D Generation and Reconstruction via Decoupled LoRA Control**  
   Zhenxing Mi ⋅ YUXIN WANG ⋅ Dan Xu  
   [arXiv:2511.18922](https://arxiv.org/abs/2511.18922) · [project](https://mizhenxing.github.io/One4D)
186. **OREO: Fidelity Alignment in 3D Generation via On-the-fly Rendering-Editing Optimization**  
   Zhiyuan MA ⋅ WENBO HU ⋅ Wang Zhao ⋅ Pengfei Wang ⋅ Ying Shan ⋅ Yabin Zhang
187. **Overlap-Consistent View Decomposition for Adapting Vision--Language Models to 360° Panoramas**  
   Seungwoo Woo ⋅ Daewon Jung ⋅ Sekyoung Youm
188. **PaD-GS: Leveraging Distortion Map for Panoramic Gaussian Splatting**  
   Yihang Xu ⋅ Qiulei Dong
189. **PanoLess: Environment Reconstruction from Partial Reflective Views**  
   Ahitagni Das ⋅ Ashok Veeraraghavan ⋅ Vivek Boominathan  
   [arXiv:2607.25362](https://arxiv.org/abs/2607.25362)
190. **Panoramic Affordance Prediction**  
   Zixin Zhang ⋅ Chenfei Liao ⋅ Hongfei Zhang ⋅ Harold Haodong Chen ⋅ Kanghao Chen ⋅ Zichen Wen ⋅ Litao Guo ⋅ Bin Ren ⋅ Xu Zheng ⋅ Yinchuan Li ⋅ Xuming Hu ⋅ Nicu Sebe ⋅ Yingcong Chen  
   [arXiv:2603.15558](https://arxiv.org/abs/2603.15558)
191. **PanoRec: Spatially-Structured Sequence Modeling for Multi-Granularity Panoramic Retrieval**  
   Zidong Cao ⋅ Ding Zhou ⋅ Wenyao Gao ⋅ Lutao Jiang ⋅ Hui Xiong
192. **PanoSAM2: Lightweight Distortion- and Memory-aware Adaptions of SAM2 for 360 Video Object Segmentation**  
   Dingwen Xiao ⋅ WEIMING ZHANG ⋅ Shiqi Wen ⋅ Addison Wang  
   [arXiv:2604.07901](https://arxiv.org/abs/2604.07901)
193. **Parametric SDF for Dynamic Surface Reconstruction**  
   Chong Gao ⋅ Kai Ye ⋅ Qiyu Dai ⋅ Yiming Shao ⋅ Qiong Zeng ⋅ Ding Liang ⋅ Yanpei Cao ⋅ Guanbin Li ⋅ Wenzheng Chen
194. **PASTEL: Panoramic Alignment for Monocular 4D Scene Reconstruction**  
   Yuankun Yang ⋅ Yi Wei ⋅ Bo Bai ⋅ Wenyang Zhou ⋅ Li Zhang
195. **PhysConvex: Physics-Informed Dynamic Convex Fields for Reconstruction and Simulation**  
   Dan Wang ⋅ Xinrui Cui ⋅ Serge Belongie ⋅ Ravi Ramamoorthi  
   [arXiv:2602.18886](https://arxiv.org/abs/2602.18886)
196. **Physically Grounded 3D Generative Reconstruction under Hand Occlusion using Proprioception and Multi-Contact Touch**  
   Gabriele Mario Caddeo ⋅ Pasquale Marra ⋅ Lorenzo Natale  
   [arXiv:2604.09100](https://arxiv.org/abs/2604.09100)
197. **Physically Grounded Dual-Opacity Gaussian Splatting for Joint RGB-TIR Reconstruction**  
   Jin Liu ⋅ Dabin leng ⋅ Jiagang Chen ⋅ Haodong Li ⋅ Jiguang Li ⋅ Zhao Huang ⋅ Xiaoshuai Zhang ⋅ Zhiwen Zheng ⋅ Xingru Huang ⋅ Qi Xu
198. **PIC: Revisiting INR for Image Coding with Fast Encoding and Sub-Millisecond Decoding**  
   Xiang Liu ⋅ Jinxiang Wang ⋅ Bin Chen ⋅ Zimo Liu ⋅ Mingyao Hong ⋅ Jiawei Li ⋅ Yaowei Wang ⋅ Shu-Tao Xia
199. **PixGS: Pixel-Space Diffusion for Direct 3D Gaussian Splat Generation**  
   Cao Duy ⋅ Phong Nguyen  
   [arXiv:2607.01803](https://arxiv.org/abs/2607.01803)
200. **Point Diffusion Mamba: Unified Diffusion-State-Space Modeling for Single-View 3D Reconstruction under Data Scarcity**  
   Wei Zhou ⋅ Xinzhe Shi ⋅ Xingxing Hao ⋅ Xing Hao ⋅ Kang Li ⋅ Jinye Peng ⋅ Ying He
201. **Point2Pose: Occlusion-Recovering 6D Pose Tracking and 3D Reconstruction for Multiple Unknown Objects Via 2D Point Trackers**  
   Tzu-Yuan Lin ⋅ Ho Lee ⋅ Kevin Doherty ⋅ Yonghyeon Lee ⋅ Sangbae Kim  
   [arXiv:2604.10415](https://arxiv.org/abs/2604.10415)
202. **PointSplat: Compact Gaussian Splatting via Human-Centric Prediction**  
   Yujie Guo ⋅ Yudong Jin ⋅ Lingteng Qiu ⋅ Zehong Shen ⋅ Zhen Xu ⋅ Zhang Jing ⋅ Xianchao Shen ⋅ Hujun Bao ⋅ Sida Peng ⋅ Xiaowei Zhou  
   [arXiv:2606.32036](https://arxiv.org/abs/2606.32036) · [project](https://zju3dv.github.io/pointsplat)
203. **Predictive Photometric Uncertainty in Gaussian Splatting for Novel View Synthesis**  
   Chamuditha Jayanga Ahangama Galappaththige ⋅ Thomas Gottwald ⋅ Peter Stehr ⋅ Edgar Heinert ⋅ Niko Suenderhauf ⋅ Dimity Miller ⋅ Matthias Rottmann  
   [arXiv:2603.22786](https://arxiv.org/abs/2603.22786) · [project](https://chumsy0725.github.io/3DGS-Uncertainty/)
204. **PrimitiveUDF: Primitive-Based Unsigned Distance Fields for Surface Reconstruction from Point Clouds**  
   Xin Deng ⋅ Bo Yang ⋅ Yifei Shi ⋅ Bing Wang
205. **PRISM3D: Probabilistic Refinement and Robust Initialization for Physically Consistent Scene Modeling under Extreme Motion Blur**  
   Gopi Raju Matta ⋅ Reddypalli Trisha ⋅ Divya Madhuri Vemunuri ⋅ Kaushik Mitra  
   [arXiv:2607.03855](https://arxiv.org/abs/2607.03855)
206. **PriSplat: Propagating Reliable Multi-view Information for Distractor-Free 3DGS**  
   Yunseo Yang ⋅ Youngho Yoon ⋅ KUK-JIN YOON
207. **R3RECON: Radiance-Field-Free Active Reconstruction via Renderability**  
   Xiaofeng Jin ⋅ Matteo Frosi ⋅ Yiran Guo ⋅ Matteo Matteucci
208. **RADmesh: Remesh-Aware Mesh Deformation**  
   Nam Anh Dinh ⋅ Itai Lang ⋅ Oded Stein ⋅ Rana Hanocka
209. **RaPTGS: Render-Agnostic Post-Training Compression of 3D Gaussian Splatting**  
   Asif Jawad ⋅ K. M. Azwad Hossain
210. **RayDer: Scalable Self-Supervised Novel View Synthesis from Real-World Video**  
   Ulrich Prestel ⋅ Stefan Andreas Baumann ⋅ Nick Stracke ⋅ Bjorn Ommer  
   [arXiv:2605.31535](https://arxiv.org/abs/2605.31535) · [project](https://compvis.github.io/rayder)
211. **Raymap-Guided Coupling for Drift-Robust Unposed Feed-Forward 3D Reconstruction**  
   Xiangyu Sun ⋅ Liu.Liu Liu.Liu ⋅ Seungkwon Yang ⋅ Jingbing Han ⋅ Seungtae Nam ⋅ Zhizhong Su ⋅ Eunbyung Park  
   [arXiv:2607.07168](https://arxiv.org/abs/2607.07168) · [project](https://xiangyu1sun.github.io/NoDrift3R-project-page/)
212. **RayMap3R: Inference-Time RayMap for Dynamic 3D Reconstruction**  
   Feiran Wang ⋅ Zezhou Shang ⋅ Gaowen Liu ⋅ Yan Yan  
   [arXiv:2603.20588](https://arxiv.org/abs/2603.20588) · [project](https://raymap3r.github.io/)
213. **Real-Time LiDAR Gaussian Splatting SLAM via Geometry-Aware Covariance Coupling**  
   SeungJun Tak ⋅ Yewon Jeon ⋅ Hwang Jaeik ⋅ Suk Min Hwang ⋅ SeongboHa SeongboHa ⋅ Hyeonwoo Yu
214. **ReconDreamer-RL: Enhancing Reinforcement Learning via Diffusion-based Reconstruction**  
   Chaojun Ni ⋅ Guosheng Zhao ⋅ Xiaofeng Wang ⋅ Zheng Zhu ⋅ Wenkang Qin ⋅ Chen Xinze ⋅ Guanghong Jia ⋅ Guan Huang ⋅ Wenjun Mei  
   [arXiv:2508.08170](https://arxiv.org/abs/2508.08170)
215. **ReconPhys: Reconstruct Appearance and Physical Attributes from Single Video**  
   Boyuan Wang ⋅ Xiaofeng Wang ⋅ Yongkang Li ⋅ Zheng Zhu ⋅ Yifan Chang ⋅ Angen Ye ⋅ Guosheng Zhao ⋅ Chaojun Ni ⋅ Guan Huang ⋅ Yijie Ren ⋅ Yueqi Duan ⋅ Xingang Wang  
   [arXiv:2604.07882](https://arxiv.org/abs/2604.07882)
216. **ReconSplat: Generalizable 3D Scene Reconstruction Beyond Observed Views**  
   Giuseppe Stracquadanio ⋅ Kevin Raj ⋅ Julia Grabinski ⋅ Stefan Roth
217. **Reconstructing 3D Human-Object Interaction via a Unified Triplane Space**  
   Yuhang Chen ⋅ Chenxing Wang
218. **Reconstructing Dense Depth of Dark Scenes with Sparse LiDAR, Noisy Events, and Blurry RGB**  
   Jianbo Cao ⋅ Yuqi Han ⋅ Siming Zheng ⋅ Bo Wang ⋅ Tong Guo ⋅ Jinli Suo
219. **Reconstructing Humans and Objects in Interaction using Large Reconstruction Models**  
   Agniv Chatterjee ⋅ Georgios Pavlakos
220. **Reconstruction by Generation: 3D Multi-Object Scene Reconstruction from Sparse Observations**  
   Andrii Zadaianchuk ⋅ Leonardo Barcellona ⋅ Lennard Schuenemann ⋅ Christian Gumbsch ⋅ Zehao Wang ⋅ Muhammad Zubair Irshad ⋅ Fabien Despinoy ⋅ Rahaf Aljundi ⋅ Efstratios Gavves ⋅ Sergey Zakharov
221. **Recurrent Sinusoidal INRs for Efficient High-Fidelity Representation**  
   Hyunmin Cho ⋅ Jaejun Yoo ⋅ Kyong Hwan Jin  
   [arXiv:2607.21485](https://arxiv.org/abs/2607.21485)
222. **Reflection-aware generative novel view synthesis**  
   GeonU Kim ⋅ Shin Dong-Yeon ⋅ Tae-Hyun Oh
223. **RefracGS: Novel View Synthesis Through Refractive Water Surfaces with 3D Gaussian Ray Tracing**  
   Yiming Shao ⋅ Qiyu Dai ⋅ Chong Gao ⋅ Guanbin Li ⋅ Yequan Wang ⋅ He Sun ⋅ Qiong Zeng ⋅ Baoquan Chen ⋅ Wenzheng Chen  
   [arXiv:2603.21695](https://arxiv.org/abs/2603.21695) · [project](https://yimgshao.github.io/refracgs/)
224. **ReInGS: Re-Initializing 3D Gaussians against Sparsity Discrepancy in Few-Shot Novel View Synthesis**  
   Junao Shen ⋅ Tian Feng ⋅ Haojie Dong ⋅ Jinkang Ji ⋅ Tianjia Shao
225. **Relaxed Rigidity with Ray-based Grouping for Dynamic Gaussian Splatting**  
   Junoh Lee ⋅ Junmyeong Lee ⋅ Yeon-Ji Song ⋅ Inhwan Bae ⋅ Jisu Shin ⋅ Hae-Gon Jeon ⋅ Jin-Hwa Kim  
   [arXiv:2603.24994](https://arxiv.org/abs/2603.24994)
226. **Render-FM: Feedforward Model for Real-time Photorealistic Volumetric Rendering**  
   Zhongpai Gao ⋅ Benjamin Planche ⋅ Meng Zheng ⋅ Anwesa Choudhuri ⋅ Van Nguyen ⋅ Terrence Chen ⋅ Ziyan Wu  
   [arXiv:2505.17338](https://arxiv.org/abs/2505.17338) · [project](https://gaozhongpai.github.io/renderfm/)
227. **REON-NVS: Real-Time Online Novel-View Synthesis from Sparse-View Videos**  
   Daeyeon Kim ⋅ Jinhyeok Kim ⋅ Gangmin Kwon ⋅ Seungjoo Shin ⋅ Sunghyun Cho
228. **RePer-360: Releasing Perspective Priors for 360° Depth Estimation via Self-Modulation**  
   Cheng Guan ⋅ Chunyu Lin ⋅ Zhijie Shen ⋅ Junsong Zhang ⋅ Jiyuan Wang  
   [arXiv:2603.05999](https://arxiv.org/abs/2603.05999) · [code](https://github.com/munimo/RePer360)
229. **ReSplat: Learning Recurrent Gaussian Splatting**  
   Haofei Xu ⋅ Daniel Barath ⋅ Andreas Geiger ⋅ Marc Pollefeys  
   [arXiv:2510.08575](https://arxiv.org/abs/2510.08575) · [code](https://github.com/cvg/resplat) · [project](https://haofeixu.github.io/resplat/)
230. **Revisiting the Volumetric Data of 4DME: Compression, Extension and Benchmarking for Micro-Expression Analysis**  
   Samuel Boccara ⋅ Amar Tious ⋅ Guoying Zhao ⋅ Yante Li ⋅ Toinon Vigier ⋅ Vincent Ricordel
231. **ReViV: Reconstructing the Viewer and the View in 4D from Monocular Egocentric Video**  
   Xiaozhong Lyu ⋅ Gen Li ⋅ Zhiyin Qian ⋅ Xucong Zhang ⋅ Marc Pollefeys ⋅ Siyu Tang  
   [arXiv:2607.17790](https://arxiv.org/abs/2607.17790) · [project](https://reviv4d.github.io/)
232. **RIGS: Radar-Informed Gaussian Splatting for Uncertainty-Aware 3D Occupancy and Motion Prediction**  
   Zeyu Han ⋅ Junzhe Wu ⋅ Fang Zhang ⋅ Maani Ghaffari Jadidi ⋅ Jianqiang Wang
233. **Robust 3DGS-based SLAM via Adaptive Kernel Smoothing**  
   Shouhe Zhang ⋅ Dayong Ren ⋅ WEN LI ⋅ Piaopiao Yu ⋅ Sensen Song ⋅ Kaikai Shao ⋅ Yurong Qian  
   [arXiv:2511.23221](https://arxiv.org/abs/2511.23221)
234. **Robust and Efficient Monocular 3D Gaussian SLAM for Kilometer-Scale Outdoor Scenes**  
   Sicheng Yu ⋅ Dongxu Shen ⋅ Beizhen ZHAO ⋅ Ding Guanzhi ⋅ Hao Wang  
   [arXiv:2606.30436](https://arxiv.org/abs/2606.30436)
235. **RoomPlanner: Reachability-Aware View Sampling for Text-to-Room 3D Gaussian Splatting**  
   Wenzhuo Sun ⋅ MingJian Liang ⋅ Wenxuan Song ⋅ Xuelian Cheng ⋅ Zongyuan Ge
236. **SA-ResGS: Self-Augmented Residual 3D Gaussian Splatting for Next Best View Selection**  
   Kim Jun-Seong ⋅ Tae-Hyun Oh ⋅ Eduardo Pérez Pellitero ⋅ Youngkyoon Jang  
   [arXiv:2601.03024](https://arxiv.org/abs/2601.03024) · [project](https://saresgs.github.io/)
237. **SAF3R: Dynamic Sparse Attention for Feed-Forward 3D Reconstruction Transformers**  
   Jianing Deng ⋅ Yuanzhe LI ⋅ Jialu Wang ⋅ Song Wang ⋅ Tianlong Chen ⋅ Huanrui Yang ⋅ Jingtong Hu  
   [arXiv:2607.03612](https://arxiv.org/abs/2607.03612) · [code](https://github.com/jndeng/SAF3R)
238. **Scal3R: Learning Efficient Multi-Relative Pose Query for Scalable Online 3D Reconstruction**  
   Chin-Yang Lin ⋅ Yang-Che Sun ⋅ Cheng Sun ⋅ Fu-En Yang ⋅ Min-Hung Chen ⋅ Yen-Yu Lin ⋅ Wei-Chen Chiu ⋅ Yu-Lun Liu
239. **SceneHI: High-Resolution 3D-Consistent Scene Texturing with Controllable Illumination**  
   Athanasios Tragakis ⋅ Marco Aversa ⋅ Daniela Ivanova ⋅ Chaitanya Kaul ⋅ Roderick Murray-Smith ⋅ Daniele Faccio ⋅ Paul Henderson
240. **Schroedinger’s Cat: Probabilistic Representation and Prediction of Potential Scene Kinematics**  
   Timy Phan ⋅ Jannik Wiese ⋅ Bjorn Ommer
241. **SEAR: Simple and Efficient Adaptation of Visual Geometric Transformers for RGB+Thermal 3D Reconstruction**  
   Vsevolod Skorokhodov ⋅ Chenghao Xu ⋅ Shuo Sun ⋅ Olga Fink ⋅ Malcolm Mielle  
   [arXiv:2603.18774](https://arxiv.org/abs/2603.18774)
242. **Seek to Segment: Active Perception for Panoramic Referring Segmentation**  
   Song Tang ⋅ Shuming Hu ⋅ Xincheng Shuai ⋅ Henghui Ding ⋅ Yu-Gang Jiang  
   [arXiv:2607.02497](https://arxiv.org/abs/2607.02497) · [project](https://henghuiding.com/APRS/)
243. **Seen2Scene: Completing Realistic 3D Scenes with Visibility-Guided Flow**  
   Quan Meng ⋅ Yujin Chen ⋅ Lei Li ⋅ Matthias Niessner ⋅ Angela Dai  
   [arXiv:2603.28548](https://arxiv.org/abs/2603.28548) · [project](https://quan-meng.github.io/projects/seen2scene/)
244. **SegVGGT: Joint 3D Reconstruction and Instance Segmentation from Multi-View Images**  
   Jinyuan Qu ⋅ Hongyang Li ⋅ Lei Zhang  
   [arXiv:2603.19926](https://arxiv.org/abs/2603.19926)
245. **SFM: Taming State Space Models for Text-to-Motion via Spatial-Frequency Modeling**  
   Shang Gao ⋅ Haicheng Liao ⋅ Wenshuo Chen ⋅ Yumu Xie ⋅ Jiaxun Zhang ⋅ Bin Rao ⋅ Chengyue Wang ⋅ Yanchen Guan ⋅ Zhiyong Cui ⋅ Shiqi Ou ⋅ Yutao Yue ⋅ Zhenning Li
246. **SharpGS: Sharpness-Preserving 3D Gaussian Splatting with Differentiable Blur-Driven Density Control**  
   Moonsoo Jeong ⋅ Dongbeen Kim ⋅ Minseong Kim ⋅ Sungkil LEE
247. **SHINE-PPG: Non-Lambertian Intrinsic Decomposition for Illumination-Robust rPPG**  
   Shih-Yu Yang ⋅ Yen-Chun Chou ⋅ Pei-Kai Huang ⋅ Chiou-Ting Hsu
248. **SkipGS: Post-Densification Backward Skipping for Efficient 3DGS Training**  
   Jingxing Li ⋅ Yongjae Lee ⋅ Deliang Fan  
   [arXiv:2603.08997](https://arxiv.org/abs/2603.08997) · [code](https://github.com/ASU-ESIC-FAN-Lab/SkipGS)
249. **SkyLume: A Large-Scale Multi-Illumination Aerial Benchmark for Urban Scene Reconstruction and Beyond**  
   Zhuoxiao Li ⋅ Wenzong Ma ⋅ Taoyu Wu ⋅ Jinjing Zhu ⋅ Shuai Zhang ⋅ Jing OU ⋅ Tongyan Hua ⋅ Yinrui Ren ⋅ Rongjun Qin ⋅ Hui Xiong ⋅ Wufan Zhao
250. **SLAM-Former: Putting SLAM into One Transformer**  
   Yijun Yuan ⋅ Zhuoguang Chen ⋅ Kenan Li ⋅ Weibang Wang ⋅ Minghui Qin ⋅ Zhijian Fang ⋅ Weicheng Zheng ⋅ Hang Zhao  
   [arXiv:2509.16909](https://arxiv.org/abs/2509.16909) · [project](https://tsinghua-mars-lab.github.io/SLAM-Former)
251. **SMG: Semantic Motion Graph for Monocular Dynamic Gaussian Splatting**  
   Haozheng Yu ⋅ Xinyu Yang ⋅ Rundong Luo ⋅ Jennifer Sun ⋅ Bharath Hariharan
252. **SMP-UWGS: Coupled Physics-Geometry Optimization for Scalable Multi-Partition Underwater 3D Reconstruction**  
   宇轩 刘 ⋅ Jinhui Zhang
253. **Sparse-View Surface Reconstruction using Gaussian Splatting through High-Confidence Depth Propagation with Normal Priors**  
   Liang Han ⋅ Bangcai Wei ⋅ Junsheng Zhou ⋅ Yushen Liu ⋅ Zhizhong Han  
   [arXiv:2607.03765](https://arxiv.org/abs/2607.03765) · [project](https://hanl2010.github.io/DP-GS)
254. **Spectral Gating via Damped Oscillations for Adaptive Implicit Neural Representations**  
   Alex Costanzino ⋅ Pierluigi Zama Ramirez ⋅ Giuseppe Lisanti ⋅ Luigi Di Stefano  
   [arXiv:2606.23129](https://arxiv.org/abs/2606.23129) · [project](https://alex-costanzino.github.io/fdho/)
255. **SplatPainter: Interactive Authoring of 3D Gaussians from 2D Edits via Test-Time Training**  
   Yang Zheng ⋅ Hao Tan ⋅ Kai Zhang ⋅ Peng Wang ⋅ Leonidas Guibas ⋅ Gordon Wetzstein ⋅ Wang Yifan  
   [arXiv:2512.05354](https://arxiv.org/abs/2512.05354) · [project](https://y-zheng18.github.io/SplatPainter/)
256. **Stabilizing Deep Reconstruction Operators with Contractive Anchoring**  
   Arghya Sinha ⋅ Trishit Mukherjee ⋅ Kunal Chaudhury  
   [arXiv:2607.23341](https://arxiv.org/abs/2607.23341)
257. **StarDojo: Benchmarking Open-Ended Behaviors of Agentic Multimodal LLMs in Production–Living Simulations with Stardew Valley**  
   Weihao Tan ⋅ Changjiu Jiang ⋅ Yu Duan ⋅ Mingcong Lei ⋅ Li JiaGeng ⋅ Yitian Hong ⋅ Xinrun Wang ⋅ Bo An  
   [arXiv:2507.07445](https://arxiv.org/abs/2507.07445) · [project](https://weihaotan.github.io/StarDojo)
258. **StructSplat: Generalizable 3D Gaussian Splatting from Uncalibrated Sparse Views**  
   Jia-Chen Zhao ⋅ Beiqi Chen ⋅ Xinyang Chen ⋅ Guangcong Wang ⋅ Liqiang Nie  
   [arXiv:2606.28321](https://arxiv.org/abs/2606.28321) · [code](https://github.com/J-C-Zhao/StructSplat) · [project](https://structsplat.github.io)
259. **Structure Gaussian Splatting SLAM**  
   Yan Li ⋅ Yingzhao Li ⋅ Gim Hee Lee
260. **StructureGS: Structure-aware Gaussian Splatting for Articulated Object Reconstruction**  
   GaHye Lee ⋅ Gyoonseo Kim ⋅ Wonjong Jang ⋅ Jooeun Son ⋅ Seungyong Lee  
   [arXiv:2607.26889](https://arxiv.org/abs/2607.26889)
261. **StyleFusion360: View-Consistent Head Stylization via Adaptive Style Modulation**  
   Furkan Guzelant ⋅ Arda Goktogan ⋅ Tarık Kaya ⋅ Aysegul Dundar  
   [arXiv:2511.22411](https://arxiv.org/abs/2511.22411)
262. **SubSplat: High-Resolution Pixel-aligned 3DGS via Sub-pixel Gaussian Reparameterization**  
   Jiun Lee ⋅ Jaekwang Kim ⋅ Sangmin Lee  
   [arXiv:2607.20813](https://arxiv.org/abs/2607.20813)
263. **SupIR-GS: Thermal Infrared Super-Resolution Novel View Synthesis with Imaging-Calibrated 3D Gaussian Splatting**  
   Jin Liu ⋅ Haodong Li ⋅ Jiagang Chen ⋅ Dabin leng ⋅ Jiguang Li ⋅ Zhao Huang ⋅ Xiaoshuai Zhang ⋅ Qi Xu ⋅ Zhiwen Zheng ⋅ Xingru Huang
264. **SVI360: Spherical Video Interpolation**  
   Le Kim NGUYEN ⋅ Renato Martins ⋅ Pascal Vasseur ⋅ Cedric Demonceaux  
   [arXiv:2607.11710](https://arxiv.org/abs/2607.11710) · [project](https://icb-vision-ai.github.io/video360_interpolation/)
265. **SyncFix: Multi-View Consistent Diffusion Refinement of 3D Reconstructions**  
   Deming Li ⋅ Cheng Peng ⋅ Abhay Kumar Yadav ⋅ Rama Chellappa ⋅ Anand Bhattad
266. **SynLF: Zero-Shot Metric Depth from Light Field Cameras via Physics-Grounded Synthesis**  
   Zhexuan Cao ⋅ Yuduo Guo ⋅ Peisheng Ding ⋅ Zhan Shi ⋅ Hui Qiao
267. **SyntheticDoc: A Large Synthetic Dataset for Document Unwarping and Illumination Correction**  
   Daniel Woortmann ⋅ Tanguy Magne ⋅ Olga Sorkine-hornung
268. **Tackling Misattribution in 3D Intrinsic Decomposition via Proximity Attention Point Rendering**  
   Alireza Moazeni ⋅ Shichong Peng ⋅ Yanshu Zhang ⋅ Chirag Vashist ⋅ Ke Li
269. **Temporally Aware Densification for Dynamic 3D Gaussian Splatting**  
   VIKRAM SANDU ⋅ Mayurdeep Pathak ⋅ Rajiv Soundararajan  
   [arXiv:2606.23212](https://arxiv.org/abs/2606.23212)
270. **Temporally Stable Generative Illumination with a One-Step Diffusion Model**  
   Harish Anand ⋅ Alexandr Kuznetsov ⋅ Sungye Kim ⋅ Wojciech Uss ⋅ Wojciech Kaliński ⋅ Rama Harihara
271. **TetraSDF: Analytic Isosurface Extraction with Multi-resolution Tetrahedral Grid**  
   Seonghun Oh ⋅ Youngjung Uh ⋅ Jin-Hwa Kim  
   [arXiv:2511.16273](https://arxiv.org/abs/2511.16273)
272. **The Sterkfontein Caves Dataset: A Novel View Rendering Challenge from the Cradle of Humankind**  
   Ireton Liu ⋅ Brian Xu ⋅ Dominic Stratford ⋅ Steven James ⋅ Richard Klein ⋅ James Tompkin
273. **ThermoGS: Decoupling Physical Surface Attributes for Spatio-Temporal Thermal Field Emulation via 4D Gaussian Splatting**  
   Kun Yang ⋅ Yuxiang Liu ⋅ Zeyu Cui ⋅ Shen Yan ⋅ Maojun Zhang ⋅ Yu Liu ⋅ Xue Wang ⋅ Qing Wang
274. **TIDES: Time-Derivative Event Simulation via Deformable Reconstruction**  
   Christopher Thirgood ⋅ Dipon Kumar Ghosh ⋅ Simon Hadfield
275. **TopoFuse: Topology-Aware Tri-Planar Fusion for 3D Cryo-Electron Tomography Segmentation**  
   Rohit Kumar Salla ⋅ Neelesh Gupta ⋅ Xingjian Li ⋅ Min Xu
276. **TopoGS: Planar Reconstruction via Topology-Aware 3D Gaussian Splatting**  
   Shanshan Pan ⋅ Jiale Chen ⋅ Yilin Liu ⋅ Hui Huang  
   [arXiv:2607.16838](https://arxiv.org/abs/2607.16838) · [project](https://vcc.tech/research/2026/TopoGS)
277. **TouchAnything: Diffusion-Guided 3D Reconstruction from Sparse Robot Touches**  
   Langzhe Gu ⋅ Hung-Jui Huang ⋅ Mohamad Qadri ⋅ Michael Kaess ⋅ Wenzhen Yuan  
   [arXiv:2604.08945](https://arxiv.org/abs/2604.08945) · [project](https://grange007.github.io/touchanything)
278. **Towards Alias-Free 4D Gaussian Representations with Motion-Aware Filtering**  
   Ankit Dhiman ⋅ Kunal Kathare ⋅ Pranav Vignesh ⋅ LOKESH BOREGOWDA ⋅ Venkatesh Babu Radhakrishnan
279. **Triangle Splatting SLAM**  
   Nicholas Fry ⋅ Eric Dexheimer ⋅ Kirill Mazur ⋅ Paul Kelly ⋅ Andrew Davison  
   [arXiv:2605.31419](https://arxiv.org/abs/2605.31419)
280. **TriFlow: Generating Artist-Like 3D Mesh Topology via Nearest-Vertex Vector Fields**  
   Haoxuan Li ⋅ Ziya Erkoç ⋅ Daniele Sirigatti ⋅ Vladislav Rosov ⋅ Lei Li ⋅ Angela Dai ⋅ Matthias Niessner  
   [arXiv:2606.20131](https://arxiv.org/abs/2606.20131) · [project](https://derkleineli.github.io/triflow/)
281. **TRiGS: Temporal Rigid-Body Motion for Scalable 4D Gaussian Splatting**  
   Suwoong Yeom ⋅ Joonsik Nam ⋅ Seunggyu Choi ⋅ Lucas Lee ⋅ Sangmin Kim ⋅ Jaesik Park ⋅ Joonsoo Kim ⋅ Kugjin Yun ⋅ Kyeongbo Kong ⋅ Suk-Ju Kang  
   [arXiv:2604.00538](https://arxiv.org/abs/2604.00538) · [project](https://wwwjjn.github.io/TRiGS-project_page/)
282. **TriNLOS: Triplane Representations for Neural Non-Line-of-Sight Imaging**  
   Bonmu Do ⋅ Ji Hyun Nam
283. **TriSplat: Adaptive Triplane for Sparse-View Large-Scale Scene Reconstruction**  
   Ryo Umagami ⋅ Tomohiro Hashimoto ⋅ Xuangeng Chu ⋅ Ziteng Cui ⋅ Yusuke Mukuta ⋅ Jia Deng ⋅ Tatsuya Harada
284. **TrustCLIP: Learning Private Visual Features via Adversarial Reconstruction**  
   Nikos Athanasiou ⋅ Ilya A. Petrov ⋅ Angela Yao ⋅ Shugao Ma ⋅ Eric Sauser ⋅ Edoardo Remelli ⋅ Shreyas Hampali ⋅ Johannes Schönberger ⋅ Fadime Sener ⋅ Bugra Tekin  
   [arXiv:2607.04484](https://arxiv.org/abs/2607.04484) · [project](https://atnikos.github.io/trustclip/)
285. **Twin-DAgger: Synergizing Digital Twins and Human Corrections for Efficient Robot Manipulation**  
   Jiahang Li ⋅ Zhirui Zhang ⋅ Kairan Ding ⋅ Fan Fei ⋅ Yunkai Tang ⋅ Jiaming Liu ⋅ Xiao He ⋅ Ziyu Chen ⋅ Gaohao Zhou ⋅ Jieji Ren ⋅ Yandong Guo ⋅ Shanghang Zhang ⋅ Boxin Shi
286. **Under One Sun: Multi-Object Generative Perception of Materials and Illumination**  
   Nobuo Yoshii ⋅ Xinran (Nicole) Han ⋅ Ryo Kawahara ⋅ Todd Zickler ⋅ Ko Nishino  
   [arXiv:2603.19226](https://arxiv.org/abs/2603.19226) · [project](https://vision.ist.i.kyoto-u.ac.jp/research/onesun/)
287. **UniDynamics: Event-RGB Fusion for Unified Future 4D Dynamic Scene Generation**  
   Daikun Liu ⋅ Xin Zhan ⋅ Teng Wang ⋅ Xiaoping Wang ⋅ Changyin Sun
288. **Unified Panoramic–Gaussian Representation for Monocular 4D Scene Synthesis**  
   Yuankun Yang ⋅ Yi Wei ⋅ Wenyang Zhou ⋅ Li Zhang  
   [arXiv:2607.01663](https://arxiv.org/abs/2607.01663)
289. **UniFusion: Sparse-View 4D Reconstruction via Unified Spatio-temporal Depth Alignment**  
   Yongzhe Lyu ⋅ Shaofei Wang ⋅ Yixin Chen ⋅ Siyuan Huang
290. **UniQueR: Unified Query-based Feedforward 3D Reconstruction**  
   Chensheng Peng ⋅ Quentin HERAU ⋅ Jiezhi Yang ⋅ Yichen Xie ⋅ Yihan Hu ⋅ Wenzhao Zheng ⋅ Matthew Strong ⋅ Masayoshi TOMIZUKA ⋅ Wei Zhan  
   [arXiv:2603.22851](https://arxiv.org/abs/2603.22851)
291. **UniSim-SLAM: Feed-Forward SLAM with Unified Sim(3) Optimization**  
   inha Lee ⋅ Dongjae Jeong ⋅ Junhee Lee ⋅ Kyungdon Joo  
   [arXiv:2608.01706](https://arxiv.org/abs/2608.01706) · [project](https://vision3d-lab.github.io/unisim-slam/)
292. **UniTriSplat: A Unified 3D Gaussian Splatting Framework with Uniform Spherical Rasterization for Universal Cameras**  
   Yipeng Zhu ⋅ Huajian Huang ⋅ Tristan Braud ⋅ Sai Kit Yeung  
   [arXiv:2606.29794](https://arxiv.org/abs/2606.29794) · [project](https://yipengzhu0809.github.io/UniTriSplat/)
293. **VideoSfM: Exploiting Temporal Structure for Video-Based Structure-from-Motion**  
   Zador Pataki ⋅ Paul-Edouard Sarlin ⋅ Marc Pollefeys
294. **ViewSplat: View-Adaptive Dynamic Gaussian Splatting for Feed-Forward Synthesis**  
   Moonyeon Jeong ⋅ Seunggi Min ⋅ Suhyeon Lee ⋅ Hongje Seong  
   [arXiv:2603.25265](https://arxiv.org/abs/2603.25265) · [project](https://cvlab-uos.github.io/ViewSplat)
295. **VIGS-SLAM: Visual Inertial Gaussian Splatting SLAM**  
   Zihan Zhu ⋅ Wei Zhang ⋅ Moyang Li ⋅ Norbert Haala ⋅ Marc Pollefeys ⋅ Daniel Barath  
   [arXiv:2512.02293](https://arxiv.org/abs/2512.02293) · [project](https://vigs-slam.github.io)
296. **VKSR: Scalable Kernel Surface Reconstruction Using Vecchia's Approximation**  
   Maximilian Weiherer ⋅ Chukwudi Williams Umah ⋅ Bernhard Egger
297. **VolSplat: Rethinking Feed-Forward 3D Gaussian Splatting with Voxel-Aligned Prediction**  
   Weijie Wang ⋅ Yeqing Chen ⋅ Zeyu Zhang ⋅ Hengyu Liu ⋅ Haoxiao Wang ⋅ ZhiYuan Feng ⋅ Wenkang Qin ⋅ Feng Chen ⋅ Jiawang Bian ⋅ Zheng Zhu ⋅ Donny Y. Chen ⋅ Bohan Zhuang  
   [arXiv:2509.19297](https://arxiv.org/abs/2509.19297) · [code](https://github.com/ziplab/VolSplat) · [project](https://lhmd.top/volsplat)
298. **VSDiffusion: Taming Ill-Posed Shadow Generation via Visibility-Constrained Diffusion**  
   Jing Li ⋅ Jing Zhang  
   [arXiv:2603.08020](https://arxiv.org/abs/2603.08020)
299. **Walking in the Implicit: Interactive World Exploration via Neural Scene Representation**  
   Zhiqi Li ⋅ Chengrui Dong ⋅ Zhenhua Du ⋅ Hangning Zhou ⋅ Cong Qiu ⋅ Hailong Qin ⋅ Mu Yang ⋅ Dongxu Wei ⋅ Peidong Liu  
   [arXiv:2606.30045](https://arxiv.org/abs/2606.30045)
300. **Weight-Space Mixture-of-Experts for Implicit Neural Representation Classification**  
   Stanisław Janik ⋅ Michal Byra  
   [arXiv:2607.29463](https://arxiv.org/abs/2607.29463)
301. **What if? Emulative Simulation with World Models for Situated Reasoning**  
   Ruiping Liu ⋅ Yufan Chen ⋅ Yuheng Zhang ⋅ Junwei Zheng ⋅ Kunyu Peng ⋅ Chengzhi Wu ⋅ Chenguang Huang ⋅ Di Wen ⋅ Jiaming Zhang ⋅ Kailun Yang ⋅ Rainer Stiefelhagen  
   [arXiv:2603.06445](https://arxiv.org/abs/2603.06445) · [code](https://github.com/RuipingL/WanderDream)
302. **What VGGT Knows About Overlap: Probing Geometric Foundation Models for Co-Visibility**  
   Filippo Ziliotto ⋅ Luciano Serafini ⋅ Lamberto Ballan ⋅ Tommaso Campari  
   [arXiv:2607.09503](https://arxiv.org/abs/2607.09503)
303. **When 3D Gaussian Splatting Recovers Real Surfaces**  
   Songhe Wang ⋅ David Miller
304. **Wid3R: Wide Field-of-View 3D Reconstruction via Camera Model Conditioning**  
   Dongki Jung ⋅ Jaehoon Choi ⋅ Adil Qureshi ⋅ Somi Jeong ⋅ Dinesh Manocha ⋅ Suyong Yeon  
   [arXiv:2602.05321](https://arxiv.org/abs/2602.05321)
305. **WildCity: A Real-World Dataset for City-Scale Rendering and Beyond**  
   Xiangyu Han ⋅ Mengyu Yang ⋅ Jiaqi Li ⋅ Bowen Chang ⋅ Ziyu Chen ⋅ Hexu Zhao ⋅ Rahul Agrawal ⋅ Anthony Rodriguez ⋅ Rajani Acharya ⋅ Fiona Hua ⋅ Marco Pavone ⋅ Chen Feng ⋅ Yiming Li
306. **WildSplat: Feedforward Gaussian Splatting from Unposed In-the-Wild Images**  
   Xiyu Zhang ⋅ Jingyu Zhuang ⋅ Hongjia Zhai ⋅ Zizheng Yan ⋅ Jinwei Chen ⋅ Guofeng Zhang ⋅ Qingnan Fan  
   [arXiv:2607.05347](https://arxiv.org/abs/2607.05347) · [project](https://zju3dv.github.io/wildsplat/)
307. **WilLaGS: Latent-Conditional 3D Appearance Fields for Robust Gaussian Splatting In-the-Wild**  
   yuhao Bai ⋅ Qianqiu Tan ⋅ Lilong Chen ⋅ Huanhuan Lv ⋅ Lijun Chen
308. **World Reconstruction From Inconsistent Views**  
   Lukas Höllein ⋅ Matthias Niessner  
   [arXiv:2603.16736](https://arxiv.org/abs/2603.16736) · [code](https://github.com/lukasHoel/video_to_world) · [project](https://lukashoel.github.io/video_to_world)
309. **X-SG2S: Safe and Generalizable Gaussian Splatting with X-dimensional Watermarks**  
   Zihang Cheng ⋅ Wentao Bao ⋅ HUIPING ZHUANG ⋅ Chun Li ⋅ Xin Meng ⋅ Ziqian Zeng ⋅ Cen Chen ⋅ Ming Li ⋅ Fei Yu
310. **Zero-Shot Novel Depth Synthesis Using Foundation Models Scene Representations**  
   Denis Akola ⋅ David Fouhey
311. **ZeroSplat: Generalized Referring Segmentation in 3D Gaussian Splatting**  
   Jiayu Ding ⋅ Meilu Song ⋅ Xiaoyi Zhang ⋅ Hongbo Jin ⋅ Yichen Jin ⋅ Xiangtian Si  
   [arXiv:2607.18801](https://arxiv.org/abs/2607.18801) · [project](https://inkmind-ai.github.io/ZeroSplat)
312. **Φeat: Physically-Grounded Material Feature Representation**  
   Giuseppe Vecchio ⋅ Adrien Kaiser ⋅ Claudia Cuttano ⋅ ROUFFET Romain ⋅ Rosalie MARTIN ⋅ Elena Garces ⋅ Tamy Boubekeur
313. **∂DIBR: Differentiable Depth Image-based Rendering for Fast Novel View Synthesis**  
   Armand Losfeld ⋅ Sarah Dury ⋅ Gauthier Lafruit ⋅ Mehrdad Teratani ⋅ Daniele Bonatto

## Depth, Geometry, Matching & Camera Pose

*129 papers · 86 with links*

1. **3D Scene-Adaptive Trajectory-Controllable Human Image Animation with Camera Movement**  
   Deyin Liu ⋅ Jicheng Xu ⋅ Lin Wu ⋅ Xiaowei Zhao ⋅ Xiatian Zhu ⋅ Anjan Dutta ⋅ Zhe Jin  
   [arXiv:2606.30514](https://arxiv.org/abs/2606.30514) · [project](https://robinhood256100.github.io/web-disp)
2. **A Benchmark for Heterogeneous Stereo Deblurring with Physically- and Epipolar-constrained Cross Attention**  
   Jiah Kim ⋅ Hoju Shin ⋅ Seung-Wook Kim ⋅ Seowon Ji  
   [arXiv:2606.25962](https://arxiv.org/abs/2606.25962)
3. **A second-order theory of texture for depth from focus**  
   Sreekar Ranganathan ⋅ Ioannis Gkioulekas  
   [arXiv:2608.10411](https://arxiv.org/abs/2608.10411) · [project](https://imaging.cs.cmu.edu/second-order-texture/)
4. **Actor as Its Own Critic: Unifying Region Understanding and Localization via CycleGRPO**  
   Xin Zhang ⋅ Haochen Wang ⋅ Yikang Zhou ⋅ Zhuochen Wang ⋅ Robby T. Tan ⋅ Xiangtai Li  
   [arXiv:2607.11581](https://arxiv.org/abs/2607.11581) · [code](https://github.com/devinxzhang/CycleGRPO)
5. **Any to Full: Prompting Depth Anything for Depth Completion in One Stage**  
   Zhiyuan Zhou ⋅ Ruofeng Liu ⋅ TAICHI LIU ⋅ Weijian Zuo ⋅ Shanshan Wang ⋅ Zhiqing Hong ⋅ Desheng Zhang  
   [arXiv:2603.05711](https://arxiv.org/abs/2603.05711) · [code](https://github.com/zhiyuandaily/Any2Full)
6. **AnyMatch: Supercharging Universal Multi-Modal Image Matching with Large-Scale Single-View Images**  
   Meng Yang ⋅ Zizhuo Li ⋅ Linfeng Tang ⋅ Fan Fan ⋅ Jiayi Ma  
   [arXiv:2606.31077](https://arxiv.org/abs/2606.31077)
7. **APT: Anchor-aligned Perturbations for Tamper Localization in Fully Regenerated Images**  
   Suhyeon Ha ⋅ Woo Jae Kim ⋅ Joonsung Jeon ⋅ Sooel Son ⋅ Sung-eui Yoon
8. **AquaStereo: Enabling Underwater Stereo Matching via Depth-Conditioned Diffusion and Geometry Self-Distillation**  
   Qizhe Wei ⋅ Yingping Liang ⋅ Shao You ⋅ Ying Fu  
   [arXiv:2607.04303](https://arxiv.org/abs/2607.04303) · [code](https://github.com/qz-wei/AquaStereo)
9. **ARC-Loc: Leveraging Azimuthal Ray Convergence as a Geometric Cue for Direct Cross-View Localization**  
   Hyeongsik Kim ⋅ Mincheol Kim ⋅ Heejoon Moon ⋅ Je Hyeong Hong
10. **AutoCompass: Accurate Visual Localization on Public Maps by Learning from Weak Labels**  
   Javier Tirado-Garín ⋅ Alan Paul ⋅ Shuai Chen ⋅ Axel Barroso-Laguna ⋅ Tommaso Cavallari ⋅ Daniyar Turmukhambetov ⋅ Victor Adrian Prisacariu ⋅ Eric Brachmann
11. **BBQ-V: Benchmarking Visual Stereotype Bias in Large Multimodal Models**  
   Vishal Narnaware ⋅ Ashmal Vayani ⋅ Rohit Gupta ⋅ Swetha Sirnam ⋅ Shah Mubarak  
   [arXiv:2502.08779](https://arxiv.org/abs/2502.08779)
12. **Beyond 2D Matching: A Unified Single-Stage Framework for Geometry-Aware Cross-View Object Geo-Localization**  
   Liyao Wang ⋅ Ruipu Wu ⋅ Haojun Xu ⋅ Lei Shi ⋅ Linjiang Huang ⋅ Si Liu  
   [arXiv:2606.30576](https://arxiv.org/abs/2606.30576)
13. **BLASt3R: Bundle Adjustment of Any Image Set with Multi-View Matching and Monocular priors**  
   Vincent Leroy ⋅ Philippe Weinzaepfel ⋅ Lojze Zust ⋅ Yohann Cabon ⋅ Jerome Revaud
14. **Blind to Position, Biased in Language: Probing Mid-Layer Representational Bias in Vision-Language Encoders for Zero-Shot Language-Grounded Spatial Understanding**  
   Na Min An ⋅ Inha Kang ⋅ Minhyun Lee ⋅ Hyunjung Shim  
   [arXiv:2509.23098](https://arxiv.org/abs/2509.23098)
15. **Boosting 6D Object Pose Estimation via Monocular Depth Cues**  
   Fengda Hao ⋅ Rui Song ⋅ Qingyuan Wang ⋅ Jiaojiao Li ⋅ Zhiyong Hu ⋅ David Ferstl ⋅ Yinlin Hu
16. **Boosting Correspondence Learning with Structure-Aware Estimator**  
   Tianyu Yan ⋅ Wei An ⋅ Pu Wang ⋅ Yingqian Wang
17. **Boosting Text-Driven Video Segmentation via Geometry-Aware Distillation**  
   Tianyu Zhu ⋅ Yingping Liang ⋅ Hesong Li ⋅ Ying Fu  
   [arXiv:2606.24464](https://arxiv.org/abs/2606.24464) · [code](https://github.com/Tony1882880/GeoLaV)
18. **Bridge-UniPS: Bridging Calibrated Photometric Stereo toward Universal Photometric Stereo**  
   Minzhe Xu ⋅ Xiaoyan Liu ⋅ YuJie Xing ⋅ Qian Chen
19. **CameraAnything: Refilming Videos with Arbitrary Camera Control**  
   Yixuan Li ⋅ Yanhong Zeng ⋅ Ka Leong Cheng ⋅ Jiayi Zhu ⋅ Hanlin Wang ⋅ Wen Wang ⋅ Yihao Meng ⋅ Hao Ouyang ⋅ Qiuyu Wang ⋅ Yue Yu ⋅ Zidong Wang ⋅ Yiyuan Zhang ⋅ Yujun Shen ⋅ Dahua Lin  
   [arXiv:2607.24591](https://arxiv.org/abs/2607.24591) · [project](https://yixuanli98.github.io/cameraanything/)
20. **Category-Level 3D Correspondence in Camera Space via Morphable Object Priors**  
   Leonhard Sommer ⋅ Artur Jesslen ⋅ Basavaraj Sunagad ⋅ Adam Kortylewski  
   [arXiv:2605.28257](https://arxiv.org/abs/2605.28257) · [code](https://github.com/GenIntel/HouseCorr3D)
21. **ConfCtrl: Enabling Precise Camera Control in Video Diffusion via Confidence-Aware Interpolation**  
   Liudi Yang ⋅ George Eskandar ⋅ Fengyi Shen ⋅ Mohammad Altillawi ⋅ Yang Bai ⋅ Chi zhang ⋅ Ziyuan Liu ⋅ Abhinav Valada  
   [arXiv:2603.09819](https://arxiv.org/abs/2603.09819)
22. **Consistent Monocular Depth Estimation with Contact Region Boundary-Aware Refinement**  
   Yinuo Wang ⋅ QingMiao QingMiao ⋅ Wangmeng Zuo
23. **Consistent Video-to-Video Translation via Explicit Correspondences**  
   Gaurav Parmar ⋅ Zhengqi Li ⋅ Richard Zhang ⋅ Jun-Yan Zhu ⋅ Srinivasa G. Narasimhan ⋅ Eli Shechtman ⋅ Yotam Nitzan
24. **Controllable Generative Reference for Stereo Image Compression via Reliability-Aware Gating**  
   Zhineng Zhao ⋅ Mingyao Hong ⋅ Fengfan Shi ⋅ Zhihai He
25. **Cooking beyond Frames: A Stereo Event Camera Dataset in the Kitchen**  
   Chengming Feng ⋅ Hesam Araghi ⋅ Liming Zheng ⋅ Julien Dupeyroux ⋅ Xucong Zhang ⋅ Jan van Gemert ⋅ Nergis Tomen  
   [arXiv:2608.04865](https://arxiv.org/abs/2608.04865)
26. **Cross-token Guidance Transformer for Weakly Supervised Object Localization**  
   Zhiwei Chen ⋅ Yiran Nie ⋅ Ruize Han ⋅ Qinqin Zhou
27. **CrossFeat: Bridging Imaging Modalities in Feature Descriptor Space**  
   Paul Schneider ⋅ Nazim Haouchine
28. **CSS-BA: Gate Guided Column Space Search for Bundle Adjustment**  
   Ayano Kaneda ⋅ Takafumi Taketomi ⋅ Shugo Yamaguchi ⋅ Shigeo Morishima  
   [arXiv:2607.15652](https://arxiv.org/abs/2607.15652)
29. **DDStereo: Efficient Dual Decoder Transformers for Stereo 3D Road Anomaly Detection**  
   Shiyi Mu ⋅ Zichong Gu ⋅ Zhiqi Ai ⋅ Yilin Gao ⋅ Shugong Xu  
   [arXiv:2606.24805](https://arxiv.org/abs/2606.24805) · [code](https://github.com/shiyi-mu/DDStereo)
30. **DG-Force: Disentangling and Gathering Forensic Cues is Needed for Image Manipulation Localization**  
   Yong Yao ⋅ Zhenyu Cui ⋅ Lei Chen ⋅ Jiwen Lu ⋅ Jiahuan Zhou
31. **DINOv3D: 2D-3D Joint Optimization for Unified Spatial Understanding**  
   Bo Zhou ⋅ Jianzhe Gao ⋅ Zhihui Wang ⋅ Lingxiang Wu ⋅ Jinqiao Wang ⋅ Yazhou Yao ⋅ Wenguan Wang
32. **Disentangling Pictorial Cue Understanding from Language Bias in VLMs via Depth Ordering Task**  
   Yiqian Liu ⋅ Iuliia Kotseruba ⋅ John Tsotsos  
   [arXiv:2607.01503](https://arxiv.org/abs/2607.01503) · [code](https://github.com/lyiqian/o3-d)
33. **DualCamCtrl: Dual-Branch Diffusion Model for Geometry-Aware Camera-Controlled Video Generation**  
   Hongfei Zhang ⋅ Kanghao Chen ⋅ Zixin Zhang ⋅ Harold Haodong Chen ⋅ Yuanhuiyi Lyu ⋅ Kun Zhou ⋅ Yuqi Zhang ⋅ Shuai Yang ⋅ Yingcong Chen  
   [arXiv:2511.23127](https://arxiv.org/abs/2511.23127) · [project](https://soyouthinkyoucantell.github.io/dualcamctrl-page/)
34. **E-MOTION: A Dataset for Event-Based Scene Flow Estimation with Independent Moving Objects**  
   Ivan Gutierrez Rodriguez ⋅ Julien Moreau ⋅ Chiara Bartolozzi ⋅ Arren Glover
35. **Estimating Velocity and Spin of Spherical Objects from Rolling-Shutter Image(s)**  
   Wenjie Xue ⋅ Jun Yang ⋅ Jingmin Wang ⋅ Limin Shang  
   [arXiv:2606.31760](https://arxiv.org/abs/2606.31760)
36. **EventVGGT: Exploring Cross-Modal Distillation for Consistent Event-based Depth Estimation**  
   Yinrui Ren ⋅ Jinjing Zhu ⋅ Kanghao Chen ⋅ Zhuoxiao Li ⋅ Jing OU ⋅ Zidong Cao ⋅ Tongyan Hua ⋅ Peilun Shi ⋅ Yingchun Fu ⋅ Wufan Zhao ⋅ Hui Xiong  
   [arXiv:2603.09385](https://arxiv.org/abs/2603.09385) · [code](https://github.com/yinruiRen/EventVGGT)
37. **FeDepth: Federated Learning for Depth Estimation under Robot Heterogeneity**  
   Ganghyeon Lee ⋅ inha Lee ⋅ Junhee Lee ⋅ Jeongeon Lee ⋅ Sung Whan Yoon ⋅ Kyungdon Joo  
   [arXiv:2608.01129](https://arxiv.org/abs/2608.01129) · [project](https://vision3d-lab.github.io/fedepth/)
38. **Fisheye3R: Adapting Unified 3D Feed-Forward Foundation Models to Fisheye Lenses**  
   Ruxiao Duan ⋅ Erin Hong ⋅ Dongxu Zhao ⋅ Eric Turner ⋅ Alex Wong ⋅ Yunwen Zhou  
   [arXiv:2603.28896](https://arxiv.org/abs/2603.28896) · [code](https://github.com/android-xr/fisheye3r)
39. **FlowPainter: Inpainting Optical Flow via Confidence-Guided Completion**  
   Yuang Meng ⋅ Chenyang Wu ⋅ Xianshun Liu ⋅ Chun-Le Guo ⋅ Zichen Liang ⋅ Lina Lei ⋅ Jie Liang ⋅ Hui Zeng ⋅ Chongyi Li ⋅ Yabin Zhang  
   [arXiv:2607.10140](https://arxiv.org/abs/2607.10140) · [code](https://github.com/mya012/FlowPainter)
40. **FoundationGeo: Learning Spatial Pixel-Wise Fields for Monocular Metric Geometry**  
   Muxin Liu ⋅ Xiaoyang Lyu ⋅ Tianhe Ren ⋅ Peng Dai ⋅ Xiaoshan Wu ⋅ Zhiyue Zhang ⋅ Jiaqi Zhang ⋅ Jiehong Lin ⋅ Shaoshuai Shi ⋅ Qi Xiaojuan  
   [arXiv:2607.11588](https://arxiv.org/abs/2607.11588) · [project](https://mx-liu6.github.io/FoundationGeo-web/)
41. **FoundDP: Revisiting Weak Disparity Observability in Dual-Pixel Depth Estimation**  
   fengchen he ⋅ Hao Xu ⋅ Dayang Zhao ⋅ Tingwei Quan ⋅ Shaoqun zeng  
   [arXiv:2607.01900](https://arxiv.org/abs/2607.01900) · [code](https://github.com/EchoLighting/FoundDP)
42. **Fragmented Text Is Insufficient for Image Representation: Fine-Grained Correspondence in Multimodal Dataset Distillation**  
   Jingwei Fang ⋅ Yaxin Hou ⋅ Bo Han ⋅ Xu Zhang ⋅ Hui LIU ⋅ Junhui Hou ⋅ Yuheng Jia
43. **FreeFlow: A Bias-free Hierarchical Transformer for Optical Flow Estimation**  
   Vladislav Bargatin ⋅ Alexander Yakovenko ⋅ Khaled Abud ⋅ Dmitriy Vatolin
44. **From Perspective to Fisheye Depth Estimation and Open-Vocabulary Segmentation**  
   Rit Gangopadhyay ⋅ Alex Wong
45. **Gaussian Belief Propagation Network for Depth Completion**  
   Jie Tang ⋅ Pingping Xie ⋅ Jian Li ⋅ Ping Tan  
   [arXiv:2601.21291](https://arxiv.org/abs/2601.21291)
46. **Generating Multi-view Adversarial Examples for Visual Geometry Grounded Transformer**  
   Qi Song ⋅ Ziyuan Luo ⋅ Haoliang Han ⋅ Renjie Wan
47. **Geo-ID: Test-Time Geometric Consensus for Cross-View Consistent Intrinsics**  
   Alara Dirik ⋅ Stefanos Zafeiriou  
   [arXiv:2603.13859](https://arxiv.org/abs/2603.13859)
48. **GeoBrowse: A Geolocation Benchmark for Agentic Tool Use with Expert-Annotated Reasoning Traces**  
   Xinyu Geng ⋅ Yanjing Xiao ⋅ Yuyang Zhang ⋅ Hanwen Wang ⋅ Xinyan Liu ⋅ Rui Min ⋅ Tianqing Fang ⋅ Yi Ren Fung  
   [arXiv:2604.04017](https://arxiv.org/abs/2604.04017) · [code](https://github.com/ornamentt/GeoBrowse)
49. **GeoEdit: Geometry-Aware Object Editing via Dual-Branch Denoising**  
   Yi He ⋅ Jiangming Wang ⋅ Xinyu Wang ⋅ Mark Fong ⋅ Songchun Zhang ⋅ Yuxuan Xue ⋅ Hai-Tao Zheng ⋅ Yue Ma  
   [arXiv:2606.30003](https://arxiv.org/abs/2606.30003) · [code](https://github.com/Heey731/GeoEdit)
50. **Geometric Distillation from Rectified Stereo: Leveraging Epipolar Cues for Monocular Depth**  
   Jung-Hee Kim ⋅ Xiaoming Liu  
   [arXiv:2607.15600](https://arxiv.org/abs/2607.15600)
51. **Geometry Aware Reliable Instance Selection for Noisy Partial Label Learning**  
   Rohit Sinha ⋅ Saroj Kumar
52. **Geometry-Aware Visual Representation for Remaining Useful Life Prediction**  
   Hieu Vu ⋅ Thanh Nguyen ⋅ Eyad Elyan
53. **GeoMix: Descriptor-Free Visual Localization via Global Context and Multi-Detector Training**  
   Yejun zhang ⋅ Xinjue Wang ⋅ Zihan Wang ⋅ Esa Rahtu ⋅ Juho Kannala  
   [arXiv:2607.02486](https://arxiv.org/abs/2607.02486) · [code](https://github.com/YejunZhang/Geomix)
54. **GimbalDiffusion: Gravity-Aware Camera Control for Video Generation**  
   Frédéric Fortier-Chouinard ⋅ Yannick Hold-Geoffroy ⋅ Valentin Deschaintre ⋅ Matheus Gadelha ⋅ Jean-Francois Lalonde  
   [arXiv:2512.09112](https://arxiv.org/abs/2512.09112) · [project](https://lvsn.github.io/GimbalDiffusion/)
55. **ICDepth: Taming Video Diffusion Models for Video Depth Estimation via In-Context Conditioning**  
   Xuanhua He ⋅ JIAXIN XIE ⋅ Mingzhe Zheng ⋅ Qifeng Chen  
   [arXiv:2607.01677](https://arxiv.org/abs/2607.01677) · [project](https://xuanhuahe.github.io/ICDepth/)
56. **Image Warping for Image-to-Image Translation**  
   Shen Zheng ⋅ Anurag Ghosh ⋅ Gaurav Parmar ⋅ Srinivasa G. Narasimhan
57. **Infinite-Homography as Robust Conditioning for Camera-Controlled Video Generation**  
   Min-Jung Kim ⋅ Jeongho Kim ⋅ Hoiyeong Jin ⋅ Junha Hyung ⋅ Choo Jaegul  
   [arXiv:2512.17040](https://arxiv.org/abs/2512.17040) · [project](https://emjay73.github.io/InfCam/)
58. **InFlux++: Real and Synthetic Data for Estimating Dynamic Camera Intrinsics**  
   Erich Liang ⋅ Caleb Kha-Uong ⋅ Chinmaya Saran ⋅ Sreemanti Dey ⋅ David Liu ⋅ Junhan Ouyang ⋅ Benjamin Zhou ⋅ Jia Deng  
   [arXiv:2607.05389](https://arxiv.org/abs/2607.05389) · [project](https://influx.cs.princeton.edu/)
59. **Kilometer-Vision: A New Frontier for Large-Scale Spatial Awareness in VLMs**  
   Aravindh Mahendran ⋅ Michael King ⋅ Matthew Grimes ⋅ Antoine Yang ⋅ Tyler Zhu ⋅ Joseph Heyward ⋅ Tengda Han ⋅ Shiry Ginosar ⋅ Chen Sun ⋅ Dima Damen ⋅ Simon Osindero ⋅ Noah Snavely ⋅ Simon Lynen ⋅ Joao Carreira ⋅ Viorica Patraucean
60. **Last-Layer-Centric Feature Recombination: Unleashing 3D Geometric Knowledge in DINOv3 for Monocular Depth Estimation**  
   Gongshu Wang ⋅ Zhirui Wang ⋅ Kan Yang  
   [arXiv:2604.26454](https://arxiv.org/abs/2604.26454)
61. **Learning Geometry-Aware Embedding Fields for Intrinsic Riemannian Mappings**  
   Bo Pang ⋅ Simone Foti ⋅ Tolga Birdal
62. **LinStereo: Linear-Complexity Global Attention for Multi-Scale Iterative Stereo Matching**  
   Yiran Wang ⋅ Oliver Turner ⋅ Viorela Ila  
   [arXiv:2606.25437](https://arxiv.org/abs/2606.25437)
63. **LiteMatch: Lightweight Zero-Shot Stereo Matching via Cost Volume Stabilization**  
   Md Raqib Khan ⋅ Santosh Vipparthi ⋅ Subrahmanyam Murala  
   [arXiv:2606.31636](https://arxiv.org/abs/2606.31636) · [project](https://mdraqibkhan.github.io/Litematch)
64. **LoMa: Local Feature Matching Revisited**  
   David Nordström ⋅ Johan Edstedt ⋅ Georg Bökman ⋅ Jonathan Astermark ⋅ Anders Heyden ⋅ Viktor Larsson ⋅ Mårten Wadenbäck ⋅ Michael Felsberg ⋅ Fredrik Kahl  
   [arXiv:2604.04931](https://arxiv.org/abs/2604.04931) · [code](https://github.com/davnords/LoMa)
65. **Lost in the Tail: Addressing Geographic Imbalance in Urban Visual Place Recognition**  
   Zoey Shu ⋅ Jiacheng Yang ⋅ Yang Lu ⋅ Waishan Qiu ⋅ Chuan Li ⋅ Da Chen  
   [arXiv:2607.00090](https://arxiv.org/abs/2607.00090)
66. **Masked Depth Modeling for Spatial Perception**  
   Bin Tan ⋅ CHANGJIANG SUN ⋅ Xiage Qin ⋅ Hanat Adai ⋅ Zelin Fu ⋅ Tianxiang Zhou ⋅ Han Zhang ⋅ YINGHAO XU ⋅ Xing Zhu ⋅ Yujun Shen ⋅ Nan Xue  
   [arXiv:2601.17895](https://arxiv.org/abs/2601.17895)
67. **MegaFlow: Zero-Shot Large Displacement Optical Flow**  
   Dingxi Zhang ⋅ Fangjinhua Wang ⋅ Marc Pollefeys ⋅ Haofei Xu  
   [arXiv:2603.25739](https://arxiv.org/abs/2603.25739) · [code](https://github.com/cvg/megaflow) · [project](https://kristen-z.github.io/projects/megaflow)
68. **MetricAnything: Scaling Metric Depth Pretraining with Noisy Heterogeneous Sources**  
   Jiahui Yang ⋅ Donglin Di ⋅ Xuancheng Zhang ⋅ Lei Fan ⋅ Jianxun Cui ⋅ Hao Li ⋅ Baorui Ma  
   [arXiv:2601.22054](https://arxiv.org/abs/2601.22054) · [project](http://metric-anything.github.io/metric-anything-io/) · [project](https://metric-anything.github.io/metric-anything-io/)
69. **MG-RWKV: Multi-Grained Context-Aware RWKV for Temporal Forgery Localization**  
   Jingchen Ni ⋅ Cangjin Yu ⋅ Zytang Jiang ⋅ Quan Zhang ⋅ Keyu Lv ⋅ Shannan Yan ⋅ Linyue Pan ⋅ Ke Zhang ⋅ Chun Yuan  
   [arXiv:2607.00902](https://arxiv.org/abs/2607.00902)
70. **MUSE: Unlocking Timestep as Native Task Steering for One-Step Dense Prediction**  
   Shuo Zhou ⋅ Zhaoxin Li ⋅ Xiujuan Chai
71. **MV-GEL: Language-Driven Multi-View Geometric Entity Localization on Meshes**  
   Kartik Bali ⋅ Roland Aydin  
   [arXiv:2606.31533](https://arxiv.org/abs/2606.31533) · [code](https://github.com/kbali1297/MV-GEL)
72. **Natural Language Camera Movement Understanding**  
   Yuwen Tan ⋅ Joey Huang ⋅ Jin Huang ⋅ Haoxiang Li ⋅ Boqing Gong  
   [arXiv:2607.03043](https://arxiv.org/abs/2607.03043)
73. **OmniCamera: A Unified Framework for Multi-task Video Generation with Arbitrary Camera Control**  
   Yukun Wang ⋅ Ruihuang Li ⋅ Jiale Tao ⋅ Shiyuan Yang ⋅ Liyi Chen ⋅ Zhantao Yang ⋅ Handz Handz ⋅ Yulan Guo ⋅ Shuai Shao ⋅ Qinglin Lu  
   [arXiv:2604.06010](https://arxiv.org/abs/2604.06010)
74. **OmniDS: Dual-Stream Context Fusion for Omnidirectional Depth from Fisheye Cameras**  
   Chaesong Park ⋅ Jihyeon Hwang ⋅ Muyeol Sung ⋅ Jongwoo Lim  
   [arXiv:2607.03038](https://arxiv.org/abs/2607.03038) · [project](https://parkchaesong.github.io/omnids)
75. **On the real-world generalisability of Optical Flow models**  
   Petter Reijalt ⋅ Alexander Gielisse ⋅ Rickard Karlsson ⋅ Jan van Gemert  
   [arXiv:2607.10470](https://arxiv.org/abs/2607.10470)
76. **OnPoint: Offline-to-Online Multi-Level Distillation for Point-Supervised Online Temporal Action Localization**  
   Sakib Reza ⋅ Gauri Jagatap ⋅ Mohsen Moghaddam ⋅ OCTAVIA CAMPS ⋅ Andrea Fanelli  
   [arXiv:2607.00289](https://arxiv.org/abs/2607.00289)
77. **OpenCVL: An Open, Diverse, and Large-Scale Dataset for Fine-Grained Cross-View Localization**  
   Zimin Xia ⋅ Mubariz Zaffar ⋅ Junsheng Fu ⋅ Alexandre ALahi ⋅ Julian Kooij
78. **OpenSpatial: A Principled Data Engine for Empowering Spatial Intelligence**  
   Jianhui Liu ⋅ Haoze Sun ⋅ Wenbo Li ⋅ Yanbing Zhang ⋅ Rui Yang ⋅ zhiliang zhu ⋅ Yijun Yang ⋅ Shenghe Zheng ⋅ Nan Jiang ⋅ Jiaxiu Jiang ⋅ Haoyang Huang ⋅ Tien-Tsin Wong ⋅ Nan Duan ⋅ Qi Xiaojuan  
   [arXiv:2604.07296](https://arxiv.org/abs/2604.07296) · [code](https://github.com/VINHYU/OpenSpatial)
79. **OTCache: Optimal Transport for Geometry-Aware Caching in Diffusion Models**  
   Huanlin Gao ⋅ Fang Zhao ⋅ Qiang Hui ⋅ Fuyuan Shi ⋅ Shaoan Zhao ⋅ Yantao Li ⋅ Chao Tan ⋅ Ting Lu ⋅ Yuren You ⋅ Kai Wang ⋅ Shiguo Lian  
   [arXiv:2606.31026](https://arxiv.org/abs/2606.31026) · [code](https://github.com/UnicomAI/OTCache)
80. **Physically Grounded Monocular Depth via Nanophotonic Wavefront Encoding**  
   Bingxuan Li ⋅ Jiahao Wu ⋅ Yuan Xu ⋅ Zezheng Zhu ⋅ Yunxiang Zhang ⋅ Kenneth Chen ⋅ Yanqi Liang ⋅ Nanfang Yu ⋅ Qi Sun  
   [arXiv:2503.15770](https://arxiv.org/abs/2503.15770)
81. **PixVOD: Pixel-Distributed Direct Visual Odometry and Depth Estimation**  
   Shinjeong Kim ⋅ Ignacio Alzugaray ⋅ Callum Rhodes ⋅ Paul Kelly ⋅ Andrew Davison  
   [arXiv:2606.03989](https://arxiv.org/abs/2606.03989) · [project](https://www.shinjeongkim.com/pixvod/)
82. **Pose Anything Anywhere: Model-free Object Poses from Arbitrary References**  
   Hongli XU ⋅ Jiaqi Hu ⋅ Junwen Huang ⋅ Boyang ZHONG ⋅ Peter Yu ⋅ Nassir Navab ⋅ Benjamin Busam ⋅ Slobodan Ilic
83. **PRISM-VO: Scale-Aware Visual Odometry Using Photometric Plenoptic Bundle Adjustment**  
   Aymeric Fleith ⋅ Julian Zirbel ⋅ Daniel Cremers ⋅ Niclas Zeller  
   [arXiv:2607.00176](https://arxiv.org/abs/2607.00176) · [project](https://prism-vo.github.io/)
84. **Proposal Score Realignment Guided by Semantic Completeness for Weakly Supervised Temporal Action Localization**  
   Maodong Li ⋅ Zhihao Wang ⋅ Jingxiong Wang ⋅ Jian Wang ⋅ Bing Li
85. **Pseudo-Stereo Inputs: A Solution to the Occlusion Challenge in Self-Supervised Stereo Matching**  
   Ruizhi Yang ⋅ Xingqiang Li ⋅ Jiajun Bai ⋅ Jinsong Du  
   [arXiv:2410.02534](https://arxiv.org/abs/2410.02534)
86. **Qwen-3D: A Generalist 3D Vision-Language Model for Spatial Understanding**  
   Lucy Lin ⋅ Ayush Jain ⋅ Yifan Liu ⋅ Katerina Fragkiadaki  
   [arXiv:2608.02980](https://arxiv.org/abs/2608.02980) · [project](https://qwen-3d.github.io/)
87. **RaysUp: Ultra-light Universal Feature Upsampling via Geometry-Aware Ray Representation**  
   Ding Yuchuan ⋅ Linfei Li ⋅ Lin Zhang ⋅ Ying Shen  
   [arXiv:2606.22749](https://arxiv.org/abs/2606.22749) · [code](https://github.com/MAP-RaysUp/RaysUp)
88. **Recurrent Cross-View Object Geo-Localization**  
   Xiaohan Zhang ⋅ Siyuan Cao ⋅ Xiaokai Bai ⋅ Yiming Li ⋅ Zhangkai Shen ⋅ Zhe Wu ⋅ Lun Luo ⋅ Qi Ming ⋅ Xiaoxi Hu ⋅ Hui-Liang Shen  
   [arXiv:2509.12757](https://arxiv.org/abs/2509.12757) · [code](https://github.com/Temperature-ai/ReCOT.git)
89. **RegVGGT: Sustainable Visual Geometry Grounding for Streaming via Regulated Memory**  
   Hongbo Mao ⋅ Junjun Jiang ⋅ Youyu Chen ⋅ Jiaxin Zhang ⋅ Zhemeng Dong ⋅ Xianming Liu
90. **Repurposing Geometric Foundation Models for Multi-view Diffusion**  
   Wooseok Jang ⋅ Seonghu Jeon ⋅ Jisang Han ⋅ Jinhyeok Choi ⋅ Minkyung Kwon ⋅ Seungryong Kim ⋅ Saining Xie ⋅ Sainan Liu  
   [arXiv:2603.22275](https://arxiv.org/abs/2603.22275) · [project](https://cvlab-kaist.github.io/GLD/)
91. **ReTarget: Representation Transformation via Adversarial Regularization for Geometric Misalignment**  
   Jia-You Chen ⋅ Shang-Tse Chen
92. **Rolling Shutter Camera Self-Calibration**  
   Yongcong Zhang ⋅ Navid Rabbani ⋅ Bangyan Liao ⋅ Chengbo Wang ⋅ Yizhen Lao ⋅ Adrien Bartoli  
   [arXiv:2608.01509](https://arxiv.org/abs/2608.01509)
93. **RoMa v2: Harder Better Faster Denser Feature Matching**  
   Johan Edstedt ⋅ David Nordström ⋅ Yushan Zhang ⋅ Georg Bökman ⋅ Jonathan Astermark ⋅ Viktor Larsson ⋅ Anders Heyden ⋅ Fredrik Kahl ⋅ Mårten Wadenbäck ⋅ Michael Felsberg  
   [arXiv:2511.15706](https://arxiv.org/abs/2511.15706) · [code](https://github.com/Parskatt/romav2)
94. **Scaling Dense Prediction with Latent Decoding**  
   Xiaoyang Wu ⋅ Yixing Lao ⋅ Chengyao Wang ⋅ Senqiao Yang ⋅ Yujia Zhang ⋅ Hengshuang ZHAO
95. **Sector-Level Cross-View Geo-Localization with Implicit Orientation via Azimuthal Scanning**  
   Yiru Li ⋅ Le Wu ⋅ Yingchen Tan ⋅ Yingying Zhu
96. **SeeClear: Reliable Transparent Object Depth Estimation via Generative Opacification**  
   Xiaoying Wang ⋅ Yumeng He ⋅ Jingkai Shi ⋅ Jiayin Lu ⋅ Yin Yang ⋅ Ying Jiang ⋅ Chenfanfu Jiang  
   [arXiv:2603.19547](https://arxiv.org/abs/2603.19547) · [project](https://heyumeng.com/SeeClear-web/)
97. **Segmentation-Guided Homography Estimation for Long-Term Planar Tracking**  
   Jonáš Šerých ⋅ Jiri Matas
98. **SemLight: Distilled Semantic–Geometric Fusion for Efficient Local Feature Matching**  
   Guanglu Shi ⋅ Xiangzeng Liu ⋅ Yunan LI ⋅ Tuo Pang ⋅ Qiguang Miao
99. **Sequential Visual Place Recognition: Exploiting Trajectory Priors for Robust Localization**  
   Dominik Kloepfer ⋅ Patrick Wenzel
100. **SOCO: Benchmarking Semantic Object Correspondence in Vision Foundation Models**  
   Olaf Dünkel ⋅ Basavaraj Sunagad ⋅ Haoran Wang ⋅ David Hoffmann ⋅ Christian Theobalt ⋅ Adam Kortylewski  
   [arXiv:2605.31597](https://arxiv.org/abs/2605.31597) · [project](https://genintel.github.io/SOCO/)
101. **Spatial-TTT: Streaming Visual-based Spatial Intelligence with Test-Time Training**  
   FANGFU LIU ⋅ Diankun Wu ⋅ Jiawei Chi ⋅ Yimo Cai ⋅ Yi-Hsin Hung ⋅ Xumin Yu ⋅ Hao Li ⋅ Han Hu ⋅ Yongming Rao ⋅ Yueqi Duan  
   [arXiv:2603.12255](https://arxiv.org/abs/2603.12255) · [project](https://liuff19.github.io/Spatial-TTT)
102. **Stable and Scalable Bundle Adjustment of Holistic 3D Structures**  
   Shaohui Liu ⋅ Rémi Pautrat ⋅ Daniel Barath ⋅ Richard Hartley ⋅ Viktor Larsson ⋅ Marc Pollefeys
103. **Stand Up and Move: Benchmarking Interactive Spatial Intelligence in WalkerBench**  
   Zhiqi Ge ⋅ Gang Yang ⋅ Ziyang Pan ⋅ Jingzhe Zhu ⋅ Yuancheng Gu ⋅ Juncheng Li ⋅ Qizhou Wang ⋅ Rui Tang ⋅ Siliang Tang ⋅ Jun Xiao ⋅ Yueting Zhuang
104. **StereoEdit: A Diffusion-Based Framework for Stereo-Consistent Image Editing**  
   Baolin Liu ⋅ Zongyuan Yang ⋅ Yingde Song ⋅ yongping xiong
105. **StereoGS: Sparse-View 3D Gaussian Splatting via Stereo Priors**  
   Wenhao Yuan ⋅ Yiyuan Ge ⋅ Deli Cai  
   [arXiv:2606.30545](https://arxiv.org/abs/2606.30545) · [project](https://stringerywh00.github.io/StereoGS_project_page/)
106. **Stream3D-VLM: Online 3D Spatial Understanding with Incremental Geometry Priors**  
   Hanxun Yu ⋅ Xuan Qu ⋅ Lei Ke ⋅ Boqiang Zhang ⋅ YUXIN WANG ⋅ Jianke Zhu ⋅ Dong Yu  
   [arXiv:2606.06891](https://arxiv.org/abs/2606.06891) · [project](https://stream3d-vlm.github.io/)
107. **Text-Guided 6D Object Pose Rearrangement via Closed-Loop VLM Agents**  
   Sangwon Baik ⋅ Gunhee Kim ⋅ Mingi Choi ⋅ Hanbyul Joo  
   [arXiv:2604.09781](https://arxiv.org/abs/2604.09781)
108. **Towards Geometry-Grounded Dense Semantic Matching with VGGT Priors**  
   Songlin Yang ⋅ Tianyi Wei ⋅ Yushi Lan ⋅ Zeqi Xiao ⋅ Anyi Rao ⋅ Xingang Pan  
   [arXiv:2509.21263](https://arxiv.org/abs/2509.21263)
109. **Towards Interactive Global Geolocation Assistant**  
   Zhiyang Dou ⋅ Zipeng Wang ⋅ Xumeng Han ⋅ Guorong Li ⋅ Zhenjun Han ⋅ Zhipei Huang  
   [arXiv:2412.08907](https://arxiv.org/abs/2412.08907)
110. **Towards Spatial Supersensing in the Wild**  
   Tianjun Gu ⋅ Tianyu Xin ⋅ Kuan Zhang ⋅ Bowen Yang ⋅ Yinan Han ⋅ Peize Li ⋅ Yucheng Lu ⋅ Jianhang Liu ⋅ Xinran Zhang ⋅ KOK CHUNG CHUA ⋅ Qiyue Zhao ⋅ Qinlei Xie ⋅ Yupeng Chen ⋅ Marco Pavone ⋅ Yiming Li  
   [arXiv:2607.13681](https://arxiv.org/abs/2607.13681) · [project](https://vsi-super-wild.github.io/)
111. **Trajectory-aware Cross-view Geo-Localization with Sequential Observations**  
   Tianyi Gao ⋅ Jiayu Lin ⋅ Danielle Beaulieu ⋅ Nathan Jacobs  
   [arXiv:2607.15491](https://arxiv.org/abs/2607.15491) · [project](https://humblegamer.github.io/trajloc/)
112. **Triangular Consistency as a Universal Constraint for Learning Optical Flow**  
   Yi Xiao ⋅ Carlos Coronel ⋅ Jing Zhan ⋅ Haniyeh Oskouie ⋅ Alex Wong ⋅ DONG LAO  
   [arXiv:2606.19938](https://arxiv.org/abs/2606.19938)
113. **TriMotion: Modality-Agnostic Camera Control for Video Generation**  
   Seunghyun Shin ⋅ Song Jifei ⋅ Wooseok Jeon ⋅ Hae-Gon Jeon ⋅ Jiankang Deng  
   [arXiv:2606.20774](https://arxiv.org/abs/2606.20774)
114. **Understanding the Impact of Geometric Foundation Models on Vision-Language-Action Models**  
   Yurou Yang ⋅ Muyuan Lin ⋅ Roberto Martín-Martín ⋅ Labrie Martin ⋅ Shreekant Gayaka ⋅ Cheng-Hao Kuo ⋅ Luca Carlone  
   [arXiv:2605.24642](https://arxiv.org/abs/2605.24642)
115. **Unfold The World: Factorize 4D Properties in Reinforcing Spatial Understanding**  
   Yijun Yang ⋅ Shenghe Zheng ⋅ Wenbo Li ⋅ Jianhui Liu ⋅ Haoze Sun ⋅ Yanbing Zhang ⋅ Jiaxiu Jiang ⋅ Lin Song ⋅ Haoyang Huang ⋅ Nan Duan ⋅ Lei Zhu
116. **Unified and Efficient Point-Line Local Features**  
   François Costa ⋅ Raphael Kreft ⋅ Felix Möller ⋅ Hardik Shah ⋅ Ramanathan Rajaraman ⋅ Eckhard Goedeke ⋅ Shaohui Liu ⋅ Rémi Pautrat ⋅ Marc Pollefeys
117. **Unified Video Dense Prediction from Disjoint Data**  
   Yihong Sun ⋅ Seoung Wug Oh ⋅ Jiahui Huang ⋅ Bharath Hariharan ⋅ Joon-Young Lee  
   [arXiv:2607.21592](https://arxiv.org/abs/2607.21592) · [project](https://unid-video.github.io/)
118. **UniPR-3D: Towards Universal Visual Place Recognition with Visual Geometry Grounded Transformer**  
   Tianchen Deng ⋅ Chen Xun ⋅ Ziming Li ⋅ Hongming Shen ⋅ Shuhao Zhai ⋅ Danwei Wang ⋅ Javier Civera ⋅ Hesheng Wang  
   [arXiv:2512.21078](https://arxiv.org/abs/2512.21078) · [code](https://github.com/dtc111111/UniPR-3D)
119. **UniStitch: Unifying Semantic and Geometric Features for Image Stitching**  
   Yuan Mei ⋅ Lang Nie ⋅ Kang Liao ⋅ Yunqiu Xu ⋅ Chunyu Lin ⋅ Bin Xiao  
   [arXiv:2603.10568](https://arxiv.org/abs/2603.10568) · [project](http://mmelodyy.github.io/projects/unistitch)
120. **VectorReLoc: Reliable Vectorized SD Map Visual Re-localization with Contrastive Feature Alignment**  
   Ziming Liu ⋅ Quanjie Xiang ⋅ Wang yun ⋅ wang yiting ⋅ chao wen ⋅ Zhuanjian XU ⋅ Leichen Wang ⋅ HAO SUN ⋅ Guangyu Gao
121. **ViewSpatial-Bench: Evaluating Multi-perspective Spatial Localization in Vision-Language Models**  
   Dingming Li ⋅ Hongxing Li ⋅ Zixuan Wang ⋅ Yuchen Yan ⋅ Hang Zhang ⋅ Siqi Chen ⋅ Guiyang Hou ⋅ Shengpei Jiang ⋅ Wenqi Zhang ⋅ Jun Xiao ⋅ Weiming Lu ⋅ Yueting Zhuang  
   [arXiv:2505.21500](https://arxiv.org/abs/2505.21500) · [project](https://zju-real.github.io/ViewSpatial-Page/)
122. **Visual Spatial Tuning**  
   Rui Yang ⋅ ziyu zhu ⋅ Yanwei Li ⋅ Jingjia Huang ⋅ Shen Yan ⋅ Siyuan Zhou ⋅ Zhe Liu ⋅ Xiangtai Li ⋅ Shuangye Li ⋅ Wenqian Wang ⋅ Yi Lin ⋅ Hengshuang ZHAO  
   [arXiv:2511.05491](https://arxiv.org/abs/2511.05491)
123. **Vulnerability of Privacy-Preserving Visual Localization against Diffusion-based Attacks**  
   Maxime Pietrantoni ⋅ Torsten Sattler ⋅ Gabriela Csurka
124. **WAFT-Stereo: Warping-Alone Field Transforms for Stereo Matching**  
   Yihan Wang ⋅ Jia Deng  
   [arXiv:2603.24836](https://arxiv.org/abs/2603.24836) · [code](https://github.com/princeton-vl/WAFT-Stereo)
125. **Warp-free Cross-view Geo-localization via Feature-space Consensus Mining**  
   Zhuo Song ⋅ Lian Xu ⋅ Runqing Jiang ⋅ Kunhong Li ⋅ Yongjian Zhang ⋅ Ye Zhang ⋅ Yulan Guo  
   [arXiv:2608.09321](https://arxiv.org/abs/2608.09321)
126. **When Cars Have Stereotypes: Auditing Demographic Bias in Objects from Text-to-Image Models**  
   Dasol Choi ⋅ Jihwan Lee ⋅ Minjae Lee ⋅ Minsuk Kahng  
   [arXiv:2508.03483](https://arxiv.org/abs/2508.03483)
127. **WiFlow: Estimating Optical Flow using WiFi Channel State Information**  
   Thomas Weigel ⋅ Simon Kiefhaber ⋅ Fabian Portner ⋅ Matthias Hollick ⋅ Simone Schaub-Meyer
128. **Zero-shot Depth from Defocus**  
   Yiming Zuo ⋅ Hongyu Wen ⋅ Venkat Subramanian ⋅ Patrick Chen ⋅ Karhan Kayan ⋅ Mario Bijelic ⋅ Felix Heide ⋅ Jia Deng  
   [arXiv:2603.26658](https://arxiv.org/abs/2603.26658) · [code](https://github.com/princeton-vl/FOSSA) · [project](https://zedd.cs.princeton.edu)
129. **ZipDepth: Bringing Lightweight Zero-Shot Monocular Depth Anywhere, on Any Device**  
   Fabio Tosi ⋅ Luca Bartolomei ⋅ Matteo Poggi ⋅ Stefano Mattoccia  
   [arXiv:2607.08771](https://arxiv.org/abs/2607.08771) · [code](https://github.com/fabiotosi92/ZipDepth) · [project](https://zipdepth.github.io/)

## Point Cloud & 3D Perception

*57 papers · 31 with links*

1. **Adaptive Neural Dynamics for Robust Geometric LiDAR-Inertial State Estimation on UAVs**  
   Sitian Peng ⋅ Rui Wang
2. **Analytic Bayesian Uncertainty for LiDAR Segmentation: A Single-pass Generative Approach**  
   Hanieh Shojaei Miandashti ⋅ Qianqian Zou ⋅ Claus Brenner
3. **BitRIC: Efficient Neural Compression of LiDAR Range Images via Hierarchical Bitplanes**  
   Kang You ⋅ Tong Chen ⋅ Dandan Ding ⋅ M. Salman Asif ⋅ Zhan Ma
4. **CascadeProto: Cascaded Cross-Modal Prototype Purification via Entropy-Aware Learning for Few-Shot 3D Point Cloud Segmentation**  
   Changshuo Wang ⋅ Weijun Li ⋅ Fan Mo ⋅ Zhonghang Liu ⋅ Shuting He ⋅ Prayag Tiwari ⋅ Dimitrios Kanoulas
5. **DeGuNet: Depth-Guided Ultra-Compact Backbones for Efficient LiDAR-Camera 3D Detection**  
   haifa zhang ⋅ Yijing Wang ⋅ Peixi Peng ⋅ Zhiqiang Zuo  
   [arXiv:2607.12419](https://arxiv.org/abs/2607.12419)
6. **Delaunay Canopy: Building Wireframe Reconstruction from Airborne LiDAR Point Clouds via Delaunay Graph**  
   Donghyun Kim ⋅ Chanyoung Kim ⋅ YoungJoong Kwon ⋅ Seong Jae Hwang  
   [arXiv:2604.02497](https://arxiv.org/abs/2604.02497)
7. **DepWorldSG: Depth-Aware 3D Semantic Scene Graph Generation via World-Model Priors**  
   Seok-Young Kim ⋅ Abdelrahman Elskhawy ⋅ TAEWOOK HA ⋅ Dooyoung Kim ⋅ Eunjae Shin ⋅ Benjamin Busam ⋅ Woontack Woo
8. **Don’t Starve the Boundaries: Boundary-Constrained Label Propagation for Weakly Supervised 3D Segmentation**  
   Shuwei Wu ⋅ shuo jin ⋅ Zhijin He ⋅ Siyue Yu ⋅ ENG LIM ⋅ Qiufeng Wang ⋅ Jimin Xiao
9. **DRS-VPT: Directly Re-localizing in Scenes using a Vision and Point Transformer**  
   Lanke Fu ⋅ Maurice Fallon
10. **ESNE: Efficient Surface Normal Estimation for LiDAR Point Clouds with Sequential Modeling and Variability Guidance**  
   Kohei Matsuzaki ⋅ Keisuke Nonaka
11. **Event-LiDAR: 3D Eventification for Efficient Point Cloud Processing**  
   Masatoshi Murakami ⋅ Eisho Tsuji ⋅ Ken Sakurada
12. **Ex-Sim(3)-Reg: 2D-3D Correspondence Pruning via Extended Sim(3) Registration**  
   Pei An ⋅ Muyao Peng ⋅ Junfeng Ding ⋅ Jiaqi Yang ⋅ Liangliang Nan
13. **G2P: Gaussian-to-Point Attribute Alignment for Boundary-Aware 3D Segmentation**  
   Hojun Song ⋅ Chae-yeong Song ⋅ Jeong-hun Hong ⋅ chaewon moon ⋅ Soo Ye Kim ⋅ Yiyi Liao ⋅ Jaehyup Lee ⋅ Sang-hyo Park  
   [arXiv:2601.03510](https://arxiv.org/abs/2601.03510)
14. **Graph-GSReg: Leveraging 3D Scene Graphs for Gaussian Splatting Registration**  
   Jaewon Lee ⋅ Mangyu Kong ⋅ Euntai Kim  
   [arXiv:2606.29782](https://arxiv.org/abs/2606.29782)
15. **GraphCPD: Coherent Point Drift for Point Cloud Registration via Graph Signal Processing**  
   Yingcheng Lai ⋅ Xingjian Wang ⋅ Li Chai
16. **GridFlow: Structured Latent Flow for Seamless City-Scale 3D Point Cloud Generation**  
   Xinyu Wang ⋅ Muhammad Ibrahim ⋅ Atif Mansoor ⋅ Ajmal Mian
17. **HHA: Hierarchical Hyperbolic Constraints for Imperceptible Point Cloud Attacks**  
   Keke Tang ⋅ Yu Liao ⋅ Weilong Peng ⋅ Xiaofei Wang ⋅ Daizong Liu ⋅ Zhongyun Hua ⋅ Peican Zhu ⋅ Zhihong Tian
18. **InSeg: Interactive Refinement via Intent Propagation for Point Cloud Semantic Segmentation**  
   Yudong Liu ⋅ Yunfei Li ⋅ Ge Gao ⋅ Han Huang ⋅ Ming Gu
19. **LeAD-M3D: Leveraging Asymmetric Distillation for Real-Time Monocular 3D Detection**  
   Johannes Meier ⋅ Jonathan Michel ⋅ Oussema Dhaouadi ⋅ Yung-Hsu Yang ⋅ Christoph Reich ⋅ Zuria Bauer ⋅ Stefan Roth ⋅ Marc Pollefeys ⋅ Jacques Kaiser ⋅ Daniel Cremers  
   [arXiv:2512.05663](https://arxiv.org/abs/2512.05663) · [project](https://deepscenario.github.io/LeAD-M3D/)
20. **Learning 1-Bit LiDAR-based Localization with Auxiliary Objective**  
   Kaijie Yin ⋅ Zhiyuan Zhang ⋅ Tian Gao ⋅ Wentao Zhu ⋅ Cheng-zhong Xu ⋅ Hui Kong  
   [arXiv:2606.27729](https://arxiv.org/abs/2606.27729)
21. **Learning Manifolds in High-D Point Embedding for Anisotropic Surface Approximation from Unstructured Point Clouds**  
   Hongbo Li ⋅ Haikuan Zhu ⋅ Xiaohu Guo ⋅ Wenping Wang ⋅ Jing Hua ⋅ Zichun Zhong  
   [arXiv:2607.28855](https://arxiv.org/abs/2607.28855)
22. **Learning to Suppress SPAD-based LiDAR Flare**  
   Xuanya Zhu ⋅ Linghao Shen  
   [arXiv:2607.03247](https://arxiv.org/abs/2607.03247)
23. **Learning to Tessellate: Point Cloud Generation via Recursive Spectral Partitioning**  
   Monan Sun ⋅ Bangzhen Liu ⋅ Huaidong Zhang ⋅ Shengfeng He  
   [arXiv:2608.02432](https://arxiv.org/abs/2608.02432) · [code](https://huggingface.co/Mo-nan/PointRSP)
24. **LESV:Language Embedded Sparse Voxel Fusion for Open-Vocabulary 3D Scene Understanding**  
   Fusang WANG ⋅ Nathan Piasco ⋅ Moussab Bennehar ⋅ Luis G Roldao Jimenez ⋅ Dzmitry Tsishkou ⋅ Fabien Moutarde  
   [arXiv:2604.01388](https://arxiv.org/abs/2604.01388)
25. **Markov-Renewal Single-Photon LiDAR Simulator**  
   Weijian Zhang ⋅ PRATEEK CHENNURI ⋅ Hashan Weerasooriya ⋅ Bole Ma ⋅ Stanley Chan  
   [arXiv:2512.04924](https://arxiv.org/abs/2512.04924)
26. **MASS: Motion-Aligned Selective Scan for Flow-Based Video Frame Interpolation**  
   Jun-Sang YOO ⋅ Seung-Won Jung
27. **Memory Tree Guided Key Frame Querying for Efficient 3D Question Answering**  
   Hsiang-Wei Huang ⋅ Fu-Chen Chen ⋅ Li-Wu Tsao ⋅ Cheng-Han Lee ⋅ Che-Chun Su ⋅ Lu Xia ⋅ Ronghui Peng ⋅ Jenq-Neng Hwang ⋅ Min Sun ⋅ Cheng-Hao Kuo
28. **NegROI: Click-Centric Uncertainty-Guided Refinement with Scene-Conditioned Negative Prompts for Robust Interactive 3D Segmentation**  
   shuheng zhang ⋅ Feng Wu  
   [arXiv:2607.05955](https://arxiv.org/abs/2607.05955)
29. **NoPA: Non-Parametric Online 3D Scene Graph Generation**  
   Qi Xun Yeo ⋅ Seungjun Lee ⋅ Yan Li ⋅ Gim Hee Lee  
   [arXiv:2607.00529](https://arxiv.org/abs/2607.00529)
30. **OCA: ODE-Driven Cross-Attention for Image-to-Point-Cloud Registration**  
   Pei An ⋅ Jiaqi Yang ⋅ Yulong Wang ⋅ Quan Siwen ⋅ Liangliang Nan
31. **PGCR: Pose–Geometry Coupled Reasoning for Image-to-Point Cloud Registration**  
   Xinjun Li ⋅ Wenfei Yang ⋅ Yihan Chen ⋅ Zhixin Cheng ⋅ Shifeng Zhang ⋅ Xu Zhou ⋅ Tianzhu Zhang
32. **PrintAnything: Learning Geometric Plan Map for 3D Printing G-code Generation from Unoriented Point Clouds**  
   Sangmin Hong ⋅ Daniel Sungho Jung ⋅ Heewon Kim ⋅ Kyoung Mu Lee
33. **Progressive and Localized Super-Resolution of 3D Objects via Localized Latent Voxel Diffusion**  
   Yuxin Liu ⋅ Minshan Xie ⋅ Jiawen Liang ⋅ Runsong Zhu ⋅ Chi-Wing Fu ⋅ Tien-Tsin Wong
34. **PUF: Plug-and-Play Uncertainty-Aware Fusion for Online 3D Scene Graph Generation**  
   Yi Yang ⋅ Myrna Castillo Silva ⋅ Bodo Rosenhahn ⋅ Michael Yang  
   [arXiv:2607.07170](https://arxiv.org/abs/2607.07170) · [code](https://github.com/yyyyangyi/PUF)
35. **RadarGen: Automotive Radar Point Cloud Generation from Cameras**  
   Tomer Borreda ⋅ Fangqiang Ding ⋅ Sanja Fidler ⋅ Shengyu Huang ⋅ Or Litany  
   [arXiv:2512.17897](https://arxiv.org/abs/2512.17897) · [project](https://radargen.github.io/)
36. **RAG-3DSG: Enhancing 3D Scene Graphs with Re-Shot Guided Retrieval-Augmented Generation**  
   Yue Chang ⋅ Rufeng Chen ⋅ Zhaofan ZHANG ⋅ Yi Chen ⋅ Yifan Tian ⋅ Sihong Xie  
   [arXiv:2601.10168](https://arxiv.org/abs/2601.10168)
37. **RBE-Flow:Recurrent Bayesian Estimation on Feature Manifolds for Cross-Modal Registration**  
   Mengzhu Ding ⋅ Xin Song ⋅ Xiaoke Ding ⋅ Hongwei Ding ⋅ Xuecong Liu  
   [arXiv:2606.30492](https://arxiv.org/abs/2606.30492) · [code](https://github.com/NEU-Liuxuecong/RBE-Flow)
38. **ReCamDriving: LiDAR-Free Camera-Controlled Video Synthesis for Novel Trajectories**  
   Yaokun li ⋅ Shuaixian Wang ⋅ Mantang GUO ⋅ Jiehui Huang ⋅ Taojun Ding ⋅ Mu Hu ⋅ Kaixuan Wang ⋅ Shaojie Shen ⋅ Guang Tan  
   [arXiv:2512.03621](https://arxiv.org/abs/2512.03621) · [project](https://recamdriving.github.io/)
39. **RECO: Region-Aware Compensation for Extrinsic Perturbations in Roadside 3D Detection**  
   Junsheng Du ⋅ Yuhuan Lu ⋅ Zhaocheng He  
   [arXiv:2607.20947](https://arxiv.org/abs/2607.20947)
40. **RegHead: Non-Humanoid Head Blendshapes via Feed-Forward Registration**  
   Jiahao Luo ⋅ Hao Zhang ⋅ Jianqi Chen ⋅ Yijie He ⋅ Jiaxu Zou ⋅ Michael Vasilkovsky ⋅ Sergei Korolev ⋅ Sergey Tulyakov ⋅ Chaoyang Wang ⋅ Peter Wonka ⋅ James Davis ⋅ Jian Wang  
   [arXiv:2607.12206](https://arxiv.org/abs/2607.12206) · [project](https://snap-research.github.io/RegHead/)
41. **Register Any Point: Scaling 3D Point Cloud Registration by Flow Matching**  
   Yue Pan ⋅ Tao Sun ⋅ Liyuan Zhu ⋅ Lucas Nunes ⋅ Iro Armeni ⋅ Jens Behley ⋅ Cyrill Stachniss  
   [arXiv:2512.01850](https://arxiv.org/abs/2512.01850) · [code](https://github.com/PRBonn/RAP)
42. **RePL: Pseudo-label Refinement for Semi-supervised LiDAR Semantic Segmentation**  
   Donghyeon Kwon ⋅ Taegyu Park ⋅ Suha Kwak  
   [arXiv:2604.06825](https://arxiv.org/abs/2604.06825)
43. **SHReg: Strictly Rotation-Equivariant Point Cloud Registration via Spherical Harmonics**  
   Chongjian Wang ⋅ Junjie Gao  
   [arXiv:2607.23096](https://arxiv.org/abs/2607.23096)
44. **Structured SIR: Efficient and Expressive Importance-Weighted Inference for High-Dimensional Image Registration**  
   Ivor Simpson ⋅ Neill Campbell  
   [arXiv:2603.17415](https://arxiv.org/abs/2603.17415)
45. **SuperFlex: Deformable Superquadrics for Point Cloud Decomposition**  
   Gabriel Tavernini ⋅ Elisabetta Fedele ⋅ Tiago Novello ⋅ Leonidas Guibas ⋅ Marc Pollefeys ⋅ Francis Engelmann  
   [arXiv:2607.01015](https://arxiv.org/abs/2607.01015) · [project](https://superflex3d.github.io)
46. **SV-TAD: Native Sparse Convolutions for Efficient Temporal Action Detection**  
   Ricardo Ignacio Pizarro Carreño ⋅ Roberto Valle ⋅ José Buenaposada ⋅ Luis M. Bergasa ⋅ Luis Baumela
47. **SynFlow: Scaling Up LiDAR Scene Flow Estimation with Synthetic Data**  
   Qingwen Zhang ⋅ Xiaomeng Zhu ⋅ ChenHan Jiang ⋅ Patric Jensfelt  
   [arXiv:2604.09411](https://arxiv.org/abs/2604.09411) · [project](https://kin-zhang.github.io/SynFlow)
48. **Think While You Map: Asynchronous Vision-Language Agents for Incremental 3D Scene Graphs**  
   Deniz Bickici ⋅ Michael Pabst ⋅ Shohei Mori ⋅ Dieter Schmalstieg  
   [arXiv:2606.31471](https://arxiv.org/abs/2606.31471) · [project](https://denizbickici.github.io/thinkgraphs/)
49. **Towards Practical Lossless Neural Compression for LiDAR Point Clouds**  
   pengpeng yu ⋅ Haoran Li ⋅ Runqing Jiang ⋅ Dingquan Li ⋅ Jing Wang ⋅ Liang Lin ⋅ Yulan Guo  
   [arXiv:2603.25260](https://arxiv.org/abs/2603.25260) · [code](https://github.com/pengpeng-yu/FastPCC)
50. **Tri-Efficient Transfer Learning for Point Cloud Videos**  
   Yiding Sun ⋅ Dongxu Zhang ⋅ Jihua Zhu ⋅ Haozhe Cheng ⋅ Zhengqiao Li ⋅ Pengcheng Li ⋅ Chaowei Fang ⋅ Yonghao Dong ⋅ Lin Chen  
   [arXiv:2606.24175](https://arxiv.org/abs/2606.24175)
51. **Two-Parameter Flow Map Learning for Continuous-Time Diffeomorphic Image Registration**  
   Mohammadjavad Matinkia ⋅ Nilanjan Ray
52. **Uncertainty-Driven Gaussian Sphere Propagation for 3D Semantic Segmentation**  
   Zhicheng Yan ⋅ Qingyong Li ⋅ Yixiao Song ⋅ Wen Wang
53. **Unsupervised Point Cloud Registration via Training-Time Semantic Guidance**  
   Kezheng Xiong ⋅ Shiyun Xu ⋅ Sheng Ao ⋅ Siqi Shen ⋅ Cheng Wang ⋅ Chenglu Wen
54. **VoxAnchor: Explicit Voxel-Semantic Grounding for Spatial Understanding in Videos**  
   Xinglin Li ⋅ TingTing Long ⋅ Jingzhi Zhou ⋅ Chuxuan Zeng ⋅ Jiajing Chen ⋅ Jian Yang ⋅ Jin Xie
55. **When the City Teaches the Car: Label-Free 3D Perception from Infrastructure**  
   ZHEN XU ⋅ Jinsu Yoo ⋅ Cristian Bautista ⋅ Zanming Huang ⋅ Tai-Yu Pan ⋅ Zhenzhen Liu ⋅ Katie Luo ⋅ Mark Campbell ⋅ Bharath Hariharan ⋅ Wei-Lun Chao  
   [arXiv:2603.16742](https://arxiv.org/abs/2603.16742) · [project](https://jinsuyoo.info/civet/)
56. **White Aggregation and Restoration for Few-shot 3D Point Cloud Semantic Segmentation**  
   Jiyun Im ⋅ SuBeen Lee ⋅ Miso Lee ⋅ Jae-Pil Heo  
   [arXiv:2509.13907](https://arxiv.org/abs/2509.13907) · [code](https://github.com/JiyunIm00/WARM.git)
57. **XPos3R: Cross-Modal Transformer for Intraoperative 2D/3D Registration**  
   Shiyan Su ⋅ Ruyi Zha ⋅ HONGDONG LI ⋅ Xuelian Cheng ⋅ Zongyuan Ge

## Computational Imaging & Novel Sensors

*27 papers · 8 with links*

1. **340 FPS Reflection-free Video from Spikes Modulated by a Rapidly Rotating Polarizer**  
   Lishuai Huang ⋅ Yeliduosi Xiaokaiti ⋅ Youwei Lyu ⋅ Langyue Chang ⋅ Boxin Shi ⋅ Shikui Wei ⋅ Yao Zhao ⋅ Meng Jian ⋅ Yashen Wang ⋅ Yakun Chang
2. **Broadband Wide Field of View Imaging with Computational Mirrors**  
   Vishwanath Saragadam ⋅ Niki Nezakati ⋅ Amit Roy-Chowdhury ⋅ Vivek Boominathan  
   [arXiv:2605.00029](https://arxiv.org/abs/2605.00029)
3. **CLDefocus: Physically Grounded Compound-Lens Defocus Blur Synthesis**  
   Yunkyu Lee ⋅ Woohyeok Kim ⋅ Sunghyun Cho
4. **D3F-IR: Dual-Domain Deterministic Flow Matching for Visible-to-Infrared Translation**  
   Peiyi Zeng ⋅ Diedong Feng ⋅ Zhen Liu ⋅ Zhenming Peng ⋅ Bing Zeng ⋅ Shuaicheng Liu
5. **Degradation-Robust and Temporally Consistent Infrared–Visible Video Fusion via One-step Diffusion Framework**  
   Songcheng Du ⋅ HaoYuan Xu ⋅ Xingyuan Li ⋅ Yang Zou ⋅ Jinyuan Liu ⋅ YUNPENG BAI ⋅ Ying Li
6. **DualResPS: Dual-Resolution Photometric Stereo Using a Frame-Event Hybrid Camera**  
   Haotian Zhuang ⋅ Bohan Yu ⋅ Zhuofeng Wang ⋅ Boxin Shi
7. **E-VLA: Event-Augmented Vision-Language-Action Model for Dark and Blurred Scenes**  
   Jiajun Zhai ⋅ Hao Shi ⋅ Shangwei Guo ⋅ Kailun Yang ⋅ Kaiwei Wang  
   [arXiv:2604.04834](https://arxiv.org/abs/2604.04834) · [code](https://github.com/JJayzee/E-VLA)
8. **EvDiff: High Quality Video with an Event Camera**  
   Weilun Li ⋅ Lei Sun ⋅ Ruixi Gao ⋅ Qi Jiang ⋅ Yuqin Ma ⋅ Kaiwei Wang ⋅ Ming-Hsuan Yang ⋅ Luc Van Gool ⋅ Danda Paudel
9. **EVEE: Event-Based Online Adaptation for Matching on Unknown Targets**  
   Zejing Zhao ⋅ Cheng Ju ⋅ Yanwen Zhang ⋅ Akio NAMIKI
10. **Event-based Sparse-view Background-Oriented Schlieren Tomography**  
   Xinyu Zhou ⋅ Shihao Hu ⋅ Peiqi Duan ⋅ Chao Xu ⋅ Boxin Shi
11. **EventSpecPS: Photometric Stereo with Multispectral Reflectance Using an Event Camera**  
   Jingqian Wu ⋅ Bohan Yu ⋅ Jun Hoong Chan ⋅ Edmund Lam ⋅ Boxin Shi
12. **EVKit: An Open-source Flexible Toolkit for Efficient Event Camera Data Storage and Loading**  
   Yilun Wu ⋅ Guido De Croon
13. **From Noise to Events: Conditional Diffusion for Event Data Augmentation**  
   Ruofei Wang ⋅ Ziyuan Luo ⋅ Peiqi Duan ⋅ Xiufeng HUANG ⋅ Boxin Shi ⋅ Renjie Wan
14. **Hybrid Event–Frame Sensors: Modeling, Calibration, and Simulation**  
   yunfan lu ⋅ Nico Messikommer ⋅ Xiaogang Xu ⋅ Liming Chen ⋅ Yuhan Chen ⋅ Nikola Zubic ⋅ Davide Scaramuzza ⋅ Hui Xiong  
   [arXiv:2511.18037](https://arxiv.org/abs/2511.18037)
15. **MAVFusion: Efficient Infrared and Visible Video Fusion via Motion-Aware Sparse Interaction**  
   Xilai Li ⋅ Weijun Jiang ⋅ Xiaosong Li ⋅ Yang Liu ⋅ Hongbin Wang ⋅ Tao Ye ⋅ Huafeng Li ⋅ Haishu Tan  
   [arXiv:2604.01958](https://arxiv.org/abs/2604.01958) · [code](https://github.com/ixilai/MAVFusion)
16. **NeLU3D: Neural Inverse Structured Light without Modeling the Projector**  
   Giancarlo Pereira ⋅ David Fouhey ⋅ Claudio Silva ⋅ Daniele Panozzo
17. **Physics-Guided Deep Learning for Linear Mueller Matrix Acquisition**  
   Yuan Liang ⋅ Shaoli Liu ⋅ Jiachun Huang
18. **Pol-CACTI: A System and dataset forHigh-Speed Polarized Video Compressive Imaging**  
   Yunfeng Song ⋅ Yidong Luo ⋅ Ping Wang ⋅ xingjian jiang ⋅ Xin Yuan
19. **Poppy: Polarization-Based Plug-and-Play Guidance for Enhancing Surface Normal Estimation**  
   Irene Kim ⋅ Sai Tanmay Reddy Chakkera ⋅ Alexandros Graikos ⋅ Dimitris Samaras ⋅ Akshat Dave  
   [arXiv:2603.27891](https://arxiv.org/abs/2603.27891) · [project](https://irnkim.github.io/poppy/)
20. **Provable and Robust Wavefront Sensing via Self-Reference Interferometry**  
   Nebiyou Yismaw ⋅ Vishwanath Saragadam ⋅ Aswin C. Sankaranarayanan ⋅ M. Salman Asif  
   [arXiv:2604.03564](https://arxiv.org/abs/2604.03564)
21. **REALM: An RGB and Event Aligned Latent Manifold for Cross-Modal Perception**  
   Vincenzo Polizzi ⋅ David Lindell ⋅ Jonathan Kelly
22. **Rethinking IRSTD: Single-Point Supervision Guided Encoder-only Framework is Enough for Infrared Small Target Detection**  
   Rixiang Ni ⋅ Boyang Li ⋅ Chen Jun ⋅ Zhijie Chen ⋅ Feiyu Ren ⋅ Yuji Wang ⋅ Haoyang Yuan ⋅ Wujiao He ⋅ Wei An  
   [arXiv:2604.05363](https://arxiv.org/abs/2604.05363) · [code](https://github.com/NIRIXIANG/SPIRE-IRSTD)
23. **SAFER-Activities: A Dataset for Smart Assessment of Fall Events and Routine Activities**  
   Diwas Lamsal ⋅ Pramod Wickramatilake ⋅ Jednipat Moonrinta ⋅ Mongkol Ekpanyapong ⋅ Matthew Dailey
24. **Stokes-Informed Diffusion for Robust Linear Polarization Estimation**  
   Yidong Luo ⋅ Chenggong Li ⋅ Yuchao Feng ⋅ Boxin Shi ⋅ Junchao Zhang ⋅ Xin Yuan  
   [arXiv:2607.21239](https://arxiv.org/abs/2607.21239)
25. **Two-Way Street: Efficient VSLAM using Collaborative In-Sensor and Off-Sensor processing**  
   Hongyi Zhang ⋅ Laurie Bose ⋅ Piotr Dudek ⋅ Walterio Mayol-Cuevas
26. **Unwarping the Lens: A Physics-Grounded Approach to Video Glasses Removal**  
   Radim Špetlík ⋅ David Futschik ⋅ Radek Danecek ⋅ Feitong Tan ⋅ Ziqian Bai ⋅ Rohit Pandey ⋅ Yinda Zhang
27. **Video Can Teach PAN-Sharpening: PSF-Aware Cross-Domain Supervision**  
   Hyun-Ho Kim ⋅ Munchurl Kim ⋅ Jaehyup Lee

## Low-Level Vision & Image Restoration

*100 papers · 63 with links*

1. **AdaBridge-SR: Adaptive Bridge Matching for Real-World Image Super-Resolution**  
   Jiangang Wang ⋅ Shangquan Sun ⋅ Aiping Zhang ⋅ Yuning Cui ⋅ Wenqi Ren
2. **Adversarial Score Distillation for Stable One-Step Diffusion in Real-World Image Super-Resolution**  
   Wei Zhu ⋅ Kai Zhang ⋅ Yu Zheng ⋅ Lei Luo ⋅ Jian Yang
3. **Allo{SR}2: Rectifying One-Step Super-Resolution to Stay Real via Allomorphic Generative Flows**  
   Zihan Wang ⋅ XUDONG HUANG ⋅ Junbo Qiao ⋅ WEI LI ⋅ jie hu ⋅ Xinghao Chen ⋅ Shaohui Lin  
   [arXiv:2604.19238](https://arxiv.org/abs/2604.19238)
4. **ART-VSR: Adaptive Rectified Trajectories for One-Step Video Super-Resolution**  
   JianHui Zhang ⋅ Chen Fang ⋅ Wanghao Wanghao ⋅ chaoyu feng ⋅ LEI LEI ⋅ Jue Wang ⋅ Shuaicheng Liu
5. **Auto-Prompting: Layer-Specific Prompt Fusion Discovery via Differentiable Search**  
   Xi Xiao ⋅ Xingjian Li ⋅ Yunbei Zhang ⋅ Cheng Han ⋅ Tianming Liu ⋅ Tianyang Wang ⋅ Runmin Jiang ⋅ Jihun Hamm ⋅ Xiao Wang ⋅ Min Xu
6. **AVSR-Diff: Scale-Agnostic Diffusion Priors for Temporally Consistent Arbitrary-Scale Video Super-Resolution**  
   Geunhyuk Youk ⋅ Jeonghyeok Do ⋅ Dayeon Kim ⋅ Jihyong Oh ⋅ Munchurl Kim  
   [arXiv:2607.00987](https://arxiv.org/abs/2607.00987) · [project](https://kaist-viclab.github.io/AVSR-Diff/)
7. **Bayesian Self-Attention with Local Pixel Correlations for Lightweight Denoising Transformers**  
   Runyang He ⋅ Zuowei Shen ⋅ Hui JI
8. **BWAFDA: Block-wise Weighted Attention Fusion with Detail-aware for No-Reference Image Quality Assessment**  
   Shilv Cai ⋅ Jian Jin ⋅ Tianang Chen ⋅ Zhuangzi Li ⋅ Weisi Lin
9. **ClearText-Video: A Large-Scale Text-Centric Video Dataset Bridging Video Restoration and Scene-Text Enhancement**  
   JINLONG LI ⋅ Jiaming Ding ⋅ Dingfu Lu ⋅ Malcolm Hsiu ⋅ Chuang Ke ⋅ Kangning Yang ⋅ Bochen Guan ⋅ Lan Fu ⋅ Jie Cai ⋅ Huiming Sun ⋅ Zibo Meng
10. **CogSENet: Blind Image Deblurring with Blur-Conditioned Semantic Routing and Explicit Frequency Fusion**  
   Pan Wang ⋅ Yihao Hu ⋅ Xiujin Liu  
   [arXiv:2606.30030](https://arxiv.org/abs/2606.30030)
11. **CUST : Clustered Unit-level Similarity Transformer for Lightweight Image Super-Resolution**  
   Jeongsoo Kim  
   [arXiv:2607.11088](https://arxiv.org/abs/2607.11088) · [code](https://github.com/jwgdmkj/CUST)
12. **Degradation-Agnostic Clarity Learning for Unpaired Image Dehazing**  
   Zhiyuan Song ⋅ Hannan Lu ⋅ Haiqian Han ⋅ Bo Li ⋅ Chang Liu ⋅ Pengxu Wei ⋅ Xiangyang Ji ⋅ Liang Lin
13. **DeLux: Cross-Modal Local Artifact Restoration in Video Using Neuromorphic Data**  
   Bartosz Stachowiak ⋅ Dariusz Brzezinski  
   [arXiv:2606.27576](https://arxiv.org/abs/2606.27576)
14. **Denoised Variance-Based Pruning with Optimal Brain Bias Compensation**  
   Geon Tack Lee ⋅ Choo Jaegul ⋅ Kang Eun Jeon
15. **Denoising-GS: Gaussian Splatting with Spatial-aware Denoising**  
   Qingyuan Zhou ⋅ Xinyi Liu ⋅ WEIDONG YANG ⋅ Ning Wang ⋅ Shuquan Ye ⋅ Ben Fei ⋅ Ying He ⋅ Wanli Ouyang  
   [arXiv:2605.14880](https://arxiv.org/abs/2605.14880)
16. **Depth-guided Multi-view Exposure Bracketing for HDR Robot Vision**  
   Jinnyeong Kim ⋅ Juhyung Choi ⋅ Woohyeok Kim ⋅ Sunghyun Cho ⋅ Seung-Hwan Baek  
   [arXiv:2608.16014](https://arxiv.org/abs/2608.16014)
17. **Difficulty-Conditioned Attribute-Specific Restoration for Low-Light Image Enhancement**  
   Mingzhu Zhang ⋅ Shuang Li ⋅ Jiaxu Leng ⋅ Long Sun ⋅ Can Zhang ⋅ Miaoqing Wang ⋅ Xinbo Gao
18. **Diffusion-based dual-view reflection removal**  
   Tianyi Xu ⋅ Zifeng Wang ⋅ Boyang Lyu ⋅ Shuchen Weng ⋅ Boxin Shi
19. **DnA: Denoising Attention for Visual Tasks**  
   Ron Campos ⋅ Subhajit Maity ⋅ Xin Li ⋅ Srijan Das ⋅ Aritra Dutta  
   [arXiv:2606.27372](https://arxiv.org/abs/2606.27372)
20. **Dotting the Eye: An Intent-Driven Image Retouching Agent for Visual Focus Enhancement**  
   ChujieQin ChujieQin ⋅ Zilong Zhang ⋅ Zewei Chang ⋅ Chun-Le Guo ⋅ Ruixing Wang ⋅ Tao Hu ⋅ Ming-Ming Cheng ⋅ Chongyi Li
21. **Dual-Output Multi-Exposure HDR Reconstruction via SDR Fusion and Gain Map Inverse Tone Mapping**  
   Jinho Kim ⋅ Jinwoo Kim ⋅ Seon Joo Kim  
   [arXiv:2608.05626](https://arxiv.org/abs/2608.05626)
22. **Expert Weaving: Marrying Masked AutoRegressive and Diffusion Models for Unified Image Restoration**  
   Xin Lu ⋅ Jie Huang ⋅ Jie Xiao ⋅ Dong Li ⋅ Xueyang Fu
23. **Experts-Guided Unbalanced Optimal Transport for ISP Learning from Unpaired and/or Paired Data**  
   Georgy Perevozchikov ⋅ Nancy Mehta ⋅ Egor Ershov ⋅ Radu Timofte  
   [arXiv:2512.05635](https://arxiv.org/abs/2512.05635) · [code](https://github.com/gosha20777/EGUOT-ISP.git)
24. **ExpoMotion: A Large-Scale Benchmark and A Householder Projection Network for Multi-Exposure Fusion**  
   Yao Liu ⋅ Lishen Qu ⋅ Jie Liang ⋅ shihao zhou ⋅ Hui Zeng ⋅ Yabin Peng ⋅ Huipeng Lin ⋅ Yabin Zhang ⋅ Jufeng Yang  
   [arXiv:2607.03110](https://arxiv.org/abs/2607.03110) · [code](https://github.com/Leo-LiuYao/ExpoMotion)
25. **Exposure Bias Can Alleviate Itself via Directional and Frequency Rectification in Flow Matching**  
   Guanbo Huang ⋅ Jingjia Mao ⋅ Fanding Huang ⋅ fengkai liu ⋅ Xiangyang Luo ⋅ Yaoyuan Liang ⋅ Jiasheng Lu ⋅ xiaoe Wang ⋅ Pei Liu ⋅ Ruiliu Fu ⋅ Ruqi Huang ⋅ Shao-Lun Huang  
   [arXiv:2606.28226](https://arxiv.org/abs/2606.28226)
26. **Fabric Image Demoiréing Benchmark from Synthesis to Restoration**  
   Pengchao Wei ⋅ Xiaojie Guo
27. **Fidelity- and Perception-Aware Local Implicit Attention for Arbitrary-Scale Image Super-Resolution**  
   Yu-Syuan Xu ⋅ Hao-Lun Sun ⋅ Hao-Wei Chen ⋅ Hsien-Kai Kuo ⋅ Chun-Yi Lee  
   [arXiv:2606.21910](https://arxiv.org/abs/2606.21910) · [code](https://github.com/XUSean0118/FPLIA)
28. **Flow Straight to Reality: Perceptually Consistent Flow Matching for Efficient Image Restoration**  
   Sangwoo (Jason) Jo ⋅ Donggeun Ko ⋅ Jayeon Kang ⋅ Youngsang Kwak ⋅ Jaehwa Kwak ⋅ Sungjoon Choi  
   [arXiv:2608.10544](https://arxiv.org/abs/2608.10544) · [code](https://github.com/aiimaginglab/PCFlow)
29. **FMA-Net++: Motion- and Exposure-Aware Joint Video Super-Resolution and Deblurring**  
   Geunhyuk Youk ⋅ Jihyong Oh ⋅ Munchurl Kim  
   [arXiv:2512.04390](https://arxiv.org/abs/2512.04390) · [project](https://kaist-viclab.github.io/fmanetpp_site/)
30. **Freqformer: Image-Demoiréing Transformer via Effective Frequency Decomposition**  
   Xiaoyang Liu ⋅ Bolin Qiu ⋅ Zheng Chen ⋅ Libo Zhu ⋅ Zihan Zhou ⋅ Kai Liu ⋅ Jiezhang Cao ⋅ Yulun Zhang  
   [arXiv:2505.19120](https://arxiv.org/abs/2505.19120) · [code](https://github.com/xyLiu339/Freqformer)
31. **FreqOrtho-SR: Frequency-Guided Orthogonal Expert Learning for Real-World Image Super-Resolution**  
   Minh Hoang ⋅ Dinh Tran ⋅ Quyen Nguyen Duc ⋅ Phuong Dam ⋅ Daeyoung Kim  
   [arXiv:2606.28745](https://arxiv.org/abs/2606.28745) · [code](https://github.com/sonhm3029/FreqOrtho-SR)
32. **From Local Windows to Adaptive Candidates via Individualized Exploratory: Rethinking Attention for Image Super-Resolution**  
   Chunyu Meng ⋅ Wei Long ⋅ Shuhang Gu  
   [arXiv:2601.08341](https://arxiv.org/abs/2601.08341)
33. **FUMO: Prior-Modulated Diffusion for Single Image Reflection Removal**  
   Telang Xu ⋅ Chaoyang Zhang ⋅ Guangtao Zhai ⋅ Xiaohong Liu  
   [arXiv:2603.19036](https://arxiv.org/abs/2603.19036) · [code](https://github.com/Lucious-Desmon/FUMO)
34. **Generative Manifold Distillation: Aligning Restoration Trajectories with the Natural Image Prior**  
   Yuyang Hu ⋅ Mojtaba Sahraee-Ardakan ⋅ Kangfu Mei ⋅ Arpit Bansal ⋅ Chenyang Qi ⋅ Peyman Milanfar ⋅ Mauricio Delbracio  
   [arXiv:2512.11121](https://arxiv.org/abs/2512.11121)
35. **Geodesic Flow Matching on a Riemannian Degradation Manifold for Blind Image Restoration**  
   Akshay Bankar ⋅ Ankita Chatterjee ⋅ Sayan Banerjee ⋅ Shreyas Pandith ⋅ Kalakonda Shashank ⋅ Amit Unde  
   [arXiv:2606.06278](https://arxiv.org/abs/2606.06278)
36. **HNDiff: Haze-Noise Diffusion for Image Dehazing**  
   Jin-Ting He ⋅ Fu-Jen Tsai ⋅ Yan-Tsung Peng ⋅ Min-Hung Chen ⋅ Chia-Wen Lin ⋅ Yen-Yu Lin  
   [arXiv:2608.10995](https://arxiv.org/abs/2608.10995) · [project](https://jin-ting-he.github.io/HNDiff)
37. **Hybrid-LUT: Channel-Aware Hybrid Lookup Table and Filtering for Efficient Image Restoration**  
   Zhilin Ai ⋅ Boyu Li ⋅ Sidi Yang ⋅ Wenqing Shi ⋅ Wenyong Zhou ⋅ Binxiao Huang ⋅ Chenchen Ding ⋅ Ngai Wong  
   [arXiv:2608.11646](https://arxiv.org/abs/2608.11646) · [code](https://github.com/Ai-ZL/Hybrid-LUT)
38. **IQA-T1: Tool-based Visual Evidence Reasoning for Image Quality Assessment**  
   Jinjian Wu ⋅ Jiaqi Tang ⋅ Wei Wei ⋅ Yingying Yan ⋅ Jianmin Chen ⋅ Botong Geng ⋅ Lei Zhang ⋅ Qifeng Chen  
   [arXiv:2607.12375](https://arxiv.org/abs/2607.12375) · [code](https://github.com/zibuyu-02/IQA-T1)
39. **JanusMesh: Fast and Zero-Shot 3D Visual Illusion Generation via Cross-Space Denoising**  
   Siang Zhang ⋅ Huai-Hsun Cheng ⋅ Tsung-Ju Yang ⋅ Yu-Lun Liu  
   [arXiv:2606.20563](https://arxiv.org/abs/2606.20563) · [project](https://siang1105.github.io/JanusMesh.github.io/)
40. **Learn to See the Unseen in Low-light Spike Streams**  
   Liwen Hu ⋅ Yang Li ⋅ Mianzhi Liu ⋅ Guo Yijia ⋅ Shenghao Xie ⋅ Wenqiang Zu ⋅ gang ding ⋅ Tiejun Huang ⋅ Lei Ma
41. **Leveraging Phase Information to Boost Unrolled Network Learning for Image Deblurring**  
   Samira Malek ⋅ Haichuan Zhang ⋅ Chul Lee ⋅ Vishal Monga  
   [arXiv:2607.00251](https://arxiv.org/abs/2607.00251)
42. **LGD-Net: Leader-Guided Cross-Modal Dynamics for Hyperspectral and Panchromatic Image Fusion**  
   Raj kumar ⋅ Balasubramanian Raman ⋅ Pravendra Singh
43. **LogicIR: Logic Gate Networks for Image Restoration**  
   Hongjae Lee ⋅ Myungjun Son ⋅ Jaeseong Yu ⋅ Seung-Won Jung  
   [arXiv:2606.26609](https://arxiv.org/abs/2606.26609) · [code](https://github.com/jimmy9704/LogicIR)
44. **LUCE: Constrained Curve-Domain Guidance for Training-Free Low-Light Enhancement with Hue-Preserving Decoupling**  
   Yijie Wei ⋅ Vran Lee ⋅ Yeqiang Liu ⋅ Mina Han ⋅ Xue Liu ⋅ Zhenbo Li
45. **MArFE: Multi-Contrast MRI Arbitrary Scale Super-Resolution with Fourier Enhancement**  
   ZHIWEN SHI
46. **MixCompress: Mixture of Experts for Variable Rate Learned Image Compression**  
   Calvin-Khang Ta ⋅ Praneet Singh ⋅ Tong Shao ⋅ Peng Yin  
   [arXiv:2607.14334](https://arxiv.org/abs/2607.14334)
47. **MLVC: A Multi-platform Learned Video Codec for Real-World Deployment**  
   Tanel Pärnamaa ⋅ Martin Lumiste ⋅ Ardi Loot ⋅ Evgenii Indenbom ⋅ Andrei Znobishchev ⋅ Ando Saabas  
   [arXiv:2606.28027](https://arxiv.org/abs/2606.28027) · [code](https://github.com/microsoft/mlvc)
48. **Multi-Block-Attention-based Color Constancy**  
   Oguzhan Ulucan ⋅ Diclehan Ulucan ⋅ Marc Ebner
49. **Multi-modality Image Fusion under Adverse Weather: Mask-Guided Feature Restoration and Interaction**  
   Xilai Li ⋅ Xiaosong Li ⋅ Haishu Tan ⋅ Tao Ye ⋅ Huafeng Li ⋅ Hongbin Wang  
   [arXiv:2606.26812](https://arxiv.org/abs/2606.26812) · [code](https://github.com/ixilai/AMG-Fuse)
50. **Next-Frame Decoding for Ultra-Low-Bitrate Image Compression with Video Diffusion Priors**  
   Yunuo Chen ⋅ Chuqin Zhou ⋅ Jiangchuan Li ⋅ Xiaoyue Ling ⋅ Bing He ⋅ Jincheng Dai ⋅ Li Song ⋅ Guo Lu  
   [arXiv:2603.15129](https://arxiv.org/abs/2603.15129) · [code](https://github.com/UnoC-727/NeFIC)
51. **NGPS: Structure-Preserving Self-Supervised Denoising via Neighbor-Guided Patch Sampling**  
   Jaehyun Cho ⋅ YOUNGJOON YOO  
   [arXiv:2606.23200](https://arxiv.org/abs/2606.23200) · [code](https://github.com/cv-cho/NGPS)
52. **OARS: Process-Aware Online Alignment for Generative Real-World Image Super-Resolution**  
   Shijie Zhao ⋅ Xuanyu Zhang ⋅ Bin Chen ⋅ Weiqi Li ⋅ Qunliang Xing ⋅ Kexin Zhang ⋅ Yan Wang ⋅ Junlin Li ⋅ Li Zhang ⋅ Jian Zhang ⋅ Tianfan Xue  
   [arXiv:2603.12811](https://arxiv.org/abs/2603.12811)
53. **Off the Planckian Locus: Using 2D Chromaticity to Improve In-Camera Color**  
   SaiKiran Tedla ⋅ Joshua Little ⋅ Hakki Karaimer ⋅ Michael S Brown  
   [arXiv:2511.17133](https://arxiv.org/abs/2511.17133) · [project](https://cst-mlp.github.io)
54. **ORFC: Orthogonal Reparameterization for Low-Bitrate ViT Feature Coding**  
   Letian Zhang ⋅ Wenhan Yang ⋅ Lingyu Duan
55. **PASDiff: Physics-Aware Semantic Guidance for Joint Real-world Low-Light Face Enhancement and Restoration**  
   Yilin Ni ⋅ Wenjie Li ⋅ Zhengxue Wang ⋅ Juncheng Li ⋅ Guangwei Gao ⋅ Jian Yang  
   [arXiv:2603.24969](https://arxiv.org/abs/2603.24969) · [code](https://github.com/IVIPLab/PASDiff)
56. **Perceiving Better Moments: Cover Frame Reselection and Enhancement for Live Photos with the Live2K Dataset**  
   Junyu Lou ⋅ Kai Chen ⋅ Weiyi You ⋅ Hui Zeng ⋅ Yabin Zhang ⋅ Shuhang Gu  
   [arXiv:2607.04151](https://arxiv.org/abs/2607.04151)
57. **Physics Meets Perception: A Reinforcement Learning Framework for Unpaired Real-World Image Dehazing**  
   Yunwei Lan ⋅ Zhigao Cui ⋅ Chang Liu ⋅ Menglin Zhang ⋅ Nian Wang ⋅ Cong Zhang ⋅ Dong Liu
58. **PolarAPP: Beyond Polarization Demosaicking for Polarimetric Applications**  
   Yidong Luo ⋅ Chenggong Li ⋅ Yunfeng Song ⋅ Ping Wang ⋅ Boxin Shi ⋅ Junchao Zhang ⋅ Xin Yuan  
   [arXiv:2603.23071](https://arxiv.org/abs/2603.23071)
59. **ProGVC: Progressive-based Generative Video Compression via Auto-Regressive Context Modeling**  
   Daowen Li ⋅ Ruixiao Dong ⋅ Ying Chen ⋅ Kai Li ⋅ Ding Ding ⋅ Li Li  
   [arXiv:2603.17546](https://arxiv.org/abs/2603.17546)
60. **P²Fusion: Prompt-based Progressive Infrared-Visible Image Fusion via Dual-Prior Distillation**  
   Yi Shi ⋅ Huichao Xie ⋅ Yuqing Wang ⋅ Mingyu Wang ⋅ Kaihui Yang ⋅ Yu Liu ⋅ Lu Ruitao ⋅ Lizhe Li ⋅ Junwei Han ⋅ Dingwen Zhang
61. **QualiTeacher: Quality-Conditioned Pseudo-Labeling for Real-World Image Restoration**  
   Fengyang Xiao ⋅ Jingjia Feng ⋅ Peng Hu ⋅ Yuhan Chen ⋅ Dingming Zhang ⋅ Lei Xu ⋅ Guanyi Qin ⋅ Lu Li ⋅ Chunming He ⋅ Sina Farsiu  
   [arXiv:2603.08030](https://arxiv.org/abs/2603.08030)
62. **RADIANCE: Relative Adaptive Denoising with IP-Adapter for Novel Concept Enhancement**  
   Zi-Xiang Ni ⋅ Bo-Lun Huang ⋅ Teng-Fang Hsiao ⋅ Bo-Kai Ruan ⋅ Hong-Han Shuai
63. **Raw-JPEG Adapter: Efficient Raw Image Compression with JPEG**  
   Mahmoud Afifi ⋅ Ran Zhang ⋅ Michael S Brown  
   [arXiv:2509.19624](https://arxiv.org/abs/2509.19624)
64. **RawGen: Learning Camera Raw Image Generation**  
   Dongyoung Kim ⋅ Junyong Lee ⋅ Abhijith Punnappurath ⋅ Mahmoud Afifi ⋅ Sangmin Han ⋅ Alex Levinshtein ⋅ Michael S Brown  
   [arXiv:2604.00093](https://arxiv.org/abs/2604.00093)
65. **ReAL: Reference-to-Image (R2I) Aware Latent Diffusion for Image Super-Resolution**  
   Byeonghun Lee ⋅ Hyunmin Cho ⋅ Sunghoon Im ⋅ Kyong Hwan Jin
66. **RefReward-SR: LR-Conditioned Reward Modeling for Preference-Aligned Super-Resolution**  
   Yushuai Song ⋅ Weize Quan ⋅ Weining Wang ⋅ Jiahui Sun ⋅ Jing Liu ⋅ Meng Li ⋅ Pengbin Yu ⋅ Zhentao Chen ⋅ Wei Shen ⋅ Lunxi Yuan ⋅ Dong-ming Yan  
   [arXiv:2603.24198](https://arxiv.org/abs/2603.24198)
67. **RL-AWB: Deep Reinforcement Learning for Auto White Balance Correction in Low-Light Night-time Scenes**  
   Yuan-Kang Lee ⋅ Kuan-Lin Chen ⋅ Chia-Che Chang ⋅ Yu-Lun Liu  
   [arXiv:2601.05249](https://arxiv.org/abs/2601.05249) · [project](https://ntuneillee.github.io/research/rl-awb/)
68. **Robust Self-Supervised Cross-Modal Super-Resolution against Real-World Misaligned Observations**  
   Xiaoyu Dong ⋅ Jiahuan Li ⋅ Ziteng Cui ⋅ Naoto Yokoya  
   [arXiv:2602.18822](https://arxiv.org/abs/2602.18822) · [project](https://drive.google.com/file/d/1fqTYuSY7Qp7PFHiHViZs7y6lz6Bws7ws/view?usp=sharing)
69. **RTE-FM-Dehazer: Radiative Transfer Equation Inspired Flow Matching for Real-World Image Dehazing**  
   Chenfeng Wei ⋅ Chun Wang ⋅ Boyang Zhao ⋅ Si Zuo ⋅ Shenhong WANG ⋅ Chenguang Yang  
   [arXiv:2607.01748](https://arxiv.org/abs/2607.01748)
70. **SCALE: Semantic-Calibrated Guidance Enhancement for Prompt-Faithful Diffusion**  
   Tianhang Lu ⋅ Sudong Cai ⋅ Bingzhi Chen ⋅ Shao-Dong Shen ⋅ Chunting Liu ⋅ Longguang Wang ⋅ Bing Wang
71. **SLAIR: Structured Latent Flow Matching for All-in-One Image Restoration**  
   Shuyi Liang ⋅ Yixin Yang ⋅ Hanyue Lou ⋅ Yuning Cui ⋅ Boxin Shi
72. **SLER-IR: Spherical Layer-wise Expert Routing for All-in-One Image Restoration**  
   Shurui Peng ⋅ Xin Lin ⋅ Shi Luo ⋅ Jincen Ou ⋅ Dizhe Zhang ⋅ Lu Qi ⋅ Truong Nguyen ⋅ Chao Ren  
   [arXiv:2603.05940](https://arxiv.org/abs/2603.05940)
73. **SparkVSR: Interactive Video Super-Resolution via Sparse Keyframe Propagation**  
   Jiongze Yu ⋅ Xiangbo Gao ⋅ Pooja Verlani ⋅ Akshay Gadde ⋅ Yilin Wang ⋅ Balu Adsumilli ⋅ Zhengzhong Tu  
   [arXiv:2603.16864](https://arxiv.org/abs/2603.16864) · [project](https://sparkvsr.github.io/)
74. **Spectral and Trajectory Regularization for Diffusion Transformer Super-Resolution**  
   Jingkai Wang ⋅ Yixin Tang ⋅ Jue Gong ⋅ Jiatong Li ⋅ Shu Li ⋅ Libo Liu ⋅ Jianliang Lan ⋅ Yutong Liu ⋅ Yulun Zhang  
   [arXiv:2603.06275](https://arxiv.org/abs/2603.06275) · [code](https://github.com/jkwang28/StrSR)
75. **Spectral Prior for Reducing Exposure Bias in Diffusion Models**  
   Yuya Kobayashi ⋅ Masato Ishii ⋅ Yuhta Takida ⋅ Takashi Shibuya ⋅ Yuki Mitsufuji  
   [arXiv:2607.22091](https://arxiv.org/abs/2607.22091) · [code](https://github.com/SonyResearch/SPA)
76. **SplitHDR: Saturation-Aware HDR Recovery and Denoising for Real-Time Detection**  
   Jaewon Kim ⋅ Sol Namkung ⋅ Dongsuk Jeon
77. **Stream-DiffVSR: Low-Latency Streamable Video Super-Resolution via Auto-Regressive Diffusion**  
   Hau-Shiang Shiu ⋅ Chin-Yang Lin ⋅ Zhixiang Wang ⋅ Chi-Wei Hsiao ⋅ Po-Fan Yu ⋅ Yu-Chih Chen ⋅ Yu-Lun Liu  
   [arXiv:2512.23709](https://arxiv.org/abs/2512.23709) · [project](https://jamichss.github.io/stream-diffvsr-project-page/)
78. **Synthetic Sub-Aperture Phase Augmentation for Demosaicing 2×2 Shared Microlens Sensors**  
   Jeisung Lee ⋅ Wonil Song
79. **TAQ: Static-Deployable Temporal-Aware Quantization for Real-World Video Super-Resolution**  
   Jinwoo Chung ⋅ Sangho An ⋅ Sungyeop Jung ⋅ Jangho Kim
80. **TaskTok: Delving into Task Tokens for Task-driven Image Restoration**  
   Hongjae Lee ⋅ Sojung Kang ⋅ Jaeseong Yu ⋅ Seung-Won Jung  
   [arXiv:2606.26615](https://arxiv.org/abs/2606.26615) · [code](https://github.com/jimmy9704/TaskTok)
81. **TDSR-VLA: Transition-aware Denoising Sequence Representations for Vision-Language-Action**  
   Dong-Woo Kim ⋅ KEUNHO SONG ⋅ Seungmin Lee ⋅ Hwanhee Ju ⋅ Eun Cha ⋅ Daekyum Kim
82. **TEASR: Training-Efficient Any-Step Diffusion Transformer for Real-World Image Super-Resolution**  
   Xiang Gao ⋅ Chenxin Zhu ⋅ Yushun Fang ⋅ Qiang Hu ⋅ Xiaoyun Zhang  
   [arXiv:2606.16188](https://arxiv.org/abs/2606.16188)
83. **The Devil Is in the Dark Pixels: Toward Brightness Bias-Robust Denoising**  
   Sungjun Cho ⋅ Zhuangzhuang Chen ⋅ Xiaomeng Li  
   [arXiv:2607.16320](https://arxiv.org/abs/2607.16320) · [code](https://github.com/xmed-lab/BBRD)
84. **There and Back Again: A Flexible-Frame Transformer for Multi-Exposure Fusion**  
   Lishen Qu ⋅ Yao Liu ⋅ shihao zhou ⋅ Jie Liang ⋅ Hui Zeng ⋅ Yabin Zhang ⋅ Jufeng Yang  
   [arXiv:2606.27905](https://arxiv.org/abs/2606.27905)
85. **Tiled Prompts: Overcoming Prompt Misguidance in Image and Video Super-Resolution**  
   Bryan Kim ⋅ Jonghyun Park ⋅ Jong Chul Ye  
   [arXiv:2602.03342](https://arxiv.org/abs/2602.03342) · [project](https://bryanswkim.github.io/tiled-prompts/)
86. **TIR-Agent: Training an Explorative and Efficient Agent for Image Restoration**  
   Yisheng Zhang ⋅ Guoli Jia ⋅ Haote Hu ⋅ Shanxu Zhao ⋅ Kaikai Zhao ⋅ Long Sun ⋅ Xinwei Long ⋅ Kai Tian ⋅ Che Jiang ⋅ Zhaoxiang Liu ⋅ Kai Wang ⋅ Shiguo Lian ⋅ Kaiyan Zhang ⋅ Bowen Zhou  
   [arXiv:2603.27742](https://arxiv.org/abs/2603.27742)
87. **Towards Reconfigurable Visual Feature Compression**  
   Jiahang Zhang ⋅ Wenhan Yang ⋅ Minghao Liu ⋅ Jiaying Liu
88. **TPCNet: A Low-Light Image Enhancement Network Inspired by Triple Physical Constraints**  
   Jing-Yi Shi ⋅ Ming-Fei Li ⋅ Ling-An Wu
89. **TRaM-VSR: Importance-Aware Token Routing and Merging for One-Step Diffusion Video Super-Resolution**  
   Sicheng Gao ⋅ Yixuan Liu ⋅ Tong Shen ⋅ Zhuyun Zhou ⋅ Zongwei Wu ⋅ Radu Timofte  
   [arXiv:2607.22231](https://arxiv.org/abs/2607.22231) · [code](https://github.com/Ree1s/TRaM-VSR)
90. **Tuning Real-World Image Restoration at Inference: A Test-Time Scaling Paradigm for Flow Matching Models**  
   Purui Bai ⋅ Junxian Duan ⋅ Pin Wang ⋅ Jinhua Hao ⋅ Ming Sun ⋅ Chao Zhou ⋅ Huaibo Huang  
   [arXiv:2603.22027](https://arxiv.org/abs/2603.22027)
91. **TurboMPLE: Joint Infrared Turbulence Mitigation and Physical Fields Estimation via Mutual Progressive Layered Extraction**  
   Yitong An ⋅ Yubo Jiang ⋅ Xiangzhi Bai
92. **UHD-MFF: Shattering Barriers in Multi-Focus Ultra-High-Definition Image Fusion via Learnable Lookup Tables**  
   Yibing Zhang ⋅ Xunpeng Yi ⋅ Qinglong Yan ⋅ Yeda Wang ⋅ Han Xu ⋅ Jiayi Ma  
   [arXiv:2606.31242](https://arxiv.org/abs/2606.31242) · [code](https://github.com/zyb5/UHD-MFF)
93. **VOCA: Visual Odometry with Codec Awareness**  
   Nouri Alexander Hilscher ⋅ Mateo Mayo ⋅ Dominik Muhle ⋅ Christoph Hermes ⋅ Daniel Cremers  
   [arXiv:2607.00189](https://arxiv.org/abs/2607.00189)
94. **WARP: Wide Attention with Rich Projections for Image Super-Resolution**  
   Jiwon Kim ⋅ Kyoung Mu Lee
95. **Wat3R: Underwater 3D Geometry Learning without Underwater Annotations**  
   Jiangwei Ren ⋅ Xingyu Jiang ⋅ Zijie Song ⋅ Wei Xu ⋅ Hongkai Lin ⋅ Dingkang Liang ⋅ Xiang Bai
96. **WaterGen: Decoupling Scene and Medium in Underwater Image Generation**  
   Jiayi Wu ⋅ Tianfu Wang ⋅ Tianyi Xiong ⋅ Dehao Yuan ⋅ Xiaomin Lin ⋅ Md Jahidul Islam ⋅ Cornelia Fermuller ⋅ Christopher Metzler ⋅ Yiannis Aloimonos  
   [arXiv:2606.31147](https://arxiv.org/abs/2606.31147)
97. **When the Teacher Has More Bits: Self-Teacher Latent Distillation for Learned Image Compression**  
   Abdellah Mennaoui ⋅ Joseph Meehan ⋅ Jean-Luc Dugelay ⋅ Ghalia Hemrit
98. **YeTI: You Only Need Two Noisy Images for Real-World sRGB Noise Generation**  
   Jaekyun Ko ⋅ Byung Wan Lim ⋅ Dongjin Kim ⋅ Soomin Lee ⋅ Tae Hyun Kim  
   [arXiv:2607.09193](https://arxiv.org/abs/2607.09193)
99. **Zero-Shot Inference-Time Rectification for Real-World Arbitrary-Scale Super-Resolution**  
   Yifan Zuo ⋅ tianlin zhu ⋅ zhenlong xia ⋅ Jiebin Yan ⋅ Xiaoshui Huang ⋅ Sanqian Li ⋅ Yuming Fang ⋅ Qiang Wu
100. **Zoom-IQA: Image Quality Assessment with Reliable Region-Aware Reasoning**  
   Guoqiang Liang ⋅ Jianyi Wang ⋅ Zhonghua Wu ⋅ Shangchen Zhou ⋅ Chen Change Loy  
   [arXiv:2601.02918](https://arxiv.org/abs/2601.02918) · [project](https://ethanliang99.github.io/ZOOMIQA-Projectpage)

# Recognition & Perception


## Object Detection & Segmentation

*150 papers · 85 with links*

1. **A Dual-space Patch-driven Complementary Learning Framework for Semi-supervised Multi-organ Segmentation**  
   Baixi Liang ⋅ Shuohong Xia ⋅ Sihao Li ⋅ Yunyun Yang
2. **A Simple Baseline with Placement Prior for Point-Supervised Oriented Object Detection**  
   Runxiang Liu ⋅ Kaikai Xie ⋅ Qianxi Cao ⋅ Yuming Fang ⋅ Jiebin Yan ⋅ Junjie Chen
3. **Adaptive Latent Trajectory Anchoring for Action Segmentation Dataset Condensation**  
   Arthème Gauthier-Villars ⋅ Guodong Ding ⋅ Angela Yao  
   [arXiv:2607.09081](https://arxiv.org/abs/2607.09081)
4. **Adaptive Spectrum-Aware Feature Disentangled Network for Small Object Detection**  
   Yang Guo ⋅ Zihan Yang ⋅ Feifei Kou ⋅ Yulan Hu ⋅ Ran Zhang ⋅ Siyuan Yao  
   [arXiv:2606.29029](https://arxiv.org/abs/2606.29029) · [code](https://github.com/ManOfStory/SFDNet)
5. **Adversarial Attack and Disturbance Detection by Hadamard-Coded Output Representations for Object Detection and Semantic Segmentation**  
   Lucas Görnhardt ⋅ Timo Bartels ⋅ Niklas Schwarz ⋅ Tim Fingscheidt  
   [arXiv:2606.09536](https://arxiv.org/abs/2606.09536)
6. **AffoGato: Open-Vocabulary Affordance Grounding with Automated Data Generation at Scale**  
   Junha Lee ⋅ Eunha Park ⋅ Chunghyun Park ⋅ Dahyun Kang ⋅ Minsu Cho  
   [arXiv:2506.12009](https://arxiv.org/abs/2506.12009) · [project](https://junha-l.github.io/affogato/)
7. **Align and Segment: Unsupervised Learning for Building Segmentation From Misaligned Labels**  
   Venkanna Babu Guthula ⋅ Oswin Krause ⋅ Dimitri Gominski ⋅ Hui Zhang ⋅ Johan Mottelson ⋅ Ankit Kariryaa ⋅ Nico Lang ⋅ Christian Igel  
   [arXiv:2607.10841](https://arxiv.org/abs/2607.10841) · [code](https://github.com/venkanna37/align-and-segment)
8. **BEVOpen3D: Towards Open-World 3D Object Detection in Bird's-Eye-View**  
   Huyue Zeng ⋅ Jiaqi Yang ⋅ Xian-Feng Han
9. **Beyond Isolated Objects: Relationship-aware Open Vocabulary Scene Understanding via 3D Scene Graph Analysis**  
   Xianhao Chen ⋅ Jiarui Hu ⋅ Yuanbo Yang ⋅ Xiyu Zhang ⋅ Tengyue Wang ⋅ Hujun Bao ⋅ Guofeng Zhang ⋅ Zhaopeng Cui  
   [arXiv:2607.05348](https://arxiv.org/abs/2607.05348) · [project](https://cxavireh.github.io/relgraphov-projectpage)
10. **Beyond Language: Grounding Referring Expressions with Hand Pointing in Egocentric Vision**  
   LING LI ⋅ Bowen Liu ⋅ Zinuo Zhan ⋅ Peng Jie ⋅ Jianhui Zhong ⋅ Kenglun Chang ⋅ Zhidong Deng  
   [arXiv:2603.26646](https://arxiv.org/abs/2603.26646)
11. **Breaking the Model Forgetting Cycle in Long-Incremental 3D Object Detection**  
   Peisheng Qian ⋅ Jie Xu ⋅ Xulei Yang ⋅ Na Zhao  
   [arXiv:2607.14560](https://arxiv.org/abs/2607.14560) · [code](https://github.com/qianpeisheng/LDMR)
12. **C2E: Boosting Ego-Only 3D Object Detection via Multi-Teacher Contrastive Knowledge Distillation**  
   Jinlong Wang ⋅ Xun Huang ⋅ Qiming Xia ⋅ Shijia Zhao ⋅ Chenglu Wen  
   [arXiv:2607.01827](https://arxiv.org/abs/2607.01827)
13. **Cast and Attached Shadow Detection via Iterative Light and Geometry Reasoning**  
   Shilin Hu ⋅ Jingyi Xu ⋅ Sagnik Das ⋅ Dimitris Samaras ⋅ Hieu Le  
   [arXiv:2512.06179](https://arxiv.org/abs/2512.06179) · [project](https://shilin21.github.io/attached_detection/)
14. **Causal Yet Future-Aware: Dual-Path Temporal Modeling for Online Action Segmentation**  
   Zhichao Zheng ⋅ Peirong Ma ⋅ Ying Zhou ⋅ Li Kong ⋅ Junsheng Zhou
15. **CoGoal3D: Collaborative 3D Object Detection with 3D-Aware Fusion and Refinement**  
   Zhihao Yang ⋅ Zhiyu Xiang ⋅ Peng Xu ⋅ Tianyu Pu ⋅ Kai Wang ⋅ Eryun Liu ⋅ Dongping Zhang ⋅ Yong Ding  
   [arXiv:2607.19036](https://arxiv.org/abs/2607.19036) · [code](https://github.com/Megalo-f/CoGoal3D)
16. **Comprehensive Robustness Analysis of LiDAR-based 3D Object Detection in Autonomous Driving**  
   Adwait Chandorkar ⋅ Kai Krink ⋅ Yerdana Maulenbay ⋅ Hasan Tercan ⋅ Tobias Meisen  
   [arXiv:2607.02074](https://arxiv.org/abs/2607.02074)
17. **Context-Interactive Reasoning for Group Activity Detection**  
   Xi Ai ⋅ Weihong Ren ⋅ Shuhuan Han ⋅ Haoran Xu ⋅ Qian Dong ⋅ Pengyang Su ⋅ Zijian Wang ⋅ Shengchun Lin ⋅ Zhiyong Wang ⋅ Honghai Liu
18. **CoT-PL: Chain-of-Thought Pseudo-Labeling for Open-Vocabulary Object Detection**  
   Hojun Choi ⋅ Youngsun Lim ⋅ Jaeyo Shin ⋅ Hyunjung Shim
19. **CountEx: Fine-Grained Counting via Exemplars and Exclusion**  
   Yifeng Huang ⋅ Gia Nguyen ⋅ Minh Hoai Nguyen  
   [arXiv:2602.19432](https://arxiv.org/abs/2602.19432) · [code](https://github.com/bbvisual/CountEx)
20. **CURE: Contextual Debiasing and Unbiased Refinement for Training-Free Open-Vocabulary Semantic Segmentation**  
   Jiean Wang ⋅ Sanqing Qu ⋅ Fan Lu ⋅ Huanhuan Bao ⋅ Wei Tian ⋅ Bo Jin ⋅ Jiangtong Li ⋅ Junqiao Zhao ⋅ Guang Chen
21. **DA-F2F: Domain-Adaptive Object Detection with Feature-to-Feature Modulation and Alignment**  
   HoTaek Oh ⋅ Hee-Jun Kim ⋅ Hyo-Jun Lee
22. **Defect-aware Hybrid Prompt Optimization for Zero-Shot Multi-type Anomaly Detection and Segmentation**  
   Nadeem Nazer ⋅ Hongkuan Zhou ⋅ Lavdim Halilaj ⋅ Ylli Sadikaj ⋅ Steffen Staab
23. **Deformable and Multi-view Gradient-Aligned Physical Adversarial Camouflage**  
   Jiawei Liang ⋅ Puning Zhao ⋅ tianrui lou ⋅ Haoqing Zhang ⋅ Xianghao Jiao ⋅ Bozheng Lin ⋅ Ming Zhang ⋅ Xiaochun Cao
24. **Detect by Track: Making Detector-Free Matcher Trackable**  
   Yusuke Sekikawa ⋅ HIDEKI SHIRAI ⋅ Ruka Eto ⋅ Yuzhe Hao ⋅ Kengo Mitsui ⋅ Nakamasa Inoue
25. **Detecting Backdoors in Object Detection via Pre-NMS Prediction Distribution Shift**  
   Longtian Wang ⋅ Chenhao Lin ⋅ Zhengyu Zhao ⋅ Le Yang ⋅ Shiwei Wang ⋅ Yuhan Zhi ⋅ Xiaofei Xie ⋅ Chao Shen
26. **DGSeg: Dynamic Gating of Semantic-Spatial Guided Predictions for Reasoning Segmentation**  
   Ruizhe Zeng ⋅ Siyu Cao ⋅ Lu Zhang ⋅ Zhi-yong Liu  
   [arXiv:2607.04779](https://arxiv.org/abs/2607.04779) · [code](https://github.com/RZZeng/DGSeg)
27. **Diffusion Model as a Generalized Segmentation Learner**  
   Haoxiao Wang ⋅ Antao Xiang ⋅ Haiyang Sun ⋅ Peilin Sun ⋅ Changhao Pan ⋅ Yifu Chen ⋅ Minjie Hong ⋅ Weijie Wang ⋅ Shuang Chen ⋅ Yue Chen ⋅ ZHOU ZHAO
28. **DINOde: Continuous Vision-Text Alignment for Open-Vocabulary Semantic Segmentation**  
   Sung-Hoon Yoon ⋅ Hoyong Kwon ⋅ Changgyoon Oh ⋅ KUK-JIN YOON  
   [arXiv:2607.21371](https://arxiv.org/abs/2607.21371) · [code](https://github.com/yoon307/DINOde)
29. **Domain Adaptive Object Detection via Dual-Stream Bilevel-Cycle Optimization**  
   Yannan Chen ⋅ Wei Wang ⋅ Ruoyu Chen ⋅ Wenqiang Wang ⋅ Jiancheng Wang ⋅ Mingbo Yang ⋅ Yaowei Wang ⋅ Xiaochun Cao  
   [arXiv:2606.31373](https://arxiv.org/abs/2606.31373)
30. **Efficient RGB-T Object Detection via Sparse Cross-Modality Fusion**  
   CHAO TIAN ⋅ Zikun Zhou ⋅ Chao Yang ⋅ guoqing zhu ⋅ Zhenyu He  
   [arXiv:2606.30215](https://arxiv.org/abs/2606.30215)
31. **EM3M: An Electron Micrograph Dataset for Microstructural Segmentation and Generation**  
   Nan Wang ⋅ Zhiyi Xia ⋅ Yiming Li ⋅ Shi Tang ⋅ Zoe Fan ⋅ Xi Fang ⋅ Haoyi Tao ⋅ ZHANG SIYUAN ⋅ Guolin Ke ⋅ Yanhui Hong  
   [arXiv:2508.16239](https://arxiv.org/abs/2508.16239) · [code](https://huggingface.co/datasets/UniParser/EM3M) · [project](https://www.bohrium.com/apps/uni-aims)
32. **Exclusivity-Guided Mask Learning for Semi-Supervised Crowd Instance Segmentation and Counting**  
   Jiyang Huang ⋅ Hongru Chen ⋅ Wei Lin ⋅ Jia Wan ⋅ Antoni Chan  
   [arXiv:2603.16241](https://arxiv.org/abs/2603.16241)
33. **Explicit Semantic–Spatial Alignment for Open-Vocabulary Object Detection**  
   Pengyang Su ⋅ Weihong Ren ⋅ Shuhuan Han ⋅ Qian Dong ⋅ Haoran Xu ⋅ Xi Ai ⋅ Zijian Wang ⋅ Zhiyong Wang ⋅ Honghai Liu
34. **Exploring Efficient Reasoning Segmentation with Small Language Models**  
   Changsong Wen ⋅ Zelin Peng ⋅ Yu Huang ⋅ Xiaokang Yang ⋅ Wei Shen
35. **Extending a Large View Synthesis Model for Multi-view Panoptic Segmentation**  
   Kwonyoung Ryu ⋅ In-Jae Lee ⋅ Jonghyun Jin ⋅ Hyunjee Lee ⋅ Jongmin Lee ⋅ Jaesik Park  
   [arXiv:2607.19765](https://arxiv.org/abs/2607.19765) · [project](https://kwonyoung9120.github.io/PanopticLVSM/)
36. **FAIR: Feature-Augmented Implicit Regularization for AI-generated Fake Image Detection**  
   Md Redwanul Haque ⋅ Manzur Murshed ⋅ Manoranjan Paul ⋅ Tsz-Kwan Lee
37. **Fast and Flexible Robustness Certificates for Semantic Segmentation**  
   Thomas Massena ⋅ Corentin Friedrich ⋅ Franck Mamalet ⋅ Mathieu Serrurier  
   [arXiv:2512.06010](https://arxiv.org/abs/2512.06010)
38. **FeVOS: Foresight Expression Video Object Segmentation**  
   Kehan Lan ⋅ Kaining Ying ⋅ Henghui Ding  
   [arXiv:2606.25585](https://arxiv.org/abs/2606.25585) · [project](https://henghuiding.com/FeVOS/)
39. **FMS2: Unified Flow Matching for Segmentation and Synthesis of Thin Structures**  
   Babak Asadi ⋅ Peiyang Wu ⋅ Mani Golparvar-Fard ⋅ Viraj Jayminkumar Shah ⋅ Ramez Hajj
40. **Following the Flow: Advection-Consistent Modeling for Event-based Small Object Detection**  
   Wen Guo ⋅ Fulong Cai ⋅ Wuzhou Quan  
   [arXiv:2606.22378](https://arxiv.org/abs/2606.22378) · [code](https://github.com/fulongcai/PACT)
41. **FoundYou: A Unified Model for Personalized Segmentation and Retrieval**  
   Gabriele Trivigno ⋅ Marcos Alfaro Perez ⋅ Claudia Cuttano ⋅ Gabriele Berton ⋅ Luis Payá ⋅ Carlo Masone
42. **Free-Lunch Augmentation by Revisiting Diffusion-Based Data Generation for Cross-Domain Few-Shot Object Detection**  
   Zijian Zhuang ⋅ Yixiong Zou ⋅ Yuhua Li ⋅ Ruixuan Li  
   [arXiv:2608.04394](https://arxiv.org/abs/2608.04394) · [code](https://github.com/zzzzj311-droid/Free-Lunch-SITN)
43. **Free‑CD: Probabilistically Decoupled Training-Free Open-Vocabulary Change Detection with Resolution-Invariant Feature Inversion**  
   Yongshuo Zhu ⋅ LU LI ⋅ Keyan Chen ⋅ Zhenwei Shi ⋅ ZHOU Fugen
44. **Frequency Director: Learnable Mixture of Frequency Experts for Unified Concealed Scene Segmentation**  
   Guangqian Guo ⋅ Aixi Ren ⋅ Xuehui Yu ⋅ Pengxu Wei ⋅ Yong Guo ⋅ shan gao
45. **From Drop-off to Recovery: A Mechanistic Analysis of Segmentation in MLLMs**  
   Boyong Wu ⋅ Sanghwan Kim ⋅ Zeynep Akata  
   [arXiv:2603.17228](https://arxiv.org/abs/2603.17228)
46. **From Visual Primitives to Semantic Masks: Fine-Grained Visual-Linguistic Alignment for Open-Vocabulary Remote Sensing Image Segmentation**  
   Yuchen Deng ⋅ Yang Xu ⋅ Zhihui Wei ⋅ Zebin Wu
47. **FSDC-DETR: A Frequency-Spatial Domain Collaborative DETR for Small-Object Detection**  
   Aiwen Liu ⋅ Chengguang Zhu ⋅ Gang Wang ⋅ Dandan Zhu ⋅ Haodong Lin ⋅ Yan Wang ⋅ Huiyu Zhou ⋅ Zhengyi Pan  
   [arXiv:2607.05176](https://arxiv.org/abs/2607.05176)
48. **FST-SAM3: Taming SAM~3 with Frequency-Spatio-Temporal Refinement for Video Polyp Segmentation**  
   Guanhao Wu ⋅ Guilian Chen ⋅ Huisi Wu ⋅ Jing Qin
49. **Fully Rotation-Equivariant Spectral-Spatial Learning for Multispectral Object Detection**  
   Peng Zhang ⋅ Tingfa Xu ⋅ Shuaihao Han ⋅ Jianan Li  
   [arXiv:2607.05148](https://arxiv.org/abs/2607.05148)
50. **GEAR-Seg: A Grounded Explainable Agent for Reasoning Segmentation and Data Engine**  
   Yanan Wang ⋅ Wen li ⋅ Yibin Ying ⋅ Zhenghao Fei  
   [arXiv:2607.00544](https://arxiv.org/abs/2607.00544)
51. **Geo-DPO: Aligning Semantic Intent with Geometry for 3D Affordance Segmentation**  
   Ziqian Yang ⋅ Xiaolei Wang ⋅ Xianglin Qiu ⋅ Weiguang Zhao ⋅ Quan Zhang ⋅ Jimin Xiao
52. **GeoDetect: Geometric Adversarial Detection for VLPs**  
   Afsaneh Hasanebrahimi ⋅ Hanxun Huang ⋅ Christopher Leckie ⋅ James Bailey ⋅ Sarah Erfani  
   [arXiv:2607.14737](https://arxiv.org/abs/2607.14737)
53. **Group3D: MLLM-Guided Semantic Grouping for Open-Vocabulary 3D Object Detection**  
   Youbin Kim ⋅ Jinho Park ⋅ Hogun Park ⋅ Eunbyung Park  
   [arXiv:2603.21944](https://arxiv.org/abs/2603.21944) · [project](https://ubin108.github.io/Group3D/)
54. **HIDA: A Human-Intuition-Guided Depth-Aware Framework for Zero-Shot Amodal Segmentation**  
   PENG LI ⋅ Kelin Wang ⋅ Bingchuan Chen ⋅ Ya-Li Hou ⋅ Mingxia Shen ⋅ Bo Li
55. **Hierarchical and Holistic Open-Vocabulary Functional 3D Scene Graphs for Indoor Spaces**  
   Xinggang Hu ⋅ Chenyangguang Zhang ⋅ Alexandros Delitzas ⋅ Xiangkui Zhang ⋅ Marc Pollefeys ⋅ Francis Engelmann ⋅ Xiangyang Ji  
   [arXiv:2605.15753](https://arxiv.org/abs/2605.15753)
56. **Hierarchical Prompt Injector for Domain Generalization Segmentation**  
   Xin Kun Lin ⋅ Ruoyu Guo ⋅ Jiaqi Guo ⋅ Maurice Pagnucco ⋅ Yang Song
57. **Hierarchical Spatial and Channel Aggregation for Cross-domain Few-shot Segmentation**  
   Sujun Sun ⋅ Mingwu Ren ⋅ Haofeng Zhang  
   [arXiv:2606.24296](https://arxiv.org/abs/2606.24296)
58. **HVA-Fusion:Hierarchical Velocity-Aware 4D Radar-LiDAR Fusion for Robust 3D Object Detection**  
   Jingxian Wu ⋅ Lu Wang ⋅ Lisheng Xu ⋅ Jun Cheng
59. **IACD: Iterative Adversarial Collaborative Detection via Dual-Perspective Blind Spot Discovery**  
   Xiaoyan Li ⋅ Cuicui Jiang ⋅ Jiaoping Chen ⋅ Rumei Yang
60. **InfraNet: Quality-Aware RGB Guidance for Infrared Object Detection**  
   Zichao Feng ⋅ Haodong Zhu ⋅ JingYing Yang ⋅ Linlin Yang ⋅ Yangyang Ren ⋅ Sheng Xu ⋅ Yuguang Yang ⋅ Xuhui Liu ⋅ Juan Zhang ⋅ Tian Wang ⋅ Baochang Zhang  
   [arXiv:2607.03795](https://arxiv.org/abs/2607.03795)
61. **Intra-Class Consistency Guided Class-Agnostic Event Segmentation**  
   Zhipeng Sui ⋅ Haiqing Hao ⋅ Weihua He ⋅ Wenhui Wang
62. **IP-SAM: Rethinking Prompt-Conditioned Segmentation for Prompt-Absent Deployment**  
   Huiyao Zhang ⋅ Jin Bai ⋅ Rui Guo ⋅ Jianwen Tan ⋅ Hongfei Wang ⋅ Ye Li  
   [arXiv:2603.27250](https://arxiv.org/abs/2603.27250)
63. **Iterative Refinement of Semantic and Spatial Representations for Open-Vocabulary Camouflaged Object Segmentation**  
   Fangyan Wang ⋅ Ge Jiao ⋅ Guowen Yue
64. **Label-Free Text Prototype Adaptation for Open Vocabulary Segmentation**  
   Keli Wang ⋅ Meixuan Li ⋅ Tianyu Li ⋅ Guoqing Wang
65. **Learning Accurate Segmentation Purely from Self-Supervision**  
   Zuyao You ⋅ Zuxuan Wu ⋅ Yu-Gang Jiang  
   [arXiv:2602.23759](https://arxiv.org/abs/2602.23759)
66. **Learning Probabilistic Embeddings for Unsupervised Action Segmentation**  
   Shuai Li ⋅ Duc Vu ⋅ Juergen Gall  
   [arXiv:2607.05263](https://arxiv.org/abs/2607.05263) · [code](https://github.com/derkbreeze/PEOT)
67. **Learning Structurally Consistent Representations for Multi-View Radar Semantic Segmentation**  
   ALI ZIA ⋅ Muhammad Ramzan ⋅ Abdelwahed Khamis ⋅ Usman Ali ⋅ Abdul Rehman  
   [arXiv:2606.31609](https://arxiv.org/abs/2606.31609)
68. **Learning Structured Visual Compositional Representations for Weakly Supervised Referring Expression Comprehension**  
   Lian Xu ⋅ Mohammed Bennamoun ⋅ Farid Boussaid ⋅ Hamid Laga ⋅ Yulan Guo ⋅ Dan Xu  
   [arXiv:2607.04638](https://arxiv.org/abs/2607.04638)
69. **Liquid Fusion of Heterogeneous Representations Towards General Salient Object Detection**  
   Ke Chen ⋅ Ling Zhou ⋅ Yi Liu ⋅ Guangqi Jiang ⋅ Gengshen Wu ⋅ Shoukun Xu  
   [arXiv:2606.26849](https://arxiv.org/abs/2606.26849) · [code](https://github.com/cke520/LFNet)
70. **LlamaSeg: Image Segmentation via Autoregressive Mask Generation**  
   Jiru Deng ⋅ Tengjin Weng ⋅ Tianyu Yang ⋅ Wenhan Luo ⋅ Zhiheng Li ⋅ Wenhao Jiang  
   [arXiv:2505.19422](https://arxiv.org/abs/2505.19422) · [code](https://github.com/GML-FMGroup/llamaseg)
71. **LongEgoRefer: A Benchmark for Long-Form Egocentric Video Referring Expression Comprehension**  
   Shunya Kato ⋅ Taiki Miyanishi ⋅ Shuhei Kurita ⋅ Mahiro Ukai ⋅ Nakamasa Inoue ⋅ Chenhui Chu  
   [arXiv:2607.02096](https://arxiv.org/abs/2607.02096) · [code](https://github.com/shunya-kato/LongEgoRefer)
72. **LoRC: Detecting AI-Generated Images via Low-Rank Collapse in the Semantic-Residual Space**  
   Haozhen Yan ⋅ Ruoxin Chen ⋅ Jiahui Zhan ⋅ Taiping Yao ⋅ Bo Wang ⋅ Youchang xiao ⋅ Shouhong Ding ⋅ Liqing Zhang ⋅ Jianfu Zhang
73. **Low-latency Event-based Object Detection with Spatially-Sparse Linear Attention**  
   Haiqing Hao ⋅ Zhipeng Sui ⋅ Rong Zou ⋅ Zijia Dai ⋅ Nikola Zubic ⋅ Davide Scaramuzza ⋅ Wenhui Wang  
   [arXiv:2603.06228](https://arxiv.org/abs/2603.06228)
74. **M4-SAR: A Multi-Resolution, Multi-Polarization, Multi-Scene, Multi-Source Dataset and Benchmark for optical-SAR Object Detection**  
   Chao Wang ⋅ Wei Lu ⋅ Xiang Li ⋅ Jian Yang ⋅ Lei Luo  
   [arXiv:2505.10931](https://arxiv.org/abs/2505.10931) · [code](https://github.com/wchao0601/M4-SAR)
75. **Map-Det3D: Metric Feed-Forward 3D Reconstruction Prior for Multi-view 3D Object Detection from Streaming Inputs**  
   Yung-Hsu Yang ⋅ Luigi Piccinelli ⋅ Samuel Rota Bulò ⋅ Sunghwan Hong ⋅ Denys Rozumnyi ⋅ Johannes Schönberger ⋅ Zuria Bauer ⋅ Hermann Blum ⋅ Peter Kontschieder ⋅ Marc Pollefeys  
   [arXiv:2608.12179](https://arxiv.org/abs/2608.12179) · [project](https://royyang0714.github.io/Map-Det3D)
76. **MediRound: Multi-Round Entity-Level Reasoning Segmentation in Medical Images**  
   Qinyue Tong ⋅ Ziqian Lu ⋅ Jun Liu ⋅ Rui Zuo ⋅ Zheming Lu ⋅ Yueming Jin  
   [arXiv:2511.12110](https://arxiv.org/abs/2511.12110) · [code](https://github.com/Edisonhimself/MediRound)
77. **MiNQVIS: Mitigating Noisy Queries for Robust Online Video Instance Segmentation**  
   Jie Qiao ⋅ Jianxu Chen ⋅ Xiaowei Xu
78. **Mitigating Pose–Scale Discrepancy Bias and Reforming Multi-Support Reasoning for Few-Shot Semantic Segmentation**  
   Shreya Biswas ⋅ Zhaozheng Yin
79. **MoCA3D: Monocular 3D Bounding Box Prediction in the Image Plane**  
   Changwoo Jeon ⋅ Rishi Upadhyay ⋅ Achuta Kadambi  
   [arXiv:2603.19538](https://arxiv.org/abs/2603.19538)
80. **ModuSeg: Decoupling Object Discovery and Semantic Retrieval for Training-Free Weakly Supervised Segmentation**  
   Qingze He ⋅ Fagui Liu ⋅ Dengke Zhang ⋅ Qingmao Wei ⋅ Quan Tang  
   [arXiv:2604.07021](https://arxiv.org/abs/2604.07021) · [code](https://github.com/Autumnair007/ModuSeg)
81. **MoMCE: Mixture of Modality and Cue Experts for Multimodal Deception Detection**  
   Dongliang Zhu ⋅ Ruimin Hu ⋅ Zitong Yu ⋅ Xiaobao Guo ⋅ Mei Wang ⋅ Shuo Ye ⋅ Fei Ma ⋅ Xiaochun Cao
82. **MomentSeg: Moment-Centric Sampling for Enhanced Referring Video Object Segmentation**  
   Ming Dai ⋅ Sen Yang ⋅ Boqiang Duan ⋅ Wankou Yang ⋅ Jingdong Wang
83. **MonoSR: Open-Vocabulary Spatial Reasoning on Monocular Images**  
   Qirui Wang ⋅ Jingyi He ⋅ Yining Pan ⋅ Si Yeo ⋅ Xulei Yang ⋅ Shijie Li  
   [arXiv:2511.19119](https://arxiv.org/abs/2511.19119)
84. **NegAS: Negative Label Guided Attention and Scoring for Out-of-Distribution Object Detection with Vision-Language Models**  
   Yingjie Zhang ⋅ Shuai Li ⋅ Peng Wang  
   [arXiv:2606.22537](https://arxiv.org/abs/2606.22537)
85. **NUN: Nested Unfolding Network for Real-World Concealed Object Segmentation**  
   Chunming He ⋅ Rihan Zhang ⋅ Longxiang Tang ⋅ Dingming Zhang ⋅ Bojian Zhang ⋅ Fengyang Xiao ⋅ Jingjia Feng ⋅ Sina Farsiu
86. **OBBSeg: Irregular Lesion Segmentation under Oriented Bounding Box Annotations**  
   Jun Wei ⋅ Xinchang Liu ⋅ Yu Liu ⋅ Chuhua Yang ⋅ Shuhui Wang ⋅ Hui Huang  
   [arXiv:2607.06007](https://arxiv.org/abs/2607.06007) · [code](https://github.com/StarLxc3/OBBSeg)
87. **Online 3D Instance Segmentation at task-oriented granularity with Unposed Monocular Video**  
   Dong Wu ⋅ Baicheng Li ⋅ Yingdian Cao ⋅ Shunkai Zhou ⋅ Yiwen Lu ⋅ Hongbin Zha
88. **Online Reasoning Video Object Segmentation**  
   jinyuan Liu ⋅ Yang Wang ⋅ Zeyu Zhao ⋅ Weixin Li ⋅ Song Wang ⋅ Ruize Han  
   [arXiv:2604.11411](https://arxiv.org/abs/2604.11411)
89. **OP3DSG: Open-vocabulary Part-aware 3D Scene Graph Generation for Real-world Environments**  
   Yirum Kim ⋅ Ue-Hwan Kim  
   [arXiv:2606.29786](https://arxiv.org/abs/2606.29786)
90. **Open-Vocabulary 3D Object Detection with Co-Distillation Discovery and Dual Guidance Robust Training**  
   Shangbo Yuan ⋅ Jie Xu ⋅ Xiaofeng Zhu ⋅ Na Zhao
91. **Open-Vocabulary BEV Segmentation with 3D-Aware Geometric Constraints**  
   Hojun Choi ⋅ Seulbin Hwang ⋅ Dae Kim ⋅ Kisung Kim ⋅ Hyunjung Shim ⋅ Jinhan Lee  
   [arXiv:2606.24353](https://arxiv.org/abs/2606.24353) · [project](https://hchoi256.github.io/projects/ovbevseg/)
92. **Open-Vocabulary Long Term Action Anticipation**  
   Syed Talal Wasim ⋅ Jinhui Yi ⋅ Hamid Suleman ⋅ Ahmad Javed ⋅ Yanan Luo ⋅ Muhammad Muzammal Naseer ⋅ Juergen Gall
93. **OpenPanoD: Aligning Multimodal Prompts and Spherical Representations for Open-Vocabulary Panoramic Detection**  
   Hang Xu
94. **Orthogonal Knowledge Refreshing for Domain-Incremental Object Detection**  
   Aoting Zhang ⋅ Dongbao Yang ⋅ Chang Liu ⋅ Xiaopeng Hong ⋅ Can Ma ⋅ Yu ZHOU  
   [arXiv:2607.17340](https://arxiv.org/abs/2607.17340)
95. **P3-SAM: Native 3D Part Segmentation**  
   CHANGFENG MA ⋅ YANG LI ⋅ Xinhao Yan ⋅ Jiachen Xu ⋅ Yunhan Yang ⋅ Chunshi Wang ⋅ Zibo Zhao ⋅ Yanwen Guo ⋅ Zhuo Chen ⋅ Chunchao Guo  
   [arXiv:2509.06784](https://arxiv.org/abs/2509.06784) · [project](https://murcherful.github.io/P3-SAM/)
96. **Pano3D: Unified 3D Reconstruction and Panoptic Segmentation**  
   Victor Barberteguy ⋅ Ahmet Iscen ⋅ Mathilde Caron ⋅ Alireza Fathi ⋅ Gül Varol ⋅ Cordelia Schmid  
   [arXiv:2606.14307](https://arxiv.org/abs/2606.14307) · [project](https://victorbbt.github.io/Pano3D/)
97. **PASR: Pattern-Aware Scene-Conditioned Reasoning for Camouflaged Object Detection**  
   Xinyu Wang ⋅ Jintang Xue ⋅ C.-C. Jay Kuo
98. **Per‑Object IoU Forecasting for Deadline‑Aware Real‑Time Embedded Detection Control**  
   Erfan Foorginejad ⋅ Akshar Chavan ⋅ Marco Brocanelli
99. **PhenoLeaf-TS: A Time-Series Benchmark for Leaf Instance Segmentation, Tracking, and Growth Stage Classification**  
   Rijad Saric ⋅ Basim Azam ⋅ Sarmad Khan ⋅ Edhem Custovic
100. **PhysFlowNet: Learning Canonical Latent Manifolds via Spatio-Spectral Physics Priors for Underwater Object Detection**  
   XUETING Liu ⋅ Haoyu Ji ⋅ Wenze Huang ⋅ Zhihao Yang ⋅ Yu Gao ⋅ Weihong Ren ⋅ Zhiyong Wang ⋅ Honghai Liu
101. **Pixel-wise Planarity for High-Precision Monocular Plane Segmentation**  
   Ahmetcan Yavuz ⋅ Alpay Ozkan ⋅ Rémi Pautrat ⋅ Shaohui Liu ⋅ Marc Pollefeys
102. **PKINet-v2: Towards Powerful and Efficient Poly-Kernel Remote Sensing Object Detection**  
   Xinhao Cai ⋅ Liulei Li ⋅ Gensheng Pei ⋅ Zeren Sun ⋅ Yazhou Yao ⋅ Wenguan Wang  
   [arXiv:2603.16341](https://arxiv.org/abs/2603.16341)
103. **PLOT: Pseudo-Labeling via Object Tracking for Monocular 3D Object Detection**  
   SeokYeong Lee ⋅ Sithu Aung ⋅ JunYong Choi ⋅ Seungryong Kim ⋅ Ig-Jae Kim ⋅ Junghyun Cho
104. **PointLAM: Local Attentive Mamba for Efficient Point-based 3D Object Detection**  
   Xuanming Shang ⋅ Weijia Zhang ⋅ Chao Ma
105. **QASA: Quality-Guided K-Adaptive Slot Attention for Unsupervised Object-Centric Learning**  
   Tianran Ouyang ⋅ Xingping Dong ⋅ Jing Zhang ⋅ Mang Ye ⋅ Kaihao Zhang ⋅ Bo Du  
   [arXiv:2601.12936](https://arxiv.org/abs/2601.12936)
106. **QST-SAM: Leveraging Cross-modal Instructions for Few-shot Referring Video Object Segmentation**  
   Xin Liu ⋅ Weijia Li ⋅ Tao Chen ⋅ Hongsong Wang ⋅ Guosen Xie ⋅ Caifeng Shan ⋅ Fang Zhao
107. **RA-SOD: Reliability-Aware RGB-T Salient Object Detection under Modality Degradation**  
   Hongbo Gao ⋅ Zhengyu Li ⋅ XUERU NIE ⋅ Dihao Zhu ⋅ lijun zhao ⋅ Yunke Wang ⋅ Chang Xu
108. **RAF: Reliability-Aware Fusion of Camera, LiDAR, and 4D RADAR for Robust 3D Object Detection in Adverse Weather**  
   Heejun Park ⋅ Jaeseok Jeong ⋅ KUK-JIN YOON  
   [arXiv:2607.04587](https://arxiv.org/abs/2607.04587) · [code](https://github.com/parkie0517/RAF)
109. **REAL-OW: Rehearsal-free Open World Object Detection with Low-Rank Adaptation and Dual-Stage Objectness Modeling**  
   Huazhong Zhang ⋅ Xiaowen Fu ⋅ Yang Zhang ⋅ Linlin Shen ⋅ Jinbao Wang  
   [arXiv:2607.03004](https://arxiv.org/abs/2607.03004)
110. **Real-Time Source-Free Object Detection**  
   Sairam V C Rebbapragada ⋅ Varun Gopal ⋅ Poornima Jain ⋅ Vineeth N Balasubramanian ⋅ Muhammad Haris Khan  
   [arXiv:2606.31834](https://arxiv.org/abs/2606.31834) · [code](https://github.com/Sairam13001/RT-SFOD/)
111. **ReliefSAM: A Geometry-Augmented Multi-Prior Adapter for Bas-Relief Segmentation**  
   YIHANG CHEN ⋅ Xiang Lyu ⋅ Rui Xu ⋅ Jiao PAN ⋅ Fadjar Thufail ⋅ Brahmantara Brahmantara ⋅ JIAQING LIU ⋅ Satoshi Tanaka ⋅ Liang Li
112. **Rethinking Prototype-based Similarity Learning for Few-Shot Object Detection**  
   KunHo Heo ⋅ Seungjae kim ⋅ Wongyu Lee ⋅ SuYeon Kim ⋅ MyeongAh Cho  
   [arXiv:2606.23069](https://arxiv.org/abs/2606.23069) · [code](https://github.com/VisualScienceLab-KHU/ReSet)
113. **Rethinking Pseudo-Labels: Multi-Granularity Supervision for Domain Adaptive Object Detection**  
   Haohao Ma ⋅ Weimin Lu ⋅ Qiqi Ge
114. **RiO-DETR: DETR for Real-time Oriented Object Detection**  
   Zhangchi Hu ⋅ Yifan Zhao ⋅ Yansong Peng ⋅ Wenzhang SUN ⋅ Xiangchen Yin ⋅ Jie Chen ⋅ Peixi Wu ⋅ Hebei Li ⋅ xinghao wang ⋅ Dongsheng Jiang ⋅ Xiaoyan Sun  
   [arXiv:2603.09411](https://arxiv.org/abs/2603.09411) · [code](https://github.com/RicePasteM/RiO-DETR)
115. **Robust onion: Peeling Open Vocab Object Detectors Under Noise**  
   Priyank Pathak ⋅ Mukilan Karuppasamy ⋅ Aaditya Baranwal ⋅ Shruti Vyas ⋅ Yogesh Rawat  
   [arXiv:2606.26734](https://arxiv.org/abs/2606.26734)
116. **RT-DETRv4: Painlessly Furthering Real-Time Object Detection with Vision Foundation Models**  
   Zijun Liao ⋅ Yian Zhao ⋅ Xin Shan ⋅ Yu Yan ⋅ Chang Liu ⋅ lei lu ⋅ Xiangyang Ji ⋅ Jie Chen  
   [arXiv:2510.25257](https://arxiv.org/abs/2510.25257)
117. **RT-SDGOD: Real-Time Single-Domain Generalized Object Detection**  
   Yupeng Zhang ⋅ Fangzhuo Gao ⋅ Ruize Han ⋅ Wei Feng ⋅ Liang Wan  
   [arXiv:2606.09367](https://arxiv.org/abs/2606.09367)
118. **S2-FracMix: Self-Saliency Fractal Mixup**  
   Khawar Islam ⋅ Arif Mahmood ⋅ Xin Jin ⋅ NAVEED AKHTAR
119. **Safe Generalization: Mitigating Catastrophic Forgetting in Single-Source Multi-Organ Segmentation via Collaborative Causal Learning**  
   Yucheng Song ⋅ Ruoxi Yu ⋅ Feng Shu ⋅ Cheng Huang ⋅ HaoKang Ding ⋅ Zhifang Liao
120. **SAM-MT: Real-Time Interactive Multi-Target Video Segmentation**  
   Ruiqi Shen ⋅ Chang Liu ⋅ Henghui Ding  
   [arXiv:2607.08688](https://arxiv.org/abs/2607.08688) · [project](https://henghuiding.com/SAM-MT/)
121. **SAM2Matting: Generalized Image and Video Matting**  
   Ruiqi Shen ⋅ Guangquan Jie ⋅ Chang Liu ⋅ Henghui Ding  
   [arXiv:2606.27339](https://arxiv.org/abs/2606.27339) · [project](https://henghuiding.com/SAM2Matting/)
122. **SARIF: Segment Anything for Robust Image Forensics**  
   Dong-Hyun Moon ⋅ Ju-Hyeon Nam ⋅ Sang-Chul Lee  
   [arXiv:2606.21108](https://arxiv.org/abs/2606.21108) · [code](https://github.com/Inha-CVAI/SARIF_ECCV2026)
123. **Seeing as Humans Do: Learning from Motion to Segment Anything Without Supervision**  
   Weijian Jian ⋅ Xiaoyue Zhang ⋅ Bin Xiao ⋅ Chunyu Xie ⋅ Yixiao He ⋅ Yutao Liu ⋅ Dawei Leng ⋅ Yuhui Yin
124. **Segmenting Visuals With Querying Words: Language Anchors For Semi-Supervised Image Segmentation**  
   Numair Nadeem ⋅ Saeed Anwar ⋅ Muhammad Asad ⋅ Abdul Bais  
   [arXiv:2506.13925](https://arxiv.org/abs/2506.13925)
125. **Segmenting, Fast and Slow: Real-Time Open-Vocabulary Video Instance Segmentation with Dual-Path Processing**  
   Luca Barsellotti ⋅ Martin Sundermeyer ⋅ Mattia Segu ⋅ Nikita Araslanov ⋅ Muhammad Ferjad Naeem ⋅ Marcella Cornia ⋅ Yongqin Xian ⋅ Maxim Berman  
   [arXiv:2607.00124](https://arxiv.org/abs/2607.00124)
126. **SegPAR: Class-Centric Decision-Based Sparse Attack for Semantic Segmentation**  
   Dongsu Song ⋅ Daeyun Go ⋅ BOSEUNG SEO ⋅ Jay Hoon Jung  
   [arXiv:2608.11285](https://arxiv.org/abs/2608.11285) · [code](https://github.com/KAU-QuantumAILab/SegPAR)
127. **Selective Synergistic Learning for Video Object-Centric Learning**  
   WonJun Moon ⋅ Jae-Pil Heo  
   [arXiv:2606.15527](https://arxiv.org/abs/2606.15527)
128. **SEMIR: Topology-Preserving Graph Minors for Thin-Structure Segmentation**  
   Luke Miller ⋅ Yugyung Lee  
   [arXiv:2606.24935](https://arxiv.org/abs/2606.24935)
129. **SFD-Net: Sharp Feature Detection Network Based on Local Geometric Features**  
   Inyoung Oh ⋅ Kwanghee Ko
130. **SGQA: Semantic-Geometric Quality Alignment for Training-Free Few-Shot Instance Segmentation**  
   Yuhao Qing ⋅ Liuyan Feng ⋅ Haoyuan Li
131. **Slim-DETR: Real-Time Tiny Object Detection with Efficient Interaction and Gaussian Query**  
   Tong Wu ⋅ Jiahao Zhang ⋅ Juntao Guan ⋅ Lai Rui
132. **SOVTrack: Open-Vocabulary Multi-Object Tracking with Self-Supervised Pseudo Labeling and Feature Distillation**  
   Zekun QIAN ⋅ Ruize Han ⋅ Junhui Hou ⋅ Wei Feng
133. **StAR: Segment Anything Reasoner**  
   Seokju Yun ⋅ Dongheon Lee ⋅ Noori Bae ⋅ Jaesung Jun ⋅ Chanseul Cho ⋅ Youngmin Ro
134. **Sticking Information in Plain Sight: Encoding and Detecting Hidden Stickers in the Real World**  
   Christina Shatford ⋅ Szymon Rusinkiewicz
135. **Taming Dynamic Clutter: Variance-Driven Adaptive Gain Control for Bio-inspired Small Target Detection**  
   Jiaxiang Li ⋅ Shaobing Gao ⋅ Qinbing Fu ⋅ Meiyi Li ⋅ Tiansheng Lu ⋅ Minjie Tan
136. **Task-Agnostic Incremental Vision-Language Object Detection via Prompt Augmentation and Distribution-Aware Fusion**  
   Yonghan Jiang ⋅ Zhengyuan Xie ⋅ Wenchu Liu ⋅ Linlan Huang ⋅ Fei Yang ⋅ Xialei Liu
137. **TMI: Text-to-Image Meets Image-to-Image for Complementary Data Synthesis to Boost Long-Tailed Instance Segmentation**  
   Hyeonseop Song ⋅ Seokhun Choi ⋅ Hoseok Do  
   [arXiv:2607.08201](https://arxiv.org/abs/2607.08201) · [project](https://seokhunchoi.github.io/TMI)
138. **Toward Robust In-Context Segmentation via Concept Guidance**  
   Zhigang Chen ⋅ Xiawu Zheng ⋅ Rongrong Ji  
   [arXiv:2606.28149](https://arxiv.org/abs/2606.28149) · [code](https://github.com/Kakarot1103/CG-ICS)
139. **Towards High-Resolution Visual Perception via Hierarchical Entity Exploration**  
   Ziyu Ma ⋅ Shidong Yang ⋅ Yuxiang Ji ⋅ Yiming Hu ⋅ Tongwen Huang ⋅ Yong Wang ⋅ Jianfei Cai ⋅ Xiangxiang Chu  
   [arXiv:2607.00816](https://arxiv.org/abs/2607.00816)
140. **Towards Open-World Referring Expression Comprehension: A Benchmark with Training-free Multi-task Consistency Checker**  
   Zongjian Wu ⋅ Lei Zhang  
   [arXiv:2605.25706](https://arxiv.org/abs/2605.25706) · [project](https://zongjianwu.github.io/openref)
141. **Towards Sparsely Annotated Open World Object Detection**  
   HEEJU HAN ⋅ AJEONG KIM ⋅ Jinsun Park  
   [arXiv:2608.12714](https://arxiv.org/abs/2608.12714)
142. **Towards Unsupervised Multi-modal Semantic Segmentation**  
   Haitian Zhang ⋅ Thai Nguyen ⋅ Xiangyuan Wang ⋅ Mohan Liu ⋅ Addison Wang  
   [arXiv:2607.12372](https://arxiv.org/abs/2607.12372)
143. **UniPart: Towards Zero-shot Language-Grounded 3D Part Segmentation for Embodied Interaction**  
   Xinqiang Yu ⋅ Zekun Qi ⋅ Jiawei He ⋅ Wenyao Zhang ⋅ Xuchuan Chen ⋅ Guocai Yao ⋅ Li Yi ⋅ Zhaoxiang Zhang ⋅ HE WANG
144. **Unsupervised Semantic Segmentation Facilitates Model Understanding**  
   Xiaoyan Yu ⋅ Lisa Mais ⋅ Peter Hirsch ⋅ Nick Lechtenbörger ⋅ Jannik Franzen ⋅ Andreas Mardt ⋅ Dagmar Kainmueller  
   [arXiv:2605.29691](https://arxiv.org/abs/2605.29691)
145. **VCP-DCN: Beyond Visual Concealed Property via Depth Collaborative Network for Camouflaged Object Detection**  
   Songsong Duan ⋅ Xi Yang ⋅ Nannan Wang  
   [arXiv:2607.27843](https://arxiv.org/abs/2607.27843)
146. **What is the Right Embedding Space for Contrastive Learning in Referring Expression Counting?**  
   Kostas Triaridis ⋅ Panagiotis Kaliosis ⋅ E-Ro Nguyen ⋅ Jingyi Xu ⋅ Dimitris Samaras ⋅ Hieu Le
147. **When Specialists Meet Generalists: Segmenter-Coordinated Asymmetric Learning for Label-Deficient Concealed Object Segmentation**  
   Chunming He ⋅ Dingming Zhang ⋅ Longxiang Tang ⋅ Ziyun Yang ⋅ Fengyang Xiao ⋅ Sina Farsiu
148. **When W4A4 Breaks Camouflaged Object Detection: Token-Group Dual-Constraint Activation Quantization**  
   Tianqi Li ⋅ Wenyu Fang ⋅ Xin He ⋅ Xue Geng ⋅ Xu Cheng ⋅ Yun Liu  
   [arXiv:2604.16855](https://arxiv.org/abs/2604.16855) · [code](https://github.com/MCG-NKU/nku-model-compre)
149. **X2SAM: Any Segmentation in Images and Videos**  
   Hao Wang ⋅ Limeng Qiao ⋅ Chi Zhang ⋅ Lin Ma ⋅ Guanglu Wan ⋅ Xiangyuan Lan ⋅ Xiaodan Liang  
   [arXiv:2605.00891](https://arxiv.org/abs/2605.00891)
150. **ZMIS-SAM: Segment Anything Model Enhanced With Wavelet Transform For Zooplankton Microscopy Image Instance Segmentation**  
   Dekun Yuan ⋅ Zhongwei Li ⋅ Zheng Qiao ⋅ Jie Zhang  
   [arXiv:2607.27585](https://arxiv.org/abs/2607.27585)

## Tracking & Correspondence over Time

*31 papers · 13 with links*

1. **Back-Tracking from Clarity: Self-Learning to See Text from Afar**  
   Duc Tri Tran ⋅ Phi Le Nguyen ⋅ Minh Hoai Nguyen
2. **CoMaTrack: Competitive Multi-Agent Game-Theoretic Tracking with Vision-Language-Action Models**  
   Li Gao ⋅ Liu Liu ⋅ Mingyang Lyu ⋅ Yang Cai  
   [arXiv:2603.22846](https://arxiv.org/abs/2603.22846) · [code](https://github.com/wlqcode/CoMaTrack-Bench)
3. **ConTrack: Constrained Hand Motion Tracking with Adaptive Trade-off Control**  
   Yutong Liang ⋅ Quanquan Peng ⋅ Rizhao Qiu ⋅ Xiaolong Wang  
   [arXiv:2606.03177](https://arxiv.org/abs/2606.03177) · [project](https://www.lyt0112.com/projects/ConTrack)
4. **Cross-Species Animal Re-Identification with Semantic Consistency Learning**  
   Shuoyi Chen ⋅ Yuejia Li ⋅ Mang Ye
5. **FeatTracker: Short- and Long-Range Temporal Feature Consistency for Robust Underwater Object Tracking**  
   Jiaqing Li ⋅ Bin Lin ⋅ Chaocan Xue ⋅ Wu Ai ⋅ Qingping Zheng
6. **FusionTrack: Collaborative Multi-Object Tracking with Arbitrary Multi-UAVs**  
   Xiaohe Li ⋅ Pengfei Li ⋅ Kaixin Zhang ⋅ Jiahao Li ⋅ Zide Fan
7. **GAP-Track: Bridging the Resolution Gap for Cross-Resolution RGBT Tracking**  
   Shiyu Zhang ⋅ Tianyang Xu ⋅ Zhangyong Tang ⋅ Wang He ⋅ Xiao-Jun Wu ⋅ Josef Kittler
8. **GoStop: Reinforcement Learning for Adaptive Temporal Aggregation in Event-Based Feature Tracking**  
   Youngho Kim ⋅ Hoonhee Cho ⋅ Jae-young Kang ⋅ KUK-JIN YOON  
   [arXiv:2607.15699](https://arxiv.org/abs/2607.15699) · [code](https://github.com/kmax2001/GoSTOP)
9. **HieDG: A Hierarchical Discrete Geometry-Guided Framework for Multi-Animal Tracking**  
   Chenxun Deng ⋅ Zhongde Zhang ⋅ Ye Yuan ⋅ Chengyang Zhang ⋅ Yifan Zhang ⋅ Bohao Chen ⋅ Hongying Yan ⋅ Hang Zhou ⋅ Hua Han ⋅ Xi Chen  
   [arXiv:2607.00494](https://arxiv.org/abs/2607.00494)
10. **High-Throughput Event-Based Feature Detection and Tracking on an Embedded CPU**  
   Ethan Elms ⋅ Yasir Latif ⋅ Tat-Jun Chin
11. **History-Aware Transformation of ReID Features for Multiple Object Tracking**  
   Ruopeng Gao ⋅ Yuyao Wang ⋅ Chunxu Liu ⋅ Limin Wang  
   [arXiv:2503.12562](https://arxiv.org/abs/2503.12562) · [code](https://github.com/MCG-NJU/HATReID-MOT)
12. **HumanTracker: Towards Comprehensive and Human-Aligned Motion Tracking Benchmark**  
   Dairu Liu ⋅ Zekun Qi ⋅ Jiayu Zeng ⋅ Yu Guan ⋅ Chenghuai Lin ⋅ Xuchuan Chen ⋅ Xinqiang Yu ⋅ Wenyao Zhang ⋅ HE WANG ⋅ Li Yi  
   [arXiv:2608.13555](https://arxiv.org/abs/2608.13555)
13. **Incentive Noise and Structural Prior Infusion for Multi-Modal Object Re-Identification**  
   Weixiang Zhou ⋅ Yuhao Wang ⋅ Xingguo Xu ⋅ Cong Wang ⋅ Weizhen Zhou ⋅ Zhixun Su ⋅ Jinshan Pan
14. **Instance Segmentation as Tracking: A New Paradigm for Multi-Small-Object Tracking with Event Cameras**  
   Nuo Chen ⋅ Shiman He ⋅ Boyang Li ⋅ Yingqian Wang ⋅ Chao Xiao ⋅ QianYin QianYin ⋅ Ruojing Li ⋅ Yihang Luo ⋅ Wei An ⋅ Miao Li
15. **Local-to-global Cross-modal Coordination for Self-supervised RGB-T Tracking**  
   Yueying Zhang ⋅ Timing Li ⋅ Bing Cao ⋅ Pengfei Zhu
16. **Mode-Conditioned Residual Calibration for Multi-Object Tracking**  
   Muyu Li ⋅ Henan Hu ⋅ Deepak Jain ⋅ Xudong Zhao
17. **ModTrack: Sensor-Agnostic Multi-View Tracking via Identity-Informed PHD Filtering with Covariance Propagation**  
   Aditya Iyer ⋅ Jack Roberts ⋅ Nora Ayanian  
   [arXiv:2603.15812](https://arxiv.org/abs/2603.15812)
18. **Motion-aware Sparse Pipeline for Lightweight Object Tracking**  
   Qingmao Wei ⋅ Fagui Liu ⋅ Dengke Zhang ⋅ Qingze He ⋅ Quan Tang
19. **MuCHeR: Multi-Person Camera-Centric Human Detection, Mesh Recovery and Tracking**  
   Guénolé Fiche ⋅ Philippe Weinzaepfel ⋅ Romain Brégier ⋅ Fabien Baradel
20. **OCTA-SOT: Online Cross-Modal Trajectory Adjustment for RGBT Anti-UAV Single Object Tracking under Spatio-Temporal Misalignment**  
   Xiaokang Liu ⋅ Qi Jia ⋅ Jinrui Wang ⋅ Chengzhou Li ⋅ Yu Liu ⋅ Weimin Wang
21. **ODONet: Online Dynamic Offset Network for Visual Object Tracking**  
   Qinghua Liu ⋅ Wanli Xue ⋅ Shengyong Chen
22. **Progressively Spiral Mamba Fusion for Multimodal Tracking**  
   Zixuan Wang ⋅ Baojie Fan ⋅ Jiajun Ai ⋅ Wenzhang Zhou
23. **PS-MOT: Cultivating Instance Awareness from Point Seeds for Multi-Object Tracking**  
   Kai Luo ⋅ Fei Teng ⋅ Mengfei Duan ⋅ Wanjun Jia ⋅ Xu Wang ⋅ Hao Shi ⋅ Kunyu Peng ⋅ Zhiyong Li ⋅ Kailun Yang  
   [arXiv:2606.30476](https://arxiv.org/abs/2606.30476) · [code](https://github.com/xifen523/PS-MOT)
24. **Region-Aware Multimodal Interleaving for Animal Re-Identification**  
   Yihao Wu ⋅ Di Zhao ⋅ Wayne Getz ⋅ Lingqiao Liu ⋅ Gillian Dobbie ⋅ Daniel Wilson ⋅ Yun Sing Koh
25. **Rethinking Temporal Modeling in Visual Object Tracking via Decoupled Auxiliary Supervision**  
   Dailing Zhang ⋅ Shiyu Hu ⋅ Honghao Fu ⋅ Xiaokun Feng ⋅ Yipei Wang ⋅ Kang Cheong ⋅ Kaiqi Huang
26. **RT-RMOT: A Dataset and Framework for RGB-Thermal Referring Multi-Object Tracking**  
   Yanqiu Yu ⋅ Zhifan Jin ⋅ Sijia Chen ⋅ Tongfei Chu ⋅ En Yu ⋅ Liman Liu ⋅ Wenbing Tao  
   [arXiv:2602.22033](https://arxiv.org/abs/2602.22033)
27. **SENTRY: SAM2-Enhanced Neighbor-Aware and Temporally Reasoned Memory for Visual Tracking**  
   Mohamad Alansari ⋅ Yonathan Michael ⋅ Hasan AlMarzouqi ⋅ Muhammad Muzammal Naseer ⋅ Naoufel Werghi ⋅ Sajid Javed  
   [arXiv:2606.24449](https://arxiv.org/abs/2606.24449) · [project](https://hamadya.github.io/SENTRY/page/)
28. **SpectralSplats: Robust Differentiable Tracking via Spectral Moment Supervision**  
   Avigail Cohen Rimon ⋅ Amir Mann ⋅ Mirela Ben-Chen ⋅ Or Litany  
   [arXiv:2603.24036](https://arxiv.org/abs/2603.24036) · [project](https://avigailco.github.io/SpectralSplats/)
29. **Stabilizing Real-World Visual Active Tracking with Action-Smooth Test-Time Adaptation**  
   Haowei Sun ⋅ Shiteng Zhang ⋅ Jinwu Hu ⋅ Kaining Chen ⋅ Mingkui Tan
30. **TETO: Tracking Events with Teacher Observation for Motion Estimation and Frame Interpolation**  
   Jini Yang ⋅ Eunbeen Hong ⋅ Soowon Son ⋅ Hyunkoo Lee ⋅ Sunghwan Hong ⋅ Sunok Kim ⋅ Seungryong Kim  
   [arXiv:2603.23487](https://arxiv.org/abs/2603.23487)
31. **Track4World: Feedforward World-centric Dense 3D Tracking of All Pixels**  
   Jiahao Lu ⋅ Jiayi Xu ⋅ WENBO HU ⋅ Ruijie Zhu ⋅ Chengfeng Zhao ⋅ Sai Kit Yeung ⋅ Ying Shan ⋅ Yuan Liu  
   [arXiv:2603.02573](https://arxiv.org/abs/2603.02573) · [code](https://github.com/TencentARC/Track4World) · [project](https://jiah-cloud.github.io/Track4World.github.io/)

## Anomaly & Out-of-Distribution Detection

*52 papers · 27 with links*

1. **A Comprehensive Analysis about Unsupervised Outlier Detection for Images**  
   Zhonghang Liu ⋅ Siyuan Chen ⋅ Jingwen Yu ⋅ Changshuo Wang ⋅ Kunyang Li ⋅ Jiangbo Lu
2. **Anomaly Factory 3D: A Modular Framework for Diverse Pseudo-Anomaly Synthesis in Unsupervised 3D Anomaly Detection**  
   Ali Balapour ⋅ Faraz Hach  
   [arXiv:2606.29181](https://arxiv.org/abs/2606.29181)
3. **ArcAD: Anomaly-Rectified Calibration for Cold-Start Supervised Anomaly Detection**  
   Ningning Han ⋅ Lei Fan ⋅ Jia Guo ⋅ Yunkang Cao ⋅ Xiu Su ⋅ Feng Cao ⋅ Donglin Di ⋅ Tonghua Su  
   [arXiv:2607.02252](https://arxiv.org/abs/2607.02252) · [code](https://github.com/LGC-AD/ArcAD)
4. **BAAF: Universal Transformation of One-Class Classifiers for Unsupervised Image Anomaly Detection**  
   Declan McIntosh ⋅ Alexandra Branzan Albu  
   [arXiv:2602.13091](https://arxiv.org/abs/2602.13091)
5. **BATQuant: Outlier-Resilient MXFP4 Quantization via Learnable Block-wise Optimization**  
   Jifu Li ⋅ Manyi Zhang ⋅ Xiaobo Xia ⋅ Han Bao ⋅ Haoli Bai ⋅ Zhenhua Dong ⋅ Xianzhi Yu  
   [arXiv:2603.16590](https://arxiv.org/abs/2603.16590)
6. **Beyond Common Sense: Grounding Logical Anomaly Detection in Inspection Criteria**  
   Yuanze Li ⋅ YuanShihao YuanShihao ⋅ Zimeng Zhu ⋅ Ming LIU ⋅ Wangmeng Zuo ⋅ Guangming Shi
7. **Beyond Prompts: Unconditional 3D Inversion for Out-of-Distribution Shapes**  
   Victoria Chen ⋅ Emery Pierson ⋅ Léopold Maillard ⋅ Maks Ovsjanikov  
   [arXiv:2604.14914](https://arxiv.org/abs/2604.14914) · [project](https://daidedou.sorpi.fr/publication/beyondprompts)
8. **Bounding-Box Trajectories Matter for Video Anomaly Detection**  
   Inpyo Song ⋅ Jangwon Lee  
   [arXiv:2605.21957](https://arxiv.org/abs/2605.21957)
9. **CL-Anomaly: Layer-Adaptive Mixture-of-Experts with Multimodal Large Language Model for Continual Learning in Anomaly Detection**  
   Wen Dong ⋅ Zhao Wang ⋅ Shuangqing Zhang ⋅ Kai Sun ⋅ Ben Li ⋅ Guosen Xie ⋅ Caifeng Shan ⋅ Fang Zhao  
   [arXiv:2607.02930](https://arxiv.org/abs/2607.02930) · [code](https://github.com/WenDongyp/CL-Anomaly)
10. **CLUE-VAD: Structured Semantic Clues for Understanding Explainable Events in Video Anomaly Detection**  
   MYOUNG-CHUL KIM ⋅ Junhee Lee ⋅ ChaeBeen Bang ⋅ MyeongAh Cho
11. **CMDS-AD: Cross-Modal Dual-Stream Decoupling for Few-Shot Anomaly Detection**  
   Junhao Cai ⋅ Deyu Zeng ⋅ Junhao Pang ⋅ JunYu Chen ⋅ Qiwei Liang ⋅ Xiaopin ZHONG ⋅ Zongze Wu  
   [arXiv:2606.20300](https://arxiv.org/abs/2606.20300) · [code](https://github.com/Junhaocai27/CMDS-AD) · [project](https://cmds-ad.github.io/)
12. **DeCo: Zero-Shot Anomaly Generation through Decoupling and Recoupling**  
   Shilei Zeng ⋅ Xurui Li ⋅ Yaohan Tang ⋅ Yu Zhou  
   [arXiv:2608.07904](https://arxiv.org/abs/2608.07904) · [code](https://github.com/HUST-SLOW/DeCo)
13. **DeCoFlow: Structural Decomposition of Normalizing Flows for Continual Anomaly Detection**  
   hun im ⋅ Jungi Lee ⋅ Subeen Cha ⋅ Pilsung Kang  
   [arXiv:2606.26687](https://arxiv.org/abs/2606.26687)
14. **DeltaDeno: Zero-Shot Anomaly Generation via Delta-Denoising Attribution**  
   Chaoran Xu ⋅ Chengkan Lv ⋅ Qiyu Chen ⋅ Yunkang Cao ⋅ Feng Zhang ⋅ Zhengtao Zhang  
   [arXiv:2511.16920](https://arxiv.org/abs/2511.16920) · [code](https://github.com/CROVO1026/DeltaDeno)
15. **DeMuS: Learning Decoupled Matching and Scoring for Batch Zero-Shot Industrial Anomaly Detection**  
   Zhengyang Zhao ⋅ Hailong Sun ⋅ Binhang Qi ⋅ Hongrui Yu ⋅ Zhongchi Wang ⋅ Hang Xu
16. **Distribution-Aware Feature Selection for Post-hoc Out-of-Distribution Detection**  
   Max Gutbrod ⋅ David Rauber ⋅ Christoph Palm
17. **Divide and Align: Disentangled Vision-Language Learning for Text-Based Person Anomaly Search**  
   Alex Ergasti ⋅ Tomaso Fontanini ⋅ Claudio Ferrari ⋅ Massimo Bertozzi ⋅ Andrea Prati
18. **ECC: Encoder-Centric Corruption for Fine-Grained Vision in VLMs**  
   Hyesong Choi ⋅ Daeun Kim ⋅ Sungmin Cha ⋅ Kwang Moo Yi ⋅ Dongbo Min
19. **EGVLR: Evidence-Grounded Vision–Language Reinforcement for Anomaly Reasoning**  
   SHIH-CHIH(Leo) LIN ⋅ Ying-Heng Lu ⋅ DONG YE ⋅ Shang-Hong Lai
20. **Exploiting Local Flatness for Efficient Out-of-Distribution Detection**  
   Seonghwan Park ⋅ Hyunji Jung ⋅ Dongyeop Lee ⋅ Namhoon Lee  
   [arXiv:2606.29952](https://arxiv.org/abs/2606.29952)
21. **Fast Dynamic Prototypes for Unsupervised Anomaly Detection and Localization**  
   Mingliang Li ⋅ Hanxi Li ⋅ Lin Wu ⋅ Changhong Liu ⋅ Xiaowei Zhao
22. **FlowDec: Temporal Conditional Flow Decorruptor for Robust Continuous Vision-Language Navigation**  
   Yufei Zhang ⋅ Changhao Chen  
   [arXiv:2606.22424](https://arxiv.org/abs/2606.22424)
23. **FuDU: A Fuzzy Dual-dimension Uncertainty Framework for Streaming Active Learning in Industrial Defect Detection**  
   Zhaoyang Wang ⋅ Haiyong Chen ⋅ Binyi Su ⋅ Xinwei Lyu
24. **Global Logic and Local Search: Dual-Stream Multimodal In-Context Learning for Verifiable Industrial Anomaly Detection**  
   Runzhi Deng ⋅ Yundi Hu ⋅ Yiming Zhong ⋅ Zhao Wang ⋅ Xixi Liu ⋅ Hongsong Wang ⋅ Caifeng Shan ⋅ Fang Zhao  
   [arXiv:2607.03817](https://arxiv.org/abs/2607.03817)
25. **GroundingAnomaly: Spatially-Grounded Diffusion for Few-Shot Anomaly Synthesis**  
   Yishen Liu ⋅ Hongchang Chen ⋅ Pengcheng Zhao ⋅ Yunfan Bao ⋅ Yuxi Tian ⋅ Jieming Zhang ⋅ HAO CHEN ⋅ Zhi Zheng ⋅ Yongchun Liu ⋅ Ying Li ⋅ Dongpu Cao  
   [arXiv:2604.08301](https://arxiv.org/abs/2604.08301)
26. **HLRAD: High-dimensional Latent Representation for Unified Anomaly Detection**  
   Tianrui Zhang ⋅ Ziheng Zang ⋅ Ningmu Zou
27. **If It's Not Efficient, It's Not Usable: Real-Time OOD Detection with Latent De-Biasing and High-Quality Negative Samples**  
   Yuchuan Li ⋅ Jae-Mo Kang ⋅ Il-Min Kim
28. **IMMoE: Incomplete Multi-View Anomaly Detection via Mixture of View Experts Fusion**  
   Lei Hu  
   [arXiv:2607.19032](https://arxiv.org/abs/2607.19032) · [code](https://github.com/HULEI7/IMMoE)
29. **Inductive Visual Logic for Few-Shot Out-Of-Distribution Adaptation in VLMs**  
   Hung-Jen Chen ⋅ Yu-Heng Ho ⋅ Ting-Yao Huang ⋅ Po-Hsiang Hsu ⋅ LIYU CHEN ⋅ Chun-Yi Lee ⋅ Min Sun
30. **Learning to Corrupt for Better Restoration**  
   Joonkyu Park ⋅ Wooseok Lee ⋅ Jaeha Kim ⋅ Sehoon Kim ⋅ Bokyeung Lee ⋅ Kyoung Mu Lee
31. **Leveraging Dark Knowledge for Intrinsic Multimodal Out-of-Distribution Detection**  
   Nimeshika Udayangani Hewa Dehigahawattage ⋅ Sarah Erfani ⋅ Christopher Leckie
32. **LogiCo: A Unified Framework for Logical and Structural Anomaly Detection**  
   Ximiao Zhang ⋅ Min Xu ⋅ Xiuzhuang Zhou  
   [arXiv:2606.28688](https://arxiv.org/abs/2606.28688) · [code](https://github.com/cnulab/LogiCo)
33. **MATCH: Flow Matching for Multi-View Anomaly Detection**  
   Mathis Kruse ⋅ Melissa Schween ⋅ Bodo Rosenhahn
34. **Modality-Aware Out-of-Distribution Detection for Multi-Modal Action Recognition**  
   Lars Doorenbos ⋅ Duc Vu ⋅ Serdar Ozsoy ⋅ Juergen Gall  
   [arXiv:2606.24404](https://arxiv.org/abs/2606.24404)
35. **O-VAD: Industrial Video Anomaly Detection through Object-Centric Tracking and Reasoning**  
   Mei Yuan ⋅ Qi Long ⋅ Qifeng Wu ⋅ Zhenyang Li ⋅ Yizhou Zhao ⋅ Lei Wang ⋅ Yang Liu ⋅ Min Xu  
   [arXiv:2607.18142](https://arxiv.org/abs/2607.18142)
36. **PA-VAD: Diffusion-Based Pseudo-Only Video Anomaly Detection via Domain-Aligned Memory Updates**  
   SATOSHI HASHIMOTO ⋅ Yanan Wang ⋅ Hitoshi Nishimura ⋅ Mori Kurokawa  
   [arXiv:2512.06845](https://arxiv.org/abs/2512.06845)
37. **PADFormer: Pose-agnostic Anomaly Detection from Sparse View Images**  
   Ruiqi Wang ⋅ Yiming Qian ⋅ FENGGEN YU ⋅ Yuxuan Lu ⋅ Dakuo Wang ⋅ Hao Richard Zhang ⋅ Jing Huang  
   [arXiv:2608.04210](https://arxiv.org/abs/2608.04210)
38. **Pistachio: Towards Synthetic, Balanced, and Long-Form Video Anomaly Benchmarks**  
   jie li ⋅ Hongyi Cai ⋅ Mingkang Dong ⋅ Muxin Pu ⋅ Shan You ⋅ Fei Wang ⋅ Tao Huang  
   [arXiv:2511.19474](https://arxiv.org/abs/2511.19474)
39. **Proximity-CLIP: Text-Guided Semantic Proximity Learning for Zero-Shot Anomaly Detection**  
   Manwen Yang ⋅ Leqian Ding ⋅ Yu Guo ⋅ Fei Wang
40. **Ranked Activation Shift for Post-hoc Out-of-Distribution Detection**  
   Gianluca Guglielmo ⋅ Marc Masana  
   [arXiv:2604.08572](https://arxiv.org/abs/2604.08572) · [code](https://github.com/gigug/RAS)
41. **ReactVAU: A Slow-Fast Decoupled Framework for Streaming Video Anomaly Understanding**  
   Chia-Hui Chen ⋅ Shih-Ying Yeh ⋅ Fu-En Yang ⋅ Min-Hung Chen ⋅ Shang-Hong Lai
42. **ReFP-AD: Rectified Flow Preconditioning for Energy-Based Anomaly Detection**  
   Camile Lendering ⋅ Erkut Akdag ⋅ Joaquin Figueira Chacon ⋅ Egor Bondarev  
   [arXiv:2608.01793](https://arxiv.org/abs/2608.01793) · [code](https://github.com/CLendering/ReFP-AD)
43. **ReinDriveGen: Reinforcement Post-Training for Out-of-Distribution Driving Scene Generation**  
   Hao ZHANG ⋅ Lue Fan ⋅ Weikang Bian ⋅ Zehuan Wu ⋅ Lewei Lu ⋅ Zhaoxiang Zhang ⋅ Hongsheng LI  
   [arXiv:2604.01129](https://arxiv.org/abs/2604.01129) · [project](https://drive-sim.github.io/ReinDriveGen/)
44. **Rethinking Adversary in Semantic Segmentation: An Out-of-Distribution Perspective**  
   Shuchang Wang ⋅ Shuchang Wang ⋅ Xiaoman Liu ⋅ Zhenbo Shi ⋅ Zhidong Yu ⋅ weisongjn weisongjn ⋅ Wei Yang
45. **Rethinking Continual Anomaly Detection on the Edge: Benchmarking Under Realistic Industrial Conditions**  
   Chad Weatherly ⋅ Sen Lin  
   [arXiv:2605.24251](https://arxiv.org/abs/2605.24251)
46. **STEP: Score-Based Temporal Energy for Human Pose Video Anomaly Detection**  
   Jakub Micorek ⋅ Mateusz Kozinski ⋅ Horst Possegger
47. **Towards Video Anomaly Detection from Event Streams: A Baseline and Benchmark Datasets**  
   Peng Wu ⋅ Yuting Yan ⋅ Guansong Pang ⋅ Yujia Sun ⋅ Qingsen Yan ⋅ Peng Wang ⋅ Yanning Zhang  
   [arXiv:2603.24991](https://arxiv.org/abs/2603.24991)
48. **Uncertainty-Weighted Fusion of Image and Synthetic Event for Video Anomaly Detection**  
   SUNGHEON JEONG ⋅ Jihong Park ⋅ Mohsen Imani
49. **Unified Multi-Layer Subspace Modeling for Cross-Domain OOD Detection**  
   Gerhard Krumpl ⋅ Henning Avenhaus ⋅ Horst Possegger
50. **UniScale: Arbitrary-Scale Anomaly Generation**  
   Shilei Zeng ⋅ Linxin Guan ⋅ Xurui Li ⋅ Yaohan Tang ⋅ Yu Zhou
51. **VarProtoAD: Variational Prototype-Conditioned Prompting for Zero-Shot Anomaly Detection**  
   Mengyang Zhao ⋅ Zhuolin He ⋅ Haiyang Yu ⋅ Teng Fu ⋅ Ke Niu ⋅ Xiangyang Xue
52. **Why Feature Magnitude Deceives OOD Detectors: An Angular Separation Perspective**  
   Hanlin Li ⋅ Jing Ma ⋅ Zehang Wei ⋅ Jiamin Yan ⋅ Xiang Xiang

## Image Classification & Visual Recognition

*15 papers · 8 with links*

1. **BIP: Bi-level Information Transfer and Completion Prompting for Visual Recognition with Missing Modalities**  
   Haoran Fan ⋅ Xu Han ⋅ Xianglong Bao ⋅ Zheng Gao ⋅ Qi Fan ⋅ Yang Song ⋅ Jiaojiao Jiang
2. **CGCE: Classifier-Guided Concept Erasure in Generative Models**  
   Viet Nguyen ⋅ Vishal Patel  
   [arXiv:2511.05865](https://arxiv.org/abs/2511.05865)
3. **Combining Discrepancy-Confusion Uncertainty and Calibration Diversity for Active Fine-Grained Image Classification**  
   Yinghao Jin ⋅ Xi Yang  
   [arXiv:2509.24181](https://arxiv.org/abs/2509.24181)
4. **HEM: a margin-based loss for visual categorisation tasks**  
   Michael Spratling ⋅ Heiko Schütt  
   [arXiv:2501.12191](https://arxiv.org/abs/2501.12191) · [project](https://codeberg.org/mwspratling/HEMLoss)
5. **LaVPR: Benchmarking Language and Vision for Place Recognition**  
   Ofer Idan ⋅ Dan Badur ⋅ yosi keller ⋅ Yoli Shavit  
   [arXiv:2602.03253](https://arxiv.org/abs/2602.03253) · [code](https://github.com/oferidan1/LaVPR)
6. **Lessons and Open Questions from a Unified Study of Camera-Trap Species Recognition Over Time**  
   Sooyoung Jeon ⋅ Hongjie Tian ⋅ Lemeng Wang ⋅ Zheda Mai ⋅ Vidhi Bakshi ⋅ Jiacheng Hou ⋅ Ping Zhang ⋅ Arpita Chowdhury ⋅ Jianyang Gu ⋅ Wei-Lun Chao  
   [arXiv:2603.20509](https://arxiv.org/abs/2603.20509)
7. **Multi-Anchor Distillation with Text-Guided Analytic Classifier for Continual Learning**  
   Qier Meng ⋅ De Cheng ⋅ Jiahao Li ⋅ Cheng Deng
8. **Neural Collapse-Inspired Multi-Label Federated Learning under Label-Distribution Skew**  
   Can Peng ⋅ Yuyuan Liu ⋅ YINGYU YANG ⋅ Pramit Saha ⋅ Qianye Yang ⋅ J. Noble  
   [arXiv:2509.12544](https://arxiv.org/abs/2509.12544)
9. **OPAL: Orthonormal Prototype Alignment Learning for Interpretable Image Classification**  
   Ilán Carretero ⋅ Gustavo ANGULO ⋅ Rocío Amor ⋅ Valery Naranjo
10. **Revisiting Autoregressive Models for Generative Image Classification**  
   Ilia Sudakov ⋅ Artem Babenko ⋅ Dmitry Baranchuk  
   [arXiv:2603.19122](https://arxiv.org/abs/2603.19122)
11. **Self-Improving Diffusion Classifiers with Minority Preference Optimization**  
   Hyunsoo Kim ⋅ Jungmyung Wi ⋅ Soobin Um ⋅ Donghyun Kim ⋅ Suhyun Kim  
   [arXiv:2607.03770](https://arxiv.org/abs/2607.03770)
12. **TiCRL: Textual Image Classification with Reinforcement Learning-Based Curriculum Learning**  
   Gayoung KIM ⋅ Yuncheol Kang
13. **Towards Reliable Multi-Label Classification via Conditional Dependency Modeling**  
   Arkapal Panda ⋅ Aditya Shankar Pal ⋅ Utpal Garain
14. **Variational Patch Gating for Training-Free Few-Shot Classification**  
   Ahmed Radwan ⋅ Ahmad Abdel-Qader ⋅ Islam Osman ⋅ Mohamed Shehata
15. **VICAL: Vicinal Consistency Alignment for Long-Tailed Visual Recognition**  
   Jianggang Zhu ⋅ Zheng Wang ⋅ Bin Zhu ⋅ Yi-Ping Phoebe Chen ⋅ Jingjing Chen

# Humans, Agents & Autonomy


## Human Pose, Motion & Avatars

*181 papers · 102 with links*

1. **3D FaceShell: Attribute Transfer in 3D Face Avatars as a VLM Defense Mechanism**  
   Weston Bondurant ⋅ Srijan Das ⋅ Hieu Le ⋅ Stephanie Schuckers  
   [arXiv:2607.16280](https://arxiv.org/abs/2607.16280)
2. **Affordance-Guided Diffusion Prior for 3D Hand Reconstruction**  
   Naru Suzuki ⋅ Takehiko Ohkawa ⋅ Tatsuro Banno ⋅ Jihyun Lee ⋅ Ryosuke Furuta ⋅ Yoichi Sato  
   [arXiv:2510.00506](https://arxiv.org/abs/2510.00506) · [project](https://narusuzuki.github.io/projects/26-affhandgen/)
3. **ANFI: Rethinking Neighbor Feature Interaction in Person Re-ID**  
   Xulin Li ⋅ Yan Lu ⋅ Bin Liu ⋅ Jiaze Li ⋅ Qinhong Yang ⋅ Tao Gong ⋅ Qi Chu ⋅ Nenghai Yu  
   [arXiv:2607.25407](https://arxiv.org/abs/2607.25407)
4. **ARMS: Anchor–Relational Motion Streaming for Seamless Solo-Social Motion Transitions**  
   Huakun Liu ⋅ Qing Yu ⋅ Kent Fujiwara ⋅ Hideaki Uchiyama ⋅ Kiyoshi Kiyokawa
5. **BackTranslation2.0 - A Linguistically Motivated Metric to Assess Sign Language Production**  
   Oliver Cory ⋅ Maksym Ivashechkin ⋅ Oline Ranum ⋅ Jian He Low ⋅ Edward Fish ⋅ Anton Pelykh ⋅ Karahan Sahin ⋅ Ozge Mercanoglu Sincan ⋅ Richard Bowden
6. **Beyond Alignment: A Generative Matching Paradigm via Flow Matching for Zero-Shot Skeleton-Based Action Recognition**  
   Xuan Liu ⋅ Cong Wu ⋅ Wei Fang ⋅ Zhenhua Feng
7. **BiCE-HG: A Bi-Conditional Egocentric Hand Gesture Dataset for Intelligent Reality Systems**  
   Awfa Dakheel ⋅ Charith Abhayaratne
8. **Category-Level Articulated Object Pose Estimation via Pose–Shape Hypothesis Generation and Verification**  
   Kaifeng Tang ⋅ Chi Xu ⋅ Xin Ao ⋅ Yuting Ge ⋅ Tingrui Guo ⋅ Jun Zhou
9. **CGCC: Towards Generalizable Clothes-Changing Person Re-Identification**  
   Yizhi Wu ⋅ Fangyi Liu ⋅ wei yu ⋅ Mang Ye
10. **ClusterStyle: Modeling Intra-Style Diversity with Prototypical Clustering for Stylized Motion Generation**  
   Kerui Chen ⋅ Jianrong Zhang ⋅ Ming Li ⋅ Zhonglong Zheng ⋅ Hehe Fan  
   [arXiv:2512.02453](https://arxiv.org/abs/2512.02453)
11. **CMCC-ReID: Cross-Modality Clothing-Change Person Re-Identification**  
   Xu Haoxuan ⋅ Hanzi Wang ⋅ Guanglin Niu  
   [arXiv:2604.02808](https://arxiv.org/abs/2604.02808)
12. **CMDer: Controllable Mode Decomposition-Based Single Motion Synthesis with Diffusion**  
   Junliang Chen ⋅ Sihang Chen ⋅ Xiaojuan Gu ⋅ Yoonsang Lee ⋅ Kevin Romond ⋅ Fang-Lue Zhang
13. **CoDePose: Multi-View 3D Human Pose Estimation via Coupled 2D-3D Denoising Diffusion**  
   Yanlu Cai ⋅ Yuxuan Liu ⋅ WEIZHONG ZHANG ⋅ Yuan Wu ⋅ Cheng Jin
14. **CoMind: Understanding Collaborative Human Activity from Multiple Minds and Views**  
   Alexey Gavryushin ⋅ Dingxi Zhang ⋅ Zhao Huang ⋅ Alexandros Delitzas ⋅ Jiaqi Chen ⋅ Ben Ellis ⋅ Cedric Zöllner ⋅ Manthan Patel ⋅ Manuel Kaufmann ⋅ Marc Pollefeys ⋅ Xi Wang  
   [arXiv:2607.06691](https://arxiv.org/abs/2607.06691) · [project](https://comind.ethz.ch/)
15. **ComplexMimic: Human–Scene Interaction Imitation in Complex 3D Environments**  
   Lu Pan ⋅ Hongwei Zhao  
   [arXiv:2607.02034](https://arxiv.org/abs/2607.02034)
16. **Controlling Motion Transfer in Diffusion Transformers via Attention Heads**  
   Sunyoung Jung ⋅ Jiwoo Park ⋅ Yoonseok Choi ⋅ Kyobin Choo ⋅ Ming-Hsuan Yang ⋅ Seong Jae Hwang  
   [arXiv:2607.11081](https://arxiv.org/abs/2607.11081) · [project](https://sunyj-hxppy.github.io/halo/)
17. **Coordinate Singularities Break Conformal Coverage for Gaze and Head Pose**  
   Mohammadreza Jamalifard ⋅ Yaxiong Lei ⋅ Parastoo Azizinezhad ⋅ Javier Andreu-Perez  
   [arXiv:2607.02565](https://arxiv.org/abs/2607.02565)
18. **CtrlCoMo: Controllable Co-Speech Motion Generation with Gesture–Action Disentanglement**  
   Xinghan Wang ⋅ Ming Zhou ⋅ Yanbo Zheng ⋅ Youjiang Xu ⋅ Yuan Zhang ⋅ Mingyuan Gao ⋅ Nan Zhuang ⋅ Yadong Mu
19. **DART: Deformable Adaptive Reasoning with Temporal Queries for Online Skeleton-Based Action Recognition**  
   Chaoyang Zheng ⋅ Yang Xiao ⋅ Tingbing Yan ⋅ Jinfang Gan ⋅ Xintao Zhang ⋅ Ran Wang ⋅ Zhiguo Cao ⋅ Joey Tianyi Zhou
20. **DETRAM: End-to-end DEtection, Tracking and Recovery of HumAn Meshes**  
   Chunggi Lee ⋅ Seonwook Park ⋅ Wanhua Li ⋅ Umar Iqbal ⋅ Hanspeter Pfister  
   [arXiv:2607.09089](https://arxiv.org/abs/2607.09089)
21. **DETRPose: Real-Time End-to-End Multi-Person Pose Estimation via Modified Transformer Decoder and Novel Denoising Keypoints**  
   Sebastian Janampa ⋅ Marios Pattichis  
   [arXiv:2506.13027](https://arxiv.org/abs/2506.13027) · [code](https://github.com/SebastianJanampa/DETRPose)
22. **DiffProxy: Multi-View Human Mesh Recovery via Diffusion-Generated Dense Proxies**  
   renke wang ⋅ zhenyu zhang ⋅ Ying Tai ⋅ Jun Li ⋅ Jian Yang  
   [arXiv:2601.02267](https://arxiv.org/abs/2601.02267) · [code](https://github.com/wrk226/DiffProxy) · [project](https://wrk226.github.io/DiffProxy.html)
23. **DiGS-Avatar: Single-Image Animatable 3D Human Reconstruction via UV-Space Diffusion**  
   jiakun li ⋅ Li Fang ⋅ Hao Zhu ⋅ Fei Hu ⋅ Long Ye ⋅ Yuan Zhang ⋅ Jinyao Yan
24. **DisentangledTMR: Privacy-Preserving Skeleton Motion Retargeting via Factorized Transformers**  
   Thomas Carr ⋅ Depeng Xu ⋅ Shuhan Yuan ⋅ Aidong Lu
25. **Disentangling and Reusing Interaction Cues for Zero-Shot HOI Detection**  
   Jie Gu ⋅ He-Yang Xu ⋅ Hongxiang Gao ⋅ Chengyu Liu
26. **DSAR: Dual-Stream Autoregressive Modeling of Temporal Cloth Dynamics for Photorealistic Animatable Avatars**  
   Xiong Haozhong ⋅ Yao Yu ⋅ Yu Zhou ⋅ Sidan DU  
   [arXiv:2608.10500](https://arxiv.org/abs/2608.10500)
27. **ECHO: Ego-centric Modeling of Human-Object Interactions**  
   Ilya A. Petrov ⋅ Vladimir Guzov ⋅ Riccardo Marin ⋅ Emre Aksan ⋅ Xu Chen ⋅ Daniel Cremers ⋅ Thabo Beeler ⋅ Gerard Pons-Moll  
   [arXiv:2508.21556](https://arxiv.org/abs/2508.21556) · [project](https://ptrvilya.github.io/echo/)
28. **Ego-Human Motion Prediction with 3D-Aware LLM**  
   Yujin Bae ⋅ Jaewoo Jeong ⋅ HYEONSEONG KIM ⋅ KUK-JIN YOON  
   [arXiv:2607.07001](https://arxiv.org/abs/2607.07001) · [project](https://jaewoo97.github.io/Ego3DLM/)
29. **Egocentric World Model for Photorealistic Hand Object Interaction Synthesis**  
   Dayou Li ⋅ Lulin Liu ⋅ Bangya Liu ⋅ Shijie Zhou ⋅ Jiu Feng ⋅ Ziqi Lu ⋅ Minghui Zheng ⋅ Chenyu You ⋅ Zhiwen Fan  
   [arXiv:2603.13615](https://arxiv.org/abs/2603.13615)
30. **EgoExo-Con: Exploring View-Invariant Video Temporal Understanding**  
   Minjoon Jung ⋅ Junbin Xiao ⋅ Junghyun Kim ⋅ Byoung-Tak Zhang ⋅ Angela Yao  
   [arXiv:2510.26113](https://arxiv.org/abs/2510.26113) · [project](https://minjoong507.github.io/projects/EgoExo-Con/)
31. **EgoExoMoCap: Distributed Human Motion Capture via Ego- and Exocentric Body Tracking from Head-Mounted Devices**  
   Jiaxi Jiang ⋅ Bharat Bhatnagar ⋅ Nan Yang ⋅ Lingni Ma ⋅ Sebastian Starke ⋅ Robin Kips ⋅ Nadine Bertsch ⋅ Christian Holz ⋅ Federica Bogo
32. **EgoGVAE: Ego-body Mesh Reconstruction via Guided Variational Autoencoder**  
   Jaehun Jung ⋅ Wonjun Kim  
   [arXiv:2607.27755](https://arxiv.org/abs/2607.27755)
33. **ELHINN: Unifying Dense Crowd Simulation Across Scales via Eulerian–Lagrangian Hydrodynamics**  
   Yanshan Zhou ⋅ Pingrui Lai ⋅ Jiaqi Yu ⋅ Cunyan Li ⋅ Hua Yang ⋅ Xiaoyun Zhang
34. **EmbodiedHead: Real-Time Listening and Speaking Avatar for Conversational Agents**  
   Yu Zhang ⋅ Kaiyuan Shen ⋅ Yang Li  
   [arXiv:2604.17211](https://arxiv.org/abs/2604.17211)
35. **EMOTE: Expressive Motion and Shape Disentanglement for Human Animation**  
   DongbinZhang DongbinZhang ⋅ Hao Liu ⋅ Bingquan Dai ⋅ Kangjie Chen ⋅ Chuming Wang ⋅ Chen Li ⋅ Jing LYU ⋅ Haoqian Wang
36. **EmoteGPT: 3D Human Facial Expression from Natural Language Descriptions**  
   Haoran Wang ⋅ Mohit Mendiratta ⋅ Christian Theobalt ⋅ Adam Kortylewski  
   [arXiv:2607.02674](https://arxiv.org/abs/2607.02674) · [project](https://genintel.github.io/EmoteGPT)
37. **Escaping the Low-Frequency Bias: Adversarial Frequency Perturbation for Generalisable Gaze Estimation**  
   Yang Xu ⋅ Feng Lu
38. **ETCH-X: Robustify Expressive Body Fitting to Clothed Humans with Composable Synthetic Data**  
   Xiaoben Li ⋅ Jingyi Wu ⋅ Zeyu CAI ⋅ YU Siyuan ⋅ Boqian Li ⋅ Yuliang Xiu
39. **Event Stream-based Sign Language Translation: A High-Definition Benchmark Dataset and A Novel Baseline**  
   Shiao Wang ⋅ Xiao Wang ⋅ Duoqing Yang ⋅ Yao N/A ⋅ Fuling Wang ⋅ Jianing Li ⋅ Lin Zhu ⋅ Bo Jiang  
   [arXiv:2408.10488](https://arxiv.org/abs/2408.10488) · [code](https://github.com/Event-AHU/OpenESL)
40. **Event-based Gaze Control Systems for Real-time Spin Estimation in Professional Ball Games**  
   Yunpu Hu ⋅ Fabian Schilling ⋅ Valentina Cavinato ⋅ Asude Aydin ⋅ Agis Politis ⋅ Ricardo Morales ⋅ Kirk Scheper ⋅ Peter Dürr ⋅ Naoya Takahashi
41. **Every Dog Has Its Day, Probably: A Balanced Synthetic Benchmark and Probabilistic Modeling for 3D Dog Pose Estimation**  
   Joo Young Choi ⋅ Wonkwang Lee ⋅ Juhyeong Seon ⋅ Gunhee Kim
42. **Fast Sam 3D Body: Accelerating SAM 3D Body for Real-Time Full-Body Human Mesh Recovery**  
   Timing Yang ⋅ Sicheng He ⋅ Hongyi Jing ⋅ Jiawei Yang ⋅ Zhijian Liu ⋅ Chuhang Zou ⋅ Yue Wang  
   [arXiv:2603.15603](https://arxiv.org/abs/2603.15603)
43. **FDM-MFVT: Few-step Sampling Diffusion Model for Mask-Free Virtual Try-On**  
   Jiaxin Liu ⋅ XIAOYE LIANG ⋅ Lai Jiang ⋅ Jun Liu ⋅ Mai Xu  
   [arXiv:2606.29319](https://arxiv.org/abs/2606.29319)
44. **FFAvatar: Feed-Forward 4D Head Avatar Reconstruction from Arbitrary Images**  
   Jianjiang Yao ⋅ Ke Xian ⋅ Renxiang Dai ⋅ Robert Qiu
45. **FitControler: Toward Fit-Aware Virtual Try-On**  
   Lu Yang ⋅ Yicheng Liu ⋅ Letian Zhou ⋅ Yanan Li ⋅ Xiang Bai ⋅ Hao Lu  
   [arXiv:2512.24016](https://arxiv.org/abs/2512.24016)
46. **FlexiAvatar: Unified 3D Gaussian Human Avatars Under Arbitrary Body Visibility**  
   Yihalem Yimolal Tiruneh ⋅ Muhammad Salman Ali ⋅ Uyoung Jeong ⋅ Muneeb Khan ⋅ MD Sayem ⋅ ALLANUR BAYRAMGELDIYEV ⋅ Binod Bhattarai ⋅ Seungryul Baek  
   [arXiv:2607.19100](https://arxiv.org/abs/2607.19100)
47. **FlowerDance: MeanFlow for Efficient and Refined 3D Dance Generation**  
   Kaixing Yang ⋅ Xulong Tang ⋅ Ziqiao Peng ⋅ Xiangyue Zhang ⋅ Chubin Chen ⋅ xukun zhou ⋅ Puwei Wang ⋅ Hongyan Liu ⋅ Jun He  
   [arXiv:2511.21029](https://arxiv.org/abs/2511.21029)
48. **Forecasting Animal Motion**  
   Neerja Thakkar ⋅ Shiry Ginosar ⋅ Jacob Walker ⋅ Jitendra Malik ⋅ Joao Carreira ⋅ Carl Doersch
49. **Forge4D: Feed-Forward 4D Human Reconstruction and Interpolation from Uncalibrated Sparse-View Videos**  
   Yingdong Hu ⋅ YISHENG HE ⋅ Jinnan Chen ⋅ Weihao Yuan ⋅ Kejie Qiu ⋅ Zehong Lin ⋅ Siyu Zhu ⋅ Zilong Dong ⋅ Steven Hoi ⋅ Jun Zhang  
   [arXiv:2509.24209](https://arxiv.org/abs/2509.24209) · [project](https://zhenliuzju.github.io/huyingdong/Forge4D)
50. **From Gaze to Meaning: An AI Agent for Unified Zero-Shot Grounding and Explanation**  
   Shayan Nasiriboukani ⋅ Sara Atito ⋅ Mohammad Nezamipour ⋅ Muhammad Awais
51. **G2FM: A Geodesic Flow Matching Framework with Geometric Prior for Category-Level 9-DoF Pose Estimation**  
   Qianyu Chen ⋅ Xiaogang Zhang ⋅ Yangyi Wan ⋅ Zhengzhao Pan ⋅ Kai Wang ⋅ Yuqi Cai ⋅ Wenbin Yan ⋅ feng yang ⋅ Hua Chen
52. **Gaze-to-text Generation: Beyond Categorical Decoding of Human Attention**  
   Sounak Mondal ⋅ Dimitris Samaras ⋅ Gregory Zelinsky ⋅ Minh Hoai Nguyen  
   [arXiv:2607.23917](https://arxiv.org/abs/2607.23917)
53. **Generative Action Tell-Tales: Assessing Human Motion in Synthesized Videos**  
   Xavier Thomas ⋅ Youngsun Lim ⋅ Ananya Srinivasan ⋅ Audrey Zheng ⋅ Deepti Ghadiyaram  
   [arXiv:2512.01803](https://arxiv.org/abs/2512.01803)
54. **Generative Relightable Avatars**  
   Kunwar Singh ⋅ Christian Theobalt ⋅ Rishabh Dabral  
   [arXiv:2606.22718](https://arxiv.org/abs/2606.22718) · [project](https://vcai.mpi-inf.mpg.de/projects/GRA/)
55. **GenHOI: Generalized Hand-Object Pose Estimation with Occlusion Awareness**  
   HUI YANG ⋅ Wei Sun ⋅ Jian Liu ⋅ Jian Xiao ⋅ Tao Xie ⋅ Hossein Rahmani ⋅ Ajmal Mian ⋅ Nicu Sebe ⋅ Gim Hee Lee  
   [arXiv:2603.19013](https://arxiv.org/abs/2603.19013)
56. **GenLCA: 3D Diffusion for Full-Body Avatars from In-the-Wild Videos**  
   Yiqian Wu ⋅ Rawal Khirodkar ⋅ Egor Zakharov ⋅ Timur Bagautdinov ⋅ Lei Xiao ⋅ Zhaoen Su ⋅ Shunsuke Saito ⋅ Xiaogang Jin ⋅ Junxuan Li  
   [arXiv:2604.07273](https://arxiv.org/abs/2604.07273) · [project](https://onethousandwu.com/GenLCA-Page)
57. **Geometry-Preserving Image Generation for 6D Object Pose Estimation**  
   Jiafeng Zhang ⋅ Rui Song ⋅ Zhengtai Zhang ⋅ Jiaojiao Li ⋅ Kailang Cao ⋅ Lizhang Peng ⋅ David Ferstl ⋅ Yinlin Hu
58. **GKDT: General Keypoint Detection Transformer**  
   Changsheng Lu ⋅ Yuxin Chen ⋅ Haokun GUI ⋅ Rong Wang ⋅ Jie Yang ⋅ Harry Yang ⋅ Anton van den Hengel ⋅ Jiaya Jia  
   [arXiv:2607.00752](https://arxiv.org/abs/2607.00752) · [code](https://github.com/AlanLuSun/General-Keypoint-Detection)
59. **GRAFT: Geometric Refinement and Fitting Transformer for Human Scene Reconstruction**  
   Pradyumna YM ⋅ Yuxuan Xue ⋅ Yue Chen ⋅ Nikita Kister ⋅ István Sárándi ⋅ Gerard Pons-Moll  
   [arXiv:2604.19624](https://arxiv.org/abs/2604.19624) · [project](https://pradyumnaym.github.io/graft)
60. **Granular Semantic Cognition for Visible-Infrared Person Re-Identification**  
   Haifeng Yang ⋅ Jinjia Peng ⋅ Huibing Wang
61. **Gravity-aware partially calibrated absolute pose estimation from affine- or rotation-covariant features**  
   Marcus Valtonen Örnhag ⋅ Alberto Jaenal Gálvez ⋅ Stefan Adalbjörnsson
62. **HairWeaver: Few-Shot Photorealistic Hair Motion Synthesis with Sim-to-Real Guided Video Diffusion**  
   Di Chang ⋅ Ji Hou ⋅ Aljaz Bozic ⋅ Assaf Neuberger ⋅ Felix Juefei-Xu ⋅ Olivier Maury ⋅ Gene Lin ⋅ Tuur Stuyck ⋅ Doug Roble ⋅ Mohammad Soleymani ⋅ Stéphane Grabli  
   [arXiv:2602.11117](https://arxiv.org/abs/2602.11117) · [project](https://boese0601.github.io/hairweaver/)
63. **Head Avatars with Dynamic Explicit Hair**  
   Vanessa Sklyarova ⋅ Haonan Chen ⋅ Berna Kabadayi ⋅ Tobias Kirschstein ⋅ Zicong Fan ⋅ Xi Wang ⋅ Gerard Pons-Moll ⋅ Matthias Niessner ⋅ Marc Pollefeys ⋅ Michael Black ⋅ Justus Thies  
   [arXiv:2607.23861](https://arxiv.org/abs/2607.23861) · [project](https://dynhair.is.tue.mpg.de/)
64. **HiReFF: High-Resolution Feedforward Human Reconstruction from Uncalibrated Sparse-View Video**  
   YIMING JIANG ⋅ Hanzhang Tu ⋅ Wenfeng Song ⋅ Siyou Lin ⋅ Liang An ⋅ Shuai Li ⋅ Aimin Hao ⋅ Yebin Liu  
   [arXiv:2606.29333](https://arxiv.org/abs/2606.29333) · [project](https://iridescentjiang.github.io/HiReFF)
65. **HOIMask: Towards Generative Masked Modeling for Human Object Interaction Generation**  
   Yihong Ji ⋅ Jinsong Zhang ⋅ He Hu ⋅ Hongboxu Hongboxu  
   [arXiv:2608.15141](https://arxiv.org/abs/2608.15141) · [project](https://jyhflash.github.io/HOIMask/)
66. **HuCollisionField: Resolving Self-Collisions via Neural Fields for Human Prediction**  
   Zhengyuan Li ⋅ Zeyun Deng ⋅ Yifan Shen ⋅ Liang-Yan Gui ⋅ Miaolan Xie ⋅ Joseph Campbell ⋅ Xifeng Gao ⋅ Kui Wu ⋅ Zherong Pan ⋅ Aniket Bera
67. **Human Mesh Modeling for Anny Body**  
   Romain Brégier ⋅ Guénolé Fiche ⋅ Matthieu Armando ⋅ Laura Bravo-Sánchez ⋅ Thomas Lucas ⋅ Philippe Weinzaepfel ⋅ Grégory Rogez ⋅ Fabien Baradel  
   [arXiv:2511.03589](https://arxiv.org/abs/2511.03589) · [code](https://github.com/naver/anny)
68. **Identity-Preserving Human Reconstruction from a Single Image via 3D Token Inference**  
   Yanqi Bao ⋅ Jiaxiang Shang ⋅ Yang Gao ⋅ Yingchun Liu ⋅ Jing Huo ⋅ Jing Liao
69. **InclusiveHuman-10K: Towards Inclusive Human Parsing Beyond the Intact-Limb Assumption**  
   Heming Du ⋅ Jiaying Ying ⋅ Xiaofeng Cao ⋅ Zhu Li ⋅ Yuanyuan Liu ⋅ Kaihao Zhang ⋅ Xin Chen ⋅ Xin Yu
70. **Infinite Gaze Generation for Videos with Autoregressive Diffusion**  
   JENNA KANG ⋅ Colin Groth ⋅ Tong Wu ⋅ Finley Torrens ⋅ Patsorn Sangkloy ⋅ Gordon Wetzstein ⋅ Qi Sun  
   [arXiv:2603.24938](https://arxiv.org/abs/2603.24938)
71. **InfiniteDance: Scalable 3D Dance Generation Towards in-the-wild Generalization**  
   Ronghui Li ⋅ zhongyuan hu ⋅ Li Siyao ⋅ youliang zhang ⋅ Haozhe Xie ⋅ Mingyuan Zhang ⋅ Jie Guo ⋅ Xiu Li ⋅ Ziwei Liu  
   [arXiv:2603.13375](https://arxiv.org/abs/2603.13375) · [project](https://infinitedance.github.io/)
72. **Instant Expressive Gaussian Head Avatars at Over 100 FPS**  
   Kaiwen Jiang ⋅ Xueting Li ⋅ Seonwook Park ⋅ Ravi Ramamoorthi ⋅ Shalini De Mello ⋅ Koki Nagano  
   [arXiv:2512.16893](https://arxiv.org/abs/2512.16893) · [project](https://research.nvidia.com/labs/amri/projects/instant4d)
73. **InteractiveAvatar: Real-Time Streaming Video Generation for Consistent and Intent-Aware Avatars**  
   Quanyue Song ⋅ Yishan He ⋅ Guo Zhi ⋅ yanfei zhang ⋅ Shihao Cheng ⋅ Zhixiang He ⋅ Chi Zhang ⋅ Caigui Jiang ⋅ Xuelong Li  
   [arXiv:2606.22905](https://arxiv.org/abs/2606.22905)
74. **InterPet4D: A Multimodal 4D Human-Pet Interaction Dataset for Pet Motion Generation**  
   YICHEN PENG ⋅ Jyun-Ting Song ⋅ Chen-Chieh Liao ⋅ Kris Kitani ⋅ Hideki Koike ⋅ Erwin Wu  
   [arXiv:2607.10287](https://arxiv.org/abs/2607.10287)
75. **IRG-MotionLLM: Interleaving Motion Generation, Assessment and Refinement for Text-to-Motion Generation**  
   Yuanming Li ⋅ Qize Yang ⋅ Nan Lei ⋅ Shenghao Fu ⋅ Ling-An Zeng ⋅ Jian-Fang Hu ⋅ Xihan Wei ⋅ WEISHI ZHENG  
   [arXiv:2512.10730](https://arxiv.org/abs/2512.10730) · [code](https://github.com/HumanMLLM/IRG-MotionLLM)
76. **JacobianAvatar: Temporally Consistent Semi-rigid Avatar Reconstruction from a Monocular Video**  
   Changyeon Won ⋅ Min-Gyu Park ⋅ Seonghwan Park ⋅ Ju Yoon ⋅ Hae-Gon Jeon  
   [arXiv:2606.31115](https://arxiv.org/abs/2606.31115)
77. **JointHOI: Jointly Generating Contact Maps Enhances Hand Object Interaction Generation**  
   Mingyeong Song ⋅ Jungbin Cho ⋅ Jisoo Kim ⋅ Ananya Bal ⋅ Kartik Sharma ⋅ Youngjae Yu ⋅ Laszlo Jeni ⋅ Junhyug Noh  
   [arXiv:2607.01768](https://arxiv.org/abs/2607.01768)
78. **K-Mask: Kinematic-Aware Masked Modeling for Controllable Text-to-Motion Synthesis**  
   Faisal Ahmed ⋅ Chenqiu Zhao ⋅ Anup Basu
79. **Kirin: Animal Motion Generation from In-the-Wild Video**  
   Brian Nlong Zhao ⋅ Zhuoyang Pan ⋅ James Rehg ⋅ Jiajun Wu ⋅ Elliott (Shangzhe) Wu
80. **LaMP: Learning Vision-Language-Action Policies with 3D Scene Flow as Latent Motion Prior**  
   Xinkai Wang ⋅ Chenyi Wang ⋅ Yifu Xu ⋅ Mingzhe Ye ⋅ Fu-Cheng Zhang ⋅ Jialin Tian ⋅ Xinyu Zhan ⋅ Lifeng Zhu ⋅ Cewu Lu ⋅ Lixin Yang
81. **Language-Guided Transformer Tokenizer for Human Motion Generation**  
   Sheng Yan ⋅ yong wang ⋅ Xin Du ⋅ Junsong Yuan ⋅ Mengyuan Liu  
   [arXiv:2602.08337](https://arxiv.org/abs/2602.08337) · [project](https://eanson023.github.io/LG-Tok/)
82. **LaxMotion: Rethinking Supervision Granularity for 3D Human Motion Generation**  
   Sheng Liu ⋅ Yuanzhi Liang ⋅ Sidan DU  
   [arXiv:2511.11368](https://arxiv.org/abs/2511.11368)
83. **Layering Virtual Try-On**  
   Chun Feng ⋅ Bowei Chen ⋅ Shan Mengyi ⋅ Ira Kemelmacher-Shlizerman  
   [arXiv:2607.22924](https://arxiv.org/abs/2607.22924)
84. **Learning Generatable Mutual Distance for Scene-Aware Human Motion Generation**  
   Zonglin Yang ⋅ Chaoyue Xing ⋅ Yixuan Yin ⋅ Miaomiao Liu ⋅ Liyuan Pan
85. **LEO-Fuse: A Modality- and Task-Agnostic Universal Framework for Multimodal Human Sensing**  
   Emrecan Aslan
86. **Live Avatar: Streaming Real-time Audio-Driven Avatar Generation with Infinite Length**  
   Yubo Huang ⋅ Hailong Guo ⋅ Fangtai Wu ⋅ Weiqiang Wang ⋅ Shijie Huang ⋅ Qijun Gan ⋅ Shifeng Zhang ⋅ Lin Liu ⋅ Sirui Zhao ⋅ Enhong Chen ⋅ Jiaming Liu ⋅ Steven Hoi  
   [arXiv:2512.04677](https://arxiv.org/abs/2512.04677) · [project](https://liveavatar.github.io/)
87. **Local Spacing-Aware Hungarian Matching for Stable Point-Supervised Crowd Counting**  
   Kai Jiang ⋅ Yiming Lin ⋅ Zurui Ao
88. **LOOM: Weaving Geometry-Consistent Human-Object Interaction Videos via Progressive Curriculum Learning**  
   Bangya Liu ⋅ Zelin Zhao ⋅ Ziyang Song ⋅ Suman Banerjee ⋅ Xinyu Gong
89. **LUNA: Learning Universal 3D Human Animation Beyond Skinning**  
   Peng Li ⋅ Rawal Khirodkar ⋅ Junxuan Li ⋅ Yuan Dong ⋅ Chen Cao ⋅ Yuan Liu ⋅ Wenhan Luo ⋅ Yike Guo ⋅ Shunsuke Saito  
   [arXiv:2606.31981](https://arxiv.org/abs/2606.31981) · [project](https://penghtyx.github.io/LUNA/)
90. **LVSPM: Long Sequence View Synthesis and Pose Estimation Model**  
   Xi Chen ⋅ Yachi Zhang ⋅ Linghao Chen ⋅ Minghua Liu ⋅ Hao Su ⋅ Zexiang Xu ⋅ Xiaoshuai Zhang
91. **Making Avatars Interact: Towards Text-Driven Human-Object Interaction for Controllable Talking Avatars**  
   youliang zhang ⋅ zhengguang zhou ⋅ Zhentao Yu ⋅ Ziyao Huang ⋅ Teng Hu ⋅ Sen Liang ⋅ Guozhen Zhang ⋅ Ziqiao Peng ⋅ Shunkai Li ⋅ Yi Chen ⋅ Zixiang Zhou ⋅ Yuan Zhou ⋅ Qinglin Lu ⋅ Xiu Li  
   [arXiv:2602.01538](https://arxiv.org/abs/2602.01538) · [project](https://interactavatar.github.io)
92. **MemPose: Category-level Object Pose Estimation with Memory**  
   Xiao Lin ⋅ Minghao Zhu ⋅ Yun Peng ⋅ Liuyi Wang ⋅ Qiyi Wang ⋅ Chengju Liu ⋅ Qijun Chen  
   [arXiv:2607.04930](https://arxiv.org/abs/2607.04930)
93. **MoAKE: Toward Unified All-in-One Action Quality Assessment via Mixture of Action Knowledge Experts**  
   Huangbiao Xu ⋅ Huanqi Wu ⋅ Xiao Ke ⋅ Jiaxin Cai ⋅ Junyi Wu ⋅ Jinglin Xu  
   [arXiv:2607.19826](https://arxiv.org/abs/2607.19826) · [code](https://github.com/XuHuangbiao/MoAKE)
94. **Monocular Avatar Reconstruction via Cascaded Diffusion Priors and UV-Space Differentiable Shading**  
   Hong Li ⋅ Minqi Meng ⋅ Yanjun Liang ⋅ Chongjie Ye ⋅ Houyuan Chen ⋅ Weiqing Xiao ⋅ Xianda Guo ⋅ Guojun Lei ⋅ Xuhui Liu ⋅ Chaojie Yang ⋅ Yanlun Peng ⋅ HAO ZHAO ⋅ Baochang Zhang  
   [arXiv:2606.28144](https://arxiv.org/abs/2606.28144) · [project](https://luh1124.github.io/MARCUS-Avatar-Projectpage/)
95. **Monocular Models are Strong Learners for Multi-View Human Mesh Recovery**  
   Haoyu Xie ⋅ Shengkai Xu ⋅ Cheng Guo ⋅ Muhammad Saleem ⋅ Wenhan Wu ⋅ Chen Chen ⋅ Ahmed Helmy ⋅ Pu Wang ⋅ Hongfei Xue  
   [arXiv:2603.20391](https://arxiv.org/abs/2603.20391)
96. **MorphGS: Morphology-Adaptive Articulated Motion Transfer from Videos**  
   Taeyeon Kim ⋅ Youngju Na ⋅ Jumin Lee ⋅ Sebin Lee ⋅ Minhyuk Sung ⋅ Sung-eui Yoon  
   [arXiv:2601.02716](https://arxiv.org/abs/2601.02716) · [project](https://xodus777.github.io/MorphGS/)
97. **MoScale: Autoregressive Next-Scale Prediction for Human Motion Generation and Editing**  
   Inwoo Hwang ⋅ Hojun Jang ⋅ Bing Zhou ⋅ Jian Wang ⋅ Young Min Kim ⋅ chuan guo
98. **Motion Style Slider: Endpoint-Supervised Continuous Style Control for Human Motion Diffusion**  
   Chen-Chieh Liao ⋅ YICHEN PENG ⋅ YIYI CAI ⋅ Yûi Ono ⋅ Hiroki Hanaoka ⋅ Erwin Wu ⋅ Hideki Koike ⋅ Shuichi Kurabayashi
99. **MotionChain: Fine-Grained Video Motion Understanding via Structured Decomposition**  
   Hao Yang ⋅ Bo Xu ⋅ Jun Dan ⋅ Sijia Chen ⋅ Baigui Sun ⋅ Yang Liu
100. **MotionDreamer: Universal Skeletal Motion Generation for 3D Rigged Shapes**  
   Ye Tao ⋅ Yuxin Yao ⋅ Kendong Liu ⋅ Dapeng Wu ⋅ Junhui Hou
101. **Moving Beyond More Views: Redundancy-Aware Ego–Exo Fusion for Proficiency Estimation**  
   Xu Dong ⋅ Wanqing Li ⋅ Anthony Adeyemi-Ejeye ⋅ Andrew Gilbert
102. **Multi-Modal Controlled Coherent Motion Generation**  
   Yifei Liu ⋅ Qiong Cao ⋅ Hongwei Yi ⋅ Huaiguang Jiang ⋅ Changxing Ding
103. **Multi-scale Object-Aware Gaze Estimation via Geometric Reasoning**  
   Jiajie Mi ⋅ Xinyu Liu ⋅ Mengke Song ⋅ Chenglizhao Chen  
   [arXiv:2606.29334](https://arxiv.org/abs/2606.29334)
104. **Multi-THuMBS: Multi-person Tracking of 3D Human Meshes Beyond Video Shots**  
   Jeongwan On ⋅ Muhammad Salman Ali ⋅ Muneeb Khan ⋅ Sunwoo Park ⋅ Inwoong Moon ⋅ Hyung Jin Chang ⋅ Jaekwang Kim ⋅ Seong Jong Ha ⋅ Seungryul Baek  
   [arXiv:2607.01626](https://arxiv.org/abs/2607.01626) · [project](https://on-jungwoan.github.io/projects/multi-thumbs/)
105. **MV2GF: Multi-view Pedestrian Detection with a Visual Geometric Foundation Model**  
   Taiga Yamane ⋅ Satoshi Suzuki ⋅ Ryo Masumura ⋅ Shota Orihashi ⋅ Tomohiro Tanaka ⋅ Mana Ihori ⋅ Naoki Makishima
106. **MVI2V: Human Centric Image to Video Generation with Multiview Consistent Appearance**  
   Pengfei Liu ⋅ Mingyi Xu ⋅ Wentao Jiang ⋅ Tiezheng Ge ⋅ Ming Zeng
107. **ObjectForesight: Predicting 3D Object Trajectories from Human Videos**  
   Rustin Soraki ⋅ Homanga Bharadhwaj ⋅ Ali Farhadi ⋅ Roozbeh Mottaghi  
   [arXiv:2601.05237](https://arxiv.org/abs/2601.05237)
108. **Occlusion-Resilient Category-Agnostic Pose Estimation with Conditional Flow Matching**  
   Jiyong Rao ⋅ Shengjie Zhao ⋅ Yu Wang ⋅ Hao Deng
109. **Odoriko: A Shape-Aware Multimodal Diffusion Framework for Human Motion**  
   Dongseok Shim ⋅ Julian Tanke ⋅ Kengo Uchida ⋅ christian simon ⋅ Koichi Saito ⋅ Takashi Shibuya ⋅ Shusuke Takahashi ⋅ Yuki Mitsufuji  
   [arXiv:2606.21135](https://arxiv.org/abs/2606.21135)
110. **OmniDance: Multimodal Driven Dance Video Generation with Large-scale Internet Data**  
   Kaixing Yang ⋅ Jiashu Zhu ⋅ Xulong Tang ⋅ Ziqiao Peng ⋅ Xiangyue Zhang ⋅ Chubin Chen ⋅ Puwei Wang ⋅ Jiahong Wu ⋅ Xiangxiang Chu ⋅ Hongyan Liu ⋅ Jun He  
   [arXiv:2606.30019](https://arxiv.org/abs/2606.30019) · [code](https://github.com/AMAP-ML/OmniDance)
111. **OmniPoser: Flexible Human Motion Recovery in the Wild with Masked Flow Matching**  
   Minghao Liu ⋅ Tutian Tang
112. **One-Shot Feed-Forward 360° Animatable Avatar via Inpainted UV-Space Gaussian Modeling**  
   Shuling Zhao ⋅ Dan Xu
113. **OrthoTailor: Geometric Orthogonalization for Conflict-Free Unified Fashion Generation**  
   Zhaotong Yang ⋅ Ying Tai ⋅ Jiahui Zhan ⋅ Yu Zheng ⋅ Jianjun Qian ⋅ Jian Yang
114. **PartCHOI: Part-Aware Guidance for Clothed Human-Object Interaction Generation**  
   Mingwen Shao ⋅ Xinyuan Chen ⋅ Qiao Zhang ⋅ Xiang Lv ⋅ lingzhuang meng ⋅ Qinglin Zhan ⋅ Chang Liu ⋅ Chao Dong
115. **Partial Skeleton Visibility for Action Recognition: A Constrained Field-of-View Approach**  
   Yingjie Dai ⋅ Tianyang Xu ⋅ Yanglin Deng ⋅ Xiao-Jun Wu ⋅ Josef Kittler  
   [arXiv:2607.00716](https://arxiv.org/abs/2607.00716)
116. **Path-JEPA: Path Signature Based Predictive Learning for Skeleton Action Recognition**  
   Ashutosh Singh ⋅ Ashish Singh
117. **PHOSA: Photorealistic 3D Sign Avatar Modeling and Benchmark**  
   Haodong Wang ⋅ Hezhen Hu ⋅ Wengang Zhou ⋅ Houqiang Li
118. **PhysDrape: Learning Explicit Forces and Collision Constraints for Physically Realistic Garment Draping**  
   Minghai Chen ⋅ Mingyuan Liu ⋅ Ning Ma ⋅ Jianqing LI ⋅ Yuxiang Huan  
   [arXiv:2602.08020](https://arxiv.org/abs/2602.08020)
119. **PIAvatar: Physically Interactive Avatars via Deformation Gradient Decoupling**  
   Sang-Hun Han ⋅ Min-Gyu Park ⋅ Jisu Shin ⋅ Seunghyun Shin ⋅ JINHWI PARK ⋅ Hae-Gon Jeon  
   [arXiv:2606.21162](https://arxiv.org/abs/2606.21162) · [project](https://sanghunhan92.github.io/conference/PIAvatar/)
120. **Pix2NPHM: Learning to Regress NPHM Reconstructions From a Single Image**  
   Simon Giebenhain ⋅ Tobias Kirschstein ⋅ Liam Schoneveld ⋅ Davide Davoli ⋅ Zhe Chen ⋅ Matthias Niessner  
   [arXiv:2512.17773](https://arxiv.org/abs/2512.17773) · [project](https://simongiebenhain.github.io/Pix2NPHM/)
121. **PoseImageNet: Pose Estimation for Extensive Classes Based on Rich Structure Prototypes**  
   Junjie Chen ⋅ Hong Cao ⋅ Weixiang Tao ⋅ Yuming Fang ⋅ Jiebin Yan ⋅ Yifan Zuo
122. **PriorPose: Reference-Guided Joint Deformation and Alignment for Category-Level Object Pose Estimation**  
   Yihan Chen ⋅ Huan Ren ⋅ Wenfei Yang ⋅ Hang Du ⋅ Tianzhu Zhang ⋅ Feng Wu
123. **Progressive Pose-Guided 4D Animal Reconstruction from Monocular Video**  
   Siyuan Li ⋅ Weiying Chen ⋅ Yilin Wang ⋅ Xinxin Zuo ⋅ Xingyu Li ⋅ Li Cheng  
   [arXiv:2607.00157](https://arxiv.org/abs/2607.00157)
124. **Prosthesis-Aware 3D Human Pose Estimation: A Dataset and Benchmark for RSP Users**  
   Yilin Wen ⋅ Kechuan Dong ⋅ Fumiya Suginaka ⋅ Ken Endo ⋅ Yusuke Sugano
125. **Q-BridgeNet: A Quantization Network for Cross-Lingual Sign Language Translation**  
   Liqian Feng ⋅ Lintao Wang ⋅ Xiaochen Liu ⋅ Anusha Withana ⋅ Ken-Tye Yong ⋅ Dehui Kong ⋅ Zhiyong Wang ⋅ Kun Hu  
   [arXiv:2607.11215](https://arxiv.org/abs/2607.11215) · [code](https://github.com/FengLiQ/Q-BridgeNet)
126. **RAGA: Real Time Ray Traced Gaussian Shadow Casting for 3DGS Avatar-Scene Interaction**  
   Aymen Mir ⋅ Riza Alp Guler ⋅ Jian Wang ⋅ Peter Wonka ⋅ Bing Zhou ⋅ Gerard Pons-Moll  
   [arXiv:2606.29329](https://arxiv.org/abs/2606.29329) · [project](https://miraymen.github.io/raga/)
127. **RASA: Disentangled Spatial-Motional Priors for Cross-Identity Character Animation**  
   Zhen Xiao ⋅ Zhen Shen ⋅ Zhaofan Qiu ⋅ Ting Yao ⋅ Xueliang Liu ⋅ Tao Mei
128. **RealDyadic: Synthesizing Realistic Dyadic 3D Dialogue with Neural Appearance Priors**  
   Lei Zhu ⋅ Lijian Lin ⋅ Ye Zhu ⋅ Xuehan Hou ⋅ Jiahao Wu ⋅ Yu Li ⋅ Yunfei Liu ⋅ Jie Chen
129. **Reconstruction-Anchored Diffusion Model for Text-to-Motion Generation**  
   Yifei Liu ⋅ Changxing Ding ⋅ Ling Guo ⋅ Huaiguang Jiang ⋅ Qiong Cao  
   [arXiv:2601.14788](https://arxiv.org/abs/2601.14788)
130. **Reference-Free Quality Assessment for Virtual Try-On via Human Feedback**  
   Yuki Hirakawa ⋅ Takashi Wada ⋅ Ryotaro Shimizu ⋅ Takuya Furusawa ⋅ Yuki Saito ⋅ Ryosuke Araki ⋅ Tianwei Chen ⋅ Fan Mo ⋅ Yoshimitsu Aoki
131. **Reflection-Aware Reasoning for Non-Line-of-Sight Pedestrian Localization**  
   Byeonggyu Park ⋅ Mingu Jeon ⋅ Seong-Woo Kim
132. **Reliability-Aware 3D Geometric Injection for Universal Person Re-identification**  
   Bohan Su ⋅ Jiashuo Wang ⋅ Fangyi Liu ⋅ Mang Ye  
   [arXiv:2607.18863](https://arxiv.org/abs/2607.18863) · [code](https://github.com/BohanSu/UniGeo)
133. **Remembering Across Blocks: Topology-Conditioned Block-Progressive Memory for Skeleton-Based Action Recognition**  
   Seonho Lee ⋅ Sang Han ⋅ Hyeok Nam ⋅ Sung In Cho
134. **ReMoMask: Retrieval-Augmented Masked Motion Generation**  
   Zhengdao Li ⋅ siheng wang ⋅ Zeyu Zhang ⋅ Hao Tang  
   [arXiv:2508.02605](https://arxiv.org/abs/2508.02605) · [code](https://github.com/AIGeeksGroup/ReMoMask) · [project](https://aigeeksgroup.github.io/ReMoMask)
135. **Rethinking Garment Conditioning in Diffusion-based Virtual Try-On: Decouple, Don't Denoise**  
   Kihyun Na ⋅ Jinyoung Choi ⋅ Injung Kim
136. **Retrieving and Refining Winning Noise Tickets for Diffusion-Based Motion Generation**  
   Sakuya Ota ⋅ Qing Yu ⋅ Kent Fujiwara ⋅ Satoshi Ikehata ⋅ Ikuro Sato  
   [arXiv:2607.06843](https://arxiv.org/abs/2607.06843) · [project](https://sinc865.github.io/winro/)
137. **Revisiting Avatar-As-Image: High-Fidelity Registration is All You Need**  
   Margaret Kostyrko ⋅ Yuxuan Xue ⋅ Garvita Tiwari ⋅ Gerard Pons-Moll
138. **RoboGesture: Real-Time Semantic-aligned Co-Speech Gestures Generation for Humanoid Interaction**  
   Zifan Wang ⋅ Ziang Ren ⋅ Pengyang Shi ⋅ Zirui Wang ⋅ Chenghuai Lin ⋅ Tianze Wang ⋅ Zekun Qi ⋅ Liangliang Zhao ⋅ HE WANG ⋅ Li Yi
139. **Rolling Shutter Relative Pose Estimation Made Practical**  
   Daniel Barath  
   [arXiv:2606.26863](https://arxiv.org/abs/2606.26863) · [code](https://github.com/danini/rolling_shutter_made_practical)
140. **S2Gest: Split-Scan State Space Models for Dynamic Hand Gesture Recognition**  
   KeFan Chen ⋅ Yong Gu ⋅ bo li ⋅ Longjie Huang ⋅ Jiajun Zhang
141. **Saber: Anchoring Semantics to Scale-Aware Kinetic Salience for Zero-Shot Skeleton Action Recognition**  
   Zhu Yongquan ⋅ Biru Ning ⋅ Jingyu Zhang
142. **SAGE: A Synchronized Action and Gaze Estimation Framework for Comprehensive Human Behavior Analysis**  
   Chenyi Kuang ⋅ Nakul Agarwal
143. **SCORE: SubDistribution-aware Collaborative Knowledge Reinforcing for Cloth-Hybrid Lifelong Person Re-Identification**  
   Kunlun Xu ⋅ Liangyu Ma ⋅ Jiangmeng Li ⋅ Xin Tong ⋅ Xiaode Liu ⋅ Yufei Guo ⋅ Jiahuan Zhou
144. **Self-supervised Garment Dynamics with Persistent Wrinkles**  
   Xiaoyuan Yang ⋅ Deshan Gong ⋅ Taku Komura ⋅ He Wang  
   [arXiv:2606.25065](https://arxiv.org/abs/2606.25065)
145. **SemGAN: A Semantic and Hierarchical Adversarial Network for 3D Human Pose Estimation**  
   Haodong Feng ⋅ Yu Xin ⋅ Guoqing Li
146. **Sen-Cap: Sensor-Flexible and Noise-Resilient Human Motion Capture via LiDAR-Camera Integration**  
   Aoru Xue ⋅ Yujing Sun ⋅ yiming ren ⋅ Kwok-Yan Lam ⋅ Mao Ye ⋅ Yuexin Ma  
   [arXiv:2608.02285](https://arxiv.org/abs/2608.02285)
147. **SignBind-LLM: Multi-Stage Modality Fusion for Sign Language Translation**  
   Marshall Thomas ⋅ Edward Fish ⋅ Richard Bowden  
   [arXiv:2509.00030](https://arxiv.org/abs/2509.00030)
148. **SIGNER: Temporally Grounded Sign Language Generation via Time-Resolved Conditioning**  
   Taeryung Lee ⋅ Hyeongjin Nam ⋅ Gyeongsik Moon ⋅ Kyoung Mu Lee  
   [arXiv:2506.07460](https://arxiv.org/abs/2506.07460) · [project](https://taeryunglee.github.io/projects/signer)
149. **SIGNET: Motion-Level Knowledge Transfer for Cross-Language Sign Language Translation**  
   Sobhan Asasi ⋅ Ozge Mercanoglu Sincan ⋅ Richard Bowden  
   [arXiv:2606.28626](https://arxiv.org/abs/2606.28626)
150. **SignNet-1M: Large-Scale Multilingual Sign Language Video Dataset with Downstream Benchmarks**  
   Zhewen He ⋅ Junyi Hu ⋅ Haomian Huang ⋅ Zhenhua Li ⋅ Yushen Liu ⋅ Yi Fang  
   [arXiv:2606.24361](https://arxiv.org/abs/2606.24361) · [project](https://signnet.chatsign.ai/)
151. **SignRefine: Adapting Foundational Video Models for Sign Language Generation**  
   Anton Pelykh ⋅ Edward Fish ⋅ Ozge Mercanoglu Sincan ⋅ Richard Bowden
152. **SignSparK: Efficient Multilingual Sign Language Production via Sparse Keyframe Learning**  
   Jian He Low ⋅ Alexandre Symeonidis-Herzig ⋅ Maksym Ivashechkin ⋅ Ozge Mercanoglu Sincan ⋅ Richard Bowden  
   [arXiv:2603.10446](https://arxiv.org/abs/2603.10446) · [code](https://github.com/JianHe0628/SignSparK) · [project](https://cogvis-cvssp.github.io/papers/signspark/)
153. **SK-Adapter: Skeleton-Based Structural Control for Native 3D Generation**  
   Anbang Wang ⋅ AO Yuzhuo ⋅ Elliott (Shangzhe) Wu ⋅ Chi-Keung Tang  
   [arXiv:2603.14152](https://arxiv.org/abs/2603.14152) · [project](https://sk-adapter.github.io/)
154. **SKEL-CF: Coarse-to-Fine Biomechanical Skeleton and Surface Mesh Recovery**  
   Da Li ⋅ Ji-Ping Jin ⋅ Xiaodong Cun ⋅ Xuanlong Yu ⋅ Wei LIU ⋅ Rui Fan ⋅ Jiangang Kong ⋅ Kai Chen ⋅ Xi SHEN  
   [arXiv:2511.20157](https://arxiv.org/abs/2511.20157) · [project](https://pokerman8.github.io/SKEL-CF/)
155. **SkillSpotter: Pose-Aware Multi-View Skilled Action Detection and Grading in Ego-Exo Videos**  
   Björn Braun ⋅ Christian Holz  
   [arXiv:2606.31127](https://arxiv.org/abs/2606.31127) · [code](https://github.com/eth-siplab/SkillSpotter)
156. **SPAR: A Sequential Primacy and Attribution Ranking Framework for Skill Determination**  
   Hui Yu ⋅ Xiao Ke ⋅ Zhihong Zeng ⋅ Huangbiao Xu ⋅ Huanqi Wu ⋅ Yaru Su
157. **SparseCtrl-HOI: Sparse Temporal Control for Human-Object Interaction Video Generation**  
   Shenbo Xie ⋅ Mingrui Cai ⋅ Xu Yang ⋅ Yifei Liu ⋅ Changxing Ding  
   [arXiv:2607.05994](https://arxiv.org/abs/2607.05994) · [project](https://mpi-lab.github.io/SparseCtrl-HOI)
158. **SplatCtrlA: Generalizable Single Image to Fully Controllable 3D Avatar**  
   Jun Xiang ⋅ Yudong Guo ⋅ Boyang Guo ⋅ Yancheng Yuan ⋅ Juyong Zhang
159. **Stitched Embeddings: A Unified Latent Space for 3D Garments and 2D Patterns**  
   Andrea Sanchietti ⋅ Riccardo Marin ⋅ Bharat Bhatnagar ⋅ Yuanlu Xu ⋅ Gerard Pons-Moll  
   [arXiv:2607.00829](https://arxiv.org/abs/2607.00829) · [project](https://andreus00.github.io/stitchedembeddings)
160. **SWSL: Semantic-aware Weakly Supervised Learning for 3D Motion Generation using 2D Motion Data**  
   Zhicheng Shi ⋅ Tuo Feng ⋅ Wenguan Wang ⋅ Yi Yang
161. **SynHMR: Synergistic Joint-Mesh Modeling for LiDAR-based Human Mesh Reconstruction**  
   Rui Shi ⋅ Xiaoqi An ⋅ Lin Zhao ⋅ Di Wang ⋅ Chen Gong ⋅ Le Zhang
162. **TAIHRI: Task-Aware 3D Human Keypoints Localization for Close-Range Human-Robot Interaction**  
   Ao Li ⋅ Yonggen Ling ⋅ Yiyang Lin ⋅ Yuji Wang ⋅ Yong Deng ⋅ Yansong Tang  
   [arXiv:2604.08921](https://arxiv.org/abs/2604.08921) · [code](https://github.com/Tencent/TAIHRI)
163. **The Language of Visual Attention: Modeling Scanpaths via Autoregressive Token Prediction**  
   Susmit Agrawal ⋅ Matthias Bethge ⋅ Matthias Kuemmerer
164. **TimeWalker: Personalized Neural Space for Lifelong Head Avatars**  
   Dongwei Pan ⋅ Yang Li ⋅ Hongsheng LI ⋅ Kwan-Yee Lin  
   [arXiv:2412.02421](https://arxiv.org/abs/2412.02421) · [project](https://timewalker2025.github.io/timewalker.github.io/)
165. **Towards in-the-wild Egocentric 3D Hand-Object Pose Estimation**  
   Siddhant Bansal ⋅ Zhifan Zhu ⋅ Shashank Tripathi ⋅ Jiahe Zhao ⋅ Michael Black ⋅ Dima Damen  
   [arXiv:2606.30598](https://arxiv.org/abs/2606.30598) · [project](https://sid2697.github.io/epic-contact)
166. **Towards Real-World Wearable Motion Reconstruction**  
   Andrea Boscolo Camiletto ⋅ Rishabh Dabral ⋅ Eduardo Alvarado ⋅ Thabo Beeler ⋅ Marc Habermann ⋅ Christian Theobalt  
   [arXiv:2607.09780](https://arxiv.org/abs/2607.09780) · [project](https://vcai.mpi-inf.mpg.de/projects/WHIP/)
167. **Training-free Controllable Motion Generation under Heterogeneous Constraints**  
   Xiaofei Hui ⋅ Bo Yan ⋅ Haoxuan Qu ⋅ Hossein Rahmani ⋅ Jun Liu
168. **TraversRL: Traversable Pedestrian Pathway Generation With Reinforcement Learning**  
   Bin Han ⋅ Robert Wolfe ⋅ Bill Howe  
   [arXiv:2607.17479](https://arxiv.org/abs/2607.17479)
169. **TripVVT: A Large-Scale Triplet Dataset and a Coarse-Mask Baseline for In-the-Wild Video Virtual Try-On**  
   Dingbao Shao ⋅ Song Wu ⋅ Shenyi Wang ⋅ Ye Wang ⋅ Ziheng Tang ⋅ Fei Liu ⋅ Jiang Lin ⋅ Xinyu Chen ⋅ Qian Wang ⋅ Ying Tai ⋅ Jian Yang ⋅ Zili Yi  
   [arXiv:2604.27958](https://arxiv.org/abs/2604.27958)
170. **TryOnCrafter: Unleashing Camera Trajectories for Realistic Video Virtual Try-on via a Renderable 4D Try-on Proxy**  
   Hao Sun ⋅ Hao Yan ⋅ Mengting Chen ⋅ Quanjian Song ⋅ Yu Li ⋅ Juan Cao ⋅ Jinsong Lan ⋅ Xiaoyong Zhu ⋅ Bo Zheng ⋅ Sheng Tang  
   [arXiv:2606.26092](https://arxiv.org/abs/2606.26092) · [project](https://sunhao242.github.io/TryOnCrafter_web.github.io/)
171. **UF0-6D: Unified Flow-based Zero-Shot 6D Object Pose Estimation without Refinement**  
   Yingnan Guo ⋅ Chun Lim ⋅ Yu Feng ⋅ Yu Zhang
172. **Unleashing Multimodal Large Language Models for Training-free HOI Detection in the Wild**  
   Ting Lei ⋅ Jialin Liu ⋅ Zhu Xu ⋅ Yuxin Peng ⋅ Yang Liu  
   [arXiv:2607.13881](https://arxiv.org/abs/2607.13881)
173. **URHead: A Unified UV-Space Representation for Joint Mesh–3DGS Optimization in Head Avatars**  
   Seonghak Lee ⋅ Junhee Cho ⋅ Jisoo Park ⋅ Min-Gyu Park ⋅ Jongmin Lee ⋅ Ju Yoon ⋅ Junseok Kwon  
   [arXiv:2607.22673](https://arxiv.org/abs/2607.22673) · [project](https://lseonghak.github.io/website/project/urhead/)
174. **VersatileMotion: A Unified Framework for Motion Synthesis and Comprehension**  
   Zeyu Ling ⋅ Bo Han ⋅ Shiyang Li ⋅ Jikang Cheng ⋅ Hongdeng Shen ⋅ Changqing Zou  
   [arXiv:2411.17335](https://arxiv.org/abs/2411.17335)
175. **Video-Text Alignment Model for Sign Language Translation**  
   Junyi Hu ⋅ Zhewen He ⋅ Haomian Huang ⋅ Yi Fang ⋅ Aoxiang Yang  
   [arXiv:2607.09126](https://arxiv.org/abs/2607.09126) · [code](https://github.com/junyi2005/vtamo)
176. **WAPR: A Foundation Model for Wide-Angle Refinement in Unseen Object Pose Estimation**  
   Yulin Wang ⋅ Jianghao Zhou ⋅ Hongli Li ⋅ MENGTING HU ⋅ Chen LUO
177. **WearWow: Native 2K Multi-Garment Virtual Try-On via Adaptive Token Packing and Preference Alignment**  
   Xujie Zhang ⋅ Runyan Du ⋅ Song Chang ⋅ Jiang Li ⋅ Dongliang Shao ⋅ Liping Wu ⋅ Luo Wei ⋅ Xiaochao Qu ⋅ Luoqi Liu ⋅ Xiaodan Liang  
   [arXiv:2607.19923](https://arxiv.org/abs/2607.19923)
178. **What Moves? Localized Motion Representations for Compositional Scene Control**  
   Frank Fundel ⋅ Malek Ben Alaya ⋅ Thomas Ressler-Antal ⋅ Stefan Andreas Baumann ⋅ Bjorn Ommer
179. **WiFi-JEPA: Self-supervised Learning for WiFi-CSI 3D Human Pose Estimation**  
   Doeon Kim ⋅ Jungyoon Lee ⋅ SEONGSIN KIM ⋅ Seong-heum Kim  
   [arXiv:2607.11064](https://arxiv.org/abs/2607.11064)
180. **World Models for Learning Dexterous Hand-Object Interactions from Human Videos**  
   Raktim Goswami ⋅ Amir Bar ⋅ David Fan ⋅ Tsung-Yen Yang ⋅ Gaoyue Zhou ⋅ Prashanth Krishnamurthy ⋅ Michael Rabbat ⋅ Farshad Khorrami ⋅ Yann LeCun  
   [arXiv:2512.13644](https://arxiv.org/abs/2512.13644)
181. **XYZ-IBD: Benchmarking Robust 6D Object Pose Estimation under Real-World Industrial Complexity**  
   Junwen Huang ⋅ Jiaqi Hu ⋅ Peter Yu ⋅ Slobodan Ilic ⋅ Martin Sundermeyer ⋅ Benjamin Busam  
   [arXiv:2506.00599](https://arxiv.org/abs/2506.00599) · [project](https://xyz-ibd.github.io)

## Face, Portrait & Identity

*38 papers · 16 with links*

1. **Anchoring on Reality: Breaking the Pseudo-Target Ceiling in Makeup Transfer**  
   Bo Wei ⋅ Xianhui Lin ⋅ Yi Dong ⋅ Zhongzhong Li ⋅ Zonghui Li ⋅ Zirui Wang ⋅ Jiachen Yang ⋅ Xing Liu ⋅ Hong Gu ⋅ Xiaoming Li ⋅ Wangmeng Zuo  
   [arXiv:2606.31089](https://arxiv.org/abs/2606.31089)
2. **Beyond the Boundary: RL-Driven Solution Space Exploration for Blind Face Restoration**  
   Bin WU ⋅ Wei Wang ⋅ Yahui Liu ⋅ Chi Zhang ⋅ Yao Zhao
3. **Breaking High Confidence: Practical Face Impersonation under High-Security Thresholds**  
   Changjin Kim ⋅ Seunghun Paik ⋅ Dongsoo Kim ⋅ Jae Hong Seo
4. **BRepFacetGen: Reverse Engineering B-Reps By Generative Face Segmentation**  
   Ka Hei Hui ⋅ Vikas Thamizharasan ⋅ Pradeep Kumar Jayaraman ⋅ Xiang Xu
5. **CLIP-AUTT: Test-Time Personalization with Action Unit Prompting for Fine-Grained Video Emotion Recognition**  
   Muhammad Osama Zeeshan ⋅ Masoumeh Sharafi ⋅ Benoît Savary ⋅ Alessandro Lameiras Koerich ⋅ Marco Pedersoli ⋅ Eric Granger  
   [arXiv:2603.27999](https://arxiv.org/abs/2603.27999)
6. **Compositional Non-Face Re-Identification Pressure under Cumulative Vision Releases**  
   Tirth Joshi ⋅ Honggang Wang
7. **Discovering Geometric Biases in 3D Face Reconstruction: A Curvature-Aware Spectral Framework for Fairness Evaluation**  
   Veronika Shilova ⋅ Emmanuel Malherbe ⋅ Giovanni Palma ⋅ Panagiotis-Alexandros Bokaris ⋅ Laurent Risser ⋅ Jean-Michel Loubes  
   [arXiv:2607.07486](https://arxiv.org/abs/2607.07486)
8. **DTI: Dynamic Trajectory Initialization for Generative Face Video Super-Resolution**  
   Yingwei TANG ⋅ Chen Yan ⋅ Wendi Liu ⋅ Qiang Hu ⋅ Xiaoyun Zhang  
   [arXiv:2606.29198](https://arxiv.org/abs/2606.29198)
9. **Extreme Face Super-Resolution through Identity Fitting and Decoupling**  
   Jiarui Yang ⋅ Hang Guo ⋅ Wen Huang ⋅ Shu-Tao Xia ⋅ Tao Dai
10. **Face Anything: 4D Face Reconstruction from Any Image Sequence**  
   Umut Kocasarı ⋅ Simon Giebenhain ⋅ Richard Shaw ⋅ Matthias Niessner  
   [arXiv:2604.19702](https://arxiv.org/abs/2604.19702) · [project](https://kocasariumut.github.io/FaceAnything/)
11. **FaceArmor: A Universal Facial Image Protection Against Diffusion-Based Manipulations**  
   Yiming Wang ⋅ Jiahao Chen ⋅ Qingming Li ⋅ Chunyi Zhou ⋅ Zhi Chen ⋅ Lingzhong Meng ⋅ Jinbao Li ⋅ Shouling Ji
12. **FaceMoE: Mixture of Experts for Low-Resolution Face Recognition**  
   Kartik Narayan ⋅ Vishal Patel  
   [arXiv:2606.32040](https://arxiv.org/abs/2606.32040) · [code](https://github.com/Kartik-3004/FaceMoE) · [project](https://kartik-3004.github.io/FaceMoE/)
13. **Fair and Faithful: A Diffusion-Enhanced Dataset and Hybrid State-Space Mamba for Face Super-Resolution**  
   Tao Wang ⋅ Peiwen Xia ⋅ Bowen Tang ⋅ Jinwei Chen ⋅ Kaihao Zhang ⋅ Bo Li
14. **FED-Bench: A Cross-Granular Benchmark for Disentangled Evaluation of Facial Expression Editing**  
   Fengjian Xue ⋅ Xuecheng Wu ⋅ Heli Sun ⋅ Yunyun Shi ⋅ Shi Chen ⋅ Liangyu Fu ⋅ Jinheng Xie ⋅ Dingkang Yang ⋅ Hao Wang ⋅ Junxiao Xue ⋅ Liang He  
   [arXiv:2603.29697](https://arxiv.org/abs/2603.29697)
15. **FlowFace: Rectifying Identity Conditioning with Riemannian Geometry for Face Generation**  
   Xinran Deng ⋅ Yiling Wu ⋅ Ye Tian ⋅ Libo Zhang
16. **HairOrbit: Multi-view Aware 3D Hair Modeling from Single Portraits**  
   Leyang Jin ⋅ Yujian Zheng ⋅ Bingkui Tong ⋅ Yuda Qiu ⋅ Zhenyu Xie ⋅ Hao Li  
   [arXiv:2604.02867](https://arxiv.org/abs/2604.02867)
17. **ID-PreFeR: ID-Preserving Face Restoration with Mixed Data Quality**  
   Chengxuan Zhu ⋅ Yuchen Hong ⋅ Qingnan Fan ⋅ Qi Zhang ⋅ Bingtao Fu ⋅ Jinxiu Liang ⋅ Jinwei Chen ⋅ Huaqi Zhang ⋅ Chao Xu ⋅ Boxin Shi
18. **In-Context Sync-LoRA for Portrait Video Editing**  
   Sagi Polaczek ⋅ Or Patashnik ⋅ Ali Mahdavi-Amiri ⋅ Danny Cohen-Or  
   [arXiv:2512.03013](https://arxiv.org/abs/2512.03013) · [project](https://sagipolaczek.github.io/Sync-LoRA/)
19. **IREU: Identity-Related Encoder-Only Unlearning for Customized Portrait Generation**  
   Chaoyi Shi ⋅ Shanshan Zhang ⋅ Jian Yang  
   [arXiv:2606.29880](https://arxiv.org/abs/2606.29880)
20. **Learning to Attract and Repel: Dual Quality Margin Learning for Face Recognition (DQM-Face)**  
   El Belabbaci ⋅ Bhavesh Wani ⋅ Philipp Terhörst
21. **MagicMakeup: A Region-Controllable Diffusion Transformer for High-Fidelity Makeup-Transfer**  
   Ziyi Wang ⋅ Siming Zheng ⋅ yang yang ⋅ Shusong Xu ⋅ Hao Zhang ⋅ Bo Li ⋅ Changqing Zou ⋅ Peng-Tao Jiang
22. **MirrorPPR: Exemplar-Based Portrait Photo Retouching**  
   Zhihong Liu ⋅ Zheng Li ⋅ Jiachun Jin ⋅ Siqi Kou ⋅ Yitao Jian ⋅ Fengpei Yu ⋅ Zhijie Deng  
   [arXiv:2606.29308](https://arxiv.org/abs/2606.29308) · [project](https://sjtu-deng-lab.github.io/MirrorPPR)
23. **MTVDiff: Multimodal Conditional Latent Diffusion for Enhanced Thermal-to-Visible Face Translation**  
   Zhiyuan Xia ⋅ Haojie Li ⋅ Jingyu Lin ⋅ Yiguo Qiao ⋅ Cunjian Chen  
   [arXiv:2607.19886](https://arxiv.org/abs/2607.19886)
24. **Noise-Robust Face Recognition via Non-target Similarity Distribution Guided Sample Selection**  
   Fanglong Wu ⋅ Youqiang Gui ⋅ Cheng Peng
25. **Noise-Robust Facial Expression Recognition via Mamba-driven Neighbor Weight Refinement**  
   Yuzhuang Yang ⋅ Xiaolin Tian ⋅ Qigong Sun
26. **OmniFace: Bridging the Image-to-Video Gap for High-Fidelity Face Swapping via Diffusion Transformer**  
   Xu Guo ⋅ Fulong Ye ⋅ Xinghui Li ⋅ Pengqi Tu ⋅ Pengze Zhang ⋅ Qichao Sun ⋅ Songtao Zhao ⋅ Xiangwang Hou ⋅ Qian HE
27. **Parallax Portrait Matting**  
   Xin Cai ⋅ Jiawen Chen ⋅ Lars Jebe ⋅ Tianfan Xue ⋅ Zhoutong Zhang  
   [arXiv:2607.11205](https://arxiv.org/abs/2607.11205)
28. **PriSM: Parsing and Style-Mixed Consistency for Unsupervised Domain Adaptation in Facial Landmark Detection**  
   Chieh-Yu Yang ⋅ Hou-Ning Hu ⋅ Sykai Chen ⋅ Yu-Lun Liu ⋅ Yen-Yu Lin
29. **Pro-Pose: Unpaired Full-Body Portrait Synthesis via Canonical UV Maps**  
   Sandeep Mishra ⋅ Yasamin Jafarian ⋅ Andreas Lugmayr ⋅ Yingwei Li ⋅ Varsha Ramakrishnan ⋅ Srivatsan Varadharajan ⋅ Alan Bovik ⋅ Ira Kemelmacher-Shlizerman  
   [arXiv:2512.17143](https://arxiv.org/abs/2512.17143)
30. **Purify then Guide: Rethinking Domain Generalization for Multimodal Face Anti-Spoofing**  
   Yingjie Ma ⋅ Xun Lin ⋅ Zitong Yu ⋅ Haonan Wang ⋅ Ruixin Zhang ⋅ Shouhong Ding ⋅ Xin Liu ⋅ Xiaochen Yuan ⋅ Weicheng Xie ⋅ Linlin Shen  
   [arXiv:2505.09484](https://arxiv.org/abs/2505.09484)
31. **Rethinking Attention Reallocation for Multimodal Emotion Recognition**  
   Yazhe Lyu ⋅ Yixiong Zou ⋅ Jinghan Hu ⋅ Yuhua Li ⋅ Ruixuan Li
32. **Reweighting Framewise Attention in Video Transformers for Facial Emotion Recognition**  
   Seongro Yoon ⋅ Donghyeon Cho ⋅ Jinsun Park ⋅ Francois Bremond
33. **Sparsity-Inducing Divergence Losses for Biometric Verification**  
   Dimitrios Koutsianos ⋅ Ladislav Mosner ⋅ Yannis Panagakis ⋅ Themos Stafylakis  
   [arXiv:2606.31664](https://arxiv.org/abs/2606.31664)
34. **TextFace: Compositional Text-Guided Identity Preserving Face Synthesis for Face Recognition**  
   Junzhe Yang ⋅ Mingjie He ⋅ Shiguang Shan
35. **TIGER: Taming Identity, Geometry, and Generative Priors for High-Quality Face Video Restoration**  
   Yang Zhou ⋅ Wenxue Li ⋅ Peng Zhang ⋅ Yifei Chen ⋅ Fei Wang ⋅ Daiguo Zhou
36. **TRAM: Finetuning-Free Test-Time Adaptation for Generalized Face Anti-Spoofing with Only a Few Bonafide Samples**  
   Wang QIRUI ⋅ SI-QI LIU
37. **Visible Yet Unrecognizable: Frequency-Selective Facial Privacy via Attention**  
   Atul Kumar ⋅ Akshay Agarwal
38. **μFlow: Leveraging Average Images for Improving Generalisation of Deepfake Faces Detectors**  
   Orazio Pontorno ⋅ Mattia Litrico ⋅ Luca Guarnera ⋅ Mario Valerio Giuffrida ⋅ Sebastiano Battiato

## Embodied AI, Robotics & Manipulation

*148 papers · 99 with links*

1. **360CityArena: A Realistic Virtual Urban Navigation Benchmark for Embodied Agents**  
   Kenta Watanabe ⋅ Atsuyuki Miyai ⋅ Mizuki Takenawa ⋅ Kiyoharu Aizawa ⋅ Toshihiko Yamasaki  
   [arXiv:2608.08814](https://arxiv.org/abs/2608.08814) · [project](https://360mm-team.github.io/360CityArena/)
2. **3DWay: Generalizing Robot Manipulation via 3D Consistent Waypoints**  
   Huang Ziqin ⋅ Yingyue Li ⋅ Chenyangguang Zhang ⋅ Ruida Zhang ⋅ Yuxin Chen ⋅ Gu Wang ⋅ Xingyu Liu ⋅ Masayoshi TOMIZUKA ⋅ Xiangyang Ji
3. **A4-Agent: An Agentic Framework for Zero-Shot Affordance Reasoning**  
   Zixin Zhang ⋅ Kanghao Chen ⋅ Hanqing Wang ⋅ Hongfei Zhang ⋅ Harold Haodong Chen ⋅ Chenfei Liao ⋅ Litao Guo ⋅ Yinchuan Li ⋅ Yingcong Chen  
   [arXiv:2512.14442](https://arxiv.org/abs/2512.14442)
4. **ActionPlan: Future-Aware Streaming Motion Synthesis via Frame-Level Action Planning**  
   Eric Nazarenus ⋅ Chuqiao Li ⋅ Yannan He ⋅ Xianghui Xie ⋅ Jan Eric Lenssen ⋅ Gerard Pons-Moll  
   [arXiv:2603.13500](https://arxiv.org/abs/2603.13500) · [project](https://coral79.github.io/ActionPlan/)
5. **Agent-OBJ: Prompt-Driven 3D Adversaries for Multi-Modal Perception**  
   Bing Li ⋅ Sean Du ⋅ Xuhong Ren ⋅ Luqi Gong ⋅ Wee Peng Tay ⋅ Qing Guo
6. **Agentic Collaborative Cognition for Zero-Shot 3D Understanding**  
   Wenxin Wang ⋅ Bo Zhang ⋅ Feng Chen ⋅ Zixuan Wang ⋅ Wen Li ⋅ Changsheng Li ⋅ Yinjie Lei  
   [arXiv:2606.24649](https://arxiv.org/abs/2606.24649) · [project](https://zhangbo135.github.io/agentic-collaborative-cognition/)
7. **AgentVLN: Towards Agentic Vision-and-Language Navigation**  
   Zihao Xin ⋅ Wentong Li ⋅ Yixuan Jiang ⋅ Ziyuan Huang ⋅ Bin Wang ⋅ Piji Li ⋅ Jianke Zhu ⋅ Jie Qin ⋅ Sheng-Jun Huang  
   [arXiv:2603.17670](https://arxiv.org/abs/2603.17670) · [code](https://github.com/Allenxinn/AgentVLN)
8. **AMCoNav: Asynchronous Multi-module Collaborative Framework for Embodied Visual Navigation**  
   Jiaquan Yan ⋅ Fang Zhao ⋅ Yushi Chen ⋅ Long wang ⋅ Haiyong Luo ⋅ Dan Luo
9. **AnchorGUI: Asymmetric Memory for Dual-Scale Learning in GUI Navigation**  
   Shengjie Jin ⋅ Zelong Sun ⋅ Hengbo Xu ⋅ Yanbiao Ma ⋅ Zhiwu Lu
10. **Are GUI Agents Focused Enough? Automated Distraction via Semantic-level UI Element Injection**  
   Wenkui Yang ⋅ chao jin ⋅ Haisu Zhu ⋅ Weilin Luo ⋅ Derek Yuen ⋅ Kun Shao ⋅ Junxian Duan ⋅ Huaibo Huang ⋅ Jie Cao ⋅ Ran He  
   [arXiv:2604.07831](https://arxiv.org/abs/2604.07831) · [code](https://github.com/HashTAG00002/UI-Injection)
11. **ARGOS: Who, Where, and When in Agentic Multi-Camera Person Search**  
   Myungchul Kim ⋅ Kwanyong Park ⋅ Junmo Kim ⋅ In Kweon  
   [arXiv:2604.12762](https://arxiv.org/abs/2604.12762)
12. **ASSCG: Just-Right Gating over Chattering for Fast–Slow LLM Planning in Autonomous Driving**  
   Sining Ang ⋅ Yuan Chen ⋅ Liu Haiyan ⋅ Xuanyao Mao ⋅ jason bao ⋅ Xuliang Xuliang ⋅ Bingchuan Sun ⋅ Yan Wang  
   [arXiv:2606.25509](https://arxiv.org/abs/2606.25509) · [project](https://williamxuanyu.github.io/asscg/)
13. **ATP-Bench: Towards the Agentic Tool Planning for MLLM Interleaved Generation**  
   Yinuo Liu ⋅ Zi Qian ⋅ Heng Zhou ⋅ Jiahao Zhang ⋅ Yajie Zhang ⋅ Zhihang Li ⋅ Mengyu Zhou ⋅ Erchao Zhao ⋅ xiaoxi jiang ⋅ Guanjun Jiang  
   [arXiv:2603.29902](https://arxiv.org/abs/2603.29902) · [code](https://github.com/Qwen-Applications/ATP-Bench)
14. **AutoSpeed: Annotation-Free Stage-Adaptive Motion Speed Learning for Robot Manipulation**  
   Qingda Hu ⋅ Ziheng Qiu ⋅ Jieru Zhao ⋅ Zhongxue Gan ⋅ Wenchao Ding  
   [arXiv:2607.01051](https://arxiv.org/abs/2607.01051)
15. **Beyond Description: Cognitively Benchmarking Fine-Grained Action for Embodied Agents**  
   Dayong Liu ⋅ Chao Xu ⋅ Weihong Chen ⋅ Suyu Zhang ⋅ Juncheng Wang ⋅ Jiankang Deng ⋅ Baigui Sun ⋅ Yang Liu  
   [arXiv:2511.18685](https://arxiv.org/abs/2511.18685) · [project](https://cfg-bench.github.io/)
16. **Beyond Where to Look: Trajectory-Guided Reinforcement Learning for Multimodal RLVR**  
   Jinda Lu ⋅ Junkang Wu ⋅ Jinghan Li ⋅ Kexin Huang ⋅ Shuo Yang ⋅ Mingzhu Chen ⋅ Jiancan Wu ⋅ Kuien Liu ⋅ Xiang Wang  
   [arXiv:2603.26126](https://arxiv.org/abs/2603.26126)
17. **CellFluxRL: Biologically-Constrained Virtual Cell Modeling via Reinforcement Learning**  
   Dongxia Wu ⋅ Shiye Su ⋅ Yuhui Zhang ⋅ Elaine Sui ⋅ Emma Lundberg ⋅ Emily Fox ⋅ Serena Yeung-Levy  
   [arXiv:2603.21743](https://arxiv.org/abs/2603.21743)
18. **ChronoFlow Policy: Unifying Past-Future Interaction Flow in Visuomotor Policy Learning**  
   Bokai Lin ⋅ Yifu Xu ⋅ Xinyu Zhan ⋅ Hongjie Fang ⋅ Jialin Tian ⋅ Fu-Cheng Zhang ⋅ Yong-Lu Li ⋅ Cewu Lu ⋅ Lixin Yang  
   [arXiv:2606.31493](https://arxiv.org/abs/2606.31493) · [project](https://the-kamisato-sii.github.io/ChronoFlow-Policy-project-page/)
19. **CiQi-Agent: Aligning Vision, Tools and Aesthetics in Multimodal Agent for Cultural Reasoning on Chinese Porcelains**  
   Wenhan Wang ⋅ Zhixiang Zhou ⋅ Zhongtian Ma ⋅ Yanzhu Chen ⋅ Ziyu Lin ⋅ Hao Sheng ⋅ Pengfei Liu ⋅ Wenqi Shao ⋅ Qiaosheng Zhang ⋅ Yu Qiao  
   [arXiv:2603.28474](https://arxiv.org/abs/2603.28474) · [code](https://huggingface.co/datasets/SII-Monument-Valley/CiQi-VQA)
20. **Coding with Eyes: Visual Feedback Unlocks Reliable GUI Code Generating and Debugging**  
   Zhilin Liu ⋅ Ye Huang ⋅ TingXie TingXie ⋅ Ruizhi Zhang ⋅ Wen Li ⋅ Lixin Duan  
   [arXiv:2604.19750](https://arxiv.org/abs/2604.19750)
21. **ContextFlow: In-Context Flow Matching for Robot Manipulation**  
   Jian Ding ⋅ Xianjie DAI ⋅ Roei Herzig ⋅ Nussair Hroub ⋅ Jinjie Mai ⋅ Dengxin Dai ⋅ Bernard Ghanem ⋅ Mohamed Elhoseiny
22. **CoSPlan: Corrective Sequential Planning via Scene Graph Incremental Updates**  
   Shresth Grover ⋅ Priyank Pathak ⋅ Akash Kumar ⋅ Yogesh Rawat  
   [arXiv:2512.10342](https://arxiv.org/abs/2512.10342)
23. **CoToGrasp: Contact-Topology-Conditioned Dexterous Grasp Synthesis via Canonical Workspace Learning**  
   Julien Mérand ⋅ Boris Meden ⋅ Liming Chen ⋅ Mathieu GROSSARD
24. **CulinaryCut: A Physics-aware Vision-Language-Action Benchmark for Food Cutting via Material Point Method**  
   Hyunsuh Koh ⋅ CHANG-YONG SONG ⋅ Youngjae Choi ⋅ Misa Viveiros ⋅ David Hyde ⋅ Heewon Kim
25. **Diffusion Models are Open-World Affordance Learners: Leveraging Generative Priors for 3D Affordance Learning**  
   Hanqing Wang ⋅ Zhenhao Zhang ⋅ Kaiyang Ji ⋅ Mingyu Liu ⋅ Wenti Yin ⋅ yuchao chen ⋅ Zhirui Liu ⋅ Xiangyu Zeng ⋅ Tianxiang Gui ⋅ Hangxing Zhang ⋅ Jiahao Yuan ⋅ Zhiqing Cui ⋅ Jiaxin Liu ⋅ Zhiyuan Ma ⋅ Hui Xiong  
   [arXiv:2508.01651](https://arxiv.org/abs/2508.01651) · [code](https://github.com/hq-King/DAG)
26. **DiNBV-Grasp: Real-Time Distance-Aware Two-Stage Next-Best-View for Robotic Grasping**  
   Zilong Xie ⋅ Jingyu Gong ⋅ Xin Tan ⋅ Zhizhong Zhang ⋅ Yanyun Qu ⋅ Lizhuang Ma ⋅ Yuan Xie
27. **DisRM: Reward Modeling as Discriminative Prediction**  
   Runtao Liu ⋅ Jiahao Zhan ⋅ Yuxuan GUO ⋅ Yingqing He ⋅ Chen Wei ⋅ Alan Yuille ⋅ Qifeng Chen
28. **Distribution Matching Distillation Meets Reinforcement Learning**  
   Dengyang Jiang ⋅ Dongyang Liu ⋅ Zanyi Wang ⋅ Qilong Wu ⋅ Liuzhuozheng Li ⋅ Heng-Zhuang Li ⋅ Xin Jin ⋅ Zhen Li ⋅ Changsheng Lu ⋅ Mengmeng Wang ⋅ Steven Hoi ⋅ Peng Gao ⋅ Harry Yang  
   [arXiv:2511.13649](https://arxiv.org/abs/2511.13649) · [code](https://github.com/vvvvvjdy/dmdr)
29. **Domain Arithmetic: One-Shot VLA Adaptation under Environmental Shifts**  
   Taewook Kang ⋅ Taeheon Kim ⋅ Donghyun Shin ⋅ Jonghyun Choi  
   [arXiv:2607.00666](https://arxiv.org/abs/2607.00666) · [code](https://github.com/snumprlab/dart) · [project](https://twkang43.github.io/projects/dart)
30. **Driving is a Game: Combining Planning and Prediction with Bayesian Iterative Best Response**  
   Aron Distelzweig ⋅ Yiwei Wang ⋅ Faris Janjos ⋅ Marcel Hallgarten ⋅ Mihai Dobre ⋅ Alexander Langmann ⋅ Joschka Boedecker ⋅ Johannes Betz  
   [arXiv:2512.03936](https://arxiv.org/abs/2512.03936)
31. **Dual-Anchoring: Addressing State Drift in Vision-Language Navigation**  
   Kangyi Wu ⋅ Pengna Li ⋅ Kailin Lyu ⋅ Xi Lin ⋅ Lin Zhao ⋅ Qingrong He ⋅ Jinjun Wang ⋅ Jianyi Liu  
   [arXiv:2604.17473](https://arxiv.org/abs/2604.17473)
32. **E-TTS: A New Embodied Test-Time Scaling Framework for Robotic Manipulation**  
   Wen Ye ⋅ Peiyan Li ⋅ Tingyu Yuan ⋅ Yuan Xu ⋅ Xiangnan Wu ⋅ Chaoyang Zhao ⋅ Jing Liu ⋅ Nianfeng Liu ⋅ Yan Huang ⋅ Liang Wang  
   [arXiv:2606.27268](https://arxiv.org/abs/2606.27268) · [project](https://27yw.github.io/E-TTS-Web/)
33. **Efficient Camera Pose Augmentation for View Generalization in Robotic Policy Learning**  
   Sen Wang ⋅ Huaiyi Dong ⋅ Jingyi Tian ⋅ lijiayi lijiayi ⋅ Zhuo Yang ⋅ Tongtong Cao ⋅ Anlin Chen ⋅ Shuang Wu ⋅ Sanping Zhou ⋅ Le Wang  
   [arXiv:2603.29192](https://arxiv.org/abs/2603.29192)
34. **EmbodiedVAE: Disentangled Video VAE for Efficient and Controllable Embodied Manipulation**  
   Jiayi Luo ⋅ Hanxin Zhu ⋅ Chen Gao ⋅ Jiankun Wang ⋅ Cong Wang ⋅ Tianyu He ⋅ Jianxin Li ⋅ Zhibo Chen  
   [arXiv:2608.02990](https://arxiv.org/abs/2608.02990)
35. **EpiBench: Benchmarking Multi-turn Research Workflows for Multimodal Agents**  
   Xuan Dong ⋅ Huanyang Zheng ⋅ Tianhao Niu ⋅ Zhe Han ⋅ Pengzhan Li ⋅ Bofei Liu ⋅ Zhengyang Liu ⋅ Guancheng Li ⋅ Qingfu Zhu ⋅ Wanxiang Che  
   [arXiv:2604.05557](https://arxiv.org/abs/2604.05557)
36. **EvoVLA: Self-Evolving Vision-Language-Action Model**  
   Zeting Liu ⋅ ZIDA YANG ⋅ Zeyu Zhang ⋅ Hao Tang  
   [arXiv:2511.16166](https://arxiv.org/abs/2511.16166) · [code](https://github.com/AIGeeksGroup/EvoVLA) · [project](https://aigeeksgroup.github.io/EvoVLA)
37. **EvoWorld: A World-Model-Centric Framework for Continuous Self-Evolution of Modular Embodied Skills**  
   boshi zhang ⋅ Sen Cui ⋅ Baohua Yin ⋅ Youyi Kou ⋅ Junyu Wu ⋅ Zuo Pu ⋅ TAO XUE ⋅ Zhikang Chen ⋅ Shanshan Wei ⋅ Min Zhang ⋅ Miao Liu ⋅ Changshui Zhang ⋅ Zhang Tao
38. **Exo2EgoPolicy: Pose-Aligned Cross-View Policy Learning**  
   Hritam Basak ⋅ Hadi Tabatabaee ⋅ Xin Yang ⋅ Shreekant Gayaka ⋅ Nan Qiao ⋅ Yuyin Sun ⋅ Cheng-Hao Kuo ⋅ Zhaozheng Yin ⋅ Min Sun
39. **Exposing Implicit Vulnerabilities in Text-to-Image Models via Adversarial Agentic Probing**  
   Chang Ma ⋅ Junlin Han ⋅ Shuo Chen ⋅ Runjia Li ⋅ Philip Torr ⋅ Jindong Gu
40. **Fast-dVLA: Accelerating Discrete Diffusion VLA to Real-Time Performance**  
   Wenxuan Song ⋅ Jiayi Chen ⋅ Shuai Chen ⋅ Jingbo Wang ⋅ Pengxiang Ding ⋅ Han Zhao ⋅ qin yikai ⋅ Xinhu Zheng ⋅ Yan Wang ⋅ Donglin Wang ⋅ Haoang Li  
   [arXiv:2603.25661](https://arxiv.org/abs/2603.25661) · [project](https://chris1220313648.github.io/Fast-dVLA/)
41. **FindingDory: A Benchmark to Evaluate Memory in Embodied Agents**  
   Karmesh Yadav ⋅ Yusuf Ali ⋅ Gunshi Gupta ⋅ Yarin Gal ⋅ Zsolt Kira  
   [arXiv:2506.15635](https://arxiv.org/abs/2506.15635) · [project](https://findingdory-benchmark.github.io/)
42. **Fixed Reality, Diffused Possibility: Disentangling Stochastic and Deterministic Latent for Cluttered Grasping**  
   Hritam Basak ⋅ Zhaozheng Yin
43. **From Passive Observer to Active Critic: Reinforcement Learning Elicits Process Reasoning for Robotic Manipulation**  
   Yibin Liu ⋅ Yaxing Lyu ⋅ Daqi Gao ⋅ Zhixuan Liang ⋅ Weiliang Tang ⋅ Shilong Mu ⋅ Xiaokang Yang ⋅ Mingyu Ding ⋅ Yao Mu  
   [arXiv:2603.15600](https://arxiv.org/abs/2603.15600)
44. **GAIA: A Data Flywheel System for Training GUI Test-Time Scaling Critic Models**  
   Shaokang Wang ⋅ Pei Fu ⋅ Ruoceng Zhang ⋅ Shaojie Zhang ⋅ Xiuwen Xi ⋅ Jiahui Yang ⋅ Bin Qin ⋅ Ying Huang ⋅ Zhenbo Luo ⋅ Jian Luan
45. **GameWorlds: Towards Standardized and Verifiable Evaluation of Multimodal Game Agents**  
   Mingyu Ouyang ⋅ Siyuan Hu ⋅ Qinghong Lin ⋅ Hwee Tou Ng ⋅ Mike Zheng Shou  
   [arXiv:2604.07429](https://arxiv.org/abs/2604.07429) · [project](https://gameworld-bench.github.io)
46. **GEM: Generative Supervision Helps Embodied Intelligence**  
   Ruowen Zhao ⋅ Bangguo Li ⋅ ZUYAN LIU ⋅ Yinan Liang ⋅ junliang ye ⋅ FANGFU LIU ⋅ Diankun Wu ⋅ Zhengyi Wang ⋅ Xumin Yu ⋅ Yongming Rao ⋅ Han Hu ⋅ Jun Zhu  
   [arXiv:2605.28548](https://arxiv.org/abs/2605.28548) · [project](https://zhaorw02.github.io/GEM/)
47. **Grasp-Oriented Non-Prehensile Manipulation via Learning a Graspability Field**  
   Licheng Zhong ⋅ Gim Hee Lee  
   [arXiv:2606.30474](https://arxiv.org/abs/2606.30474)
48. **Gripper-aware Vision Language Action Models**  
   Hanyi Zhang ⋅ Zihong Luo ⋅ Tianyu Li ⋅ Khang Nguyen ⋅ Basu Hela ⋅ Shreyas Kumar ⋅ Ngoc Tran ⋅ Feng Dai ⋅ Charith Munasinghe ⋅ Jorge Queralta ⋅ Giovanni Toffetti ⋅ Khoa Vo ⋅ Ngan Le ⋅ Ravi Prakash ⋅ Quan Vuong ⋅ Tung Ta ⋅ Long Hu ⋅ Anh Nguyen ⋅ Baoru Huang
49. **Grounding Sim-to-Real Generalization in Dexterous Manipulation: An Empirical Study with Vision-Language-Action Models**  
   Ruixing Jin ⋅ ZiCheng Zhu ⋅ Ruixiang Ouyang ⋅ Sheng Xu ⋅ Bo Yue ⋅ Zhizheng Wu ⋅ Guiliang Liu
50. **GUI-AIMA: Aligning Intrinsic Multimodal Attention with a Context Anchor for GUI Grounding**  
   Shijie Zhou ⋅ Viet Lai ⋅ Hao Tan ⋅ Jihyung Kil ⋅ Wanrong Zhu ⋅ Changyou Chen ⋅ Ruiyi Zhang  
   [arXiv:2511.00810](https://arxiv.org/abs/2511.00810) · [code](https://github.com/sjz5202/GUI-AIMA)
51. **Guide, Think, Act: Interactive Embodied Reasoning for Vision-Language-Action Model**  
   Yiran Ling ⋅ Qing Lian ⋅ Jinghang Li ⋅ Qing Jiang ⋅ TianMing Zhang ⋅ Xiaoke Jiang ⋅ Chuanxiu Liu ⋅ Jie Liu ⋅ Lei Zhang  
   [arXiv:2605.13632](https://arxiv.org/abs/2605.13632) · [code](https://github.com/FutianLabs/GTA-VLA)
52. **Guiding the Blind: Generalizing GUI Agents to Unseen Websites via Multimodal Tutorials**  
   Xinwei Long ⋅ Kai Tian ⋅ Peng Xu ⋅ Weibo Gao ⋅ Yihua Shao ⋅ Guoli Jia ⋅ Haozhe Geng ⋅ Sa Yang ⋅ Jingxuan Li ⋅ Huayong Hu ⋅ Kaiyan Zhang ⋅ Jiaqi Wang ⋅ Bowen Zhou
53. **HAT-4D: Lifting Monocular Video for 4D Multi-Object Interactions via Human-Agent Collaboration**  
   Jiaxin Li ⋅ Yuxiang Wu ⋅ Zhenkai Zhang ⋅ Xinrui Shi ⋅ wang haoyuan ⋅ Yichen Zhao ⋅ Su Linxiang ⋅ Chenyang chenyang ⋅ Mingyu Zhang ⋅ Yifan Ding ⋅ Boran Wen ⋅ li zhang ⋅ Ruiyang Liu ⋅ Yong-Lu Li  
   [arXiv:2606.28215](https://arxiv.org/abs/2606.28215) · [project](https://lijiaxin0111.github.io/HAT4D/)
54. **HERO: Enhancing Multimodal Faithfulness via Dynamic Entropy-Aware Reinforcement Learning**  
   Xiongfeng Yang ⋅ Qingan Zhang ⋅ Yuheng Zhang ⋅ Kun-Yu Lin ⋅ Jian-Fang Hu ⋅ Dongmei Jiang ⋅ WEISHI ZHENG
55. **Hi-Nav: Hierarchical Framework for Continuous Vision-Language Navigation via Map Guidance and Waypoint Reasoning**  
   Zhiyu Zhou ⋅ Bin Guan ⋅ Wenbin Yang ⋅ Zhi Gao ⋅ Hao Fang
56. **Hierarchical 3D Scene Graph Construction and Belief-based Planning for Semantic Navigation**  
   Bing Wu ⋅ Zuyao Chen ⋅ Chang Wen Chen  
   [arXiv:2606.31071](https://arxiv.org/abs/2606.31071)
57. **HiPolicy: Hierarchical Multi-Frequency Action Chunking for Policy Learning**  
   Jiyao Zhang ⋅ Zimu Han ⋅ Junhan Wang ⋅ Xionghao Wu ⋅ Shihong Lin ⋅ Jinzhou Li ⋅ Hongwei Fan ⋅ Ruihai Wu ⋅ Dongjiang Li ⋅ Hao Dong  
   [arXiv:2604.06067](https://arxiv.org/abs/2604.06067)
58. **HippoCamp: Benchmarking Contextual Agents on Personal Computers**  
   Zhe YANG ⋅ Shulin Tian ⋅ Kairui Hu ⋅ Shuai Liu ⋅ Hoang-Nhat Nguyen ⋅ Yichi Zhang ⋅ Zujin Guo ⋅ Mengying Yu ⋅ Zinan Zhang ⋅ Jingkang Yang ⋅ Chen Change Loy ⋅ Ziwei Liu  
   [arXiv:2604.01221](https://arxiv.org/abs/2604.01221) · [project](https://hippocamp-ai.github.io/)
59. **Humanoid Whole-Body Manipulation via Active Spatial Brain and Generalizable Action Cerebellum**  
   Zhizhao Liang ⋅ Yi-Lin Wei ⋅ Xuhang Chen ⋅ Mu Lin ⋅ Yi-Xiang He ⋅ Zhexi Luo ⋅ Jun-Hui Liu ⋅ Kun-Yu Lin ⋅ WEISHI ZHENG  
   [arXiv:2605.21133](https://arxiv.org/abs/2605.21133) · [project](https://leungchaos.github.io/Humanoid-Whole-Body-Manipulation-via-Active-Spatial-Brain-and-Generalizable-Action-Cerebellum/)
60. **Hybrid Advantage Estimation with Unified Critic for VLM Agentic Reinforcement Learning**  
   Wenxuan Zhang ⋅ Yuhui Wang ⋅ Donggang Jia ⋅ Xiaoqian Shen ⋅ Jian Ding ⋅ Ivan Viola ⋅ Jürgen Schmidhuber ⋅ Mohamed Elhoseiny  
   [arXiv:2607.23605](https://arxiv.org/abs/2607.23605) · [project](https://wx-zhang.github.io/hygae-web/)
61. **Hypothesis Graph Refinement: Hypothesis-Driven Exploration with Cascade Error Correction for Embodied Navigation**  
   Peixin Chen ⋅ Guoxi Zhang ⋅ Jianwei Ma ⋅ Qing Li  
   [arXiv:2604.04108](https://arxiv.org/abs/2604.04108)
62. **Is Monitoring Enough? Strategic Agent Selection For Stealthy Attack in Multi-Agent Discussions**  
   Qiuchi Xiang ⋅ Haoxuan Qu ⋅ Hossein Rahmani ⋅ Jun Liu  
   [arXiv:2603.21194](https://arxiv.org/abs/2603.21194)
63. **KATANA: Knowledge-Aligned Topology-Aware Neural Agents for RL-Driven Vision-Language Model Compression**  
   Nafew Azim ⋅ Mir Ali ⋅ Fuad Rahman ⋅ Nabeel Mohammed
64. **Kiroshi: An Agentic Perception System for High-Accuracy Image Parsing**  
   Haipeng ZHOU ⋅ Jinshan Liu ⋅ He Zhang ⋅ Xuequan Lu ⋅ Jun Ma ⋅ Lei Zhu
65. **Knowledge-Centric Agents for Workflow Generation in ComfyUI**  
   Zhendong Li ⋅ Lei Sun ⋅ Ruibo Ming ⋅ He Zhang ⋅ Danda Paudel ⋅ Luc Van Gool ⋅ Jinjin Gu  
   [arXiv:2607.15845](https://arxiv.org/abs/2607.15845)
66. **LEAP-VLA: Latent-Enhanced Action Prototyping via Continuous Residual Latent Spaces for Vision-Language-Action Models**  
   Bo-Yun Yu ⋅ Jun Hsieh ⋅ KUAN-CHUAN PENG
67. **Learn2Fold: Structured Origami Generation with World Model Planning**  
   Yanjia Huang ⋅ Yunuo Chen ⋅ Ying Jiang ⋅ Zhengzhong Tu ⋅ Yin Yang ⋅ Chenfanfu Jiang  
   [arXiv:2603.29585](https://arxiv.org/abs/2603.29585)
68. **Learning from Failure: Inference-Time Self-Improvement for Computer-Use Agents**  
   Xueqiao Sun ⋅ Yuhui Zhang ⋅ Xiaohan Wang ⋅ Ludwig Schmidt ⋅ Serena Yeung-Levy  
   [arXiv:2606.31270](https://arxiv.org/abs/2606.31270)
69. **Learning from Reliable Negatives: Confidence-Anchored Test-Time Adaptation for GUI Grounding**  
   Yizhou Liu ⋅ Fei Tang ⋅ Yuchen Yan ⋅ Zhengxi Lu ⋅ Songqin Nong ⋅ Tao Jiang ⋅ Wenhao Xu ⋅ Wenqi Zhang ⋅ Weiming Lu ⋅ Jun Xiao ⋅ Jun Xiao
70. **Less is More: Reducing Complexity in Vision-Language-Action Systems**  
   Jinhui Ye ⋅ Ning Gao ⋅ Senqiao Yang ⋅ Jinliang Zheng ⋅ Zixuan Wang ⋅ Yuxin Chen ⋅ Pengguang Chen ⋅ Yilun Chen ⋅ Shu Liu ⋅ Jiaya Jia
71. **Lifting Ego World Models for Planning and Control**  
   Alex Wang ⋅ Trevor Darrell ⋅ Pavel Izmailov ⋅ Yutong Bai ⋅ Amir Bar
72. **M2Tok: Multi-head Multi-codebook Discrete Action Tokenization for Vision-Language-Action Models**  
   Chunpu Xu ⋅ Zhixuan Liang ⋅ Yuhao Zhang ⋅ Chi-Min Chan ⋅ Jiashuo Wang ⋅ Yang Xiao ⋅ Mengkang Hu ⋅ Xiaokang Yang ⋅ Yao Mu
73. **Mechanistic Finetuning of Vision-Language-Action Models via Few-Shot Demonstrations**  
   Chancharik Mitra ⋅ Yusen Luo ⋅ Raj Saravanan ⋅ Dantong Niu ⋅ Anirudh Pai ⋅ Jesse Thomason ⋅ Trevor Darrell ⋅ Abrar Anwar ⋅ Deva Ramanan ⋅ Roei Herzig  
   [arXiv:2511.22697](https://arxiv.org/abs/2511.22697)
74. **MindDrive: A Vision-Language-Action Model for Autonomous Driving via Online Reinforcement Learning**  
   haoyu fu ⋅ Diankun Zhang ⋅ Zongchuang Zhao ⋅ Jianfeng Cui ⋅ Hongwei Xie ⋅ Bing Wang ⋅ Guang Chen ⋅ Hangjun Ye ⋅ Dingkang Liang ⋅ Xiang Bai  
   [arXiv:2512.13636](https://arxiv.org/abs/2512.13636) · [project](https://xiaomi-mlab.github.io/MindDrive/)
75. **MM-Nav: Multi-View VLA Model for Robust Visual Navigation via Multi-Expert Learning**  
   Tianyu Xu ⋅ Jiawei Chen ⋅ Jiazhao Zhang ⋅ Wenyao Zhang ⋅ Zekun Qi ⋅ Minghan Li ⋅ Jiahang Liu ⋅ Lu Yue ⋅ Zhizheng Zhang ⋅ HE WANG  
   [arXiv:2510.03142](https://arxiv.org/abs/2510.03142) · [project](https://pku-epic.github.io/MM-Nav-Web/)
76. **MMAgent-R2: Learning to Rerank and Reject for Agentic mRAG**  
   Tao Zhang ⋅ Ziqi Zhang ⋅ Zongyang Ma ⋅ Yuxin Yang ⋅ Bing Li ⋅ Chunfeng Yuan ⋅ Kang Rong ⋅ Fengyun Rao ⋅ Jing LYU ⋅ Weiming Hu
77. **MolmoWeb: Open Visual Web Agent and Open Data for the Open Web**  
   Tanmay Gupta ⋅ Piper Wolters ⋅ Zixian Ma ⋅ Peter Sushko ⋅ Rock Yuren Pang ⋅ Yue Yang ⋅ Jason Ren ⋅ Harsh Trivedi ⋅ Taira Anderson ⋅ Winson Han ⋅ Ranjay Krishna  
   [arXiv:2604.08516](https://arxiv.org/abs/2604.08516) · [project](https://allenai.org/blog/molmoweb)
78. **NavWM: A Unified Navigation World Model for Foresight-Driven Planning**  
   Yanghong Mei ⋅ Longteng Guo ⋅ MingMing Yu ⋅ Guiyu Zhao ⋅ Xingjian He ⋅ Jing Liu  
   [arXiv:2606.24101](https://arxiv.org/abs/2606.24101)
79. **NeSy-Route: A Neural-Symbolic Benchmark for Constrained Route Planning in Remote Sensing**  
   Ming Yang ⋅ Zhi Zhou ⋅ Shi-Yu Tian ⋅ Kun-Yang Yu ⋅ Lan-Zhe Guo ⋅ Yu-Feng Li  
   [arXiv:2603.16307](https://arxiv.org/abs/2603.16307) · [project](https://mingyang1010.github.io/NeSy-Route/)
80. **NutriBench-Kitchen: Benchmarking Embodied AI for Nutrition Management**  
   YuLin Wei ⋅ Xiangchen Wang ⋅ Jianhui Pan ⋅ Jinyu Xiao ⋅ Zheng Tan ⋅ Ruozai Tian ⋅ Guanhua Chen ⋅ Feng Zheng
81. **Omni-RRM: Advancing Omni Reward Modeling via Automatic Rubric-Grounded Preference Synthesis**  
   Zicheng Kong ⋅ Dehua Ma ⋅ Zhenbo Xu ⋅ Anwen Yang ⋅ Yiwei Ru ⋅ Haoran Wang ⋅ Zixuan Zhou ⋅ Fuqing Bie ⋅ Liuyu Xiang ⋅ Huijia Wu ⋅ Jian Zhao ⋅ Zhaofeng He  
   [arXiv:2602.00846](https://arxiv.org/abs/2602.00846) · [project](https://tmfk418.github.io/Omni-RRM)
82. **One Demonstration Is Enough for Real-World Robotic Reinforcement Learning**  
   Yuwan Liu ⋅ Hongze Yu ⋅ song liu ⋅ Yuhan Wang ⋅ Junge Zhang ⋅ Yaodong Yang ⋅ Yuanpei Chen ⋅ Ceyao Zhang  
   [arXiv:2607.01651](https://arxiv.org/abs/2607.01651) · [project](https://autoserl.github.io/)
83. **One-Step Flow Policy: Self-Distillation for Fast Visuomotor Policies**  
   Shaolong Li ⋅ Lichao Sun ⋅ Yongchao Chen  
   [arXiv:2603.12480](https://arxiv.org/abs/2603.12480)
84. **OpenGround: Planning-based Online Perception for Open-World 3D Visual Grounding**  
   Wenyuan Huang ⋅ zhenyu zhang ⋅ Zhao Wang ⋅ Zhou Wei ⋅ Ting Huang ⋅ Fang Zhao ⋅ Jian Yang  
   [arXiv:2512.23020](https://arxiv.org/abs/2512.23020) · [project](https://why-102.github.io/openground.io/)
85. **ORION: Ordinal Neural Collapse as a Representation Prior for Visual Navigation**  
   E In Son ⋅ Jung-Taak Kim ⋅ Seung-Woo Seo
86. **PARL-VLA: Pruning-Aware On-Policy Reinforcement Learning for Vision-Language-Action Model**  
   ruiyan xu ⋅ Jiashu Lv ⋅ Sixu Lin ⋅ Ruixing Jin ⋅ Shuliang He ⋅ Guiliang Liu
87. **Path-level Hindsight Instructions for Semantic Exploration in Vision-Language Navigation**  
   Sungjune Kim ⋅ Sangpil Kim ⋅ Honglak Lee  
   [arXiv:2607.01754](https://arxiv.org/abs/2607.01754)
88. **Persistent Robot World Models: Stabilizing Multi-Step Rollouts via Reinforcement Learning**  
   Jai Bardhan ⋅ Patrik Drozdík ⋅ Josef Sivic ⋅ Vladimir Petrik  
   [arXiv:2603.25685](https://arxiv.org/abs/2603.25685)
89. **Personalization as Inverse Planning: Learning Latent Design Intents for Agentic Slide Generation via Structural Denoising**  
   Tianci Liu ⋅ Zihan Dong ⋅ Linjun Zhang ⋅ Haoyu Wang ⋅ Jing Gao ⋅ Emre Kiciman ⋅ Ranveer Chandra ⋅ Wei-Ting Chen  
   [arXiv:2607.00407](https://arxiv.org/abs/2607.00407)
90. **PolicyTrim: Boosting Intrinsic Policy Efficiency of Vision-Language-Action Models**  
   Xianghui Wang ⋅ Feng Chen ⋅ Wenbo Zhang ⋅ Hua Yan ⋅ Zixuan Wang ⋅ Changsheng Li ⋅ Yinjie Lei  
   [arXiv:2606.22540](https://arxiv.org/abs/2606.22540) · [project](https://inceptionwang.github.io/PolicyTrim/)
91. **Pondering the Way: Spatial-perceiving World Action Model for Embodied Navigation**  
   Hong Chen ⋅ Daqi Liu ⋅ Zehan Zhang ⋅ Haiguang Wang ⋅ Tianhao Lu ⋅ Longfei Yan ⋅ Haiyang Sun ⋅ Fangzhen Li ⋅ Hongwei Xie ⋅ Bing Wang ⋅ Guang Chen ⋅ Hangjun Ye ⋅ Yihua Tan  
   [arXiv:2606.29908](https://arxiv.org/abs/2606.29908)
92. **Practice Makes Perfect: From Explicit Decomposition to Reinforced Latent Planning in Text-to-Human Motion**  
   Ronghao Yu ⋅ Yang Liu ⋅ Juncheng Wang ⋅ Chao Xu ⋅ Yimo Shao ⋅ Baigui Sun ⋅ Yong Liu ⋅ Shan Luo
93. **ProAct: Agentic Lookahead in Interactive Environments**  
   Yangbin Yu ⋅ Mingyu Yang ⋅ junyou li ⋅ Yiming Gao ⋅ Feiyu Liu ⋅ Yijun Yang ⋅ Zichuan Lin ⋅ Jiafei Lyu ⋅ Zhicong Lu ⋅ Deheng Ye ⋅ Jie Jiang  
   [arXiv:2602.05327](https://arxiv.org/abs/2602.05327) · [code](https://github.com/GreatX3/ProAct)
94. **R3DP: Real-Time 3D-Aware Policy for Embodied Manipulation**  
   Yuhao Zhang ⋅ Wanxi Dong ⋅ Yue Shi ⋅ Yi Liang ⋅ Jingnan Gao ⋅ Qiaochu Yang ⋅ Yaxing Lyu ⋅ Zhixuan Liang ⋅ Yibin Liu ⋅ Congsheng Xu ⋅ Xianda Guo ⋅ Wei Sui ⋅ Yaohui Jin ⋅ Xiaokang Yang ⋅ Yanyan Xu ⋅ Yao Mu  
   [arXiv:2603.14498](https://arxiv.org/abs/2603.14498) · [code](https://github.com/dazazh/R3DP) · [project](https://dazazh.github.io/r3dp-project-page/)
95. **RAGrasp: A Retrieval-Augmented Framework with Diversity-Aware Modeling for Dexterous Grasp Generation**  
   Zhuo Yang ⋅ Sanping Zhou ⋅ Sen Wang ⋅ Jingyi Tian ⋅ lijiayi lijiayi ⋅ Gang Hua ⋅ Le Wang
96. **ReGRPO: Reflection-Augmented Policy Optimization for Tool-Using Agents**  
   Binjie Zhang ⋅ Mike Zheng Shou  
   [arXiv:2606.31392](https://arxiv.org/abs/2606.31392) · [code](https://github.com/showlab/ReGRPO)
97. **RelAfford6D: Relational 6D Affordance Graphs for Constraint-Driven Robotic Manipulation**  
   Guodong Zhang ⋅ Qichen He ⋅ Wenyuan Xie ⋅ Shaokai Wu ⋅ Yanbiao Ji ⋅ Qiuchang Li ⋅ Bayram Bayramli ⋅ Yue Ding ⋅ Hongtao Lu  
   [arXiv:2606.27036](https://arxiv.org/abs/2606.27036)
98. **RePlan: Reasoning-Guided Region Planning for Complex Instruction-Based Image Editing**  
   Tianyuan Qu ⋅ Lei Ke ⋅ Xiaohang Zhan ⋅ Longxiang Tang ⋅ Yuqi Liu ⋅ Bohao PENG ⋅ Bei Yu ⋅ Dong Yu ⋅ Jiaya Jia  
   [arXiv:2512.16864](https://arxiv.org/abs/2512.16864) · [project](https://replan-iv-edit.github.io)
99. **Restoring Linguistic Grounding in VLA Models via Train-Free Attention Recalibration**  
   Ninghao Zhang ⋅ Bin Zhu ⋅ Shijie Zhou ⋅ Jingjing Chen  
   [arXiv:2603.06001](https://arxiv.org/abs/2603.06001)
100. **Reward Modeling for Computer-Using Agent from Video Execution**  
   Linxin Song ⋅ Jieyu Zhang ⋅ Huanxin Sheng ⋅ Taiwei Shi ⋅ Rahul Gupta ⋅ Yang Liu ⋅ Ranjay Krishna ⋅ Jian Kang ⋅ Jieyu Zhao
101. **RL from Physical Feedback: Aligning Large Motion Models with Humanoid Control**  
   Junpeng Yue ⋅ Zepeng Wang ⋅ Jiangxing Wang ⋅ Yuxuan Wang ⋅ Yu Zhang ⋅ Xinrun Xu ⋅ Bin Cao ⋅ Sipeng Zheng ⋅ gang ding ⋅ Zongqing Lu  
   [arXiv:2506.12769](https://arxiv.org/abs/2506.12769)
102. **RoboClaw: An Agentic Framework for Scalable Long-Horizon Robotic Tasks**  
   Ruiying Li ⋅ Yunlang Zhou ⋅ Yuyao Zhu ⋅ Kylin Chen ⋅ Sukai Wang ⋅ Kongtao Hu ⋅ Minhui Yu ⋅ Bowen Jiang ⋅ Jiayao Ma ⋅ Zhan Su ⋅ Yongjian Shen ⋅ Yang Yang ⋅ Guanghui Ren ⋅ Maoqing Yao ⋅ Wenhao Wang ⋅ Yao Mu  
   [arXiv:2603.11558](https://arxiv.org/abs/2603.11558) · [code](https://github.com/RoboClaw-Robotics/RoboClaw)
103. **RoboMirror: Understand Before You Imitate for Video to Humanoid Locomotion**  
   Zhe Li ⋅ Boan Zhu ⋅ Yangyang Wei ⋅ Shuanghao Bai ⋅ Yuheng Ji ⋅ Tao Huang ⋅ Pengwei Wang ⋅ Zhongyuan Wang ⋅ S.-H. Chan ⋅ Chang Xu ⋅ Cheng Chi ⋅ Jianfei Yang ⋅ Shanghang Zhang  
   [arXiv:2512.23649](https://arxiv.org/abs/2512.23649)
104. **RoboTALES: Learning Reasoning-Guided Robot Policies via Task-Aligned Simulated Futures**  
   Hanan Gani ⋅ Tejal Kulkarni ⋅ Madhoolika Chodavarapu ⋅ Nicklas Hansen ⋅ Manmohan Chandraker  
   [arXiv:2607.06018](https://arxiv.org/abs/2607.06018) · [code](https://github.com/hananshafi/RoboTALES)
105. **Rule-VLN: Bridging Perception and Compliance via Semantic Reasoning and Geometric Rectification**  
   Jiawen Wen ⋅ Penglei SUN ⋅ Wenjie Zhang ⋅ Suixuan QIU ⋅ Weisheng Xu ⋅ Xiaofei Yang ⋅ Xiaowen Chu  
   [arXiv:2604.16993](https://arxiv.org/abs/2604.16993)
106. **SafeGuard: A Multi-Agent Perception-Reasoning Framework for Social-Risk AI-Generated Video Detection**  
   Wenlin Wu ⋅ Sheng Zhou ⋅ Peipei Song ⋅ Wenhao Wang ⋅ Junbin Xiao ⋅ Xun Yang  
   [arXiv:2607.03069](https://arxiv.org/abs/2607.03069) · [code](https://github.com/williamw99/SafeGuard)
107. **SafeSAE-VLA: Interpreting OpenVLA Progress Dynamics with Sparse Feature Analysis**  
   Socrates Osorio ⋅ Joy Yang
108. **Scalable Cross-embodiment Dexterous Grasping via Morphology-Prior Diffusion**  
   Sihang Li ⋅ Zheming Zhou ⋅ Marcelino Almeida ⋅ Omid Alizadeh ⋅ Luca Carlone ⋅ Min Sun ⋅ Chen Feng ⋅ Cheng-Hao Kuo
109. **Scaling Verification Can Be More Effective than Scaling Policy Learning for Vision-Language-Action Alignment**  
   Jacky Kwok ⋅ Xilun Zhang ⋅ Mengdi Xu ⋅ Yuejiang Liu ⋅ Azalia Mirhoseini ⋅ Chelsea Finn ⋅ Marco Pavone  
   [arXiv:2602.12281](https://arxiv.org/abs/2602.12281)
110. **SegDiff: Segmented Trajectory Diffusion for Consistent and Adaptive Robot Manipulation**  
   Haidong Cao ⋅ Wenjun Cao ⋅ Quanhao Li ⋅ Sicheng Xie ⋅ Zhiying Du ⋅ Jiaqi Leng ⋅ Zuxuan Wu ⋅ Yu-Gang Jiang  
   [arXiv:2607.11027](https://arxiv.org/abs/2607.11027)
111. **Self-Evolving Agentic Image Restoration via Deliberate Planning and Intuitive Execution**  
   Shuang Cui ⋅ Fan Ji ⋅ Guanglong Sun ⋅ Yufei Guo ⋅ Xiongxin Tang ⋅ Jiangmeng Li ⋅ Fanjiang Xu  
   [arXiv:2606.28971](https://arxiv.org/abs/2606.28971)
112. **Self-Evolving MCP-GUI Agents via Automated Environment Generation and Experience Learning**  
   Tiantian He ⋅ Yihang Chen ⋅ Keyue Jiang ⋅ Ka Lee ⋅ Kaiwen Zhou ⋅ Kun Shao ⋅ Shuai Wang  
   [arXiv:2604.09815](https://arxiv.org/abs/2604.09815)
113. **Sentinel: Embodied Cooperative Spatial Reasoning and Planning**  
   Xiangye Lin ⋅ Hongxin Zhang ⋅ Ruxi Deng ⋅ Qinhong Zhou ⋅ Chuang Gan  
   [arXiv:2605.26239](https://arxiv.org/abs/2605.26239) · [code](https://github.com/UMass-Embodied-AGI/Sentinel)
114. **SIMON: SImultaneous Multi-Object Navigation**  
   Yifeng Zhu ⋅ Siyuan Huang ⋅ Jun Bao ⋅ Jun Yu ⋅ Buyu Liu
115. **SpaMEM: Benchmarking Dynamic Spatial Reasoning via Perception–Memory Integration in Embodied Environments**  
   Chih-Ting Liao ⋅ Xi Xiao ⋅ Chunlei Meng ⋅ Zhangquan Chen ⋅ Yitong Qiao ⋅ Weilin Zhou ⋅ Tianyang Wang ⋅ Xu Zheng ⋅ Xin Cao  
   [arXiv:2604.22409](https://arxiv.org/abs/2604.22409) · [code](https://huggingface.co/datasets/mill-ct-liao/SpaMEM)
116. **SpatiO: Adaptive Test-Time Orchestration of Vision-Language Agents for Spatial Reasoning**  
   ChanYeong Hwang ⋅ Miso Choi ⋅ Sunghyun On ⋅ Jinkyu Kim ⋅ Jungbeom Lee
117. **SPEAR: A Simulator for Photorealistic Embodied AI Research**  
   Mike Roberts ⋅ Renhan Wang ⋅ Rushikesh Zawar ⋅ Rachith Dey-Prakash ⋅ Quentin Leboutet ⋅ Stephan Richter ⋅ Matthias Müller ⋅ German Ros ⋅ Rui Tang ⋅ Stefan Leutenegger ⋅ Yannick Hold-Geoffroy ⋅ Kalyan Sunkavalli ⋅ Vladlen Koltun  
   [arXiv:2607.06701](https://arxiv.org/abs/2607.06701)
118. **SwiftWA: An Efficient Action-Centered World-Action Model**  
   Chaojun Ni ⋅ Xinyu Zhou ⋅ YuKun Zhou ⋅ Jingyu Liu ⋅ Xiaofeng Wang ⋅ Zheng Zhu ⋅ Yang Wang ⋅ Qiuping Deng ⋅ Yun Ye ⋅ Hao Li ⋅ Zhichao Liu ⋅ Jindi Lv ⋅ Boyuan Wang ⋅ Guosheng Zhao ⋅ Guan Huang ⋅ Min Cao ⋅ Wenjun Mei
119. **SymbOmni: Evolving Agentic Omni Models via Symbolic Concept Learning**  
   Jinxiu Liu ⋅ Jianru Li ⋅ Tanqing Kuang ⋅ Xuanming Liu ⋅ Kangfu Mei ⋅ Yandong Wen ⋅ Weiyang Liu  
   [arXiv:2607.12042](https://arxiv.org/abs/2607.12042) · [project](https://spherelab.ai/symbomni)
120. **TabletopGen: Tabletop Scene Generation and Interactive Simulation for Robotic Manipulation**  
   Ziqian Wang ⋅ Yonghao He ⋅ Licheng Yang ⋅ Wei Zou ⋅ Hongxuan Ma ⋅ Liu.Liu Liu.Liu ⋅ Wei Sui ⋅ Yuxin Guo ⋅ Hu Su  
   [arXiv:2512.01204](https://arxiv.org/abs/2512.01204) · [project](https://d-robotics-ai-lab.github.io/TabletopGen.project/)
121. **Target-Bench: Can Video World Models Achieve Mapless Path Planning with Semantic Targets?**  
   Dingrui Wang ⋅ Zhihao Liang ⋅ Hongyuan Ye ⋅ Zhexiao Sun ⋅ Zhaowei Lu ⋅ Yuchen Zhang ⋅ Yuyu Zhao ⋅ Yuan Gao ⋅ Marvin Seegert ⋅ Finn Rasmus Schäfer ⋅ Haotong Qin ⋅ Wei Li ⋅ Luigi Palmieri ⋅ Felix Jahncke ⋅ Mattia Piccinini ⋅ Johannes Betz  
   [arXiv:2511.17792](https://arxiv.org/abs/2511.17792)
122. **TaxoGrasp: Taxonomy-Guided Human Grasp Synthesis with Sparse Contact Constraint**  
   Haitian Liu ⋅ Yin Wang ⋅ Zhiying Leng ⋅ Kanglei Zhou ⋅ Yan Wang ⋅ Frederick W. B. Li ⋅ Xiaohui Liang
123. **Teaching an Agent to Sketch One Part at a Time**  
   Xiaodan Du ⋅ Ruize Xu ⋅ David Yunis ⋅ Yael Vinker ⋅ Greg Shakhnarovich  
   [arXiv:2603.19500](https://arxiv.org/abs/2603.19500)
124. **Teaching Vision-Language-Action Models What to See and Where to Look**  
   Yuguang Yang ⋅ Canyu Chen ⋅ Zhewen Tan ⋅ Yizhi Wang ⋅ Zichao Feng ⋅ Chunyang Liu ⋅ Kehua Sheng ⋅ Bo Zhang ⋅ Yan Wang ⋅ Juan Zhang ⋅ Linlin Yang ⋅ Baochang Zhang ⋅ Xianbin Cao  
   [arXiv:2607.01658](https://arxiv.org/abs/2607.01658) · [code](https://github.com/ShivaTeam/DriveTeach-VLA)
125. **TIR-Bench: A Comprehensive Benchmark for Agentic Thinking-with-Images Reasoning**  
   Ming Li ⋅ Jike Zhong ⋅ Shitian Zhao ⋅ Haoquan Zhang ⋅ Shaoheng Lin ⋅ Yuxiang Lai ⋅ Chen Wei ⋅ Konstantinos Psounis ⋅ Kaipeng Zhang  
   [arXiv:2511.01833](https://arxiv.org/abs/2511.01833)
126. **Towards Generalizable Robotic Manipulation in Dynamic Environments**  
   Heng Fang ⋅ Shangru Li ⋅ Shuhan Wang ⋅ Xuanyang Xi ⋅ Dingkang Liang ⋅ Xiang Bai  
   [arXiv:2603.15620](https://arxiv.org/abs/2603.15620) · [code](https://github.com/H-EmbodVis/DOMINO) · [project](https://h-embodvis.github.io/DOMINO/)
127. **Towards More Efficient Decoding for Autoregressive Vision-language-action Models**  
   Wenxuan Song ⋅ Jiayi Chen ⋅ Pengxiang Ding ⋅ Yuxin Huang ⋅ Han Zhao ⋅ Yinchuan Li ⋅ Yingcong Chen ⋅ Donglin Wang ⋅ Haoang Li
128. **Towards Unified World Models for Visual Navigation via Memory-Augmented Planning and Foresight**  
   Yifei Dong ⋅ Fengyi Wu ⋅ Guangyu Chen ⋅ Lingdong Kong ⋅ Xu Zhu ⋅ Qiyu Hu ⋅ Yuxuan Zhou ⋅ Jingdong Sun ⋅ Jun-Yan He ⋅ Qi Dai ⋅ Alexander Hauptmann ⋅ Yifei Dong  
   [arXiv:2510.08713](https://arxiv.org/abs/2510.08713) · [code](https://github.com/F1y1113/UniWM)
129. **Trajectory-Level Continuous Action Representation for Robotic Manipulation**  
   Tong Yang ⋅ Jingkai Jia ⋅ Yuecheng Xu ⋅ Xueyao Chen ⋅ Chi Zhang ⋅ Wenqiang Zhang
130. **Transport Discrepancy as a Reliability Signal for Vision-Language-Action Models**  
   Wanpeng Zhang ⋅ Ye Wang ⋅ Hao Luo ⋅ Haoqi Yuan ⋅ Yicheng Feng ⋅ Chaoyi Xu ⋅ Sipeng Zheng ⋅ Qin Jin ⋅ Zongqing Lu  
   [arXiv:2512.01715](https://arxiv.org/abs/2512.01715)
131. **Trust Your Instincts: Confidence-Driven Test-Time RL for Vision-Language-Action Models**  
   Chen Siyao ⋅ Jiakang Yuan ⋅ Jiaxin Wang ⋅ Tao Chen  
   [arXiv:2606.29892](https://arxiv.org/abs/2606.29892)
132. **UniBYD: A Unified Framework for Learning Robotic Manipulation Across Embodiments Beyond Imitation of Human Demonstrations**  
   Tingyu Yuan ⋅ Biaoliang Guan ⋅ Wen Ye ⋅ Ziyan Tian ⋅ Yi Yang ⋅ Weijie Zhou ⋅ Zhaowen Li ⋅ Yan Huang ⋅ Peng Wang ⋅ Chaoyang Zhao ⋅ Jinqiao Wang  
   [arXiv:2512.11609](https://arxiv.org/abs/2512.11609)
133. **UniDrive-WM: Unified Understanding, Planning and Generation World Model For Autonomous Driving**  
   Zhexiao Xiong ⋅ Xin Ye ⋅ Burhaneddin Yaman ⋅ Sheng Cheng ⋅ Yiren Lu ⋅ Jingru Luo ⋅ Nathan Jacobs ⋅ Liu Ren  
   [arXiv:2601.04453](https://arxiv.org/abs/2601.04453) · [project](https://unidrive-wm.github.io/UniDrive-WM)
134. **Unified Prediction and Planning via Conflict-Aware Disjoint Parameter Training**  
   Taewon Seo ⋅ Seonae Jeon ⋅ Giwon Lee ⋅ KUK-JIN YOON ⋅ Daehee Park  
   [arXiv:2607.19971](https://arxiv.org/abs/2607.19971) · [project](https://dpt2026.github.io/)
135. **UniTeD: Unified Temporal Diffusion for Joint Perception and Planning in Autonomous Driving**  
   Bo Zhao ⋅ Xinting Zhao ⋅ Naifan Li ⋅ Erkang Cheng ⋅ Haibin Ling
136. **Unordered Landmark Visual Navigation**  
   Hao Ren ⋅ Junzhe Zhu ⋅ Yihan Li ⋅ Zetong Bi ⋅ Le Zheng ⋅ Zhi Li ⋅ Yiqing Yuan ⋅ Zhaoliang Wan ⋅ Dizhe Zhang ⋅ Lu Qi ⋅ HUI CHENG  
   [arXiv:2608.06833](https://arxiv.org/abs/2608.06833)
137. **VERITAS: A Multi-agent Co-scientist for Verifiable Image-Derived Hypothesis Testing**  
   Lucas Stoffl ⋅ Benedikt Wiestler ⋅ Johannes Paetzold
138. **VIPS: Vehicle-Infrastructure Cooperative Planning Benchmark via Pseudo-Simulation**  
   Hoonhee Cho ⋅ Jae-young Kang ⋅ Giwon Lee ⋅ Hyemin Yang ⋅ Heejun Park ⋅ KUK-JIN YOON
139. **VisCritic: Visual State Comparison as Process Reward for GUI Agents**  
   Jiachen Qian  
   [arXiv:2606.24525](https://arxiv.org/abs/2606.24525)
140. **VLA Knows Its Limits**  
   Haoxuan Wang ⋅ Gengyu Zhang ⋅ Yan Yan ⋅ Ramana Kompella ⋅ Gaowen Liu
141. **VLA-Hijack: A Transferable Patch Attack against Vision-Language-Action Models via Visual Proprioception Hijacking**  
   Jiyuan Fu ⋅ Kaixun Jiang ⋅ Jingkai Jia ⋅ Zhaoyu Chen ⋅ Xueyao Chen ⋅ Lingyi Hong ⋅ Shuyong Gao ⋅ Chenzhi Tan ⋅ Dingkang Yang ⋅ Wenqiang Zhang  
   [arXiv:2605.28083](https://arxiv.org/abs/2605.28083)
142. **VLA-R1: Enhancing Reasoning in Vision-Language-Action Models**  
   Angen Ye ⋅ Zeyu Zhang ⋅ Boyuan Wang ⋅ Xiaofeng Wang ⋅ Dapeng Zhang ⋅ Zheng Zhu  
   [arXiv:2510.01623](https://arxiv.org/abs/2510.01623) · [code](https://github.com/GigaAI-research/VLA-R1) · [project](https://gigaai-research.github.io/VLA-R1)
143. **WebRetriever: A Large-Scale Comprehensive Benchmark for Efficient Web Agent Evaluation**  
   Wei Dong ⋅ Tianyu Fu ⋅ Zhe Yu ⋅ Hanning Wang ⋅ Anyang Su ⋅ Zhizhou Fang ⋅ Yuyang Chen ⋅ Shuo Wang ⋅ Minghui Wu ⋅ Ping Jiang ⋅ Zhen Lei ⋅ Chenxu Zhao  
   [arXiv:2607.06118](https://arxiv.org/abs/2607.06118)
144. **What Matters in RL-Based Methods for Object-Goal Navigation? An Empirical Study and A Unified Framework**  
   Hongze Wang ⋅ Boyang Sun ⋅ Jiaxu Xing ⋅ Fan Yang ⋅ Marco Hutter ⋅ Dhruv Shah ⋅ Davide Scaramuzza ⋅ Marc Pollefeys  
   [arXiv:2510.01830](https://arxiv.org/abs/2510.01830) · [project](https://honwang0054.github.io/What-matters-in-RL-ObjNav-web/)
145. **When Rubrics Fail: Error Enumeration as Reward for Reference-Free RL Post-Training**  
   Wisdom Ikezogwo ⋅ Mehmet Saygin Seyfioglu ⋅ Ranjay Krishna ⋅ Karim Bouyarmane
146. **Who Does What and Where to Go: Orthogonal Alignment and Hierarchical Planning for Multi-Entity Trajectories**  
   Zhang Wan ⋅ Yu Li ⋅ Tianze Huang ⋅ Juan Cao ⋅ Sheng Tang
147. **WristMimic: Full-Body Humanoid Control with Wrist-Guided Manipulation**  
   Wongyun Yu ⋅ Youngwoon Kim ⋅ Minsu Cho
148. **ZAP: Zero-Shot Assembly Planning with Large Language Models**  
   Linpeng Peng ⋅ Yanbo WANG ⋅ Chuanjie Lv ⋅ Wencan Jiang ⋅ Liming Xu ⋅ Jianbiao Mei ⋅ Xinyue Yao ⋅ Yong Liu

## Autonomous Driving

*81 papers · 57 with links*

1. **AiSCREAM: Absolute Target Localization with Language-Conditioned Cross-View Alignment for Autonomous Vehicles**  
   Kei Katsumata ⋅ Jun Piao ⋅ Naoki Hosomi ⋅ Kentaro Yamada ⋅ Komei Sugiura
2. **ASTAD: Asymmetric Style Transfer for Synthetic-to-Real Adaptation in Autonomous Driving**  
   Dingyi Yao ⋅ Xinqi Zhang ⋅ Lihui Peng ⋅ Jianming HU ⋅ Danya Yao ⋅ Yi ZHANG  
   [arXiv:2606.29286](https://arxiv.org/abs/2606.29286) · [code](https://github.com/Dingyi-Yao/ASTAD)
3. **BEV-GS: Feed-forward Gaussian Splatting in Bird’s-Eye-View for Road Reconstruction**  
   Wenhua Wu ⋅ Tong Zhao ⋅ Chensheng Peng ⋅ Lei Yang ⋅ Zhe Liu ⋅ Hesheng Wang  
   [arXiv:2504.13207](https://arxiv.org/abs/2504.13207) · [code](https://github.com/cat-wwh/BEV-GS)
4. **BEVLM: Distilling Semantic Knowledge from LLMs into Bird's-Eye View Representations**  
   Thomas Monninger ⋅ Shaoyuan Xie ⋅ Qi Chen ⋅ Sihao Ding  
   [arXiv:2603.06576](https://arxiv.org/abs/2603.06576)
5. **Beyond Imitation: Learning Safe End-to-End Autonomous Driving from Hard Negatives**  
   Junli Wang ⋅ HuaZhihua HuaZhihua ⋅ Xueyi Liu ⋅ Zebin Xing ⋅ Wei Zhang ⋅ Kun Ma ⋅ Guang Chen ⋅ Hangjun Ye ⋅ Long Chen ⋅ Pengxuan Yang  
   [arXiv:2605.19771](https://arxiv.org/abs/2605.19771)
6. **BeyondSight: Object Permanence for End-to-End Autonomous Driving**  
   Sandro Papais ⋅ Letian Wang ⋅ Mudit jain ⋅ Behnaz Rezaei ⋅ Steven Waslander  
   [arXiv:2607.09138](https://arxiv.org/abs/2607.09138)
7. **CausalDrive: Real-time Causal World Models for Autonomous Driving**  
   Tianyi Yan ⋅ Huan Zheng ⋅ Dubing Chen ⋅ Meizhi Qu ⋅ Yingying Shen ⋅ Lijun Zhou ⋅ Mingfei Tu ⋅ Bing Wang ⋅ Guang Chen ⋅ Hangjun Ye ⋅ Haiyang Sun ⋅ Cheng-zhong Xu ⋅ Shen Jianbing  
   [arXiv:2606.15341](https://arxiv.org/abs/2606.15341)
8. **CCFM: Collision-Constrained Flow Matching for Safety-Critical Scenario Generation**  
   Ke Li ⋅ Kaidi Liang ⋅ Yuxin Ding ⋅ Debojyoti Biswas ⋅ Xianbiao Hu ⋅ Ruwen Qin  
   [arXiv:2607.04451](https://arxiv.org/abs/2607.04451) · [code](https://github.com/KELISBU/CCFM)
9. **Composing Driving Worlds through Disentangled Control for Adversarial Scenario Generation**  
   Yifan Zhan ⋅ Zhengqing Chen ⋅ Qingjie Wang ⋅ Zhuo He ⋅ Muyao Niu ⋅ Xiaoyang Guo ⋅ Wei Yin ⋅ Weiqiang Ren ⋅ Qian Zhang ⋅ zheng yinqiang  
   [arXiv:2603.12864](https://arxiv.org/abs/2603.12864)
10. **CooperScene: Multi-Modal Cooperative Autonomy Benchmark with C-V2X Communication Characterization**  
   Bo Wu ⋅ Ruoshen Mo ⋅ Justin Yue ⋅ Yanyu Zhang ⋅ Janice Nguyen ⋅ Guoyuan Wu ⋅ Amit Roy-Chowdhury ⋅ Matthew Barth ⋅ Hang Qiu  
   [arXiv:2606.31219](https://arxiv.org/abs/2606.31219) · [project](https://cisl.ucr.edu/CooperScene)
11. **CritiqueDriveVLM: From Verifier-Guided Reinforcement Learning to Latent Thought Distillation for Autonomous Driving**  
   Zhaohong Liu ⋅ Hao Ye ⋅ Xianlin Zhang ⋅ Mengshi Qi  
   [arXiv:2607.04179](https://arxiv.org/abs/2607.04179) · [code](https://github.com/MICLAB-BUPT/CritiqueDriveVLM)
12. **Deconfounded Lifelong Learning for Autonomous Driving via Dynamic Knowledge Spaces**  
   Jiayuan Du ⋅ Yuebing Song ⋅ Yiming Zhao ⋅ Xianghui Pan ⋅ Jiawei Lian ⋅ Yuchu Lu ⋅ Liuyi Wang ⋅ Chengju Liu ⋅ Qijun Chen  
   [arXiv:2603.14354](https://arxiv.org/abs/2603.14354) · [code](https://github.com/Mooncakebro/DeLL)
13. **DecoupleGS: Interactive 3D Gaussian Splatting for End-to-End Autonomous Driving Testing**  
   Siying Li ⋅ Ying Ni ⋅ Haotian Shi ⋅ Jie Sun ⋅ Jian Sun  
   [arXiv:2608.01761](https://arxiv.org/abs/2608.01761)
14. **Defending from GeoLocalization through Adversarial Road Trips**  
   Niccolò Niccoli ⋅ Federico Becattini ⋅ Lorenzo Seidenari  
   [arXiv:2607.03277](https://arxiv.org/abs/2607.03277)
15. **DiverseAD: A Large-Scale Driving Dataset with Diverse Atmospheric Conditions**  
   Haoyu Wang ⋅ Baorui Ma ⋅ Donglin Di ⋅ Suhang Xuan ⋅ Hao Li ⋅ Shiliang Zhang
16. **Doe-2: 3D Representation World Model for Unified Driving Scene Forecasting**  
   Dong Zhuo ⋅ Wenzhao Zheng ⋅ Sicheng Zuo ⋅ Yuanhui Huang ⋅ Siming Yan ⋅ Lu Hou ⋅ Jie Zhou ⋅ Jiwen Lu
17. **DOGE: Differentiable Bézier Graph Optimization for Road Network Extraction**  
   Jiahui Sun ⋅ Junran Lu ⋅ Jinhui Yin ⋅ Yishuo Xu ⋅ Yuanqi Li ⋅ Yanwen Guo  
   [arXiv:2511.19850](https://arxiv.org/abs/2511.19850)
18. **DreamerAD: Efficient Reinforcement Learning via Latent World Model for Autonomous Driving**  
   Pengxuan Yang ⋅ Yupeng Zheng ⋅ Zebin Xing ⋅ Deheng Qian ⋅ Pengxuan Yang ⋅ Linbo Wang ⋅ Yichen Zhang ⋅ shaoyu guo ⋅ Zhongpu Xia ⋅ Qiang Chen ⋅ Junyu han ⋅ Lingyun Xu ⋅ Yifeng Pan ⋅ Dongbin Zhao  
   [arXiv:2603.24587](https://arxiv.org/abs/2603.24587)
19. **Drive2Danger: Deceive End-to-End Autonomous Driving with Risky Instance Recognition**  
   Shuaikang Shang ⋅ Taiqi Zhang ⋅ Feng Lin ⋅ Hao Yan ⋅ Zhengxiong Li
20. **DriveFine: Refining-Augmented Masked Diffusion VLA for Accurate and Robust Driving**  
   Chenxu Dang ⋅ Sining Ang ⋅ Yongkang Li ⋅ Haochen Tian ⋅ Jie Wang ⋅ Guang Li ⋅ Hangjun Ye ⋅ Jie Ma ⋅ Long Chen ⋅ Yan Wang  
   [arXiv:2602.14577](https://arxiv.org/abs/2602.14577) · [code](https://github.com/MSunDYY/DriveFine)
21. **Driver-WM: A Driver-Centric Traffic-Conditioned Latent World Model for In-Cabin Dynamics Rollout**  
   Haozhuang Chi ⋅ Daosheng Qiu ⋅ Hao Su ⋅ Haochen Liu ⋅ Zirui Li ⋅ Haoruo Zhang ⋅ Chen Lv  
   [arXiv:2605.05092](https://arxiv.org/abs/2605.05092)
22. **DriveWeaver: Point-Conditioned Video Inpainting for Controllable Vehicle Insertion in Autonomous Driving Simulation**  
   Junzhe Jiang ⋅ Zipei Ma ⋅ Zijie Pan ⋅ Li Zhang  
   [arXiv:2606.31918](https://arxiv.org/abs/2606.31918) · [code](https://github.com/LogosRoboticsGroup/DriveWeaver)
23. **Driving like yourself: A Benchmark for Closed-Loop Personalized End-to-End Autonomous Driving**  
   Xiaoru Dong ⋅ Ruiqin Li ⋅ Xiao Han ⋅ Zhenxuan Wu ⋅ Jiamin Wang ⋅ Jian Chen ⋅ Qi Jiang ⋅ SM Yiu ⋅ Xinge Zhu ⋅ Yuexin Ma  
   [arXiv:2602.18757](https://arxiv.org/abs/2602.18757)
24. **EAGS: Error-Aware Gaussian Splatting with Dual-Confidence-Guided Modeling for Uncalibrated Driving Scenes**  
   Cen Zhigabng ⋅ Ningyan Guo ⋅ Yulan Guo ⋅ Yifan Ge ⋅ Zhiyong Feng
25. **ECoSim: Data Efficient Fine-Tuning for Controllable Traffic Simulation**  
   Yu-Hsiang Chen ⋅ WEI-JER Chang ⋅ Yi-Ting Chen ⋅ Masayoshi TOMIZUKA  
   [arXiv:2607.00545](https://arxiv.org/abs/2607.00545) · [project](https://ecosim-web.github.io/)
26. **ECTraj: Enhanced Consistency Training for Multi-Agent Trajectory Prediction**  
   Alen Mrdovic ⋅ Qingze Liu ⋅ Danrui Li ⋅ Mathew Schwartz ⋅ Kaidong Hu ⋅ Sejong Yoon ⋅ Mubbasir Kapadia ⋅ Vladimir Pavlovic  
   [arXiv:2605.08572](https://arxiv.org/abs/2605.08572)
27. **EgoDyn-Bench: Evaluating Ego-Motion Understanding in Vision-Centric Foundation Models for Autonomous Driving**  
   Finn Rasmus Schäfer ⋅ Yuan Gao ⋅ Dingrui Wang ⋅ Thomas Stauner ⋅ Stephan Günnemann ⋅ Mattia Piccinini ⋅ Sebastian Schmidt ⋅ Johannes Betz  
   [arXiv:2604.22851](https://arxiv.org/abs/2604.22851) · [code](https://github.com/TUM-AVS/EgoDyn-Bench) · [project](https://tum-avs.github.io/EgoDyn-Bench-Website/)
28. **EgoMAN: Interaction-Structured Reasoning for Egocentric 3D Hand Trajectory Prediction**  
   Mingfei Chen ⋅ Yifan Wang ⋅ Zhengqin Li ⋅ Homanga Bharadhwaj ⋅ Yujin Chen ⋅ Chuan Qin ⋅ Ziyi Kou ⋅ Yuan Tian ⋅ Eric Whitmire ⋅ Rajinder Sodhi ⋅ Hrvoje Benko ⋅ Eli Shlizerman ⋅ Yue Liu
29. **ExploreVLA: Dense World Modeling and Exploration for End-to-End Autonomous Driving**  
   Zihao Sheng ⋅ Xin Ye ⋅ Jingru Luo ⋅ Sikai Chen ⋅ Liu Ren  
   [arXiv:2604.02714](https://arxiv.org/abs/2604.02714) · [project](https://zihaosheng.github.io/ExploreVLA/)
30. **Fast and Scalable LiDAR Data Generation for Autonomous Driving Simulation without Raycasting**  
   Irfan Nafiz Shahan ⋅ Al-Mubin Nabil ⋅ Arpan Kusari
31. **FDR-Occ: Factorized Dense Routing for Full-Spectrum 3D Occupancy Prediction**  
   Dubing Chen ⋅ Huan Zheng ⋅ Tianyi Yan ⋅ Yucheng Zhou ⋅ Runzhou Tao ⋅ Zhongying Qiu ⋅ Jianfei Yang ⋅ Shen Jianbing  
   [arXiv:2607.03822](https://arxiv.org/abs/2607.03822)
32. **FLM-Occ: Feed-forward Likelihood Maximization for Efficient Indoor Occupancy Prediction**  
   Guangcheng Chen ⋅ Lihuang Fang ⋅ Huaqi Tao ⋅ Yicheng He ⋅ Li He ⋅ Zhang Hong  
   [arXiv:2606.21373](https://arxiv.org/abs/2606.21373)
33. **FreeGen: Feed-Forward Reconstruction–Generation Co-Training for Free-Viewpoint Driving Scene Synthesis**  
   Shijie Chen ⋅ Peixi Peng  
   [arXiv:2512.04830](https://arxiv.org/abs/2512.04830)
34. **FrozenDrive: Zero-Shot Text-Guided Driving Scene Generation and Data Augmentation with Parameter-Free Frozen Diffusion Model**  
   Yuhwan Jeong ⋅ HYEONSEONG KIM ⋅ Daehyun We ⋅ Seonkyu Song ⋅ Jinnyeong Yang ⋅ Hyun-Kurl Jang ⋅ Youngho Yoon ⋅ KUK-JIN YOON  
   [arXiv:2606.20110](https://arxiv.org/abs/2606.20110)
35. **Generative Lane Topology Reasoning via Autoregressive Model with Geometry Prior**  
   Jiahui Fu ⋅ Zehao Huang ⋅ Han Li ⋅ Naiyan Wang ⋅ Si Liu  
   [arXiv:2606.31814](https://arxiv.org/abs/2606.31814)
36. **GeoFlow: Efficient Driving Video Generation via Geometry-Aligned Priors**  
   Jiazheng Liu ⋅ Hang Li ⋅ jiawei zhang ⋅ Jiahe Li ⋅ Xiaohan Yu ⋅ Shengyin Fan ⋅ Jin Zheng ⋅ Xiao Bai  
   [arXiv:2608.12203](https://arxiv.org/abs/2608.12203)
37. **Geometry-Aware Spatio-Temporal Context Modeling for 4D Occupancy Forecasting**  
   Mingkui Tan ⋅ Zhuangwei Zhuang ⋅ Hui Luo ⋅ Qingyao Wu ⋅ Mingkui Tan  
   [arXiv:2608.15279](https://arxiv.org/abs/2608.15279)
38. **GeoV2V: Geometry-Grounded Video Diffusion Model for Driving Scene Generation**  
   Yuchen Xi ⋅ tippy guo ⋅ Chenwei Hou ⋅ Zixu Liu ⋅ Jin Fang ⋅ Jason Liu ⋅ Ruigang Yang
39. **HAD: Combining Hierarchical Diffusion with Metric-Decoupled RL for End-to-End Driving**  
   Wenhao Yao ⋅ Xinglong Sun ⋅ Zhenxin Li ⋅ Shiyi Lan ⋅ Zi Wang ⋅ Jose M Alvarez ⋅ Zuxuan Wu  
   [arXiv:2604.03581](https://arxiv.org/abs/2604.03581)
40. **HERO: Heterogeneous Evidential Robust Object-Level Collaborative Perception**  
   Hao SI ⋅ Ehsan Javanmardi ⋅ Hanlin Wu ⋅ Manabu Tsukada
41. **Horizon3D: Sparse Radar-Camera Fusion for Long-Range 3D Perception in Autonomous Driving**  
   Geonho Bang ⋅ Geunju Baek ⋅ DongYoung Lee ⋅ Wonjun Jeong ⋅ Jun Won Choi  
   [arXiv:2606.31096](https://arxiv.org/abs/2606.31096) · [code](https://github.com/geonhobang/ECCV2026_Horizon3D) · [project](https://geonhobang.github.io/horizon3d-project-page)
42. **HSDF-Lane: Height-Aligned Signed Distance Field with Semantic Lane Prior for 3D Lane Detection**  
   Jiyong Boo ⋅ ByeongIn Joung ⋅ Hyemin Yang ⋅ KUK-JIN YOON  
   [arXiv:2606.31172](https://arxiv.org/abs/2606.31172) · [project](https://jiyongboo.github.io/HSDF-Lane-project-page)
43. **IRIS: Intersection-aware Ray-based Implicit Editable Scenes**  
   Grzegorz Wilczyński ⋅ Mikołaj Zieliński ⋅ Krzysztof Byrski ⋅ Joanna Waczynska ⋅ Dominik Belter ⋅ Przemysław Spurek
44. **LangDriveCTRL: Natural Language Controllable Driving Scene Editing with Multi-modal Agents**  
   Yun He ⋅ Francesco Pittaluga ⋅ Ziyu Jiang ⋅ Matthias Zwicker ⋅ Manmohan Chandraker ⋅ Zaid Tasneem
45. **Learning Ego-Centric BEV Representations from a Perspective-Privileged View: Cross-View Supervision for Online HD Map Construction**  
   Daniel Lengerer ⋅ Mathias Pechinger ⋅ Klaus Bogenberger ⋅ Carsten Markgraf  
   [arXiv:2605.12218](https://arxiv.org/abs/2605.12218)
46. **Less is More: A Simple yet Effective Object-Centric Prompting Strategy for Vision-Language Reasoning in Autonomous Driving**  
   Saiqian Peng ⋅ Duanfeng Chu ⋅ Liping Lu ⋅ Bing Shi
47. **LineGraph2Road: Structural Graph Reasoning on Line Graphs for Road Network Extraction**  
   Zhengyang Wei ⋅ Renzhi Jing ⋅ Yiyi He ⋅ Jenny Suckale  
   [arXiv:2602.23290](https://arxiv.org/abs/2602.23290) · [code](https://github.com/wzzzzzzy/LineGraph2Road)
48. **LiSTAR: Ray-Centric World Models for 4D LiDAR Sequences in Autonomous Driving**  
   Pei Liu ⋅ Songtao Wang ⋅ Lang Zhang ⋅ Xinyue Peng ⋅ Yuandong Lyu ⋅ Jiaxin Deng ⋅ Songxin lu ⋅ Weiliang Ma ⋅ Xueyang Zhang ⋅ Yifei Zhan ⋅ Kun Zhan ⋅ Jun Ma  
   [arXiv:2511.16049](https://arxiv.org/abs/2511.16049) · [project](https://ocean-luna.github.io/LiSTAR.gitub.io)
49. **LMGenDrive: Bridging Multimodal Understanding and Generative World Modeling for End-to-End Driving**  
   Hao Shao ⋅ Letian Wang ⋅ Yang Zhou ⋅ Yuxuan Hu ⋅ Zhuofan Zong ⋅ Steven Waslander ⋅ Wei Zhan ⋅ Hongsheng LI  
   [arXiv:2604.08719](https://arxiv.org/abs/2604.08719)
50. **Long-term Traffic Simulation via Structured Autoregressive Modeling**  
   Lingyu Xiao ⋅ Zexin Feng ⋅ Xintao Yan  
   [arXiv:2606.31209](https://arxiv.org/abs/2606.31209)
51. **MOJITO: Modal Joint Learning for Unified End-to-End Autonomous Driving**  
   Zhijing Cheng ⋅ Xuancheng Zhang ⋅ Donglin Di ⋅ Lei Fan ⋅ Baorui Ma ⋅ Hao Li ⋅ Xun Yang  
   [arXiv:2607.23511](https://arxiv.org/abs/2607.23511) · [code](https://github.com/mumucc01/MOJITO)
52. **Multi-view Multi-vehicle Driving Dataset for Novel View Synthesis**  
   Sanjay Dharavath ⋅ Hanvitha Mukkamala ⋅ Faizan Khan ⋅ Ioannis Kakogeorgiou ⋅ Aditya Arun ⋅ Zakaria Laskar ⋅ C. V. Jawahar  
   [arXiv:2608.12442](https://arxiv.org/abs/2608.12442) · [project](https://mv2-dataset.github.io/)
53. **Noise is a Good Teacher: A Noise-Driven Framework for Robust Collaborative Perception**  
   Chengyan Huang ⋅ Zhongxiang Zhao ⋅ Ziyao Zhang ⋅ Zihao Yang ⋅ Lin Wang
54. **OccDirector: Language-Guided Behavior and Interaction Generation in 4D Occupancy Space**  
   Zhuding Liang ⋅ Tianyi Yan ⋅ Dubing Chen ⋅ Jiasen Zheng ⋅ Huan Zheng ⋅ Cheng-zhong Xu ⋅ Yida Wang ⋅ Kun Zhan ⋅ Shen Jianbing  
   [arXiv:2604.22240](https://arxiv.org/abs/2604.22240)
55. **OmniNWM: Unifying the State-Action-Reward Triad for Closed-Loop Panoramic Driving Navigation World Models**  
   Bohan Li ⋅ Zhuang Ma ⋅ Dalong Du ⋅ Baorui Peng ⋅ Zhujin Liang ⋅ Zhenqiang Liu ⋅ Xianda Guo ⋅ Chao Ma ⋅ Yueming Jin ⋅ Zheng Zhu ⋅ HAO ZHAO ⋅ Wenjun Zeng ⋅ Xin Jin
56. **PersonaDrive: Controllable Trajectory Prediction with Multi-Dimensional Driving Personas**  
   Chan Lee ⋅ Kimin Yun ⋅ Yuseok Bae ⋅ Seong Tae Kim ⋅ Jung Uk Kim  
   [arXiv:2608.15230](https://arxiv.org/abs/2608.15230) · [code](https://github.com/VisualAIKHU/PersonaDrive)
57. **PixelPilot: Scalable Vision-Language-Action Models for End-to-End Autonomous Driving**  
   Pin Tang ⋅ Guoqing Wang ⋅ Xiangxuan Ren ⋅ Zhongdao Wang ⋅ Guodongfang Zhao ⋅ Bailan Feng ⋅ Chao Ma  
   [arXiv:2607.04637](https://arxiv.org/abs/2607.04637)
58. **Plug-and-Play Traffic Element Awareness for End-to-End Autonomous Driving**  
   Zongzheng Zhang ⋅ Jijun Wang ⋅ Saining Zhang ⋅ Wang Shuo ⋅ Yiru Wang ⋅ Hai Yang ⋅ Yang Chen ⋅ Yuwen Heng ⋅ HAO SUN ⋅ Jiang anqing ⋅ HAO ZHAO
59. **PriorMaskMap: Robust Online Vectorized Map Construction with Biased Priors**  
   Haoming Xu ⋅ Wei Li ⋅ Yu Hu
60. **Rethinking Training and Inference for Trajectory Forecasting: Linking Winner-Take-All back to GMMs**  
   Qiyuan Wu ⋅ Katie Luo ⋅ Bharath Hariharan ⋅ Wei-Lun Chao ⋅ Mark Campbell
61. **ScenarioControl: Vision-language Controllable Vectorized Latent Scenario Generation**  
   Lili Gao ⋅ Yanbo Xu ⋅ William Koch ⋅ Samuele Ruffino ⋅ Luke Rowe ⋅ Behdad Chalaki ⋅ Dmitriy Rivkin ⋅ Julian Ost ⋅ Roger Girgis ⋅ Mario Bijelic ⋅ Felix Heide  
   [arXiv:2604.17147](https://arxiv.org/abs/2604.17147) · [project](https://light.princeton.edu/ScenarioControl)
62. **SEM-ROVER: Semantic Voxel-Guided Diffusion for Large-Scale Driving Scene Generation**  
   Hiba Dahmani ⋅ Nathan Piasco ⋅ Moussab Bennehar ⋅ Luis G Roldao Jimenez ⋅ Dzmitry Tsishkou ⋅ Laurent Caraffa ⋅ Jean-Philippe Tarel ⋅ Roland Brémond  
   [arXiv:2604.06113](https://arxiv.org/abs/2604.06113)
63. **SGC-Lane: Monocular 3D Lane Detection with Standard-Definition Map Guidance and Lane Completion**  
   Fuqiang Jiang ⋅ Wei Li ⋅ Tianyao Zhao ⋅ Yu Hu
64. **SIGMA-Lane: Scale-pyramId Gated MAmba for Temporally Consistent Video Lane Detection**  
   Zhang Tiancheng ⋅ Mengmeng Wang ⋅ Yan Gao ⋅ Xiangjie Kong ⋅ Guojiang Shen ⋅ Jiaxin Du  
   [arXiv:2608.16338](https://arxiv.org/abs/2608.16338)
65. **SIMSplat: Language-Aligned 4D Gaussian Splatting for Driving Scenario Generation**  
   Sung-Yeon Park ⋅ Adam Lee ⋅ Juanwu Lu ⋅ Can Cui ⋅ Luyang Jiang ⋅ Rohit Gupta ⋅ Kyungtae Han ⋅ Ahmadreza Moradipari ⋅ Ziran Wang  
   [arXiv:2510.02469](https://arxiv.org/abs/2510.02469)
66. **Social-Mamba: Socially-Aware Trajectory Forecasting with State-Space Models**  
   Po-Chien Luan ⋅ Wuyang Li ⋅ Yang Gao ⋅ Alexandre ALahi  
   [arXiv:2605.15424](https://arxiv.org/abs/2605.15424) · [code](https://github.com/vita-epfl/Social-Mamba)
67. **SPARC: Single-Pass Scaling for Motion Forecasting with Conformal Bayesian Last Layers**  
   Sakif Hossain ⋅ Julian Teusch ⋅ Jörg Müller
68. **SparseDriveV2: Scoring is All You Need for End-to-End Autonomous Driving**  
   Wenchao Sun ⋅ Xuewu Lin ⋅ Keyu Chen ⋅ Zixiang Pei ⋅ Xiang LI ⋅ Yining Shi ⋅ Sifa ZHENG  
   [arXiv:2603.29163](https://arxiv.org/abs/2603.29163) · [code](https://github.com/swc-17/SparseDriveV2)
69. **Streaming Dense Voxel Representations for 3D Occupancy Prediction**  
   Seokha Moon ⋅ Janghyun Baek ⋅ Yujin Jeong ⋅ Daewon Chae ⋅ Giseop Kim ⋅ Jungbeom Lee ⋅ Jinkyu Kim ⋅ Sunwook Choi  
   [arXiv:2503.22087](https://arxiv.org/abs/2503.22087) · [project](https://moonseokha.github.io/StreamOcc/)
70. **StreetForward: Perceiving Dynamic Street with Feedforward Causal Dynamics**  
   Zhongrui Yu ⋅ Zhao Wang ⋅ Yida Wang ⋅ Xueyang Zhang ⋅ Yifei Zhan ⋅ Kun Zhan
71. **Targeted Structure Completion for Sparse-View 3D Reconstruction in Autonomous Driving**  
   Guoqing Wang ⋅ Pin Tang ⋅ Xiangxuan Ren ⋅ Liping Hou ⋅ Chao Ma  
   [arXiv:2607.04661](https://arxiv.org/abs/2607.04661)
72. **TEX-Drive: Temporal Perception Meets Experience-Guided Mixture-of-Experts for End-to-End Autonomous Driving**  
   Yitong Li ⋅ Xuchong Zhang ⋅ Fanjie Kong ⋅ Weihuang Chen ⋅ Haonan Hou ⋅ Hongbin Sun
73. **Towards Metric-Agnostic Trajectory Forecasting**  
   Markus Knoche ⋅ Daan de Geus ⋅ Bastain Leibe  
   [arXiv:2607.01133](https://arxiv.org/abs/2607.01133) · [project](https://vision.rwth-aachen.de/TraDiE-policies)
74. **Towards Robust Driving Perception: A Flexible Scale-Driven Family for Self-Supervised Monocular Depth Estimation**  
   zhaowen zhu ⋅ Li Zhang ⋅ Chen Yujie ⋅ Zhang Tian ⋅ Yingjie Wang ⋅ Mingxia Zhan  
   [arXiv:2607.00736](https://arxiv.org/abs/2607.00736) · [code](https://github.com/startnew/flexdepth)
75. **UECP: Uncertainty-Enhanced Collaborative Perception**  
   Kang Yang ⋅ Tianci Bu ⋅ Peng Wang ⋅ Deying Li ⋅ Jie Wen ⋅ Yongcai Wang  
   [arXiv:2606.23046](https://arxiv.org/abs/2606.23046)
76. **UniDriveDreamer: A Single-Stage Multimodal World Model for Autonomous Driving**  
   Guosheng Zhao ⋅ Yaozeng Wang ⋅ Xiaofeng Wang ⋅ Zheng Zhu ⋅ Tingdong Yu ⋅ Guan Huang ⋅ Yongchen Zai ⋅ Ji Jiao ⋅ Changliang Xue ⋅ Xiaole Wang ⋅ Zhen Yang ⋅ Futang Zhu ⋅ Xingang Wang  
   [arXiv:2602.02002](https://arxiv.org/abs/2602.02002)
77. **UniFlow: Zero-Shot LiDAR Scene Flow for Autonomous Driving**  
   Siyi Li ⋅ Qingwen Zhang ⋅ Ishan Khatri ⋅ Kyle Vedder ⋅ Eric Eaton ⋅ Deva Ramanan ⋅ Neehar Peri
78. **Unpaired Geometry-Guided Sim2Real Translation for Autonomous Driving**  
   Xinzhuo Chen ⋅ Shijie Wang ⋅ Chao Gao ⋅ Jinguang Gu ⋅ Gongjin Lan
79. **Unveiling Transferability in Trajectory Prediction via Latent Scene Embeddings**  
   Theodor Westny ⋅ David Axelsson ⋅ Björn Olofsson ⋅ Erik Frisk  
   [arXiv:2606.30777](https://arxiv.org/abs/2606.30777)
80. **YouTube-Occ: Learning Indoor 3D Semantic Occupancy Prediction from YouTube Videos**  
   Haoming Chen ⋅ Lichen Yuan ⋅ TianFang Sun ⋅ Jingyu Gong ⋅ Zhizhong Zhang ⋅ Xin Tan ⋅ Yanyun Qu ⋅ Yuan Xie  
   [arXiv:2506.18266](https://arxiv.org/abs/2506.18266)
81. **ZTRS: Zero-Human Demonstration End-to-end Autonomous Driving with Trajectory Scorer**  
   Zhenxin Li ⋅ Nadine Chang ⋅ Wenhao Yao ⋅ Xinglong Sun ⋅ Zi Wang ⋅ Maying Shen ⋅ Jingde Chen ⋅ Jingyu Song ⋅ Kailin Li ⋅ Zuxuan Wu ⋅ Shiyi Lan ⋅ Jose M Alvarez

# Learning, Efficiency & Trust


## Representation & Self-Supervised Learning

*82 papers · 53 with links*

1. **A Dual-Transformer Architecture with Cross-Attention for Multi-Camera View Recommendation**  
   Josep Cabacas Maso ⋅ Carles Ventura ⋅ Ismael Benito-Altamirano
2. **A scalar per patch from pre-trained ViTs enables fast moving navigation in the real world**  
   Steeven Janny ⋅ Leonid Antsfeld ⋅ Christian Wolf  
   [arXiv:2606.21216](https://arxiv.org/abs/2606.21216)
3. **Ada-VNNs: Adaptive Equivariance for Vector Neural Networks**  
   Bing Han ⋅ Ruitao Pan ⋅ Yumin Chen ⋅ Peixin Hong ⋅ Weiyuan Liu ⋅ Zhibin Zhao ⋅ Chenxi Wang ⋅ Zhi Zhai
4. **Art Beyond Semantics: Sheaf-Informed Contrastive Learning for Multi-Relational Representations**  
   Ludovica Schaerf ⋅ Antonio Purificato ⋅ Piera Riccio ⋅ Fabrizio Silvestri ⋅ Noa Garcia  
   [arXiv:2607.16321](https://arxiv.org/abs/2607.16321)
5. **Beyond Linear Shortcuts: Rectifying Diffusion Preference Optimization with Intrinsic Generative Geometry**  
   Pin Wang ⋅ Huaibo Huang ⋅ Jiayang Sun ⋅ Hongbo Wang ⋅ Wentao Jiang ⋅ Tiezheng Ge ⋅ Jie Cao ⋅ Ran He
6. **Beyond Sequential Distance: Inter-Modal Distance Invariant Position Encoding**  
   Lin Chen ⋅ Bolin Ni ⋅ Qi Yang ⋅ Zili Wang ⋅ Kun Ding ⋅ Ying Wang ⋅ Houwen Peng ⋅ SHIMING XIANG  
   [arXiv:2603.10863](https://arxiv.org/abs/2603.10863) · [code](https://github.com/lchen1019/DIPE)
7. **Boosting 3D Foundation Models with Featureless Pose Optimization**  
   Mattia D'Urso ⋅ Christian Sormann ⋅ Mattia Rossi ⋅ Friedrich Fraundorfer
8. **CFM: Language-aligned Concept Foundation Model for Vision**  
   Kai Wittenmayer ⋅ Sukrut Rao ⋅ Amin Parchami-Araghi ⋅ Bernt Schiele ⋅ Jonas Fischer  
   [arXiv:2601.13798](https://arxiv.org/abs/2601.13798) · [code](https://github.com/kawi19/CFM)
9. **Cheers: Decoupling Patch Details from Semantic Representations Enables Unified Multimodal Comprehension and Generation**  
   Yichen Zhang ⋅ Da Peng ⋅ Zonghao Guo ⋅ zijian zhang ⋅ Xuesong Yang ⋅ Tong Sun ⋅ Shichu Sun ⋅ Yidan Zhang ⋅ Yanghao Li ⋅ Haiyan Zhao ⋅ Wang Xu ⋅ Qi Shi ⋅ Yangang Sun ⋅ Chi Chen ⋅ Shuo Wang ⋅ Yukun Yan ⋅ Xu Han ⋅ Qiang Ma ⋅ Wei Ke ⋅ Liang Wang ⋅ Zhiyuan Liu ⋅ Maosong Sun  
   [arXiv:2603.12793](https://arxiv.org/abs/2603.12793)
10. **CL4D: Contrastive Language–4D Pretraining for Vision-Language Reasoning in Dynamic Scenes**  
   Kumal Hewagamage ⋅ Isuranga Senavirathne ⋅ Yattowita Withanage Sasika Pamith Amarasinghe ⋅ Hasitha Gallella ⋅ Dulanga Weerakoon ⋅ Vigneshwaran Subbaraju ⋅ Ranga Rodrigo
11. **CLIMP: Contrastive Language-Image Mamba Pretraining**  
   Nimrod Shabtay ⋅ Itamar Zimerman ⋅ Eli Schwartz ⋅ RAJA GIRYES  
   [arXiv:2601.06891](https://arxiv.org/abs/2601.06891) · [code](https://github.com/NimrodShabtay/CLIMP)
12. **Contrastive Conditional–Unconditional Alignment for Long-tailed Diffusion Model**  
   Fang Chen ⋅ Alex Villa ⋅ Gongbo Liang ⋅ Li Fuxin ⋅ Xiaoyi Lu ⋅ Meng Tang  
   [arXiv:2507.09052](https://arxiv.org/abs/2507.09052)
13. **Control-DINO: Feature Space Conditioning for Controllable Video Diffusion**  
   Edoardo Dominici ⋅ Thomas Deixelberger ⋅ Konstantinos Vardis ⋅ Markus Steinberger  
   [arXiv:2604.01761](https://arxiv.org/abs/2604.01761) · [project](https://dedoardo.github.io/projects/control-dino/)
14. **DICT: Data Injection and Contrastive Trajectory Refinement for Conditional Image Generation with Diffusion Models**  
   Chunnan Shang ⋅ Zhizhong Wang ⋅ Xin Zhang ⋅ Hongwei Wang  
   [arXiv:2607.03899](https://arxiv.org/abs/2607.03899)
15. **DiffuPrompt: Adapting Video Foundation Models to 3D Medical Volumes via Latent Trajectory Priors**  
   Guowei Dai ⋅ Duwei Dai ⋅ yulong ji ⋅ Chen Hu ⋅ Yi Zhang
16. **Direct Autoregressive Diffusion Distillation via Error-aware Causal Pretraining**  
   Jiaxing Li ⋅ Kaichen Huang ⋅ Baixin Xu ⋅ Zexiang Liu ⋅ Xianglong He ⋅ Zile Wang ⋅ Junyao Gao ⋅ Yang Liu ⋅ Ying He ⋅ Bo An ⋅ Yangguang Li
17. **Direct Diffusion Score Preference Optimization via Stepwise Contrastive Policy-Pair Supervision**  
   Dohyun Kim ⋅ Seungwoo Lyu ⋅ Seung Kim ⋅ Paul Hongsuck Seo  
   [arXiv:2512.23426](https://arxiv.org/abs/2512.23426) · [project](https://dohyun-as.github.io/DDSPO)
18. **Disentangling Rotation and Translation from SE(3)-Equivariant Features for Shape Assembly**  
   Hee-Jun Jung ⋅ Uigeun Ahn ⋅ JINHWI PARK ⋅ Kangil Kim
19. **Don’t Settle at the Mode! Mitigating Diversity Collapse in Pretrained Flow Models via Feature Self-Guidance**  
   Pradhaan Bhat ⋅ Rishubh Parihar ⋅ Abhijnya Bhat ⋅ Venkatesh Babu Radhakrishnan
20. **DSeq-JEPA: Discriminative Sequential Joint-Embedding Predictive Architecture**  
   Xiangteng He ⋅ Shunsuke SAKAI ⋅ Shivam Chandhok ⋅ Sara Beery ⋅ Kun yuan ⋅ Nicolas Padoy ⋅ Tatsuhito Hasegawa ⋅ Leonid Sigal  
   [arXiv:2511.17354](https://arxiv.org/abs/2511.17354) · [project](https://dseqjepa-project.com)
21. **Dynamic Cluster Data Sampling for Efficient and Long-Tail-Aware Vision-Language Pre-training**  
   Mingliang Liang ⋅ Zhuoran Liu ⋅ Arjen Vries ⋅ Martha Larson  
   [arXiv:2604.27932](https://arxiv.org/abs/2604.27932) · [code](https://github.com/MingliangLiang3/DynamiCS)
22. **E-M3RF: An Equivariant Multimodal 3D Re-assembly Framework**  
   Adeela Islam ⋅ Stefano Fiorini ⋅ MANUEL LECHA SANCHEZ ⋅ Theodore Tsesmelis ⋅ Stuart James ⋅ Pietro Morerio ⋅ Alessio Del Bue  
   [arXiv:2511.21422](https://arxiv.org/abs/2511.21422)
23. **Enhancing Pretrained Model-based Continual Representation Learning via Guided Random Projection**  
   Ruilin Li ⋅ Heming Zou ⋅ Xiufeng Yan ⋅ Zheming Liang ⋅ Jie Yang ⋅ Chenliang Li ⋅ Xue Yang  
   [arXiv:2603.19145](https://arxiv.org/abs/2603.19145)
24. **EoS-FM: Can an Ensemble of Specialist Models act as a Generalist Feature Extractor?**  
   Pierre Adorni ⋅ Minh-Tan Pham ⋅ Stephane May ⋅ Sébastien Lefèvre  
   [arXiv:2511.21523](https://arxiv.org/abs/2511.21523) · [code](https://github.com/pierreadorni/EoS-FM)
25. **ExPLoRe: Expert Patch-Level Loss Routing for Multi-Objective Masked Image Modeling**  
   Konstantinos Georgiou ⋅ Maofeng Tang ⋅ Hairong Qi
26. **Fourier Self-Supervision for Fine-Grained Generalized Category Discovery**  
   Sarah Rastegar ⋅ Mina Ghadimi Atigh ⋅ Pascal Mettes ⋅ Yuki Asano ⋅ Cees Snoek  
   [arXiv:2608.08963](https://arxiv.org/abs/2608.08963) · [code](https://github.com/SarahRastegar/FourEx)
27. **From Phase to Phenomenon: Self-Supervised Learning of Subsurface Scattering with Minimal Phase-shift Inputs**  
   Arjun Majumdar ⋅ Raphael Braun ⋅ Andreas Engelhardt ⋅ Hendrik Lensch  
   [arXiv:2606.29461](https://arxiv.org/abs/2606.29461)
28. **GH-ESD: Grounded Hypothesis-Driven Error Slice Discovery for Instance-Level Vision Tasks**  
   Wei Zhang ⋅ Chaoqun Wang ⋅ Zixuan Guan ⋅ Ping Kao ⋅ Pengfei Zhao ⋅ Peng Wu ⋅ Sifeng He  
   [arXiv:2512.24592](https://arxiv.org/abs/2512.24592)
29. **GhostPoint: Self-Supervised Representation Learning by Hallucinating Occluded LiDAR Structure**  
   Bin Yang ⋅ Mohamed Abdelsamad ⋅ Miao Zhang ⋅ Michael Ulrich ⋅ Yakov Miron ⋅ Abhinav Valada ⋅ Alexandru Condurache  
   [arXiv:2608.14428](https://arxiv.org/abs/2608.14428)
30. **HilDA: Hierarchical Distillation with Diffusion for Advancing Self-Supervised LiDAR Pre-training**  
   Maciej Wozniak ⋅ Jesper Ericsson ⋅ Hariprasath Govindarajan ⋅ Truls Nyberg ⋅ Thomas Gustafsson ⋅ Patric Jensfelt ⋅ Olov Andersson  
   [arXiv:2606.20189](https://arxiv.org/abs/2606.20189) · [project](https://maxiuw.github.io/hilda)
31. **Human-like Object Grouping in Self-supervised Vision Transformers**  
   Hossein Adeli ⋅ Seoyoung Ahn ⋅ Andrew Luo ⋅ Mengmi Zhang ⋅ Nikolaus Kriegeskorte ⋅ Gregory Zelinsky  
   [arXiv:2603.13994](https://arxiv.org/abs/2603.13994)
32. **Hyperbolic Hierarchical Clustering for Visual Representation Learning**  
   Jianan Wei ⋅ Guikun Chen ⋅ Zhiyuan Weng ⋅ Chunchao Guo ⋅ Yujia Wang ⋅ Wenguan Wang
33. **IConE: Batch Independent Collapse Prevention for Self-Supervised Representation Learning**  
   Konstantinos Almpanakis ⋅ Anna Kreshuk  
   [arXiv:2603.15263](https://arxiv.org/abs/2603.15263)
34. **Intrinsically Stable Spiking Neural Networks: Overcoming the Performance Barrier in the Absence of Batch Normalization**  
   Ruichen Ma ⋅ Xiaoyang Zhang ⋅ Jian Bai ⋅ Guanchao Qiao ⋅ Liwei Meng ⋅ Ning Ning ⋅ Yang Liu ⋅ Shaogang Hu  
   [arXiv:2606.31695](https://arxiv.org/abs/2606.31695)
35. **Invisible Shortcuts: Why Vision Encoders Know Your Camera**  
   Vladan Stojnic ⋅ Ryan Ramos ⋅ Giorgos Kordopatis-Zilos ⋅ Noa Garcia ⋅ Giorgos Tolias  
   [arXiv:2608.05424](https://arxiv.org/abs/2608.05424) · [code](https://github.com/ryan-caesar-ramos/visual-encoder-traces)
36. **Kinematics-Agnostic 3D Human Motion Prediction via Equivariant Latent Diffusion**  
   Cecilia Curreli ⋅ Florian Hofherr ⋅ Dominik Muhle ⋅ Abhishek Saroha ⋅ Riccardo Marin ⋅ Daniel Cremers
37. **Let ViT Speak: Generative Language-Image Pre-training**  
   Yan Fang ⋅ Mengcheng Lan ⋅ Zilong Huang ⋅ Weixian Lei ⋅ Yunqing Zhao ⋅ Yujie Zhong ⋅ Yingchen Yu ⋅ Qi She ⋅ Yao Zhao ⋅ Yunchao Wei  
   [arXiv:2605.00809](https://arxiv.org/abs/2605.00809) · [code](https://github.com/YanFangCS/GenLIP)
38. **Let's Reward Step-by-Step: Step-Aware Contrastive Alignment for Vision-Language Navigation in Continuous Environments**  
   Haoyuan Li ⋅ Rui Liu ⋅ Hehe Fan ⋅ Yi Yang
39. **LoCA: Spatially-Aware Low-Rank Convolutional Adaptation of Vision Foundation Models**  
   Sojung An ⋅ Junha Lee ⋅ Sujeong You ⋅ Nam Ik Cho ⋅ Donghyun Kim  
   [arXiv:2607.06918](https://arxiv.org/abs/2607.06918)
40. **MIMFlow: Integrating Masked Image Modeling with Normalizing Flows for End-to-End Image Generation**  
   Yang Chen ⋅ Xiaowei Xu ⋅ Shuai Wang ⋅ Xinwen Zhang ⋅ Qiushi Guo ⋅ Tiezheng Ge ⋅ Limin Wang  
   [arXiv:2606.26016](https://arxiv.org/abs/2606.26016) · [code](https://github.com/MCG-NJU/MIMFlow)
41. **Mitigating Positional Leakage in 3D Masked Autoencoders for Robust Representation Learning**  
   Xu Yan ⋅ Huiqun Wang ⋅ Chen Wang ⋅ Lei Ren ⋅ Di Huang  
   [arXiv:2606.31570](https://arxiv.org/abs/2606.31570) · [code](https://github.com/yanx57/MPL-MAE)
42. **MJEPA: A Simple and Scalable Joint-Embedding Predictive Architecture for Audio-Visual Learning**  
   Revant Teotia ⋅ Adrien Bardes ⋅ Michael Rabbat ⋅ Sumit Chopra ⋅ Matthew Muckley ⋅ Nicolas Ballas  
   [arXiv:2606.25225](https://arxiv.org/abs/2606.25225)
43. **MorphJEPA: Morphology-Aware Latent Prediction for Hyperspectral Images**  
   Amartya Ray ⋅ Tanmay Mandaliya ⋅ Muhammad Haris Khan ⋅ Biplab Banerjee
44. **Multi-Head Normalization for Wide Vision Transformers**  
   Guoyizhe Wei ⋅ Feng Wang ⋅ Alan Yuille ⋅ Rama Chellappa
45. **Multi-View Foundation Models**  
   Leo Segre ⋅ Or Hirschorn ⋅ Shai Avidan  
   [arXiv:2512.15708](https://arxiv.org/abs/2512.15708)
46. **MultiMem: Measuring and Mitigating Memorization in Multi-Modal Contrastive Learning**  
   Wenhao Wang ⋅ Franziska Boenisch ⋅ Michael Backes ⋅ Adam Dziedzic  
   [arXiv:2606.22220](https://arxiv.org/abs/2606.22220)
47. **NAPA: Natively Multimodal Autoregressive Perception Architecture**  
   Phuc Le Khac Hong ⋅ Yasser Dahou ⋅ Sanath Narayan ⋅ Ankit Singh ⋅ Wamiq Para ⋅ Ngoc Dung Huynh ⋅ Sofian Chaybouti ⋅ Hakim Hacid
48. **Natural Image Pretraining Improves Abstract Reasoning**  
   Xiaoman Ding ⋅ Keya Hu ⋅ Katelyn Gan ⋅ Victor Yin ⋅ Kaiming He
49. **NearID: Identity Representation Learning via Near-identity Distractors**  
   Aleksandar Cvejic ⋅ Rameen Abdal ⋅ Abdelrahman Eldesokey ⋅ Bernard Ghanem ⋅ Peter Wonka  
   [arXiv:2604.01973](https://arxiv.org/abs/2604.01973) · [code](https://github.com/Gorluxor/NearID) · [project](https://gorluxor.github.io/NearID/)
50. **One Scene, Two Depths: Probing Geometric Ambiguity in Monocular Foundation Models**  
   Xiaohao Xu ⋅ Feng Xue ⋅ Xiang Li ⋅ Haowei Li ⋅ Shusheng Yang ⋅ Tianyi Zhang ⋅ Matthew Johnson-Roberson ⋅ Xiaonan Huang  
   [arXiv:2606.29600](https://arxiv.org/abs/2606.29600)
51. **Pay Attention to Attention Distribution: A New Local Lipschitz Bound for Transformers**  
   Mikalai Yudzin ⋅ Sergei Kudriashov ⋅ Alexander Gaponov ⋅ Maxim Rakhuba  
   [arXiv:2507.07814](https://arxiv.org/abs/2507.07814)
52. **Plug-and-Play Attention Linearization for Pretrained Transformers**  
   Kenan Kassab ⋅ Alexey Kashevnik ⋅ Ammar Ali ⋅ Stamatios Lefkimmiatis
53. **Pretrained Video Models as Differentiable Physics Simulators for Urban Wind Flows**  
   Janne Perini ⋅ Rafael Bischof ⋅ Moab Arar ⋅ Ayça Duran ⋅ Michael Kraus ⋅ Siddhartha Mishra ⋅ Bernd Bickel  
   [arXiv:2603.21210](https://arxiv.org/abs/2603.21210)
54. **Probing the 3D Object-Level Understanding of Pre-Trained Detection Transformers**  
   Robin Kim ⋅ Colin Samplawski ⋅ Benjamin Marlin  
   [arXiv:2608.01495](https://arxiv.org/abs/2608.01495)
55. **Progressive Representation Learning for Multimodal Sentiment Analysis with Incomplete Modalities**  
   Jindi Bao ⋅ Jianjun Qian ⋅ Mengkai Yan ⋅ Jian Yang  
   [arXiv:2603.09111](https://arxiv.org/abs/2603.09111)
56. **ProtoFair: Fair Self-Supervised Contrastive Learning via Pseudo-Counterfactual Pairs**  
   Marah Halawa ⋅ Olaf Hellwich  
   [arXiv:2605.01971](https://arxiv.org/abs/2605.01971)
57. **Puppet-CNN: Continuous Parameter Dynamics for Input-Adaptive Convolutional Networks**  
   Yucheng Xing ⋅ Xin Wang  
   [arXiv:2411.12876](https://arxiv.org/abs/2411.12876)
58. **Quick ViTs: Speeding up Vision Transformers through Equivariance**  
   David Nordström ⋅ Johan Edstedt ⋅ Fredrik Kahl ⋅ Georg Bökman  
   [arXiv:2505.15441](https://arxiv.org/abs/2505.15441)
59. **RayRoPE: Projective Ray Positional Encoding for Multi-view Attention**  
   Yu Wu ⋅ Minsik Jeon ⋅ Rick Chang ⋅ Oncel Tuzel ⋅ Shubham Tulsiani  
   [arXiv:2601.15275](https://arxiv.org/abs/2601.15275) · [project](https://rayrope.github.io/)
60. **ReGen3D: Generalizable Unified Representation Learning for 3D Understanding**  
   Haotian Zhang ⋅ Jincen Jiang ⋅ Yuhang Li ⋅ Jian Jun Zhang ⋅ Meili Wang ⋅ Jian Chang
61. **RGB-Pointmap Pretraining for Unified 3D Scene Understanding**  
   Ye Mao ⋅ Weixun Luo ⋅ Ranran Huang ⋅ Junpeng Jing ⋅ Krystian Mikolajczyk  
   [arXiv:2604.02546](https://arxiv.org/abs/2604.02546) · [project](https://yebulabula.github.io/UniScene3D/)
62. **S-VAM: Shortcut Video-Action Model by Self-Distilling Geometric and Semantic Foresight**  
   Haodong Yan ⋅ Zhide Zhong ⋅ Jiaguan Zhu ⋅ Junjie He ⋅ Weilin Yuan ⋅ Wenxuan Song ⋅ Xin Gong ⋅ Yingjie CAI ⋅ Guanyi Zhao ⋅ Xu Yan ⋅ Liu Bingbing ⋅ Yingcong Chen ⋅ Haoang Li  
   [arXiv:2603.16195](https://arxiv.org/abs/2603.16195) · [project](https://haodong-yan.github.io/S-VAM/)
63. **Scaling Laws for Black-box Adversarial Attacks**  
   Chuan Liu ⋅ Huanran Chen ⋅ Yichi Zhang ⋅ Jun Zhu ⋅ Yinpeng Dong  
   [arXiv:2411.16782](https://arxiv.org/abs/2411.16782)
64. **Silhouette-based Gait Foundation Model**  
   Dingqiang Ye ⋅ Chao Fan ⋅ Kartik Narayan ⋅ Bingzhe Wu ⋅ Chengwen Luo ⋅ Jianqiang Li ⋅ Vishal Patel  
   [arXiv:2512.00691](https://arxiv.org/abs/2512.00691) · [code](https://github.com/ShiqiYu/OpenGait)
65. **Simple Filtering Improves Masked Autoencoders**  
   Takumi Kobayashi
66. **SpatialBoost: Enhancing Visual Representation through Language-Guided Reasoning**  
   Byungwoo Jeon ⋅ Dongyoung Kim ⋅ Huiwon Jang ⋅ Insoo Kim ⋅ Jinwoo Shin  
   [arXiv:2603.22057](https://arxiv.org/abs/2603.22057)
67. **SPICE: Simple Polysemantic feature Interpretation via Clustering-based Explanations**  
   Sehyun Lee ⋅ Dahee Kwon ⋅ Damin Lee ⋅ Jaesik Choi
68. **Steerable Vision Transformers**  
   Jona Ruthardt ⋅ Manu Gaur ⋅ Deva Ramanan ⋅ Makarand Tapaswi ⋅ Yuki Asano
69. **Steering Diffusion Models via Class-Contrastive Influence for Few-Shot Classification**  
   Jeeyung Kim ⋅ Erfan Esmaeili ⋅ Qiang Qiu
70. **Topology-Weighted Effective Rank: A Zero-Cost Proxy for Training Dynamics Stability in Neural Architecture Search**  
   Haojie Zhang ⋅ Yeming Yang ⋅ Songbai Liu ⋅ Lijia Ma ⋅ Ka-Chun Wong ⋅ Qiuzhen Lin
71. **Understanding Geometric Representations in Self-Supervised Vision Transformers via Subspace Intervention**  
   Weichen Zhou ⋅ Yawen Zou ⋅ Chunzhi Gu ⋅ Ran Dong ⋅ Haoran Xie ⋅ Chao Zhang  
   [arXiv:2607.01987](https://arxiv.org/abs/2607.01987) · [code](https://github.com/Zhou-Weichen/Geosubprobe)
72. **Unified Backbone Refinement for Diffusion Models via Internal-Latent Analysis**  
   HAKSU LIM ⋅ Myeongjin Lee ⋅ Wonjoon Chang ⋅ Jaesik Choi  
   [arXiv:2607.09753](https://arxiv.org/abs/2607.09753)
73. **UniMotion: A Unified Framework for Motion-Text-Vision Understanding and Generation**  
   Ziyi Wang ⋅ Xinshun Wang ⋅ Shuang Chen ⋅ Yang Cong ⋅ Mengyuan Liu  
   [arXiv:2603.22282](https://arxiv.org/abs/2603.22282)
74. **URoPE: Universal Relative Position Embedding across Geometric Spaces**  
   Yichen Xie ⋅ Depu Meng ⋅ Yihan Hu ⋅ Chensheng Peng ⋅ Quentin HERAU ⋅ Masayoshi TOMIZUKA ⋅ Wei Zhan
75. **V-Co: A Closer Look at Visual Representation Alignment via Co-Denoising**  
   Han Lin ⋅ Xichen Pan ⋅ Zun Wang ⋅ Yue Zhang ⋅ Chu Wang ⋅ Jaemin Cho ⋅ Mohit Bansal  
   [arXiv:2603.16792](https://arxiv.org/abs/2603.16792) · [code](https://github.com/HL-hanlin/V-Co)
76. **V-JEPA 2.1: Unlocking Dense Features in Video Self-Supervised Learning**  
   Lorenzo Mur Labadia ⋅ Matthew Muckley ⋅ Amir Bar ⋅ Mido Assran ⋅ Koustuv Sinha ⋅ Michael Rabbat ⋅ Yann LeCun ⋅ Nicolas Ballas ⋅ Adrien Bardes
77. **Vision Bridge Transformer at Scale**  
   Zhenxiong Tan ⋅ Zeqing Wang ⋅ Xingyi Yang ⋅ Songhua Liu ⋅ Xinchao Wang  
   [arXiv:2511.23199](https://arxiv.org/abs/2511.23199)
78. **Vision-TTT: Efficient and Expressive Visual Representation Learning with Test-Time Training**  
   Quan Kong ⋅ Yanru Xiao ⋅ Yuhao Shen ⋅ Cong Wang  
   [arXiv:2603.00518](https://arxiv.org/abs/2603.00518)
79. **VLA-JEPA: Enhancing Vision-Language-Action Model with Latent World Model**  
   Jingwen Sun ⋅ Wenyao Zhang ⋅ Zekun Qi ⋅ Shaojie Ren ⋅ Zezhi Liu ⋅ Hanxin Zhu ⋅ Guangzhong Sun ⋅ Xin Jin ⋅ Zhibo Chen  
   [arXiv:2602.10098](https://arxiv.org/abs/2602.10098)
80. **VNC: A Scale-Space Foundation for Learnable 3D Surface Evolution**  
   Baoxing Li ⋅ Yong Deng ⋅ Xu Zhao
81. **Weight Feedback Computes the Exact Jacobian Transpose in Modern Deep Networks**  
   Junlong Shen ⋅ Xingyu Li
82. **Why Linear Probing Works: Non-Vacuous Generalization Bounds via Effective Dimension**  
   Dongxin Guo ⋅ Jikun Wu ⋅ SM Yiu

## Transfer, Adaptation & Continual Learning

*80 papers · 44 with links*

1. **3D Field of Junctions: A Noise-Robust, Training-Free Structural Prior for Volumetric Inverse Problems**  
   Namhoon Kim ⋅ NARGES MOEINI ⋅ Justin Romberg ⋅ Sara Fridovich-Keil  
   [arXiv:2603.02149](https://arxiv.org/abs/2603.02149) · [code](https://github.com/voilalab/3D-Field-of-Junctions)
2. **A Mechanism-Driven Theory of Phase Transitions in Active Learning**  
   Julia Machnio ⋅ Mads Nielsen ⋅ MOSTAFA MEHDIPOUR GHAZI  
   [arXiv:2607.00144](https://arxiv.org/abs/2607.00144)
3. **Abstract the Layout, Focus the Detail: A Dual-Granularity Representation Framework for Zero-Shot 3D Visual Grounding**  
   Zeyuan Lin ⋅ Hanxuan Li ⋅ Chen He ⋅ Ruiping Wang ⋅ Zhaoxiang Liu ⋅ Xilin CHEN
4. **Boxer: Robust Lifting of Open-World 2D Bounding Boxes to 3D**  
   Daniel DeTone ⋅ Tianwei Shen ⋅ Fan Zhang ⋅ Lingni Ma ⋅ Julian Straub ⋅ Richard Newcombe ⋅ Jakob Engel  
   [arXiv:2604.05212](https://arxiv.org/abs/2604.05212) · [project](http://facebookresearch.github.io/boxer)
5. **Bridging Theory and Practice in Source-Free Domain Adaptation via Adversarial Proxy Perturbation**  
   Dexuan Zhang ⋅ Qianyu Zhou ⋅ Thomas Westfechtel ⋅ Yusuke Mukuta ⋅ Tatsuya Harada
6. **Calibrate Before Adapt: Training-Free Pseudo-Label Calibration for Semi-Supervised Cross-Domain Few-Shot Detection**  
   Xin Yang ⋅ Fei Zhou ⋅ Wei Wei ⋅ Lei Zhang
7. **CHIMERA: Adaptive Cache Injection and Semantic Anchor Prompting for Zero-shot Image Morphing with Morphing-oriented Metrics**  
   Dahyeon Kye ⋅ Jeahun Sung ⋅ Minkyu Jeon ⋅ Jihyong Oh
8. **CloSeR: Unified Relational Distillation from Closed-Set Teachers for Category Discovery**  
   Yuanpei Liu ⋅ Zhenqi He ⋅ Jialu Tang ⋅ Kai Han
9. **COLA: Continual Orthogonal Low-Rank Adaptation for Class-Incremental Learning**  
   Monu Nagar ⋅ Debasis Das
10. **CoReLIN: Constraint-based Reasoning for Zero-shot Lifelong Interactive Navigation**  
   Apoorva Vashisth ⋅ Manav Kulshrestha ⋅ Pranav Bakshi ⋅ Damon Conover ⋅ Guillaume Sartoretti ⋅ Aniket Bera  
   [arXiv:2602.20055](https://arxiv.org/abs/2602.20055)
11. **CS-TTA: Preserving Concept Sensitivity in Test-Time Adaptation**  
   Junah Jung ⋅ YeonGyu Han ⋅ Chang Min Park ⋅ Dongheon Lee
12. **D-VLAM: Differential Vision and Language Mixing for Rehearsal Free Continual Learning**  
   Muhammad Anwar Ma'sum ⋅ Mohsen Guizani ⋅ Waseem Ullah
13. **DA-MergeLoRA: Hypernetwork-Based LoRA Merging for Few-Shot Test-Time Domain Adaptation**  
   Siobhan Reid ⋅ Zhixiang Chi ⋅ Li Gu ⋅ Omid Heidari ⋅ Ziqiang Wang ⋅ Yang Wang  
   [arXiv:2607.17467](https://arxiv.org/abs/2607.17467) · [code](https://github.com/nahbois4321/DA-MergeLoRA)
14. **Deep Noise Label Learning via Effective Rank Reduction**  
   Changyi Ma ⋅ Zihan Fang ⋅ Lihua Zhou ⋅ Tao Li ⋅ Wenyu Liu ⋅ Runsheng Yu ⋅ Xuan Song
15. **Distill Once, Adapt Life-Long: Exploring Dataset Distillation for Continual Test-Time Adaptation**  
   Hyun-Kurl Jang ⋅ Jihun Kim ⋅ Hyeokjun Kweon ⋅ KUK-JIN YOON  
   [arXiv:2606.20196](https://arxiv.org/abs/2606.20196) · [code](https://github.com/blue-531/DOALL)
16. **Domain Adaptation with Adaptive Imagination for Visual Reinforcement Learning under Limited Target Data**  
   Hyunwoo Park ⋅ Sanghyun Lee  
   [arXiv:2606.30192](https://arxiv.org/abs/2606.30192)
17. **Domain Generalization via Text-Anchored Information Bottleneck**  
   Eunyi Lyou ⋅ YUNJEONG CHOI ⋅ Junho Lee ⋅ Lee Joonseok  
   [arXiv:2607.01657](https://arxiv.org/abs/2607.01657)
18. **DP-BOA: Dirichlet-Process Birth-or-Assign for On-the-Fly Category Discovery**  
   Peiyan Gu ⋅ Zixin Teng ⋅ Xuming He  
   [arXiv:2607.13504](https://arxiv.org/abs/2607.13504)
19. **DriveVA: Video Action Models are Zero-Shot Drivers**  
   Mengmeng Liu ⋅ Diankun Zhang ⋅ Jiuming Liu ⋅ Jianfeng Cui ⋅ Hongwei Xie ⋅ Guang Chen ⋅ Hangjun Ye ⋅ Michael Yang ⋅ Francesco Nex ⋅ Hao Cheng  
   [arXiv:2604.04198](https://arxiv.org/abs/2604.04198)
20. **Dual-Margin Embedding for Fine-Grained Long-Tailed Plant Taxonomy**  
   Cheng-Yaw Low ⋅ Heejoon Koo ⋅ Jaewoo Park ⋅ Meeyoung Cha  
   [arXiv:2512.18994](https://arxiv.org/abs/2512.18994)
21. **DualCount: Structurally Consistent Density and Point Modeling for Zero-Shot Object Counting**  
   Xuan Cuong Ngo
22. **Dynamic-V2C: Editable and Continual Vision-to-Concept Bottleneck Models via Influence Functions**  
   Songning Lai ⋅ Shaofeng Liang ⋅ Jiayu Yang ⋅ Ninghui Feng ⋅ Yuxuan Fan ⋅ Wenshuo Chen
23. **Fast Spatial Memory with Scalable Elastic Test-Time Training**  
   Ziqiao Ma ⋅ Xueyang Yu ⋅ Haoyu Zhen ⋅ Yuncong Yang ⋅ Joyce Chai ⋅ Chuang Gan
24. **FD²: A Dedicated Framework for Fine-Grained Dataset Distillation**  
   Hongxu Ma ⋅ Guang Li ⋅ Shijie Wang ⋅ DONGZHAN ZHOU ⋅ Baoli Sun ⋅ Takahiro Ogawa ⋅ Miki Haseyama ⋅ Zhihui Wang
25. **Few-Shot Synthetic Image Attribution: Identifying Unseen Generators with Limited Samples**  
   Shiyu Wu ⋅ Shuyan Li ⋅ Jing Li ⋅ Jing Liu ⋅ Yequan Wang  
   [arXiv:2509.25682](https://arxiv.org/abs/2509.25682) · [code](https://github.com/teheperinko541/OmniDFA)
26. **From Local Geometry to Global Pseudo-Labeling for Robust Positive–Unlabeled Learning under Covariate Shift**  
   Firas Gabetni ⋅ Alexandre Rocchi--Henry ⋅ Ziyi LIU ⋅ Nacim Belkhir ⋅ Gianni Franchi  
   [arXiv:2605.31187](https://arxiv.org/abs/2605.31187)
27. **G-ZAP: A Generalizable Zero-Shot Framework for Arbitrary-Scale Pansharpening**  
   Zhiqi Yang ⋅ Shan Yin ⋅ Jingze Liang ⋅ Liang-Jian Deng  
   [arXiv:2603.14412](https://arxiv.org/abs/2603.14412)
28. **Geometric Gradient Rectification for Safe Open-Set Semi-Supervised Learning**  
   Jiahe Chen ⋅ Qian Shao ⋅ Qiyuan Chen ⋅ Jiaying He ⋅ Jintai Chen ⋅ Hongxia Xu ⋅ Jian Wu  
   [arXiv:2606.26973](https://arxiv.org/abs/2606.26973) · [code](https://github.com/JiaheChen2002/GGR)
29. **Geometric Regularization for Long-Tailed Semi-Supervised Learning via Gaussian Feature Bridges**  
   Hongyang He ⋅ Xinyuan Song ⋅ Yan Zhong ⋅ Daizong Liu ⋅ Yanbin Li ⋅ Yangfan He ⋅ Wenqiao Zhang
30. **Geometry-Anchored Transport Framework for Exemplar-Free Class-Incremental Learning**  
   Hongye Xu ⋅ Bartosz Krawczyk  
   [arXiv:2606.25347](https://arxiv.org/abs/2606.25347) · [code](https://github.com/HXuSz11/GATF_ECCV2026)
31. **Graph Coloring for Multi-Task Learning**  
   Santosh Patapati ⋅ Ian Noronha  
   [arXiv:2509.16959](https://arxiv.org/abs/2509.16959)
32. **H-Adapter: Pose-Robust Hairstyle Transfer via Attention-Derived, Source-Aligned Hair Masks**  
   Seulgi Jeong ⋅ Yunseong Cho ⋅ Sanghun Park  
   [arXiv:2606.25578](https://arxiv.org/abs/2606.25578) · [project](https://sanghunpark.github.io/hadapter_page/)
33. **HER-Count: Learning Hyper-Exemplar Representation for Generalized Zero-Shot Object Counting**  
   Jianing Li ⋅ Xiaobin Liu ⋅ Ruihan Xu
34. **Holistic Optimal Label Selection for Robust Prompt Learning under Partial Labels**  
   Yaqi Zhao ⋅ Haoliang Sun ⋅ Yating Wang ⋅ Yongshun Gong ⋅ Yilong Yin  
   [arXiv:2604.06614](https://arxiv.org/abs/2604.06614)
35. **HSFM: Hard-Set-Guided Feature-Space Meta-Learning for Robust Classification under Spurious Correlations**  
   Aryan Yazdan Parast ⋅ Khawar Islam ⋅ Soyoun Won ⋅ Basim Azam ⋅ NAVEED AKHTAR  
   [arXiv:2603.29313](https://arxiv.org/abs/2603.29313)
36. **Interference-Aware Continual Vision–Language Learning via Instance-Level Expert Routing**  
   Zhang Changyuan ⋅ Tianxiang Xu ⋅ Canran Xiao ⋅ Fei Shen
37. **LDC-MTL: Balancing Multi-Task Learning through Scalable Loss Discrepancy Control**  
   Peiyao Xiao ⋅ Chaosheng Dong ⋅ Shaofeng Zou ⋅ Kaiyi Ji  
   [arXiv:2502.08585](https://arxiv.org/abs/2502.08585)
38. **Learning Probabilistic Prompt for Continual Learning**  
   Hyekang Park ⋅ Sanghoon Lee ⋅ Geon Lee ⋅ Jongyoun Noh ⋅ BUMSUB HAM  
   [arXiv:2607.04711](https://arxiv.org/abs/2607.04711)
39. **Learning to Recover Task Experts from a Multi-Task Merged Model**  
   Jinwook Jung ⋅ Taegyu Kim ⋅ Kumju Jo ⋅ Sungyong Baik  
   [arXiv:2606.26902](https://arxiv.org/abs/2606.26902) · [code](https://github.com/BAIKLAB/ReTeX)
40. **Low-Rank Ternary Adaptation for Fine-Tuning Transformers**  
   Alexandru-Dragos Manolache ⋅ Yunqiang Li ⋅ Jan van Gemert
41. **Making Partial-Label Datasets Easier: A Simple Yet Highly Effective Data Augmentation for Deep Partial-Label Learning**  
   Dong-Dong Wu ⋅ Zhaoyi Li ⋅ Xiang Li ⋅ Zhiqiang Shen
42. **Mask-guided Semantic Alignment: Robust Learning with Noisy Labels via Temporal Attention Stability**  
   Yubo Nian ⋅ Can Gao
43. **Match-Any-Events: Zero-Shot Motion-Robust Feature Matching Across Wide Baselines for Event Cameras**  
   Ruijun Zhang ⋅ Hang Su ⋅ Kostas Daniilidis ⋅ Ziyun Wang  
   [arXiv:2604.18744](https://arxiv.org/abs/2604.18744) · [code](https://github.com/spikelab-jhu/Match-Any-Events)
44. **Maximum Spanning Tree Guided Confidence and Sparse Graph for Robust Noisy Label Learning**  
   Gengfeng Chen ⋅ Xu Liu ⋅ Boyi Peng ⋅ Liangqiu Xiao ⋅ Weicheng Xie ⋅ Siyang Song ⋅ Zitong Yu ⋅ Laizhong Cui ⋅ Linlin Shen
45. **MixTTA: Low-Rank Cross-Channel Mixing for Reliable Test-Time Adaptation**  
   Mansoo Jung ⋅ Youngwook Kim ⋅ Jungwoo Lee  
   [arXiv:2606.28142](https://arxiv.org/abs/2606.28142) · [code](https://github.com/delta6189/MixTTA)
46. **MMEarth-Bench: Global Model Adaptation via Multimodal Test-Time Training**  
   Lucia Gordon ⋅ Serge Belongie ⋅ Christian Igel ⋅ Nico Lang  
   [arXiv:2602.06285](https://arxiv.org/abs/2602.06285)
47. **Multi-Hypothesis Test-Time Adaptation to Mitigate Underspecification**  
   Afshar Shamsi ⋅ Xiao-Yu Guo ⋅ Hamid Alinejad-Rokny ⋅ Arash Mohammadi ⋅ Damien Teney ⋅ Ehsan Abbasnejad  
   [arXiv:2607.00259](https://arxiv.org/abs/2607.00259)
48. **Multi-modal Knowledge Preserving Adapter for Embedding Backward Compatibility**  
   Jaeseok Byun ⋅ Gukyeong Kwon ⋅ Han-Kai Hsu ⋅ MEHER GITIKA KARUMURI ⋅ Zhikang Zhang ⋅ Hao Yang ⋅ Davide Modolo
49. **Neutralizing Token Aggregation via Information Augmentation for Efficient Test-Time Adaptation**  
   Yizhe Xiong ⋅ Zihan Zhou ⋅ Yiwen Liang ⋅ Hui Chen ⋅ Zijia Lin ⋅ Xinhao Xu ⋅ Tianxiang Hao ⋅ Fan Zhang ⋅ Jungong Han ⋅ Guiguang Ding  
   [arXiv:2508.03388](https://arxiv.org/abs/2508.03388)
50. **On the Vulnerability of Parameter-Level Defenses to Model Merging**  
   Kuangpu Guo ⋅ Jian Liang ⋅ Qingyan Zheng ⋅ Yu Yongcan ⋅ Zilei Wang ⋅ Ran He ⋅ Tieniu Tan  
   [arXiv:2606.30360](https://arxiv.org/abs/2606.30360) · [code](https://github.com/krumpguo/secure-merge-attack)
51. **Online Versatile Incremental Learning: Towards Class and Domain-Agnostic Adaptation at Any Time**  
   Jaeho Lee ⋅ Jun-Yeong Moon ⋅ Min-Yeong Park ⋅ Jung Uk Kim ⋅ Gyeong-Moon Park
52. **ORACLE-3D: Open-world Region-aligned Cross-modal Learning for Label-efficient 3D Scene Understanding**  
   Yuru Wang ⋅ Pei Liu ⋅ Songtao Wang ⋅ Zehan Zhang ⋅ Xinyan Lu ⋅ Changwei Cai ⋅ Hao Li ⋅ Haipeng LIU ⋅ Qingtian Ning ⋅ Jun Ma
53. **Prior-Conditioned Gaussian Discriminants for Generalizable AI-generated Image Detection**  
   Shashank Kotyan ⋅ Makoto Shing ⋅ Yuki Imajuku ⋅ Rujikorn Charakorn ⋅ Tarin Clanuwat
54. **R2M: Real-Aware Residual Model Merging for Robust and Generalizable Deepfake Detection**  
   Jinhee Park ⋅ Guisik Kim ⋅ Choongsang Cho ⋅ Junseok Kwon
55. **Rank-Aware Hyperbolic Alignment for Vision–Language Dataset Distillation**  
   Jongoh Jeong ⋅ Sun-Kyung Lee ⋅ KUK-JIN YOON  
   [arXiv:2606.29464](https://arxiv.org/abs/2606.29464) · [project](https://andyj1.github.io/raha)
56. **Revisiting Weakly-Supervised Video Scene Graph Generation via Pair Affinity Learning**  
   MINSEOK KANG ⋅ Minhyeok Lee ⋅ Minjung Kim ⋅ Jungho Lee ⋅ Donghyeong Kim ⋅ Sungmin Woo ⋅ Inseok Jeon ⋅ Sangyoun Lee  
   [arXiv:2603.21559](https://arxiv.org/abs/2603.21559)
57. **Robust Zero-shot Anomaly Detection under Limited Auxiliary Anomaly Priors**  
   Guanyu Lu ⋅ Fang Zhou ⋅ Cheqing Jin  
   [arXiv:2606.29428](https://arxiv.org/abs/2606.29428)
58. **Robustness Emerges Early in Training Dynamics, but Is Not Preserved**  
   Jiangang Yang ⋅ Wenhui Shi ⋅ Lu Hu ⋅ Jing Xing ⋅ Jian Liu  
   [arXiv:2608.04442](https://arxiv.org/abs/2608.04442)
59. **RobustRDP: Advancing Reaction Diagram Parsing via Synthetic-to-Real Data Scaling and Robustness-Oriented Training**  
   Jianting Tang ⋅ zezhong wu ⋅ Linli Xu
60. **RUTaL: Residual Upcycling with Task Ladder for Efficient Multi-Task Learning**  
   Haiming Yao ⋅ Wei Luo ⋅ Qiyu Chen ⋅ Jianxing Liao ⋅ Wei You
61. **ScAle: Attention Head Scaling as a Minimal Adapter for Spatial Reasoning in Vision–Language Models**  
   Rahul Chowdhury ⋅ Timothy Rupprecht ⋅ Xuan Shen ⋅ Pu Zhao ⋅ Yanzhi Wang
62. **Sim, Yet Same: Physics-Aligned Simulator as Zero-Shot Data Scaler in Deformable Worlds**  
   Yunsong Zhou ⋅ Hangxu Liu ⋅ Xuekun Jiang ⋅ Xing Shen ⋅ Yuanzhen Zhou ⋅ Hui Wang ⋅ Baole Fang ⋅ Yang Tian ⋅ Mulin Yu ⋅ Qiaojun Yu ⋅ Li Ma ⋅ Hengjie Li ⋅ Hanqing Wang ⋅ Jia Zeng ⋅ Jiangmiao Pang
63. **Solving Semi-Supervised Few-Shot Learning from an Auto-Annotation Perspective**  
   Tian Liu ⋅ Anwesha Basu ⋅ James Caverlee ⋅ Shu Kong  
   [arXiv:2512.10244](https://arxiv.org/abs/2512.10244) · [project](https://tian1327.github.io/SWIFT)
64. **Spectral-Aware Analytic Class-Incremental Learning for Long-Tailed Distributions**  
   Quyen Tran ⋅ Ngoc-Hai Nguyen ⋅ Minh Quan Dao ⋅ Zhuowei Li ⋅ Nam Hai ⋅ Trung Le ⋅ Dimitris N. Metaxas  
   [arXiv:2607.22931](https://arxiv.org/abs/2607.22931)
65. **SPLIT: Training-Free AI-Generated and Partially Edited Video Detection via Spatial Patch‑Level Incoherence and Temporal Roughness**  
   Jongyeop Hyun ⋅ Hyounghun Kim
66. **Stay Unique, Stay Efficient: Preserving Model Personality in Multi-Task Merging**  
   Kuangpu Guo ⋅ Aijing Yu ⋅ Jian Liang ⋅ Yuhe Ding ⋅ Zilei Wang ⋅ Ran He ⋅ Tieniu Tan  
   [arXiv:2512.01461](https://arxiv.org/abs/2512.01461) · [code](https://github.com/krumpguo/DTS)
67. **StructPolicy: Structure-Guided Imitation Learning Robust to Visual Domain Shifts**  
   Zehao Du ⋅ Jiude Wei ⋅ Cewu Lu ⋅ Jianhua Sun
68. **SyncVL: Synchronizing Vision ⟷ Language Using Unsupervised Adaptation**  
   Maria Marrium ⋅ Muhammad Haris Khan ⋅ Sajid Javed ⋅ Arif Mahmood
69. **Task Alignment: A simple and effective proxy for model merging in computer vision**  
   Pau de Jorge Aranda ⋅ César DE SOUZA ⋅ Björn Michele ⋅ Mert Bulent SARIYILDIZ ⋅ Philippe Weinzaepfel ⋅ Florent Perronnin ⋅ Larlus Diane ⋅ Yannis Kalantidis
70. **To Erase, or Not to Erase: Robust Training-Free Concept Erasure with Preservation aware Adaptive Ranked Subspace Expansion**  
   Shaswati Saha ⋅ Rajasekhar Anguluri ⋅ Manas Gaur  
   [arXiv:2607.23492](https://arxiv.org/abs/2607.23492)
71. **Towards Robustness against Typographic Attack with Training-free Concept Localization**  
   Bohan Liu ⋅ Wenqian Ye ⋅ Guangzhi Xiong ⋅ Zhenghao He ⋅ Sanchit Sinha ⋅ Aidong Zhang  
   [arXiv:2607.02494](https://arxiv.org/abs/2607.02494) · [code](https://github.com/Liu-524/SamplingTAR)
72. **Training-free Cross-domain Few-shot Segmentation via Robust Semantic Representation and Matching**  
   Sujun Sun ⋅ Mingwu Ren ⋅ Haofeng Zhang  
   [arXiv:2606.24297](https://arxiv.org/abs/2606.24297)
73. **Training-free Discriminative Patch Mining for Robust Few-Shot Recognition with CLIP**  
   Zhenzhang Ye ⋅ Duolikun Danier ⋅ Bo Zhao ⋅ Hakan Bilen
74. **Training-Free Task Classification for Multi-Task Model Merging**  
   JUNGYONG SON ⋅ Jinwook Jung ⋅ Sungyong Baik  
   [arXiv:2606.22589](https://arxiv.org/abs/2606.22589) · [code](https://github.com/BAIKLAB/SiM)
75. **Tuning-free Visual Effect Transfer across Videos**  
   Maxwell Jones ⋅ Rameen Abdal ⋅ Or Patashnik ⋅ Ruslan Salakhutdinov ⋅ Sergey Tulyakov ⋅ Jun-Yan Zhu ⋅ Kuan-Chieh Wang  
   [arXiv:2601.07833](https://arxiv.org/abs/2601.07833) · [project](https://snap-research.github.io/RefVFX/)
76. **Unleashing the Power of Large-Scale ViT in Zero-Shot SBIR: A Strong Baseline with Multi-Layer Feature Aggregation**  
   Yang Liu ⋅ Yongjing Guo ⋅ Suisui Jia ⋅ Huaizhou Qi ⋅ Xun Du ⋅ Haonan Chen
77. **Unsupervised Source-Free Ranking of Biomedical Segmentation Models Under Distribution Shift**  
   Joshua Talks ⋅ Kevin Marchesini ⋅ Luca Lumetti ⋅ Federico Bolelli ⋅ Anna Kreshuk  
   [arXiv:2503.00450](https://arxiv.org/abs/2503.00450)
78. **Virtual Category-Guided Continual Generalized Category Discovery**  
   Jiahui Xiong ⋅ Qiuxia Lai ⋅ Hongsong Wang  
   [arXiv:2607.04984](https://arxiv.org/abs/2607.04984) · [code](https://github.com/Mrxjh105/VC-CGCD)
79. **VLOD-TTA: Test-Time Adaptation of Vision-Language Object Detectors**  
   Atif Belal ⋅ Heitor Medeiros ⋅ Marco Pedersoli ⋅ Eric Granger  
   [arXiv:2510.00458](https://arxiv.org/abs/2510.00458) · [code](https://github.com/imatif17/VLOD-TTA)
80. **XSemanticFlow: Cross Object Semantic Alignment for Zero-shot Manipulation**  
   Junyu Nan ⋅ Noam Eshed ⋅ Brian Okorn ⋅ Kris Kitani

## Efficiency, Compression & Acceleration

*103 papers · 62 with links*

1. **Accelerating Multimodal Large Language Models with Prior-Corrected Token Reduction**  
   Zengjie Chen ⋅ Yuxiang Cai ⋅ Jingcai Guo ⋅ Taotao Cai ⋅ Jianwei Yin ⋅ Zhi Chen  
   [arXiv:2606.24156](https://arxiv.org/abs/2606.24156)
2. **Accelerating Text-to-Video Generation with Calibrated Sparse Attention**  
   Shai Yehezkel ⋅ Shahar Yadin ⋅ Noam Elata ⋅ Yaron Ostrovsky-Berman ⋅ Bahjat Kawar  
   [arXiv:2603.05503](https://arxiv.org/abs/2603.05503)
3. **Accurate Zero-shot Quantization via Hierarchical Teacher-Assistant Distillation**  
   Wonjin Cho ⋅ Jeongin Yun ⋅ U Kang
4. **Activation Quantization of Vision Encoders Needs Prefixing Registers**  
   Seunghyeon Kim ⋅ Taesun Yeom ⋅ Jinho Kim ⋅ Wonpyo Park ⋅ Kyuyeun Kim ⋅ Jaeho Lee  
   [arXiv:2510.04547](https://arxiv.org/abs/2510.04547) · [code](https://github.com/spbob0418/RegCache)
5. **Aggregating Cross-Domain Knowledge via Learnable Tokens for Multi-Teacher Distillation**  
   Wu Ran ⋅ Weijia Zhang ⋅ ShuYang Pang ⋅ JingSheng Liu ⋅ Xiaohui Zhang ⋅ Yichao Yan ⋅ Chao Ma
6. **AVQ-Attention: Adaptive Vector-Quantized Attention**  
   Winfried van den Dool ⋅ Patrick Forré ⋅ Amirhossein Habibian ⋅ Yuki Asano ⋅ Max Welling  
   [arXiv:2607.12789](https://arxiv.org/abs/2607.12789)
7. **Benchmarking Federated Learning &amp; Knowledge Distillation for Point Cloud Classification**  
   Aizierjiang Aiersilan
8. **Beyond Filter Pruning: Top-K Spatial Selection for Efficient Neural Networks**  
   Sarthak Ketanbhai Modi ⋅ Hans Soegeng ⋅ Thomas Peyrin
9. **BLOB-Q: Boosting Low Bit ViT Quantization via Global Optimization on Model Distortion**  
   Wang Mark ⋅ Kaixin Xu ⋅ Xue Geng ⋅ Fen Fang ⋅ Mohamed Aly ⋅ Xulei Yang ⋅ Min Wu ⋅ Weisi Lin
10. **Capacity Overflow: A Blind Spot for Backdoor Attacks in Vision MoE**  
   Xiaolin Xu ⋅ Tiancheng Zheng ⋅ Xiaolin Xu ⋅ Ruyi Ding
11. **CaRe: Critical Parameter Rectification for Efficient Visual Modeling**  
   Mingjia Li ⋅ Hongkun Xiong ⋅ Yuheng Shi ⋅ Hengxing Liu ⋅ Xiaojie Guo
12. **Continuous Speculative Decoding for Autoregressive Image Generation**  
   Zili Wang ⋅ Zheng Zhang ⋅ Kun Ding ⋅ Qi Yang ⋅ Fei Li ⋅ SHIMING XIANG  
   [arXiv:2411.11925](https://arxiv.org/abs/2411.11925) · [code](https://github.com/MarkXCloud/CSpD)
13. **DC-Gen: Post-Training Diffusion Acceleration with Deeply Compressed Latent Space**  
   Wenkun He ⋅ Yuchao Gu ⋅ Junyu Chen ⋅ Junyi Wu ⋅ Wenhang Ge ⋅ Dongyun Zou ⋅ Yujun Lin ⋅ Zhekai Zhang ⋅ Haocheng Xi ⋅ Muyang Li ⋅ Ligeng Zhu ⋅ Jincheng YU ⋅ Junsong Chen ⋅ Enze Xie ⋅ Song Han ⋅ Han Cai  
   [arXiv:2509.25180](https://arxiv.org/abs/2509.25180) · [code](https://github.com/dc-ai-projects/DC-Gen)
14. **Denoising-Enhanced Coarse-to-Fine Infrared Small Target Detection with Attention Prior-Guided Knowledge Distillation**  
   Houzhang Fang ⋅ Ruixuan Huang ⋅ Qiuhuan Chen ⋅ Xiaolin Wang ⋅ Yi Chang ⋅ Luxin Yan  
   [arXiv:2606.21956](https://arxiv.org/abs/2606.21956)
15. **Dense Video Understanding with Inter-tokenization Acceleration**  
   Haichao Zhang ⋅ Wenhao Chai ⋅ Shwai He ⋅ Ang Li ⋅ Yun Fu
16. **DIGS: Differentiable, Incremental, Global, Scalable Pruning for Language Models**  
   Bingcong Li ⋅ Junlin Xian ⋅ TAO JIANG ⋅ jwlin jwlin ⋅ Cheng ZOU ⋅ Geng-Li Zhang
17. **Distill on a Diet: Efficient Knowledge Distillation via Learnable Data Pruning**  
   Yifan Wu ⋅ Yiqi Wang ⋅ Xichen Ye ⋅ Wenjing Yan ⋅ Xiaoqiang Li ⋅ Cheng Jin ⋅ WEIZHONG ZHANG ⋅ Xiangyu Yue  
   [arXiv:2606.25488](https://arxiv.org/abs/2606.25488)
18. **DIVA: Instruction-Aware Vision Token Pruning via Dual-Probe Attention Discrepancy**  
   Hyunwoo Kim ⋅ Kisu Lee ⋅ Yuna Shin ⋅ Ha Young Kim
19. **Diversity-Aware View Partitioning for Scalable VGGT**  
   Jinsoo Park ⋅ Donggyu Choi ⋅ Ahyun Seo ⋅ Minsu Cho ⋅ Jeany Son  
   [arXiv:2607.01885](https://arxiv.org/abs/2607.01885)
20. **DreamLite: A Lightweight On-Device Unified Model for Image Generation and Editing**  
   Kailai Feng ⋅ Yuxiang WEI ⋅ Bo Chen ⋅ yang pan ⋅ Hu Ye ⋅ Songwei Liu ⋅ Chenqian Yan ⋅ Yuan Gao ⋅ Wangmeng Zuo  
   [arXiv:2603.28713](https://arxiv.org/abs/2603.28713) · [project](https://carlofkl.github.io/dreamlite/)
21. **DroneFINE: Domain-Aware Parameter-Efficient Fine-Tuning of Vision-Language Detectors for Drone Images**  
   Wu Ke ⋅ Yanan Zhang ⋅ Yingjie Gao ⋅ Wenhao Li ⋅ Chenyu Zhou ⋅ Xinzhu Ma ⋅ Di Huang ⋅ Di Huang  
   [arXiv:2607.00338](https://arxiv.org/abs/2607.00338)
22. **EchoVLA: Robotic Vision-Language-Action Model with Synergistic Declarative Memory for Mobile Manipulation**  
   Min Lin ⋅ Xiwen Liang ⋅ Bingqian Lin ⋅ Jingzhi Liu ⋅ Zijian Jiao ⋅ Kehan Li ⋅ Ziang Yan ⋅ Yu Sun ⋅ Weijia Liufu ⋅ Yuhan Ma ⋅ Jiarui Hu ⋅ Yuecheng Liu ⋅ Shen Zhao ⋅ Yuzheng Zhuang ⋅ Xiaodan Liang  
   [arXiv:2511.18112](https://arxiv.org/abs/2511.18112)
23. **Efficient and High-Quality Depth Estimation via Pixel-Space Diffusion with Linear Attention**  
   Bingde Liu ⋅ Wu Ran ⋅ Jinglei Zhang ⋅ Huanhuan Yuan ⋅ Chao Ma
24. **Efficient Document Tampering Localization with Multi-Level Discrepancy Features and Unified DCT–Quantization Embedding**  
   Mohamed Dhouib ⋅ Ye Zhu ⋅ Sonia Vanier ⋅ Aymen Shabou  
   [arXiv:2606.22285](https://arxiv.org/abs/2606.22285)
25. **Efficient Quantization-Aware Adaptation for Visual Foundation Models**  
   Yinglong Li ⋅ Xiaoyu Liu ⋅ Yutong Liu ⋅ Yueyi Zhang ⋅ Zhiwei Xiong
26. **EffiDINO: Task-Specific Model Pruning via Gram Anchoring Subspace Consistency**  
   Jianjian Yin ⋅ Liulei Li ⋅ Tao Chen ⋅ Yi Chen ⋅ Yazhou Yao ⋅ Wenguan Wang
27. **Enhanced Neural Video Representation Compression with High Scalability**  
   Ho Man Kwan ⋅ Tianhao Peng ⋅ Fan Zhang ⋅ Mike Nilsson ⋅ Andrew Gower ⋅ David Bull
28. **ESCAPE: Episodic Spatial Memory and Adaptive Execution Policy for Long-Horizon Mobile Manipulation**  
   Jingjing Qian ⋅ Zeyuan He ⋅ Chen Shi ⋅ Lei Xiao ⋅ Li Jiang
29. **EVAR: Edge Visual Autoregressive Models via Principled Pruning**  
   Zefang Wang ⋅ Ying Li ⋅ Yanyu Li ⋅ Mingluo Su ⋅ Simin Xu ⋅ Guanzhong Tian ⋅ Huan Wang
30. **Exploratory, Communicative, and Deployable: Vision-Driven Embodied Agents for Open-World Mobile Manipulation**  
   Boyu Mi ⋅ Mengchen Ma ⋅ Yifei Yao ⋅ Xing Gao ⋅ Hanqing Wang ⋅ Junting Chen ⋅ Yangzi Li ⋅ Zihou Zhu ⋅ Guohao Li ⋅ Zhenfei Yin ⋅ Tai Wang ⋅ Yao Mu ⋅ Jiangmiao Pang  
   [arXiv:2607.13653](https://arxiv.org/abs/2607.13653) · [code](https://github.com/InternRobotics/REAL)
31. **Fast and Accurate Image Restoration with Rank Enhanced Linear Attention**  
   Yuang Ai
32. **FastSTAR: Spatiotemporal Token Pruning for Efficient Autoregressive Video Synthesis**  
   Sungwoong Yune ⋅ Suheon Jeong ⋅ Joo-Young Kim  
   [arXiv:2603.07192](https://arxiv.org/abs/2603.07192)
33. **Fisher-Routed Mixture of Experts for Federated Class-Incremental Learning**  
   Wenhao Yuan ⋅ Chenchen Lin ⋅ Jian Chen ⋅ Jinfeng Xu ⋅ Zewei Liu ⋅ Edith C. H. Ngai  
   [arXiv:2606.28835](https://arxiv.org/abs/2606.28835)
34. **Flash-DD: An Ultra Parameter-Efficient Approach to Dataset Distillation**  
   Ruonan Yu ⋅ Songhua Liu ⋅ Xinchao Wang
35. **FlashBEV: Fast and Memory-Efficient Exact BEV Transformation with IO-Awareness**  
   Shunsuke Yokokawa ⋅ Hironori Kasahara  
   [arXiv:2607.10071](https://arxiv.org/abs/2607.10071) · [code](https://github.com/yokosyun/FlashBEV)
36. **Focusing on What Matters: Saliency-Harnessing Accurate Routing for Diffusion MoE**  
   Haoyou Deng ⋅ Keyu Yan ⋅ Chaojie Mao ⋅ Xiang Wang ⋅ Yu Liu ⋅ Changxin Gao ⋅ Nong Sang  
   [arXiv:2606.26938](https://arxiv.org/abs/2606.26938)
37. **From Predictions to Embeddings: Dual Knowledge Distillation for Instance-Dependent Partial Label Learning**  
   Lilong Duan ⋅ Ke Wang ⋅ Yao Zhang ⋅ Jun Tang
38. **GCMRD: Global Consistency Multi-teacher Robustness Distillation**  
   Yuhang Zhou ⋅ Zhongyun Hua ⋅ Rushi Lan ⋅ Qing Liao ⋅ Wei Jiang
39. **HQ-DM: Single Hadamard Transformation-Based Quantization-Aware Training for Low-Bit Diffusion Models**  
   Shizhuo Mao ⋅ Hongtao Zou ⋅ Qihu Xie ⋅ Song Chen ⋅ Yi Kang  
   [arXiv:2512.05746](https://arxiv.org/abs/2512.05746)
40. **HSD: Training-Free Acceleration for Document Parsing Vision-Language Models with Hierarchical Speculative Decoding**  
   Wenhui Liao ⋅ Hongliang Li ⋅ Pengyu Xie ⋅ Xinyu Cai ⋅ Yufan Shen ⋅ Yi Xin ⋅ Qi Qin ⋅ Shenglong Ye ⋅ Tianbin Li ⋅ Ming Hu ⋅ Junjun He ⋅ Yihao Liu ⋅ Wenhai Wang ⋅ Min Dou ⋅ Bin Fu ⋅ Botian Shi ⋅ Yu Qiao ⋅ Lianwen Jin  
   [arXiv:2602.12957](https://arxiv.org/abs/2602.12957) · [code](https://github.com/whlscut/HSD)
41. **IDeaL: Data-Free Multi-Teacher Distillation via Improved Dead Leaves**  
   Feyza Yavuz ⋅ Mert Bulent SARIYILDIZ ⋅ Larlus Diane
42. **Identifiable Gated Residual Personalization for Federated Parameter-Efficient Fine-Tuning**  
   Huimin Huang ⋅ Wenhan Hu ⋅ Gang Yan
43. **Improving Knowledge Distillation Under Unknown Covariate Shift Through Confidence-Guided Data Augmentation**  
   Niclas Popp ⋅ Kevin Laube ⋅ Matthias Hein ⋅ Lukas Schott  
   [arXiv:2506.02294](https://arxiv.org/abs/2506.02294)
44. **Inference-Time Scaling of Diffusion Models via Progressive Pruning Search**  
   Rogério Guimarães ⋅ Pietro Perona
45. **LANCE: Low Rank Activation Compression for Efficient On-Device Continual Learning**  
   Marco Apolinario ⋅ Kaushik Roy  
   [arXiv:2509.21617](https://arxiv.org/abs/2509.21617)
46. **LISA: Locality-Informed Speculative Decoding for Accelerating Autoregressive Image Generation**  
   Ying Li ⋅ Siyong Jian ⋅ Zhaode Wang ⋅ Zhiwen Chen ⋅ Chengfei Lyu ⋅ Huan Wang
47. **Mapping the Concept Landscape: Structural Perception of Global Distributions for Transparent Data Pruning**  
   Dongyue Wu ⋅ Tao Ma
48. **MMLoP: Multi-Modal Low-Rank Prompting for Efficient Vision-Language Adaptation**  
   Sajjad Ghiasvand ⋅ Haniyeh Oskouie ⋅ Mahnoosh Alizadeh ⋅ Ramtin Pedarsani  
   [arXiv:2602.21397](https://arxiv.org/abs/2602.21397) · [code](https://github.com/sajjad-ucsb/MMLoP)
49. **MobileManiBench: Simplifying Model Verification for Mobile Manipulation**  
   Wenbo Wang ⋅ Fangyun Wei ⋅ Qixiu Li ⋅ Xi Chen ⋅ Yaobo Liang ⋅ Chang Xu ⋅ Jiaolong Yang ⋅ Baining Guo  
   [arXiv:2602.05233](https://arxiv.org/abs/2602.05233)
50. **MobileOcc: A Human-Aware Semantic Occupancy Dataset for Mobile Robots**  
   Junseo Kim ⋅ Guido Dumont ⋅ Xinyu Gao ⋅ Gang Chen ⋅ Holger Caesar ⋅ Javier Alonso-Mora  
   [arXiv:2511.16949](https://arxiv.org/abs/2511.16949)
51. **MobileSAM2: Lightweight Segment Anything in Images and Videos via Hypergraphical Knowledge Distillation**  
   Kai Jiang ⋅ Jiaxing Huang ⋅ Jingyi Zhang ⋅ Weiying Xie ⋅ Yunsong Li ⋅ Yufei Wang ⋅ Aoran Xiao ⋅ Dacheng Tao
52. **MobileVLA-R1: Reinforcing Vision-Language-Action for Mobile Robots**  
   Ting Huang ⋅ Dongjian Li ⋅ Rui Yang ⋅ Zeyu Zhang ⋅ ZIDA YANG ⋅ Hao Tang  
   [arXiv:2511.17889](https://arxiv.org/abs/2511.17889) · [code](https://github.com/AIGeeksGroup/MobileVLA-R1) · [project](https://aigeeksgroup.github.io/MobileVLA-R1)
53. **MoE-KD: Your Teacher Model is Worth Mixture-of-Experts for Knowledge Distillation**  
   Kuo Shi ⋅ Wenjie Zhu ⋅ Bo Peng
54. **MoE-ViE: Mixture of Experts Vision Encoder for Efficient Image and Video Understanding**  
   Bonan Zhang ⋅ Shiyu Dong ⋅ Quan Tran ⋅ Katharina Gschwind ⋅ Shuqi Yang ⋅ Sijia Chen ⋅ Adel Ahmadyan ⋅ Seungwhan Moon ⋅ Lu Zhang ⋅ Ahmed Kirmani ⋅ Babak Damavandi ⋅ Anuj Kumar
55. **Multi-Scale Representation Alignment for Visual Autoregressive Modeling with Mixture of Experts**  
   Nuoyan Zhou ⋅ Zhijun Tu ⋅ Lei Yu ⋅ Kun Cheng ⋅ jie hu ⋅ Nannan Wang ⋅ Xinghao Chen  
   [arXiv:2607.00371](https://arxiv.org/abs/2607.00371)
56. **MVPruner: Dynamic Token Pruning for Accelerating Multi-view Vision-Language Models in Autonomous Driving**  
   Nan Yang ⋅ Zhanwen Liu ⋅ Linfeng Zhang ⋅ Shangyu Xie ⋅ Yang Wang ⋅ Wenzhuo Zhou ⋅ Xiangmo Zhao  
   [arXiv:2606.27660](https://arxiv.org/abs/2606.27660)
57. **NanoVSR: Towards Real-Time Video Super-Resolution on Edge Devices**  
   Filip Pawlicki ⋅ Marcel Kańduła ⋅ Marcin Pucek ⋅ Kamil Dobies  
   [arXiv:2607.10495](https://arxiv.org/abs/2607.10495) · [code](https://github.com/filippawlicki/nanovsr)
58. **OVGGT: O(1) Constant-Cost Streaming Visual Geometry Transformer**  
   Si-yu Lu ⋅ Po-Ting Chen ⋅ Hui-Che Hsu ⋅ Sin-Ye Jhong ⋅ Wen-Huang Cheng ⋅ Yung-Yao Chen  
   [arXiv:2603.05959](https://arxiv.org/abs/2603.05959) · [code](https://github.com/VAISR/OVGGT) · [project](https://vaisr.github.io/OVGGT/)
59. **Pathryoshka: Compressing Pathology Foundation Models via Multi-Teacher Knowledge Distillation with Nested Embeddings**  
   Christian Grashei ⋅ Christian Brechenmacher ⋅ Rao Umer ⋅ Jingsong Liu ⋅ Carsten Marr ⋅ Peter Schüffler ⋅ Ewa Szczurek  
   [arXiv:2511.23204](https://arxiv.org/abs/2511.23204)
60. **Perceptual Projection Pruning: Diversity-Aware Video Token Pruning for Multimodal Large Language Models**  
   Zhuangqiu Huang ⋅ Minxin Lai ⋅ Shuo Liu ⋅ Yu Zhang ⋅ Jiaqi Wang
61. **Point Ladder Tuning: Parameter-Efficient Hierarchical Adaptation for 3D Point Cloud Understanding**  
   Junlin Chang ⋅ Longhao Zou ⋅ Rui Li  
   [arXiv:2607.19171](https://arxiv.org/abs/2607.19171) · [code](https://github.com/JunLinChang/ECCV2026-PLT)
62. **Preventing Expert Collapse in MoE-dVLMs via Modality-Wise Norm Alignment**  
   Zongkai Liu ⋅ Zhen Cao ⋅ Hui Zhang ⋅ Chao Yu ⋅ liqiang niu ⋅ Fandong Meng
63. **Prune Once: Retraining-Free Task-Agnostic Pruning for Vision-Language Models**  
   Kang MinSeok ⋅ Hyunwoo Kim ⋅ Chanyoung Kim ⋅ Minwoo Kim ⋅ Jaekoo Lee ⋅ Dahuin Jung  
   [arXiv:2608.06901](https://arxiv.org/abs/2608.06901) · [code](https://github.com/cau-hai-lab/PORTA.git)
64. **QuantV2X: A Fully Quantized Multi-Agent System for Cooperative Perception**  
   Seth Zhao ⋅ Huizhi Zhang ⋅ Zhaowei Li ⋅ Juntong Peng ⋅ Anthony Chui ⋅ Zewei Zhou ⋅ Zonglin Zonglin ⋅ Hao Xiang ⋅ Zhiyu Huang ⋅ Fujia Wang ⋅ Ran Tian ⋅ Chenfeng Xu ⋅ Bolei Zhou ⋅ Jiaqi Ma  
   [arXiv:2509.03704](https://arxiv.org/abs/2509.03704) · [code](https://github.com/ucla-mobility/QuantV2X)
65. **Rapidly Deploying On-Device Eye Tracking by Distilling Visual Foundation Models**  
   Cheng Jiang ⋅ Jogendra Nath Kundu ⋅ David Colmenares ⋅ Fengting Yang ⋅ Joseph Robinson ⋅ Yatong An ⋅ Ali Behrooz  
   [arXiv:2604.02509](https://arxiv.org/abs/2604.02509)
66. **REDistill: Robust Estimator Distillation for Balancing Robustness and Efficiency**  
   Ondrej Tybl ⋅ Lukas Neumann  
   [arXiv:2602.04677](https://arxiv.org/abs/2602.04677)
67. **REFINE: Super-efficient Pruning for 3D Gaussian Splatting via Rendering-Free Primitive Importance**  
   Zhang Chen ⋅ Shuai Wan ⋅ MengtingYu MengtingYu ⋅ Fuzheng Yang ⋅ Junhui Hou
68. **ResilPhase: Plug-and-Play Phase Mapping and Noise-Resilient Macro-Trajectory Extrapolation for Diffusion Acceleration**  
   Qicheng Zhao ⋅ Yu Li ⋅ Qi Sun ⋅ Zheyu Yan  
   [arXiv:2606.26769](https://arxiv.org/abs/2606.26769)
69. **Rethinking Token Reduction for Diffusion Models via Output-Similarity-Awareness**  
   Hangyeol Lee ⋅ Hyojeong Lee ⋅ Joo-Young Kim  
   [arXiv:2605.22011](https://arxiv.org/abs/2605.22011)
70. **RhymeFlow: Training Free Acceleration for Video Generation with Asynchronous Denoising Flow Scheduling**  
   Chensheng Dai ⋅ Shengjun Zhang ⋅ Yifan Li ⋅ Zhang Zhang ⋅ Zheng Zhu ⋅ Yueqi Duan  
   [arXiv:2606.06309](https://arxiv.org/abs/2606.06309) · [code](https://github.com/Simon-Dcs/RhymeFlow) · [project](https://simon-dcs.github.io/Website-of-RhymeFlow/)
71. **Robust Trajectory Distillation: Hybrid Reweighting Meets Teacher-Inspired Targets**  
   KaifengChen KaifengChen ⋅ Lechao Cheng ⋅ Jiyang Li ⋅ Shengeng Tang ⋅ FanZhang FanZhang ⋅ Yantao Pan ⋅ Yaxiong Wang ⋅ Tianrui Hui ⋅ Zhun Zhong  
   [arXiv:2606.29837](https://arxiv.org/abs/2606.29837)
72. **RotateAttention : RoPE-Aware Rotation and Range Rectification for INT4 Quantized Attention in Video Generation**  
   Yaofu LIU ⋅ Wangli Lan ⋅ Jinxi Li ⋅ Binhang Yuan ⋅ Harry Yang  
   [arXiv:2607.02584](https://arxiv.org/abs/2607.02584)
73. **SAFE-Pruner: Semantic Attention–Guided Future-Aware Token Pruning for Efficient Vision-Language-Action Manipulation**  
   Shilin Ma ⋅ Chubin Zhang ⋅ Changyuan Wang ⋅ Yuji Wang ⋅ Yue Wu ⋅ Zixuan Wang ⋅ Jingqi Tian ⋅ Zheng Zhu ⋅ Yansong Tang
74. **SAM+D: Parameter-Efficient Dimensional Lifting of SAM-Family Models via Depth-Routed LoRA and Depth Shifting**  
   YU SONG ⋅ Hao Sun ⋅ TENG SHIYU ⋅ Ikuko Nishikawa ⋅ Yen-wei Chen  
   [arXiv:2607.29033](https://arxiv.org/abs/2607.29033) · [code](https://github.com/JerrySongCST/SAM-Plus-D)
75. **SD3.5-Flash: Distribution-Guided Distillation of Generative Flows**  
   Hmrishav Bandyopadhyay ⋅ Rahim Entezari ⋅ Jim Scott ⋅ Reshinth Adithyan ⋅ Yi-Zhe Song ⋅ Varun Jampani
76. **Seeing Fast and Slow: Learning the Flow of Time in Videos**  
   Yen-Siang Wu ⋅ Rundong Luo ⋅ Jingsen Zhu ⋅ Tao Tu ⋅ Ali Farhadi ⋅ Matthew Wallingford ⋅ Yu-Chiang Frank Wang ⋅ Steve Marschner ⋅ Wei-Chiu Ma  
   [arXiv:2604.21931](https://arxiv.org/abs/2604.21931) · [project](https://seeing-fast-and-slow.github.io/)
77. **SFKD: Spatial–Frequency Joint-Aware Heterogeneous Knowledge Distillation via Multi-Level Wavelet Spectral Interaction**  
   Cuipeng Wang ⋅ Haipeng Wang  
   [arXiv:2607.01906](https://arxiv.org/abs/2607.01906)
78. **SIMPLER: Efficient Foundation Model Adaptation via Similarity-Guided Layer Pruning for Earth Observation**  
   Víctor Barreiro ⋅ Johannes Jakubik ⋅ Francisco Argüello ⋅ Dora Heras
79. **Sink-Token-Aware Pruning for Fine-Grained Video Understanding in Efficient Video LLMs**  
   Kibum Kim ⋅ Jiwan Kim ⋅ Kyle Min ⋅ Yueqi Wang ⋅ Jinyoung Moon ⋅ Julian McAuley ⋅ Chanyoung Park  
   [arXiv:2604.20937](https://arxiv.org/abs/2604.20937)
80. **SMART: When is it Actually Worth Expanding a Speculative Tree?**  
   Lifu Wang ⋅ Pan ZHOU
81. **SpaR3D-MoE: Adaptive 3D Spatial Reasoning from Sparse Views Meets Geometry-Inductive Mixture-of-Experts**  
   Haida Feng ⋅ Hao Wei ⋅ Haolin Wang ⋅ Shiwei Li ⋅ Chade Li ⋅ Yihong Wu  
   [arXiv:2607.06620](https://arxiv.org/abs/2607.06620)
82. **Sparse-Aware Vector Quantization for Bandwidth-Efficient Collaborative 3D Semantic Occupancy Prediction**  
   Feng Li ⋅ Chaokun Zhang ⋅ Gong Chen  
   [arXiv:2607.01928](https://arxiv.org/abs/2607.01928)
83. **SpecEyes: Accelerating Agentic Multimodal LLM via Speculative Planning and Perception**  
   Haoyu Huang ⋅ Jinfa Huang ⋅ Zhongwei Wan ⋅ Xiawu Zheng ⋅ Rongrong Ji ⋅ Jiebo Luo
84. **Structured Hyperedge Adaptation for Parameter-Efficient Fine-Tuning of Vision Transformers**  
   Edwin Kwadwo Tenagyei ⋅ Lei Wang ⋅ Ugochukwu Akpudo ⋅ Jun Zhou ⋅ Yongsheng Gao  
   [arXiv:2606.22383](https://arxiv.org/abs/2606.22383)
85. **Structured Redundancy Modeling for Efficient Visual Token Pruning in High-Resolution MLLMs**  
   Jouwon Song ⋅ Woohyeong Kim ⋅ Kyeongbo Kong  
   [arXiv:2607.23046](https://arxiv.org/abs/2607.23046)
86. **SurvMILKD: A Weakly Supervised Survival Analysis Framework for Multi-Teacher Knowledge Distillation using Pathology Foundation Models**  
   Mayur Mallya ⋅ Ali Khajegili Mirabadi ⋅ Hossein Farahani ⋅ Ali Bashashati
87. **SWIFT: Spatial-Window Integrated Frequency-aware Token Pruning for Efficient MLLMs on Edge Devices**  
   Guanglai Liu ⋅ Jubo Chen ⋅ Xiaosheng Yu
88. **Symbiotic-MoE: Unlocking the Synergy between Generation and Understanding**  
   Xiangyue Liu ⋅ Zijian Zhang ⋅ Miles Yang ⋅ Zhao Zhong ⋅ Liefeng Bo ⋅ Ping Tan  
   [arXiv:2604.07753](https://arxiv.org/abs/2604.07753)
89. **TextDS: Parameter-Efficient Representation Alignment for Scene Text Detection under Distribution Shifts**  
   Boyuan Chen ⋅ Zichen Dang ⋅ Chuang Yang ⋅ Lap-Pui Chau ⋅ Yi Wang  
   [arXiv:2606.28077](https://arxiv.org/abs/2606.28077) · [code](https://github.com/ZChenDang/TextDS)
90. **The Label Imitation Game: Turing Test Network for Zero-Shot Pseudo-Label Pruning**  
   Brent Griffin ⋅ Jason Corso  
   [arXiv:2606.30875](https://arxiv.org/abs/2606.30875) · [code](https://github.com/voxel51/ttn)
91. **TinyHistory: Lightweight Video History Embeddings via Two-Stage Context Learning**  
   lvmin zhang ⋅ Shengqu Cai ⋅ Muyang Li ⋅ Chong Zeng ⋅ Beijia Lu ⋅ Anyi Rao ⋅ Song Han ⋅ Gordon Wetzstein ⋅ Maneesh Agrawala  
   [arXiv:2512.23851](https://arxiv.org/abs/2512.23851) · [project](https://lllyasviel.github.io/TinyHistory_gitpage/)
92. **Token-level Response-visual Attention Guidance for Multimodal LLMs Knowledge Distillation**  
   Jaehyun Jang ⋅ Eunseop Yoon ⋅ Hee Suk Yoon ⋅ SooHwan Eom ⋅ Mark Hasegawa-Johnson ⋅ Chang Yoo  
   [arXiv:2607.02593](https://arxiv.org/abs/2607.02593)
93. **Towards Memory-Efficient Autoregressive Video Generation via Instance-Specific Parametric Absorption**  
   Xiaomeng Fu ⋅ Jia Li ⋅ Yiming Hu ⋅ Yong Wang ⋅ Hayden So ⋅ Jiao Dai ⋅ Xiangxiang Chu ⋅ Jizhong Han  
   [arXiv:2607.00712](https://arxiv.org/abs/2607.00712)
94. **TR-MoE: Temporal Reliability-Aware Mixture-of-Experts for Robust Tracking**  
   Tianle Wang ⋅ Xiangyang Yang ⋅ Jihua Zhu ⋅ Binrui Liu ⋅ Yanzhao Li ⋅ Shuiwang Li
95. **UltraViT: Latency-Optimized On-device Vision Encoder for Large Vision-Language Models**  
   Ioannis Maniadis Metaxas ⋅ Adrian Bulat ⋅ Alberto Baldrati ⋅ Anestis Zaganidis ⋅ Yassine Ouali ⋅ Hyeonuk Kim ⋅ Georgios Tzimiropoulos  
   [arXiv:2607.23373](https://arxiv.org/abs/2607.23373)
96. **Unifying CNNs and ViTs for Learning-Efficient and Scalable Variational AutoEncoder**  
   Zhiying Lu ⋅ Shang Chai ⋅ Chuanbin Liu ⋅ Litong Gong ⋅ Pandeng Li ⋅ Tiezheng Ge ⋅ Hongtao Xie
97. **ViQ: Text-Aligned Visual Quantized Representations at Any Resolution**  
   Xumin Yu ⋅ ZUYAN LIU ⋅ Zhenyu Yang ⋅ Yuhao Dong ⋅ Shengsheng Qian ⋅ Jiwen Lu ⋅ Han Hu ⋅ Yongming Rao  
   [arXiv:2606.27313](https://arxiv.org/abs/2606.27313)
98. **VQT: Vector Quantization Tuning for Efficient Fine-tuning and Compression of Pre-trained Vision Transformers**  
   Yinglong Li ⋅ jiyuan Xia ⋅ Jingcheng Xie ⋅ Zhiwei Xiong
99. **WebEyeTrack: Scalable Eye-Tracking for the Browser via On-Device Few-Shot Personalization**  
   Eduardo Davalos ⋅ Yike Zhang ⋅ Namrata Srivastava ⋅ Yashvitha Thatigotla ⋅ Ashwin T S ⋅ Jorge Salas ⋅ Sun-Joo Cho ⋅ Amanda Goodwin ⋅ Gautam Biswas  
   [arXiv:2508.19544](https://arxiv.org/abs/2508.19544) · [code](https://github.com/RedForestAi/WebEyeTrack)
100. **When Distillation Breaks Motion Control: Restoring Generative Trajectories for Fast Video Generators**  
   Jintao Rong ⋅ Xin Xie ⋅ Xinyi Yu ⋅ Linlin Ou ⋅ Xinyu Zhang ⋅ Chunhua Shen ⋅ Dong Gong  
   [arXiv:2506.19348](https://arxiv.org/abs/2506.19348) · [project](https://euminds.github.io/motionecho/)
101. **When Token Compression Breaks: Structural Pruning vs. Token Reduction for Robust ViT Segmentation under High Compression**  
   Tien-Phat Nguyen ⋅ Ngai-Man Cheung  
   [arXiv:2607.02237](https://arxiv.org/abs/2607.02237) · [code](https://github.com/phatnguyencs/vit-seg-compression)
102. **Which Layer Causes Distribution Deviation? Entropy-Guided Adaptive Pruning for Diffusion and Flow Models**  
   Changlin Li ⋅ Jiawei Zhang ⋅ Zeyi Shi ⋅ Zhihui Li ⋅ Xiaojun Chang  
   [arXiv:2511.21122](https://arxiv.org/abs/2511.21122) · [code](https://github.com/changlin31/EntPruner)
103. **Zero-Shot Quantization for Object Detectors using Off-the-Shelf Generative Models**  
   Hyunho Lee ⋅ Kyomin Hwang ⋅ Hyeonjin Kim ⋅ Suyoung Kim ⋅ Sunghyun Wee ⋅ Nojun Kwak  
   [arXiv:2606.31456](https://arxiv.org/abs/2606.31456)

## Trustworthy AI: Safety, Adversarial & Privacy

*89 papers · 44 with links*

1. **AracNet: Revealing Debiasing Signals across Layers with Shallow Monitors**  
   Vito Paolo Pastore ⋅ Massimiliano Ciranni ⋅ Enzo Tartaglione ⋅ Vittorio Murino
2. **Attention Misses Visual Risk: Risk-Adaptive Steering for Multimodal Safety Alignment**  
   Jonghyun Park ⋅ Minhyuk Seo ⋅ Chaewon YEO ⋅ Jonghyun Choi  
   [arXiv:2510.13698](https://arxiv.org/abs/2510.13698)
3. **Beyond Artifacts: Real-Centric Envelope Modeling for Reliable AI-Generated Image Detection**  
   Ruiqi Liu ⋅ Yi Han ⋅ Zhengbo Zhang ⋅ Liwei Yao ⋅ Zhiyuan Yan ⋅ Jialiang Shen ⋅ ZhiJin Chen ⋅ Manni Cui ⋅ Boyi Sun ⋅ Lubin Weng ⋅ Jing Dong ⋅ Yan Wang ⋅ Shu Wu
4. **BiSLW: Bi-Spectral Latent Watermarking for Generative Diffusion Models**  
   Aryan Pandit  
   [arXiv:2607.02643](https://arxiv.org/abs/2607.02643)
5. **Breaking Rigidity in Adversarial Patch Attacks**  
   Vishesh Kumar ⋅ Guha Balakrishnan ⋅ Akshay Agarwal
6. **Can Vision Models Truly Forget? Mirage: Representation-Level Certification of Visual Unlearning**  
   Zhenyu Yu ⋅ yangchen zeng ⋅ Chunlei Meng ⋅ Guangzhen Yao ⋅ Shuigeng Zhou
7. **Causal Intervention in Concept Bottleneck Models**  
   Zhiyu Zhu ⋅ Jiayu Zhang ⋅ Zhibo Jin ⋅ Xinyi Wang ⋅ Fang Chen ⋅ Przemyslaw Biecek ⋅ Jianlong Zhou
8. **CausalVAE as a Plug-in for World Models: Towards Reliable Counterfactual Dynamics**  
   Ziyi Ding ⋅ xianxin lai ⋅ Weiyu Chen ⋅ Xiao-Ping Zhang ⋅ Jiayu Chen  
   [arXiv:2604.07712](https://arxiv.org/abs/2604.07712)
9. **Code-in-the-Loop Forensics: Agentic Tool Use for Image Forgery Detection**  
   Fanrui Zhang ⋅ Qiang Zhang ⋅ Sizhuo Zhou ⋅ Jianwen Sun ⋅ Chuanhao Li ⋅ Jiaxin Ai ⋅ Yukang Feng ⋅ Yujie Zhang ⋅ Wenjie Li ⋅ Zizhen Li ⋅ Yifan Chang ⋅ Jiawei Liu ⋅ Kaipeng Zhang  
   [arXiv:2512.16300](https://arxiv.org/abs/2512.16300)
10. **CogniCred: A Dataset and Benchmark for Cognitive Credential Forgery Detection**  
   Junchi Li ⋅ Jiasheng Sun ⋅ Weizhi Chen ⋅ Ziwei Wang ⋅ Sheng Zhou ⋅ Jiajun Bu ⋅ Chenfan Qu ⋅ Bohan Yu ⋅ Jian liu ⋅ Weiqiang Wang
11. **Contextual Image Attack: How Visual Context Exposes Multimodal Safety Vulnerabilities**  
   Yuan Xiong ⋅ Miao Ziqi ⋅ Lijun Li ⋅ Chen Qian ⋅ Jie Li ⋅ Jing Shao  
   [arXiv:2512.02973](https://arxiv.org/abs/2512.02973)
12. **Continuous Adversarial Flow Models**  
   Shanchuan Lin ⋅ Ceyuan Yang ⋅ Zhijie Lin ⋅ Hao Chen ⋅ Haoqi Fan  
   [arXiv:2604.11521](https://arxiv.org/abs/2604.11521)
13. **COVERT: Privacy-Preserving Covariant Obfuscation for VLMaaS via Exact Reparameterization and Tailored Tuning**  
   Wenqiang Ruan ⋅ ZiRui Huang ⋅ Yu Lin ⋅ Qizhi Zhang ⋅ Yunlong Mao ⋅ Quanwei Cai ⋅ Jue Hong ⋅ Sheng Zhong ⋅ Ye Wu
14. **Cross-View Yaw Estimation in Location Uncertainty with Line-Aligning Yaw Scoring**  
   Taeho Kang ⋅ Nairan Zhang ⋅ Yelin Kim ⋅ Yujiao Shi ⋅ Youngki Lee  
   [arXiv:2606.22094](https://arxiv.org/abs/2606.22094)
15. **Data-Free Client Contribution Estimation via Logit Maximization for Federated Learning**  
   Asim Ukaye ⋅ Nurbek Tastan ⋅ Mubarak Abdu-Aguye ⋅ Karthik Nandakumar  
   [arXiv:2605.18892](https://arxiv.org/abs/2605.18892)
16. **DiffUE: Enhancing Utility-Unlearnability Trade-off of Unlearnable Examples via Diffusion Autoencoders**  
   Syed Irfan Ali Meerza ⋅ Oktay Ozturk ⋅ Amir Sadovnik ⋅ Jian Liu  
   [arXiv:2607.10580](https://arxiv.org/abs/2607.10580)
17. **Diffusion to Obfuscation: Time-Adaptive Synthesized Generation Against Gradient Leakage Attacks in Federated Learning**  
   Farchan Raswa ⋅ Chun-Shien Lu ⋅ Jia-Ching Wang
18. **Disentangling Hallucinations: Orthogonal Semantic Projection for Robust Interpretability**  
   Emirhan Bilgiç ⋅ Baptiste Caramiaux ⋅ Zhi Yan ⋅ Gianni Franchi  
   [arXiv:2606.14758](https://arxiv.org/abs/2606.14758) · [code](https://github.com/emirhanbilgic/Orthogonal-Semantic-Projection)
19. **Don’t Teach Instability, Teach Robustness: Selective Sensitivity Gating for Adversarial Robust Distillation**  
   Jingqi Ji ⋅ Quan Kong ⋅ Chaojie Gu ⋅ Yuanchao Shu ⋅ Cong Wang
20. **EraseSAE: Surgical Concept Erasure in Text-to-Video Diffusion Models via Sparse Autoencoders**  
   Xinghao Wang ⋅ Dong Li ⋅ Wei Yu ⋅ Yingwei Pan ⋅ Tao Gong ⋅ Qi Chu ⋅ Nenghai Yu ⋅ Ting Yao
21. **Evaluating the Interpretability of Sparse Autoencoders with Concept Annotations**  
   Jonas Klotz ⋅ Cassio F. Dantas ⋅ Pallavi Jain ⋅ Diego Marcos ⋅ Begüm Demir  
   [arXiv:2606.24716](https://arxiv.org/abs/2606.24716) · [code](https://github.com/JonasKlotz/sae-concept-eval)
22. **Evidence Triangulation for Multimodal Fact-Checking in the Wild**  
   Stefanos-Iordanis Papadopoulos ⋅ Zacharias Chrysidis ⋅ Christos Koutlis ⋅ Symeon Papadopoulos ⋅ Panagiotis Petrantonakis  
   [arXiv:2606.31367](https://arxiv.org/abs/2606.31367) · [code](https://github.com/stevejpapad/evidence-triangulation)
23. **Explainability-aware Frustum Attack: Exposing Structural Vulnerabilities in LiDAR-Based 3D Object Detectors**  
   Chengzeng You ⋅ Binbin Xu ⋅ Soteris Demetriou  
   [arXiv:2606.29963](https://arxiv.org/abs/2606.29963) · [code](https://github.com/SecMindLab/Saliency_LiDAR)
24. **FedDO: Dynamic Client Optimization for Adaptive Federated Learning**  
   Peixuan Tang ⋅ Xuehe Wang
25. **FedLAS: Feature-Modulated Bidirectional Label Smoothing for Neural Network Calibration**  
   Thiru Thillai Nadarasar Bahavan ⋅ Sachith Seneviratne ⋅ Saman Halgamuge  
   [arXiv:2606.28654](https://arxiv.org/abs/2606.28654)
26. **FedMental: Topology-Aware Federated Prototype Learning for Polymorphic Multimodal Psychiatry**  
   Haoyu Li ⋅ He Li ⋅ Wenke Huang ⋅ Yujing Rao ⋅ Xiaofen Zong ⋅ Mang Ye
27. **FedNASP: Federated Vision-Language Navigation with Adaptive Step-wise Personalization**  
   Qingqian Yang ⋅ Hao Wang ⋅ Sai Qian Zhang ⋅ Jian Li ⋅ Yang Hua ⋅ Miao Pan ⋅ Tao Song ⋅ Zhengwei Qi ⋅ Haibing Guan
28. **FedOT: Ownership Verification and Leakage Tracing via Watermarks for Federated LDMs**  
   Wenlong Cheng ⋅ Yuan Gan ⋅ Yunqiu Xu ⋅ Jiaxu Miao  
   [arXiv:2606.22875](https://arxiv.org/abs/2606.22875) · [project](https://spyzixuan.github.io/FedOT/)
29. **ForeSea: AI Forensic Search with Multi-modal Queries for Video Surveillance**  
   Hyojin Park ⋅ Yi Li ⋅ Janghoon Cho ⋅ Sungha Choi ⋅ Jungsoo Lee ⋅ TAOTAO JING ⋅ shuai zhang ⋅ Munawar Hayat ⋅ Dashan Gao ⋅ Ning Bi ⋅ Fatih Porikli  
   [arXiv:2603.22872](https://arxiv.org/abs/2603.22872)
30. **General Self-Calibration with Varying Intrinsics**  
   Norio Kosaka ⋅ Timothy Duff ⋅ Tomas Pajdla ⋅ Akihiro Sugimoto
31. **Gradient sparsity regularization for training unlearning-compatible models**  
   Sobhan Hemati ⋅ Soufiane Lamghari ⋅ Masoud Asgharian ⋅ Xu Li ⋅ Hongliang Li
32. **H-SFP: Hierarchical Federated Learning with Decoupled Split-Model Prototyping**  
   Trung-Dung Tran ⋅ Nguyen Ha ⋅ Minh-Duong Nguyen ⋅ Van-Dinh Nguyen ⋅ Kok-Seng Wong
33. **HVGCD:Rethinking Generalized Category Discovery through Hypothesis–Verification**  
   zhang baoqiang ⋅ Kunze Huang ⋅ Luyao Tang ⋅ Xiaotong Tu
34. **Improving Adversarial Robustness by Mitigating Instability through Relearning**  
   Yi Zeng ⋅ Ling Zhou ⋅ Ruilong Yu ⋅ Qihe Liu ⋅ Shijie Zhou
35. **Improving Adversarial Robustness via Activation Amplification and Attenuation**  
   Taïga Gonçalves ⋅ Yongsong Huang ⋅ Tomo Miyazaki ⋅ Shinichiro Omachi  
   [arXiv:2606.27784](https://arxiv.org/abs/2606.27784) · [code](https://github.com/tgoncalv/A3)
36. **Indelible Backdoors: On the Limits of Post-Training Defenses**  
   Jingyi Guo ⋅ Thuy Dung Nguyen ⋅ Taylor T Johnson ⋅ Kevin Leach
37. **IoUCert: Robustness Verification for Anchor-based Object Detectors**  
   Benedikt Brückner ⋅ Alejandro J. Mercado ⋅ Yanghao Zhang ⋅ Panagiotis Kouvaros ⋅ Alessio Lomuscio  
   [arXiv:2603.03043](https://arxiv.org/abs/2603.03043)
38. **Learn to Rank: Visual Attribution by Learning Importance Ranking**  
   David Schinagl ⋅ Christian Fruhwirth-Reisinger ⋅ Alexander Prutsch ⋅ Samuel Schulter ⋅ Horst Possegger  
   [arXiv:2604.05819](https://arxiv.org/abs/2604.05819)
39. **Learning from Adversity: Semantic-Aware Mask Refinement through Adversarial Perturbation**  
   Beom Young Kim ⋅ Sung Hwang  
   [arXiv:2607.29059](https://arxiv.org/abs/2607.29059) · [project](https://phoenix-eccv26.github.io)
40. **Learning with Bilevel-Minimax Optimization for Efficient and Reliable Transfer Attacks**  
   Yaohua Liu ⋅ Yifan Guo ⋅ Jiaxin Gao  
   [arXiv:2608.11815](https://arxiv.org/abs/2608.11815) · [code](https://github.com/callous-youth/BMAT)
41. **LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models**  
   Rongxu Cui ⋅ Zongzheng Zhang ⋅ Jingrui Pang ⋅ Haohan Chi ⋅ Jinbang Guo ⋅ Saining Zhang ⋅ shaoxuan Xie ⋅ Xin Jin ⋅ Yao Mu ⋅ Jiaolong Yang ⋅ Guocai Yao ⋅ Xianyuan Zhan ⋅ Ya-Qin Zhang ⋅ HAO ZHAO  
   [arXiv:2606.23686](https://arxiv.org/abs/2606.23686) · [project](https://libero-safety.github.io/)
42. **LINA: Learning INterventions Adaptively for Physical Alignment and Counterfactual Generation in Diffusion Models**  
   Shu Yu ⋅ Chaochao Lu
43. **Locality-Aware Continual Unlearning for Diffusion Models**  
   Naveen George ⋅ Naoki Murata ⋅ Yuhta Takida ⋅ Konda Reddy Mopuri ⋅ Yuki Mitsufuji  
   [arXiv:2512.02657](https://arxiv.org/abs/2512.02657)
44. **Look But Don't Touch with Sparse Autoencoders for Unlearning in Diffusion Models**  
   Enrico Cassano ⋅ Riccardo Renzulli ⋅ Rayyan Ahmed ⋅ Stephan Alaniz ⋅ Marco Grangetto
45. **Looking Back and Forth: Cross-Image Attention Calibration and Attentive Preference Learning for Multi-Image Hallucination Mitigation**  
   Xiaochen Yang ⋅ Hao Fang ⋅ Jiawei Kong ⋅ Yaoxin Mao ⋅ Bin Chen ⋅ Shu-Tao Xia  
   [arXiv:2603.07048](https://arxiv.org/abs/2603.07048)
46. **Mitigating Radar-Inertial Calibration Ambiguities via SO(3) Manifold Steering**  
   Chunshen Li ⋅ Shengpeng Wang ⋅ Zitao Ye ⋅ Wei Wang
47. **NeuralDMD: Interpretable Untrained Neural Network for Imaging from Sparse and Noisy Observations**  
   Ali SaraerToosi ⋅ Renbo Tu ⋅ Esther Lin ⋅ Kamyar Azizzadenesheli ⋅ Aviad Levis
48. **No Place to Hide: Benchmarking Video Hallucination with Background-Controlled Pairs**  
   Haojian Huang ⋅ Harold Haodong Chen ⋅ Meng Luo ⋅ Junjia Du ⋅ Shanqing Xu ⋅ Ziheng Chen ⋅ Yanxiang Huang ⋅ Yinchuan Li ⋅ Yingcong Chen  
   [arXiv:2606.31933](https://arxiv.org/abs/2606.31933) · [project](https://jethrojames.github.io/VidPair-Halluc/)
49. **Obliviate: Erasing Concepts from Autoregressive Image Generation Models**  
   Hossein Shakibania ⋅ Jonas Henry Grebe ⋅ Tobias Braun ⋅ Ege Aktemur ⋅ Saleh Aslani ⋅ Mehmet Yiğit ⋅ Marcus Rohrbach  
   [arXiv:2606.28643](https://arxiv.org/abs/2606.28643)
50. **On the Faithfulness of Post-Hoc Concept Bottleneck Models**  
   Laines Schmalwasser ⋅ Jan Blunk ⋅ Niklas Penzel ⋅ Julia Niebling ⋅ Joachim Denzler  
   [arXiv:2606.30498](https://arxiv.org/abs/2606.30498)
51. **On the Plasticity Collapse in Continual Machine Unlearning**  
   Yingdan Shi ⋅ Xiang Xu ⋅ Kaize Ding ⋅ Alfred Hero ⋅ Ren Wang
52. **On the Reliability of Cue Conflict and Beyond**  
   Pum Jun Kim ⋅ Seung-Ah Lee ⋅ Seongho Park ⋅ Dongyoon Han ⋅ Jaejun Yoo  
   [arXiv:2603.10834](https://arxiv.org/abs/2603.10834)
53. **One Trap to Block Them All: Defending Encoder Stealing via Isotropic Uniformity**  
   YITONG SHI ⋅ Kang Wei ⋅ Fushuo Huo ⋅ Shuchi Wu ⋅ Chuan Ma
54. **ORBIT: Overcoming Hallucination Risks via Bi-manifold Interaction and Traction**  
   Zhehan Kan ⋅ Yanlin Liu ⋅ Xiaochen Yang ⋅ Hongyang Yu ⋅ Qingmin Liao ⋅ Wenming Yang
55. **OrthoEraser: Coupled-Neuron Orthogonal Projection for Concept Erasure**  
   Chuancheng Shi ⋅ Wenhua Wu ⋅ Fei Shen ⋅ Xiaogang Zhu ⋅ Kun Hu ⋅ Zhiyong Wang  
   [arXiv:2603.11493](https://arxiv.org/abs/2603.11493)
56. **Preserving Knowledge across Space and Time for Continual Video Deepfake Detection**  
   Taehoon Kim ⋅ Jongwook Choi ⋅ Heejae Jo ⋅ Byungmin Park ⋅ Jongwon Choi
57. **Prevention over Correction: Learning Aligned Representations in One-shot Federated Learning**  
   YongHoon Kang ⋅ Jee-Hyong LEE
58. **Proteus: Model Leakage-Induced Adversarial Attack in Federated Learning**  
   Junjie Shan ⋅ Yue Zhang ⋅ Ziqi Zhao ⋅ Ka Ho Chow
59. **ProtoMappingNet: Interpretable Hierarchical Prototypes through Relational Prototype Mappings**  
   Jaehun Park ⋅ Jongmin Lim ⋅ Soobin Cha ⋅ Kwangsu Kim
60. **Prototype Normalization: Optimizing Prototype Separation for Heterogeneous Federated Learning**  
   Daeyoung Choi ⋅ Jihwan Shin ⋅ Gyuejeong Lee
61. **Push–Pull Attentional Anchoring for Diffusion Concept Erasure**  
   Nattanat Chatthee ⋅ Tagon Sompong ⋅ Ekapol Chuangsuwanich ⋅ Supasorn Suwajanakorn
62. **Quantile‑Adaptive Temperature Scaling for Confidence Calibration**  
   Omprakash Chakraborty ⋅ Leo Fillioux ⋅ Ismail Ayed ⋅ Jose Dolz  
   [arXiv:2606.21749](https://arxiv.org/abs/2606.21749)
63. **R-ESC: Robustly Erasing Space Concepts via Stochastic Feature Remapping**  
   Kang Eun Jeon ⋅ Yunsung Kang ⋅ Do Kang ⋅ Tae-Young Lee ⋅ Gyeong-Moon Park ⋅ Jong Hwan Ko
64. **ReShift: Aha-Moment-Driven Reasoning-Level Backdoor Attacks on Vision–Language Models**  
   Zhihao Dou ⋅ Qinjian Zhao ⋅ Zhiqiang Gao ⋅ Sumon Biswas  
   [arXiv:2607.00361](https://arxiv.org/abs/2607.00361)
65. **Rethink Backdoor Robustness in Vision Transformers**  
   Yichuan Mo ⋅ Dongxian Wu ⋅ Yifei Wang ⋅ Yisen Wang
66. **Rethinking Detection Calibration: A Coordinate Perspective**  
   Juyong Lee ⋅ Seungjin Jung ⋅ Jungmin Lee ⋅ Sunju Lee ⋅ Jongwon Choi
67. **Rethinking Robust Adversarial Concept Erasure in Diffusion Models**  
   Qinghong Yin ⋅ Yu Tian ⋅ Heming Yang ⋅ Xiang Chen ⋅ Xianlin Zhang ⋅ Yue Ming ⋅ Xueming Li ⋅ Yue Zhang  
   [arXiv:2510.27285](https://arxiv.org/abs/2510.27285) · [code](https://github.com/Qhong-522/S-GRACE)
68. **REVEAL: Reasoning-Enhanced Forensic Evidence Analysis for Explainable AI-Generated Image Detection**  
   Huangsen Cao ⋅ Qin Mei ⋅ Zhiheng Li ⋅ Yuxi Li ⋅ Zhan Meng ⋅ Ying Zhang ⋅ Chen Li ⋅ Zhimeng Zhang ⋅ Xin Ding ⋅ Yongwei Wang ⋅ Jing LYU ⋅ Fei Wu
69. **Revisiting Deepfake Detection: BCNet for Robust Generalization Beyond Semantic Dependence**  
   Jian Yang ⋅ Shibo Yao ⋅ Renshuai Tao ⋅ Chuangchuang Tan ⋅ Yao Zhao
70. **Robustness Meets Uncertainty: Evidential Adversarial Training for Robust Selective Classification**  
   Nicolas Sournac ⋅ Ahmed Jmaa ⋅ Bertrand Braeckeveldt  
   [arXiv:2607.03075](https://arxiv.org/abs/2607.03075) · [code](https://github.com/NicolasSournac/Robustness_Meets_Uncertainty.EV-AT)
71. **RoME: Robust Mixture of Low-Rank Experts against Multiple Adversarial Perturbations**  
   Woo Jae Kim ⋅ Kyle Min ⋅ Suhyeon Ha ⋅ Joonsung Jeon ⋅ Sung-eui Yoon  
   [arXiv:2607.06109](https://arxiv.org/abs/2607.06109) · [code](https://github.com/wkim97/RoME)
72. **Seeing Through Circuits: Faithful Mechanistic Interpretability for Vision Transformers**  
   Nina Żukowska ⋅ Wolfgang Stammer ⋅ Bernt Schiele ⋅ Jonas Fischer  
   [arXiv:2604.14477](https://arxiv.org/abs/2604.14477)
73. **Seeing Through the Weights: Privacy Leakage in Scene Coordinate Regression**  
   Oleksii Nasypanyi ⋅ Jaemin Cho ⋅ Utku Ozbulak ⋅ Byungkon Kang ⋅ Francois Rameau  
   [arXiv:2606.31164](https://arxiv.org/abs/2606.31164) · [project](https://jaeminch0.github.io/seeing-through-the-weights-privacy-leakage-in-scene-coordinate-regression)
74. **Seeing to Ground: Visual Attention for Hallucination-Resilient MDLLMs**  
   Vishal Narnaware ⋅ Animesh Gupta ⋅ Kevin Zhai ⋅ Zhenyi Wang ⋅ Shah Mubarak  
   [arXiv:2603.25711](https://arxiv.org/abs/2603.25711)
75. **Self-Evolving Just-In-Time Memory for Proactive Embodied Safety**  
   Bingrui Sima ⋅ Lizhong Wang ⋅ Xiaoya Lu ⋅ Kun He ⋅ Xiao Yang  
   [arXiv:2607.16247](https://arxiv.org/abs/2607.16247) · [code](https://github.com/DyMessi/JIT-Memory)
76. **SPARC: Scalable Path-Specific Counterfactual Fairness via Causal Conditional Independence**  
   Bowei Tian ⋅ Yexiao He ⋅ Ziyao Wang ⋅ Meng Liu ⋅ Yongkai Wu ⋅ Ang Li  
   [arXiv:2412.04739](https://arxiv.org/abs/2412.04739)
77. **Spectral Gradient Orthogonalization Improves Differentially Private Training at Scale**  
   Sabari Shanmugam ⋅ Nick Barnes ⋅ Kerry Taylor
78. **SpecV: Specification Verification for Robust Unified Multimodal Evaluation**  
   Weihao Yu ⋅ Rongyao Fang ⋅ Yuxuan Cai ⋅ Linjiang Huang ⋅ Yuhuan Yang ⋅ Xianwei Zhuang ⋅ Junyang Lin ⋅ Yixuan Yuan ⋅ Shuai Bai
79. **SPQR: A Multi-Dimensional Benchmark for Safety Alignment under Benign Model Adaptation**  
   Mohammed Talha Alam ⋅ Nada Saadi ⋅ Fahad Shamshad ⋅ Nils Lukas ⋅ Karthik Nandakumar ⋅ Fakhri Karray ⋅ Samuele Poppi
80. **SRRA: Stable-Rank-Based Residual Adaptation for Generalizable Deepfake Detection**  
   Huakun Liu ⋅ Wenjie Li ⋅ Changsheng Xu
81. **Stealthy Multi-task Adversarial Attacks**  
   Jiacheng Guo ⋅ Tianyun Zhang ⋅ Lei Li ⋅ Haochen Yang ⋅ Hongkai Yu ⋅ Minghai Qin  
   [arXiv:2411.17936](https://arxiv.org/abs/2411.17936)
82. **Test-time Counterfactual Calibration for Hallucination-Resistant Temporal Grounding**  
   Chufan YI ⋅ Hongyu Qu ⋅ Shiyu Xuan ⋅ Rui Yan ⋅ Xiangbo Shu ⋅ Fang Zhao ⋅ Guosen Xie
83. **The 3D Mirage: Probing and Taming 3D Hallucinations**  
   Hoang Nguyen ⋅ Xiaohao Xu ⋅ Xiaonan Huang  
   [arXiv:2512.15423](https://arxiv.org/abs/2512.15423)
84. **The Path to Reconciling Quality and Safety Alignment in Text-to-Image Generation**  
   Shouwei Ruan ⋅ Zhenyu Wu ⋅ Yao Huang ⋅ Ruochen Zhang ⋅ Yitong Sun ⋅ Caixin Kang ⋅ Shiji Zhao ⋅ Weijun Qin ⋅ Jingzhi Li ⋅ Xingxing Wei
85. **TooBad: Backdoor Diffusion Models with Ultra-Low Poison Rate and Imperceptible Trigger**  
   Vu Truong ⋅ Long Bao Le  
   [arXiv:2606.23362](https://arxiv.org/abs/2606.23362)
86. **Towards Reliable Medical Large Vision-Language Models via Counterfactual Preference Optimization**  
   Xiaoguang Zhu ⋅ NaipengWang NaipengWang ⋅ Kartik Patwari ⋅ Lianlong Sun ⋅ Chen-Nee Chuah ⋅ ChengxinPang ChengxinPang
87. **Trustworthy Image Authentication using Forensic Knowledge Graphs**  
   Tai Nguyen ⋅ Matthew Stamm  
   [arXiv:2606.23917](https://arxiv.org/abs/2606.23917)
88. **Uncertainty-aware tree height change regression**  
   Max Gaber ⋅ Dimitri Gominski ⋅ Jaime Revenga ⋅ Stefan Oehmcke ⋅ Rasmus Fensholt ⋅ Martin Brandt  
   [arXiv:2607.00638](https://arxiv.org/abs/2607.00638)
89. **Unmasking-Time Visual Calibration for Hallucination Mitigation in Multimodal Discrete Diffusion Language Models**  
   Tian Qin ⋅ Junzhe Chen ⋅ Tianshu Zhang ⋅ Lijie Wen

## Datasets, Benchmarks & Evaluation

*36 papers · 26 with links*

1. **Benchmarking Dynamic Affective Reasoning: A Viewer-Centric Video Emotion Dataset**  
   Zhiyan Zhang ⋅ Peipei Song ⋅ Jinpeng Hu ⋅ Jingyang Jia ⋅ Xun Yang ⋅ Xiaojun Chang  
   [arXiv:2607.10238](https://arxiv.org/abs/2607.10238) · [code](https://github.com/Zhang-Zhiyan/DAR)
2. **CanoVerse: 3D Object Scalable Canonicalization and Dataset for Generation and Pose**  
   Li Jin ⋅ Yuchen Yang ⋅ Weikai Chen ⋅ Yujie Wang ⋅ Dehao Hao ⋅ Tanghui Jia ⋅ Yingda Yin ⋅ Zeyu HU ⋅ Runze Zhang ⋅ Keyang Luo ⋅ Li Yuan ⋅ Long Quan ⋅ Xin Wang ⋅ Xueying Qin  
   [arXiv:2603.07144](https://arxiv.org/abs/2603.07144) · [code](https://github.com/123321456-gif/Canoverse)
3. **Condensing Large-Scale Datasets Directly with Minimal Information Loss**  
   Xinyi Shang ⋅ Peng Sun ⋅ Bei Shi ⋅ Zixuan Wang ⋅ Tao Lin  
   [arXiv:2607.00916](https://arxiv.org/abs/2607.00916) · [code](https://github.com/LINs-lab/CIM)
4. **CVSBench: A Comprehensive Benchmark for Cross-view Spatial Reasoning and Dreaming**  
   ruixun liu ⋅ Lingyu Zhang ⋅ Lanxuan Xue ⋅ Kaiyu Li ⋅ Bowen Fu ⋅ Xiangyong Cao  
   [arXiv:2606.22476](https://arxiv.org/abs/2606.22476) · [code](https://huggingface.co/datasets/zlyzlyzly/CVSBench)
5. **Diagram-MMU: A Multi-Modal Benchmark for Scientific Diagrams**  
   Weihao Bo ⋅ Shan Zhang ⋅ Yanpeng Sun ⋅ Jie Liu ⋅ Yongke Yao ⋅ Jinhao Du ⋅ Wei He ⋅ KAI ZOU ⋅ Zechao Li ⋅ Jingdong Wang  
   [arXiv:2608.12262](https://arxiv.org/abs/2608.12262) · [project](https://vi-ocean.github.io/projects/diagram-mmu)
6. **DiCoBench: Benchmarking Multi-Image Fine-Grained Perception via Differential and Commonality Visual Cues**  
   Geng Li ⋅ Yuxin Peng  
   [arXiv:2606.26602](https://arxiv.org/abs/2606.26602) · [code](https://github.com/PKU-ICST-MIPL/DICO_Bench_ECCV2026)
7. **EatVid-Bench: A Multimodal Fine-Grained Eating Behavior Video Dataset**  
   Xiangpeng Zheng ⋅ Zhenbo Xu ⋅ Gong Huang ⋅ Zhu Li ⋅ Qinghong Yang
8. **Enhancing prompt-image alignment evaluations via cyclic mutual information maximization**  
   Xingran Liao ⋅ Duanyu Feng ⋅ Mingliang Zhou ⋅ Sam Kwong ⋅ Weisi Lin
9. **HART: High-Resolution Annotation-Free Reasoning Technique through a Closed-loop Framework**  
   Jiacheng Yang ⋅ Anqi Chen ⋅ Yunkai Dang ⋅ Qi Fan ⋅ Cong Wang ⋅ Wenbin Li ⋅ Feng Miao ⋅ Yang Gao  
   [arXiv:2602.23615](https://arxiv.org/abs/2602.23615)
10. **HCSU: A Dataset and Benchmark for Fine-Grained Historical Calligraphy Style Understanding**  
   Yinsheng Yao ⋅ Yan Liu ⋅ Chen Ye  
   [arXiv:2607.04147](https://arxiv.org/abs/2607.04147) · [code](https://huggingface.co/datasets/Tongji209/HCSU)
11. **IRIS: A Real-World Benchmark for Inverse Recovery and Identification of Physical Dynamic Systems from Monocular Video**  
   Rasul Khanbayov ⋅ Mohamed Rayan Barhdadi ⋅ Erchin Serpedin ⋅ HASAN KURBAN
12. **LARY: A Latent Action Representation Yielding Benchmark**  
   Dujun Nie ⋅ Fengjiao Chen ⋅ Jun Kuang ⋅ Qi Lv ⋅ Xiaoyu Li ⋅ Xuezhi Cao
13. **OmniFall: From Staged Through Synthetic to Wild, A Unified Multi-Domain Dataset for Robust Fall Detection**  
   David Schneider ⋅ Zdravko Marinov ⋅ Moritz Mistol ⋅ Zeyun Zhong ⋅ Alexander Jaus ⋅ Rodi Düger ⋅ Rafael Baur ⋅ M. Saquib Sarfraz ⋅ Rainer Stiefelhagen  
   [arXiv:2505.19889](https://arxiv.org/abs/2505.19889) · [project](https://hf.co/datasets/simplexsigil2/omnifall)
14. **OmniMapBench: Benchmarking Visual-Centric Reasoning on Diverse Map Documents**  
   Yang Chen ⋅ Yufan Shen ⋅ Yunwen Li ⋅ Minghao Liu ⋅ Tuney Tianyu ⋅ Bin Fu ⋅ Qunshu Lin ⋅ Zhi Yu ⋅ Botian Shi  
   [arXiv:2607.09068](https://arxiv.org/abs/2607.09068) · [code](https://github.com/SIGMME/OmniMapBench)
15. **OmniPoint: Universal Monocular Metric Pointcloud from Any Camera**  
   Botao Ye ⋅ Marc Pollefeys ⋅ Ming-Hsuan Yang ⋅ Abhijit Kundu
16. **PerceptionComp: A Video Benchmark for Complex Perception-Centric Reasoning**  
   Shaoxuan Li ⋅ Zhixuan Zhao ⋅ Hanze Deng ⋅ Zirun Ma ⋅ Shulin Tian ⋅ ZUYAN LIU ⋅ Yushi Hu ⋅ Haoning Wu ⋅ Yuhao Dong ⋅ Benlin Liu ⋅ Ziwei Liu ⋅ Ranjay Krishna  
   [arXiv:2603.26653](https://arxiv.org/abs/2603.26653) · [project](https://perceptioncomp.github.io)
17. **Q-REAL: Towards Naturalness and Distortion Evaluation for AI-Generated Content**  
   Shushi Wang ⋅ Zicheng Zhang ⋅ Chunyi Li ⋅ Wei Wang ⋅ Liya Ma ⋅ Xiaoyu Li ⋅ Fengjiao Chen ⋅ Xuezhi Cao ⋅ Guangtao Zhai ⋅ Xiaohong Liu
18. **RESOLVE: A Multi-Resolution and Multi-Modal Dataset for Roadside Cooperative Perception**  
   Shaozu Ding ⋅ Linan Song ⋅ Marco Vincenzi ⋅ Dajiang Suo
19. **Rethinking Reward Signals in Video GRPO: When Scores Become Targets**  
   Rui Li ⋅ Yuanzhi Liang ⋅ Ziqi Ni ⋅ Haibin Huang ⋅ Chi Zhang ⋅ Xuelong Li  
   [arXiv:2511.19356](https://arxiv.org/abs/2511.19356)
20. **Revisiting Scene Graph Generation from the Perspective of Detector-Conditioned Reachability**  
   Runfeng Qu ⋅ Pia Bideau ⋅ Ole Hall ⋅ Julie Ouerfelli-Ethier ⋅ Klaus Obermayer ⋅ Olaf Hellwich  
   [arXiv:2607.06176](https://arxiv.org/abs/2607.06176)
21. **Rosetum3D: A Large-Scale 3D Vision Dataset from Preharvest Roses**  
   Songyan Liu ⋅ Xipei Liu ⋅ Yujie Liu ⋅ Jiali Wu ⋅ Xiaofei Liu
22. **SciIR: A Large-scale Training Dataset and Benchmark for Scientific Image Reasoning Generation**  
   Zhiyuan Ma ⋅ Zhengfeng Shi ⋅ Yuning An ⋅ Peize Li ⋅ Jiabao Wei ⋅ Ruijie Li ⋅ Junhao Xiao ⋅ Jianjun Li ⋅ Bowen Zhou  
   [arXiv:2606.30124](https://arxiv.org/abs/2606.30124)
23. **SelfMOTR: Revisiting MOTR with Self-Generating Detection Priors**  
   Fabian Gülhan ⋅ Emil Mededovic ⋅ Yuli Wu ⋅ Johannes Stegmaier  
   [arXiv:2511.20279](https://arxiv.org/abs/2511.20279) · [project](https://medem23.github.io/SM)
24. **SP-TransientBench: A Real-Captured Single Photon Perception Benchmark**  
   Hongzhou Dong ⋅ Zili Zhang ⋅ Ziting Wen ⋅ Yiheng Qiang ⋅ Runrong Deng ⋅ Wenle Dong ⋅ Ziwen Jiang ⋅ Xinyang Li ⋅ Rui Lu ⋅ Shuoyao Sun ⋅ Wenyu Wang ⋅ Ziyi Xia ⋅ Haitao Zheng ⋅ Guodong Shi ⋅ Xiaoqiang Ren  
   [arXiv:2606.18952](https://arxiv.org/abs/2606.18952)
25. **StreamSpatial: A Benchmark and Framework for Streaming 3D Visual-Spatial Reasoning**  
   Junlin Xie ⋅ Keyang Zhong ⋅ Quanlong Zheng ⋅ Ruifei Zhang ⋅ Kuo Wang ⋅ Yanhao Zhang ⋅ Haonan Lu ⋅ Xiang Wan ⋅ Guanbin Li
26. **SVGEval: A Vision-Grounded Framework for Perceptual-Quality Benchmarking and Evaluation in Text-to-SVG Generation**  
   Yiming Wang ⋅ Ye Chen ⋅ Hanqi Chen ⋅ Bingbing Ni  
   [arXiv:2608.01977](https://arxiv.org/abs/2608.01977)
27. **Syn4D: A Multiview Synthetic 4D Dataset**  
   Zeren Jiang ⋅ Yushi Lan ⋅ Yihang Luo ⋅ Yufan Deng ⋅ Zihang Lai ⋅ Edgar Sucar ⋅ Christian Rupprecht ⋅ Iro Laina ⋅ Larlus Diane ⋅ Chuanxia Zheng ⋅ Andrea Vedaldi  
   [arXiv:2605.05207](https://arxiv.org/abs/2605.05207) · [project](https://jzr99.github.io/Syn4D/)
28. **The Telephone Game: Evaluating Semantic Drift in Unified Models**  
   Sabbir Mollah ⋅ Rohit Gupta ⋅ Swetha Sirnam ⋅ Qingyang Liu ⋅ Ahnaf Munir ⋅ Shah Mubarak  
   [arXiv:2509.04438](https://arxiv.org/abs/2509.04438) · [code](https://github.com/mollahsabbir/Semantic-Drift-in-Unified-Models)
29. **TransVLM: A Vision-Language Framework and Benchmark for Detecting Any Shot Transitions**  
   Ce Chen ⋅ Yi Ren ⋅ Yuanming Li ⋅ Viktor Goriachko ⋅ Zhenhui Ye ⋅ Zujin Guo ⋅ Zhibin Hong ⋅ Mingming Gong  
   [arXiv:2604.27975](https://arxiv.org/abs/2604.27975) · [project](https://www.heygen.com/research) · [project](https://www.heygen.com/research/avatar-v-model)
30. **UEval: A Benchmark for Unified Multimodal Generation**  
   Bo Li ⋅ Yida Yin ⋅ Wenhao Chai ⋅ Xingyu Fu ⋅ Zhuang Liu  
   [arXiv:2601.22155](https://arxiv.org/abs/2601.22155)
31. **Understanding Cross-Rig Generalization in Automotive Perception: a Multi-Rig Benchmark and Rig Variation Metrics**  
   Tim Alexander Bader ⋅ Tim Eberhardt ⋅ Maximilian Dillitzer ⋅ Wilhelm Stork  
   [arXiv:2606.27554](https://arxiv.org/abs/2606.27554) · [project](https://badertim.github.io/plentiful-carla-camera-rigs)
32. **Unified Removal of Raindrops and Reflections: A New Benchmark and A Novel Pipeline**  
   Xingyu Liu ⋅ Zewei He ⋅ Yu Chen ⋅ Chunyu Zhu ⋅ Zixuan Chen ⋅ Xing Luo ⋅ Zheming Lu  
   [arXiv:2603.16446](https://arxiv.org/abs/2603.16446)
33. **Urban Boundaries, Social Barriers: A Benchmark and Vision-Centric Framework for Mapping Gated Communities and Equity Implications**  
   Minwei Zhao ⋅ WEIMING ZHANG ⋅ Jiawang DU ⋅ Qiming LIU ⋅ Weiming Zhuang ⋅ Pei Nie ⋅ Cai Wu
34. **Volume Transformer: Revisiting Vanilla Transformers for 3D Scene Understanding**  
   Kadir Yilmaz ⋅ Adrian Kruse ⋅ Tristan Höfer ⋅ Daan de Geus ⋅ Bastain Leibe  
   [arXiv:2604.19609](https://arxiv.org/abs/2604.19609) · [project](https://vision.rwth-aachen.de/Volt)
35. **Why Can Accurate Models Be Learned from Inaccurate Annotations?**  
   Chongjie Si ⋅ Yidan Cui ⋅ Fuchao Yang ⋅ Wei Shen  
   [arXiv:2505.16159](https://arxiv.org/abs/2505.16159)
36. **XDen-1K: A Density Field Dataset of Real-World Objects**  
   Jingxuan Zhang ⋅ Tianqi Yu ⋅ Yatu Zhang ⋅ Jinze Wu ⋅ Kaixin Yao ⋅ Jingyang Liu ⋅ Yuyao Zhang ⋅ Jiayuan Gu ⋅ Jingyi Yu  
   [arXiv:2512.10668](https://arxiv.org/abs/2512.10668)

# Application Domains


## Medical & Biomedical Imaging

*111 papers · 62 with links*

1. **AFFMAE: Scalable Vision Pre-Training for High-Resolution Microscopy Segmentation on Desktop Hardware**  
   David Smerkous ⋅ Zian Wang ⋅ Behzad Najafian  
   [arXiv:2602.16249](https://arxiv.org/abs/2602.16249) · [code](https://github.com/najafian-lab/affmae)
2. **AlphaRad: Grounded Zero-Shot Classification in Chest Radiology via α-Corrected Binary Cross Entropy and Factorized Latent Supervision**  
   Jianzhong You ⋅ Yuan Gao ⋅ Chris Mcintosh
3. **Anatomy of a Lie: A Multi-Stage Diagnostic Framework for Tracing Hallucinations in Vision-Language Models**  
   Lexiang Xiong ⋅ QI LI ⋅ Jingwen Ye ⋅ Xinchao Wang  
   [arXiv:2603.15557](https://arxiv.org/abs/2603.15557)
4. **Atlas is Your Perfect Context: One-Shot Customization for Generalizable Foundational Medical Image Segmentation**  
   Ziyu Zhang ⋅ Yi Yu ⋅ Simeng Zhu ⋅ Ahmed Aly ⋅ Yunhe Gao ⋅ Ning Gu ⋅ Yuan Xue  
   [arXiv:2512.18176](https://arxiv.org/abs/2512.18176)
5. **ATOMIC: A Domain-Specific Vision-Language Model for Transmission Electron Microscopy**  
   Chong-ren Tu ⋅ HUNG-WEI HSUEH ⋅ Shu-han Hsu
6. **Benchmarking Vision-Language Models for Microscopic Plant Image Understanding**  
   Tianqi Wei ⋅ Xin Yu ⋅ Zhi Chen ⋅ Scott C Chapman ⋅ Zi Helen Huang  
   [arXiv:2606.22497](https://arxiv.org/abs/2606.22497)
7. **BeTTER: Diagnose the Illusion of Embodied Reasoning in Vision-Language-Action Models**  
   Haiweng Xu ⋅ Sipeng Zheng ⋅ Hao Luo ⋅ Wanpeng Zhang ⋅ Zongqing Lu
8. **Beyond Isolated Scans: Cross-Phase Alignment of Structure and Topology for 3D Medical Pretraining**  
   Wenzhuo xu ⋅ YANJIE ZHOU ⋅ Yujian Hu ⋅ Hongkun Zhang ⋅ Minfeng Xu
9. **Beyond Random Sampling: Distribution-Aware Alignment for Semi-Supervised Medical Image Segmentation**  
   Weihao Yan ⋅ Yeqiang Qian ⋅ Yi Dong ⋅ Ming Yang  
   [arXiv:2607.04249](https://arxiv.org/abs/2607.04249)
10. **Beyond the Embedding Bottleneck: Adaptive Retrieval-Augmented 3D CT Report Generation**  
   Renjie Liang ⋅ Yiling Ma ⋅ Yang Xing ⋅ Zhengkang Fan ⋅ Chengkun Sun ⋅ Jinqian Pan ⋅ Li Li ⋅ Kuang Gong ⋅ Jie Xu  
   [arXiv:2603.15822](https://arxiv.org/abs/2603.15822) · [code](https://github.com/renjie-liang/Adaptive-RAG-for-3DCT-Report-Generation)
11. **BioMedVR: Confusion-Aware Mixture-of-Prompt Experts for Biomedical Visual Reprogramming**  
   Jiaxiang Liu ⋅ Tianxiang Hu ⋅ Juwei Guan ⋅ Yujie Wu ⋅ Yusong Wang ⋅ Yao Mu ⋅ Zuozhu Liu ⋅ Mingkun Xu  
   [arXiv:2606.24740](https://arxiv.org/abs/2606.24740) · [project](https://jxliu-ai.github.io/biomedvr-page/)
12. **BrainRiem: Riemannian Prototype Learning for Source-Free Cross-Site Brain Network Diagnosis**  
   Kunyu Zhang ⋅ Tianxiang Xu  
   [arXiv:2606.29200](https://arxiv.org/abs/2606.29200)
13. **CAR-MIL: Counterfactual Attention Regularization for Multiple Instance Learning**  
   Imane Chraki ⋅ Pierre Marza ⋅ Stergios Christodoulidis ⋅ Maria Vakalopoulou
14. **CerDETR: Cell-Prior Empowered DETR for Cervical Lesion Detection**  
   Linyun Zhou ⋅ Jin Chen ⋅ Weihan Li ⋅ Hengrui Lou ⋅ Lingxiang Jia ⋅ Weijun Qin ⋅ Xiuming Zhang ⋅ Zunlei Feng
15. **CLARITY: Medical World Model for Guiding Treatment Decisions by Simulating Context-Aware Disease Trajectories in Latent Space**  
   Tianxingjian Ding ⋅ Yuanhao Zou ⋅ Chen Chen ⋅ Shah Mubarak ⋅ Yu Tian
16. **Clinical Cognition Alignment for Gastrointestinal Diagnosis with Multimodal LLMs**  
   Huan Zheng ⋅ Yucheng Zhou ⋅ Tianyi Yan ⋅ Dubing Chen ⋅ Hongbo Lu ⋅ Wenlong Liao ⋅ Tao He ⋅ Pai Peng ⋅ Shen Jianbing  
   [arXiv:2603.20698](https://arxiv.org/abs/2603.20698)
17. **Compact and Structurally Transparent Cervical Cytology with Geometry-Driven Features and Closed-Form Attention**  
   Dichao Liu
18. **Comprehensive language–image pre-training for 3D medical image understanding**  
   Tassilo Wald ⋅ Ibrahim Ethem Hamamci ⋅ Yuan Gao ⋅ Sam Bond-Taylor ⋅ Harshita Sharma ⋅ Maximilian Ilse ⋅ Cynthia Lo ⋅ Olesya Melnichenko ⋅ Anton Schwaighofer ⋅ Noel Codella ⋅ Maria Teodora Wetscherek ⋅ Klaus Maier-Hein ⋅ Panagiotis Korfiatis ⋅ Valentina Salvatelli ⋅ Javier Alvarez-Valle ⋅ Fernando Pérez-García  
   [arXiv:2510.15042](https://arxiv.org/abs/2510.15042) · [code](https://huggingface.co/microsoft/colipri)
19. **Concept-to-Pixel: Prompt-Free Universal Medical Image Segmentation**  
   Haoyun Chen ⋅ Fenghe Tang ⋅ Wenxin Ma ⋅ S Kevin Zhou  
   [arXiv:2603.17746](https://arxiv.org/abs/2603.17746) · [code](https://github.com/Yundi218/Concept-to-Pixel)
20. **CortexVideo: A Semantic-Spatial Dual-Anchor Framework for High-Fidelity fMRI-to-Video Reconstruction**  
   Xiaoquan Shen ⋅ Jiaxuan Chen ⋅ Jiajun Li ⋅ Gang Pan
21. **CRAG-MM-Diagnostics: Enabling Stage-Wise Analysis of Knowledge-Intensive VQA**  
   Hanseok Oh ⋅ Parishad BehnamGhader ⋅ Benno Krojer ⋅ Hyunji Lee ⋅ Paul Pu Liang ⋅ Siva Reddy ⋅ Verna Dankers  
   [arXiv:2607.21155](https://arxiv.org/abs/2607.21155)
22. **Decoding Children’s Gait Behavior**  
   Yifan Shen ⋅ Boyi Li ⋅ Meihuan Huang ⋅ Yuanzhe Liu ⋅ Xu Cao ⋅ Jinyang Jin ⋅ Zhengyuan Li ⋅ Anglin Liu ⋅ Junho Kim ⋅ Jingyuan Zhu ⋅ Lan Fangzhou ⋅ Jianguo Cao ⋅ Jintai Chen ⋅ Ismini Lourentzou ⋅ James Rehg
23. **Diagnosing Aerial-View Object Detectors with Foundational Image Generative Models**  
   Stanislav Panev ⋅ Minhyek Jeon ⋅ Vaishnavi Khindkar ⋅ Ahish Deshpande ⋅ Celso de Melo ⋅ Shuowen Hu ⋅ Shayok Chakraborty ⋅ Fernando de la Torre  
   [arXiv:2607.02718](https://arxiv.org/abs/2607.02718) · [project](https://humansensinglab.github.io/AVODDiag/)
24. **DiffVP:Differential Visual Semantic Prompting for LLM-Based CT Report Generation**  
   Yuhe Tian ⋅ Kun Zhang ⋅ Haoran Ma ⋅ Rui Yan ⋅ Yingtai Li ⋅ Rongsheng Wang ⋅ S Kevin Zhou  
   [arXiv:2603.17718](https://arxiv.org/abs/2603.17718) · [code](https://github.com/ArielTYH/DiffVP/)
25. **Discrete Diffusion Models with MLLMs for Unified Medical Multimodal Generation**  
   Jiawei Mao ⋅ Yuhan Wang ⋅ Lifeng Chen ⋅ Can Zhao ⋅ Yucheng Tang ⋅ Dong Yang ⋅ Liangqiong Qu ⋅ Daguang Xu ⋅ Yuyin Zhou  
   [arXiv:2510.06131](https://arxiv.org/abs/2510.06131)
26. **Do Multimodal LLMs Understand Intraoral Dental Data? Dataset, Platform, and Baselines**  
   Luca Lumetti ⋅ Federico Rizzo ⋅ Francesca Cremonini ⋅ Ettore Candeloro ⋅ Lombardo Luca ⋅ Costantino Grana ⋅ Federico Bolelli
27. **DRIFT: Difficulty-aware Rectified Flows for Through-plane MRI Super-Resolution**  
   Yoonseok Choi ⋅ Eun-Gyu Ha ⋅ Daniel Kim ⋅ Mohammed Al-masni ⋅ Ming-Hsuan Yang ⋅ Dong-Hyun Kim
28. **Dual-Prior Guided Null-Space Learning with Mixture-of-Splines for Arbitrary Medical Slice Super-Resolution**  
   Haofei Song ⋅ Siyuan Xu ⋅ Xintian Mao ⋅ ShaoJie Guo ⋅ Qingli Li ⋅ Yan Wang  
   [arXiv:2606.26716](https://arxiv.org/abs/2606.26716) · [code](https://github.com/DeepMed-Lab-ECNU/Medical-Image-Reconstruction)
29. **ECHO: Efficient Chest X-ray Report Generation with One-step Block Diffusion**  
   Lifeng Chen ⋅ tianqi you ⋅ Hao Liu ⋅ Zhimin Bao ⋅ Jile Jiao ⋅ Xiao Han ⋅ Zhicai Ou ⋅ Tao Sun ⋅ Mou XiaoFeng ⋅ Xiaojie Jin ⋅ Yi Xu  
   [arXiv:2604.09450](https://arxiv.org/abs/2604.09450)
30. **EchoSonar-R: A Multi-View Reasoning-Enabled Model for Disease Classification and Report Generation in Echocardiography**  
   Darya Taratynova ⋅ Ahmed Aly ⋅ Numan Saeed ⋅ Mohammad Yaqub  
   [arXiv:2606.28164](https://arxiv.org/abs/2606.28164)
31. **Equivariant Symmetry-Aware Head Pose Estimation for Fetal MRI**  
   Ramya Muthukrishnan ⋅ Borjan Gagoski ⋅ Aryn Lee ⋅ Ellen Grant ⋅ Elfar Adalsteinsson ⋅ Benjamin Billot ⋅ Polina Golland  
   [arXiv:2512.04890](https://arxiv.org/abs/2512.04890)
32. **Evaluating and Understanding Model Editing for Medical Vision Language Models**  
   Guli Zhu ⋅ Chenwei Wu ⋅ Liyue Shen  
   [arXiv:2607.05310](https://arxiv.org/abs/2607.05310) · [code](https://github.com/BioMed-AI-Lab-U-Michgan/M3Bench)
33. **Falcon: Functional Assembly and Language for Compositional Reasoning in X-ray**  
   Yonathan Michael ⋅ Mohamad Alansari ⋅ Natnael Takele ⋅ Andreas Henschel ⋅ Naoufel Werghi  
   [arXiv:2606.25701](https://arxiv.org/abs/2606.25701) · [project](https://yonathan-kiflom.github.io/FALCON/page/)
34. **Flexible Control of 3D CT Generation via Text and Semantically-Defined Segmentation Prompts**  
   Weicheng Dai ⋅ Chenyu Wang ⋅ Shantanu Ghosh ⋅ Kayhan Batmanghelich  
   [arXiv:2606.00967](https://arxiv.org/abs/2606.00967)
35. **FlexiBrain: Resolution-Agnostic Voxel-Level Encoding for Native fMRI**  
   mo wang ⋅ Wenhao Ye ⋅ Junfeng Xia ⋅ Minghao Xu ⋅ Hongkai Wen ⋅ Quanying Liu  
   [arXiv:2606.11500](https://arxiv.org/abs/2606.11500) · [code](https://github.com/OneMore1/FlexiBrain)
36. **Foundation-Guided Representation Alignment for Multimodal Medical Image Registration**  
   Mengjie Guo ⋅ Xinxing Cheng ⋅ Wenqi Lu ⋅ Qingjie Meng ⋅ Guanyu Yang ⋅ Yang Chen ⋅ Ziyun Ding ⋅ Alejandro Frangi ⋅ Jinming Duan
37. **FPicker: Topology-Guided Evolution for Filament Tracing in Low-SNR Microscopy**  
   Tingyin Zhao ⋅ Mingtao Huang ⋅ Yuan Shen
38. **FreqPhys: Repurposing Implicit Physiological Frequency Prior for Robust Remote Photoplethysmography**  
   Wei Qian ⋅ Dan Guo ⋅ Jinxing Zhou ⋅ Bochao Zou ⋅ Zitong Yu ⋅ Meng Wang  
   [arXiv:2604.00534](https://arxiv.org/abs/2604.00534)
39. **From Hallucination to Grounding: Diagnosing Visual Spatial Intelligence via CRISP**  
   Zhixing Li ⋅ Yinan Yu  
   [arXiv:2606.26535](https://arxiv.org/abs/2606.26535) · [code](https://github.com/iiyamayuki/CRISP-Bench)
40. **From Macro to Micro: Benchmarking Microscopic Spatial Intelligence on Molecules via Vision-Language Models**  
   Zongzhao Li ⋅ Xiangzhe Kong ⋅ Jiahui Su ⋅ Zongyang Ma ⋅ Mingze Li ⋅ Songyou Li ⋅ Yuelin Zhang ⋅ Yu Rong ⋅ Tingyang Xu ⋅ Deli Zhao ⋅ Wenbing Huang  
   [arXiv:2512.10867](https://arxiv.org/abs/2512.10867) · [code](https://huggingface.co/datasets/zongzhao/MiSI-bench)
41. **From Minimal Clinical Prompts to 3D: Spacing-Aware Prompt Propagation for Multimodal Prostate Lesion Segmentation in bpMRI**  
   Jiacheng Wang ⋅ Heinrich von Busch ⋅ Robert Grimm ⋅ Ipek Oguz ⋅ Dorin Comaniciu ⋅ Ali Kamen ⋅ Bin Lou
42. **From Multi-Resolution Cells to Gigapixel Whole Slide Images Foundation Model for Computational Pathology**  
   Basit Alawode ⋅ Moshira Abdalla ⋅ Dwarikanath Mahapatra ⋅ Muhammad Muzammal Naseer ⋅ Sajid Javed  
   [arXiv:2608.03508](https://arxiv.org/abs/2608.03508)
43. **FSD-Net: Foundation-Guided Spatiotemporal Distillation for Video Polyp Segmentation**  
   Yahang Leng ⋅ Shiquan Min ⋅ Chengzhou Li
44. **FUSE: Filter-Free Unified Spatiotemporal Estimation of SpO2 via Wave-Transport Modeling**  
   Shahzad Ahmad ⋅ NUVVURU REDDY ⋅ Ram Padhy ⋅ Sukalpa Chanda ⋅ Umapada Pal
45. **Generalized Biomedicine Discovery**  
   Luyao Tang ⋅ Yingkai Yang ⋅ Hanqi Chen ⋅ Jiewei Zheng ⋅ Chaoqi Chen ⋅ Cheng Chen
46. **GridVQA-X: A Diagnostic Framework for Evaluating Multimodal Explainability Methods**  
   Sujay Belsare ⋅ Sushant Kumar ⋅ Sudarshan Nikhil ⋅ Ponnurangam Kumaraguru ⋅ Chirag Agarwal  
   [arXiv:2606.14740](https://arxiv.org/abs/2606.14740)
47. **Harnessing SSL for Segmentation in 3D Microscopy with Noisy Labels and Hard Patches**  
   Lingtong Xu ⋅ Ahmadreza Attarpour ⋅ Shruti Patel ⋅ Fengqing Yu ⋅ Matthew Rozak ⋅ Bojana Stefanovic ⋅ Anne Martel ⋅ Maged Goubran
48. **HASSL: Hierarchy-Aware Self-Supervised Learning Framework for Single Cell Microscopy**  
   Julius Riel ⋅ Vishwa Mohan Singh ⋅ SAI ANIRUDH ARYASOMAYAJULA ⋅ Anuun Chinbat ⋅ Hannes Leonhard ⋅ Moritz Ladenburger ⋅ Frederik Alexander ⋅ Vishisht Choudhary ⋅ Fabio Laredo ⋅ Giacomo Masserdotti ⋅ Thorben Prein ⋅ Amirhossein Kardoost ⋅ Carsten Marr  
   [arXiv:2607.04353](https://arxiv.org/abs/2607.04353)
49. **Hi-DREAM: Brain Inspired Hierarchical Diffusion for fMRI-to-image Reconstruction via ROI Encoder And visual Mapping**  
   Guowei Zhang ⋅ Yun Zhao ⋅ Kai Sun ⋅ Moein Khajehnejad ⋅ Adeel Razi ⋅ Dinh Q Phung ⋅ Levin Kuhlmann  
   [arXiv:2511.11437](https://arxiv.org/abs/2511.11437)
50. **HighlightBench: Benchmarking and Diagnosing Markup-Driven Table Reasoning in Scientific Documents**  
   Lexin Wang ⋅ Shenghua Liu ⋅ Yiwei Wang ⋅ Yujun Cai ⋅ Yuyao Ge ⋅ Jiayu Yao ⋅ Jiafeng Guo ⋅ Xueqi Cheng
51. **Histocomponent-driven Universal Model for Virtual Immunohistochemistry Multiplex Staining via Joint Manifold Evolution**  
   Jiajun Cen ⋅ Siyuan Xu ⋅ Lili Gao ⋅ Yan Wang
52. **Histopathology Multi-modal Embedding for Pathology Composed Retrieval**  
   Qifeng Zhou ⋅ Wenliang Zhong ⋅ Thao Dang ⋅ Hehuan Ma ⋅ Saiyang Na ⋅ Yuzhi Guo ⋅ Junzhou Huang  
   [arXiv:2502.07221](https://arxiv.org/abs/2502.07221) · [project](https://qfchou.github.io/HOMIE_page/)
53. **iMED: A Multi-Endoscope Dataset for Surgical 3D Perception**  
   Sierra Bonilla ⋅ Fengyi Jiang ⋅ Chinedu Nwoye ⋅ Jingpei Lu ⋅ Kailey Reardon ⋅ Humphrey Chow ⋅ Francisco Vasconcelos ⋅ Sophia Bano ⋅ Adam Schmidt ⋅ Omid Mohareri
54. **Linguistically-Aligned and Visually-Grounded Preference Optimization for Clinically-Augmented Medical Report Generation**  
   Qiang Hu ⋅ Yuxuan Luo ⋅ Yingjie Guo ⋅ Hao Wang ⋅ Qimei Wang ⋅ Qiang Li ⋅ Zhiwei Wang  
   [arXiv:2608.08494](https://arxiv.org/abs/2608.08494)
55. **Low-Level Dataset Distillation for Medical Image Enhancement**  
   Fengzhi Xu ⋅ Ziyuan Yang ⋅ Mengyu Sun ⋅ Joey Tianyi Zhou ⋅ Yi Zhang  
   [arXiv:2511.13106](https://arxiv.org/abs/2511.13106)
56. **MCPNet:Masked Coordinate Pooling-based Attention Network for Medical Landmark Detection**  
   Gyu-Sung Ham ⋅ Gi Hyun Lim ⋅ Kanghan Oh
57. **Mechanistic interventions for explainable digital pathology uncovers adversarial vulnerabilities**  
   Arijit Patra ⋅ Samiran Dey ⋅ Ajitha Rajan ⋅ Greg Slabaugh ⋅ Tapabrata Chakraborti
58. **MedCAGD: Context-Aware Gated Decoder for Robust Medical Image Segmentation**  
   Saad Wazir ⋅ Patrick Vibild ⋅ Dinh Tran ⋅ Seongah Kim ⋅ Daeyoung Kim
59. **MedQ-Deg: A Multidimensional Benchmark for Evaluating MLLMs Across Medical Image Quality Degradations**  
   Jiyao Liu ⋅ Junzhi Ning ⋅ Chenglong Ma ⋅ Wanying Qu ⋅ Jianghan Shen ⋅ Siqi Luo ⋅ Jinjie Wei ⋅ Jin Ye ⋅ Pengze Li ⋅ Tianbin Li ⋅ Jiashi Lin ⋅ Hongming Shan ⋅ Xinzhe Luo ⋅ Xiaohong Liu ⋅ Lihao Liu ⋅ Junjun He ⋅ Ningsheng Xu  
   [arXiv:2603.07769](https://arxiv.org/abs/2603.07769)
60. **MedRepBench: Benchmarking Structured Understanding of Medical Report Images**  
   Fangxin Shang ⋅ Yuan Xia ⋅ Dalu Yang ⋅ Yahui Wang ⋅ BingLinYang BingLinYang
61. **MedSPOT: A Workflow-Aware Sequential Grounding Benchmark for Clinical GUI**  
   Rozain Shakeel ⋅ Abdul Ali ⋅ Muneeb Ganie ⋅ Tausifa Jan Saleem ⋅ Tajamul Ashraf  
   [arXiv:2603.19993](https://arxiv.org/abs/2603.19993) · [code](https://github.com/Tajamul21/MedSPOT) · [project](https://rozainmalik.github.io/MedSPOT_web/)
62. **MedSynapse-V: Bridging Visual Perception and Clinical Intuition via Latent Memory Evolution**  
   Chunzheng Zhu ⋅ Jiaqi Zeng ⋅ Junyu Jiang ⋅ Jianxin Lin ⋅ Yijun Wang  
   [arXiv:2604.26283](https://arxiv.org/abs/2604.26283) · [code](https://github.com/zhcz328/MedSynapse-V)
63. **Memory-Supported Synergistic Adaptation for Training-Free Test-Time Medical Image Segmentation**  
   Lingrui Li ⋅ Nan Pu ⋅ Dong Zhao ⋅ Wenjing Li ⋅ Andrew French ⋅ Xin Chen ⋅ Zhun Zhong  
   [arXiv:2607.17693](https://arxiv.org/abs/2607.17693) · [project](https://lingrayy.github.io/MSSA/)
64. **Mimicking Radiologists: A Coarse-to-Fine Framework with Structural Sparse Tokens for Dual-LLM Computed Tomography Report Generation**  
   Hong Liu ⋅ Dong Wei ⋅ Yefeng Zheng ⋅ Xian Wu ⋅ Liansheng Wang
65. **Mind-to-Face: Neural-Driven Photorealistic Avatar Synthesis via EEG Decoding**  
   Haolin Xiong ⋅ Tianwen Fu ⋅ Yunxuan Cai ⋅ Pratusha Prasad ⋅ Haiwei Chen ⋅ Wenbin Teng ⋅ Hanyuan Xiao ⋅ Yajie Zhao  
   [arXiv:2512.04313](https://arxiv.org/abs/2512.04313)
66. **Mind2Cloud: EEG-to-Point Cloud Generation with Two-Granularity Diffusion Decoding**  
   Yongyi Lu ⋅ Xiongfeng Huang ⋅ Zhijing Yang
67. **Molecular Identifier Visual Prompting and Verifiable Reinforcement Learning for Chemical Reaction Diagram Parsing**  
   Jiahe Song ⋅ Chuang Wang ⋅ Yinfan Wang ⋅ Hao Zheng ⋅ Bowen Jiang ⋅ Rui Nie ⋅ Xingjian Wei ⋅ Junyuan Gao ⋅ Yubin Wang ⋅ Bin Wang ⋅ Lijun Wu ⋅ Jiang Wu ⋅ Qian Yu ⋅ Conghui He  
   [arXiv:2603.15011](https://arxiv.org/abs/2603.15011)
68. **MOOZY: A Patient-First Foundation Model for Computational Pathology**  
   Yousef Hassan ⋅ Vincent Quoc-Huy Trinh ⋅ Christopher Pal ⋅ Mahdi S. Hosseini  
   [arXiv:2603.27048](https://arxiv.org/abs/2603.27048)
69. **Multi-Channel Uncertainty-Weighted Score Matching for Conditional Diffusion in Medical UDA**  
   CHEN LI ⋅ Meilong Xu ⋅ Xiaoling Hu ⋅ Weimin Lyu ⋅ Chao Chen  
   [arXiv:2509.22476](https://arxiv.org/abs/2509.22476) · [code](https://github.com/superlc1995/Multi-Channel-Uncertainty-Diffusion-UDA)
70. **Neuromorphic X-ray Computed Tomography**  
   Hongjian Wang ⋅ Goran Lovric ⋅ Benjamín Béjar
71. **NeuroRefiner: Morphology-Aware Multi-Agent Refinement for 3D Fluorescence Microscopy Neuron Segmentation**  
   HAIYANG YAN ⋅ Jinyue Guo ⋅ Yanchao Zhang ⋅ Bingqing Wang ⋅ Zhenchen Li ⋅ Jing Liu ⋅ Jiazheng Liu ⋅ linlin li ⋅ Hua Han  
   [arXiv:2608.09636](https://arxiv.org/abs/2608.09636)
72. **One Slide, Many Views: Unifying Complementary Foundation Model Perspectives for WSI Analysis**  
   Yihui WANG ⋅ Yingxue Xu ⋅ Shu Yang ⋅ Yequan Bie ⋅ Jiabo MA ⋅ Fengtao Zhou ⋅ Hao Chen
73. **PhenoLIP: Phenotype Guided Medical Vision–Language Pretraining**  
   Cheng Liang ⋅ Chaoyi Wu ⋅ Weike Zhao ⋅ Ya Zhang ⋅ Yanfeng Wang ⋅ Weidi Xie
74. **Physics-Grounded Disentangled Flow Modeling for Brain Disease Progression Trajectory**  
   Jun Wang ⋅ Peirong Liu  
   [arXiv:2606.28630](https://arxiv.org/abs/2606.28630) · [code](https://github.com/jhuldr/PDF)
75. **Posterior Samplings are Missing Modalities Generators for Medical Image Translation**  
   Jonghun Kim  
   [arXiv:2607.18763](https://arxiv.org/abs/2607.18763)
76. **Progression as Latent Drift: Generative Forecasting of Slow-Evolving Pathologies**  
   Yuxiang Feng ⋅ Juncheng Wang ⋅ Chao Xu ⋅ Wenlong Hou ⋅ Huihan Wang ⋅ Yijie Qian ⋅ Yang Liu ⋅ Baigui Sun ⋅ Yong Liu ⋅ Shujun Wang  
   [arXiv:2607.08270](https://arxiv.org/abs/2607.08270) · [project](https://cutepkq.github.io/latent-drift)
77. **Proto-Gaussian: MRI Modality Translation Based on Learnable Structural Prototypes and 2D Gaussian Splatting**  
   Zizheng Li ⋅ RenDong Xie ⋅ Huadeng Wang ⋅ Zhifen He ⋅ Bin Liu ⋅ Bo Li ⋅ Xiaonan Luo
78. **Proximity-Constrained Counterfactual Decoding for Hallucination-Robust Medical VQA**  
   Dwarikanath Mahapatra ⋅ Abhijit Das ⋅ Manish Pandey ⋅ Joy Dhar ⋅ Sudipta Roy ⋅ Zongyuan Ge ⋅ Behzad Bozorgtabar ⋅ Imran Razzak
79. **PyraE2E: Enhancing End-to-End WSI Analysis via Cross-Scale Super-Resolution**  
   Yuechuan Lin ⋅ yujian liu ⋅ Weipeng Zhang ⋅ Yanyu Fan ⋅ Zikang Wang ⋅ Dongxu Shen ⋅ Liqin Fei ⋅ Xiaoli Liu ⋅ Shidang Xu
80. **RAU: Reference-based Anatomical Understanding with Vision-Language Models**  
   Yiwei Li ⋅ Yikang Liu ⋅ Jiaqi Guo ⋅ Lin Zhao ⋅ Zheyuan Zhang ⋅ Xiao Chen ⋅ Boris Mailhe ⋅ Ankush Mukherjee ⋅ Terrence Chen ⋅ Shanhui Sun  
   [arXiv:2509.22404](https://arxiv.org/abs/2509.22404)
81. **Region-Aware Multimodal Large Language Model via SlowFast Tokenization and Pseudo-Mask Guidance for 3D CT Report Generation**  
   Sunggu Kyung ⋅ Jinyoung Seo ⋅ Hyunseok Lim ⋅ Dongyeong Kim ⋅ Hyungbin Park ⋅ Jimin Sung ⋅ Wooyoung Jo ⋅ Yoojin Nam ⋅ Namkug Kim  
   [arXiv:2506.23102](https://arxiv.org/abs/2506.23102) · [code](https://github.com/babbu3682/MedRegion-CT)
82. **Resolution-Agnostic Neural Operators for Multi-Rate Sparse-View CT**  
   Aujasvit Datta ⋅ Jiayun Wang ⋅ Asad Aali ⋅ Anima Anandkumar  
   [arXiv:2512.12236](https://arxiv.org/abs/2512.12236) · [code](https://github.com/neuraloperator/sparse_ct)
83. **Rethinking Real-World MRI Denoising: Learning from Physical Noise**  
   Sebastian Rassmann ⋅ David Kügler ⋅ Sascha Brunheim ⋅ Philipp Ehses ⋅ Martin Reuter
84. **REVA-PO: Stabilizing Reinforcement Learning for Chest X-ray Report Generation**  
   Li Guo ⋅ Anas Tahir ⋅ Z. Wang  
   [arXiv:2607.10147](https://arxiv.org/abs/2607.10147) · [code](https://github.com/LiGuo12/REVA_PO/)
85. **RPM-Distill: Physiology-guided Adaptive Cross-modal Distillation for Robust Remote Physiological Measurement**  
   Jiyao Wang ⋅ Qingyong Hu ⋅ Duoxun Tang ⋅ Xiao Yang ⋅ Kaishun Wu ⋅ Jiangbo Yu  
   [arXiv:2606.28089](https://arxiv.org/abs/2606.28089) · [code](https://github.com/WJULYW/RPM-Distill)
86. **Scaling Whole-Slide Pathology Foundation Model Pretraining with Billions Off-the-Shelf Tokens**  
   Honglin Li ⋅ Zhongyi Shui ⋅ Chenglu Zhu ⋅ Lin Yang
87. **SCDL: Synergistic Confidence-Dispersion Learning for Semi-Supervised Video Polyp Segmentation**  
   yuanqin he ⋅ Yuhua Zhang ⋅ Huisi Wu ⋅ Jing Qin
88. **SDUM: A Scalable Deep Unrolled Model for Universal Cardiac MRI Reconstruction**  
   Puyang Wang ⋅ Pengfei Guo ⋅ Keyi Chai ⋅ Jinyuan Zhou ⋅ Daguang Xu ⋅ Shanshan Jiang  
   [arXiv:2512.17137](https://arxiv.org/abs/2512.17137) · [code](https://github.com/NVIDIA-Medtech/NV-Raw2insights-MRI)
89. **Seeing What Matters: Lesion-Aware High-Resolution Patch Discovery and Fusion for Chest X-ray Report Generation**  
   Yingshu Li ⋅ YUNYI LIU ⋅ Zhenghao Chen ⋅ Tong Chen ⋅ Zailong Chen ⋅ Lingqiao Liu ⋅ Lei Wang ⋅ Luping Zhou  
   [arXiv:2607.06909](https://arxiv.org/abs/2607.06909)
90. **SeekFlow: Synergizing Radiology and Pathology Foundation Models for Precision Oncology via Knowledge-Guided Evidence Flow**  
   Peixiang Huang ⋅ Yanyan Huang ⋅ Yihang Chen ⋅ Maximus Yeung ⋅ Yuming Jiang ⋅ Lequan Yu
91. **Semantic-Anchored Evidential Fusion for Domain-Robust Whole-Slide Survival Analysis**  
   YUCHENG XING XING ⋅ Ling Huang ⋅ Pei Liu ⋅ Jingying Ma ⋅ Jiaxing Xu ⋅ Kai He ⋅ Mengling Feng  
   [arXiv:2606.19966](https://arxiv.org/abs/2606.19966)
92. **SkelEM: Explicit Decoupling of Topology and Details for Self-supervised Axial Super-Resolution in Volume Microscopy**  
   Bohao Chen ⋅ Yanchao Zhang ⋅ Yanan Lv ⋅ Chenxun Deng ⋅ Hua Han ⋅ Xi Chen
93. **Skin-R1: Clinical Knowledge-Guided Dermatological Diagnosis Using Vision-Language Models**  
   Zehao Liu ⋅ Weijieying Ren ⋅ Jipeng ZHANG ⋅ Tianxiang Zhao ⋅ Jingxi Zhu ⋅ Xiaoting Li ⋅ Vasant Honavar  
   [arXiv:2511.14900](https://arxiv.org/abs/2511.14900)
94. **SOMA: From Surface Observations to Muscle Anatomy**  
   Eduardo Alvarado ⋅ Emily Kim ⋅ Friedemann Runte ⋅ Gerrit Nolte ⋅ Mario Botsch ⋅ Marc Habermann ⋅ Christian Theobalt  
   [arXiv:2606.09246](https://arxiv.org/abs/2606.09246)
95. **SPDA: Efficient Online Test-Time Adaptation for Promptable Medical Segmentation**  
   Huixuan Xu ⋅ Hu Han ⋅ Shiguang Shan ⋅ Xilin CHEN
96. **Spectral Consistent Flow for One-step 3D Medical Image Translation**  
   Haoqing Li ⋅ Jun Shi ⋅ Mingchao Li ⋅ Zehua Zhu ⋅ Qiwei Jia ⋅ Jiong SHI ⋅ Hong An  
   [arXiv:2607.10627](https://arxiv.org/abs/2607.10627)
97. **SPHERE: From MRI Sampling Mechanisms to Spatial Priors for Generalizable Brain Tumor Segmentation**  
   JiaCheng Lu ⋅ Shiyu Zhang ⋅ Hui Ding ⋅ junhui xin ⋅ Guoping Huo
98. **SUM: Unified Geometric Surgery on Spatio-Temporal Adaptation Vectors for Federated Class Incremental Learning**  
   Jaeik Kim ⋅ Jaeyoung Do  
   [arXiv:2607.19384](https://arxiv.org/abs/2607.19384)
99. **TaxoMIL: Taxonomy-Constrained Learning for Hierarchical Whole Slide Image Analysis**  
   Chaeyeon Lee ⋅ Khang Quoc ⋅ Jinsol Song ⋅ Yosep Chong ⋅ Kwangil Yim ⋅ JIN TAE KWAK  
   [arXiv:2606.31100](https://arxiv.org/abs/2606.31100) · [code](https://github.com/QuIIL/TaxoMIL)
100. **Together, Then Apart: Balancing Alignment and Distinctiveness for Multimodal Survival Analysis**  
   Wenjing Liu ⋅ Qin Ren ⋅ Wen Zhang ⋅ Yuewei Lin ⋅ Chenyu You  
   [arXiv:2511.18089](https://arxiv.org/abs/2511.18089)
101. **TopoAgent: An Agentic Framework for Automated Topology Learning in Medical Imaging**  
   Guangyu Meng ⋅ Pengfei Gu ⋅ Xueyang Li ⋅ Yiyu Shi ⋅ Erin Chambers ⋅ Danny Chen  
   [arXiv:2606.29763](https://arxiv.org/abs/2606.29763)
102. **Towards Trustworthy Dermatology MLLMs: A Benchmark and Multimodal Evaluator for Diagnostic Narratives**  
   Yuhao Shen ⋅ Jiahe Qian ⋅ Zhangtianyi Chen ⋅ Juexiao Zhou  
   [arXiv:2511.09195](https://arxiv.org/abs/2511.09195)
103. **Tricam-rPPG: A Multimodal Multispectral Dataset for remote Photoplethysmography**  
   Abhijit Sarkar ⋅ Surendrabikram Thapa ⋅ Ishtiaque Khan ⋅ Yogesh Deshpande ⋅ Amos Abbott
104. **UBone3D: Physics-Rectified Conditional Flow Matching for Anatomical 3D Shape Completion from Ultrasound**  
   Weiying Chen ⋅ Yuchong Gao ⋅ Siyuan Li ⋅ Marek Reformat ⋅ Rui Zheng ⋅ Edmond Lou
105. **Unified Multi-plane Autoregressive Diffusion for 3D Multi-Contrast MRI Synthesis**  
   Yejee Shin ⋅ Geonhui Son ⋅ Jinglu Wang ⋅ Minwoo Jung ⋅ Yan Lu ⋅ Dosik Hwang
106. **UniH3: Unifying Hierarchical Homogeneity and Heterogeneity for All-in-One Medical Image Restoration**  
   Zhiwen Yang ⋅ Jiayin Li ⋅ Chengyu Liu ⋅ Hui Zhang ⋅ Bingzheng Wei ⋅ Yan Xu
107. **Verifying Cancer Segmentation in Vision Transformers via Internal Concepts**  
   Mengmeng Ma ⋅ Yunxiang Peng ⋅ Tang Li ⋅ Lu Lin ⋅ Binsheng Zhao ⋅ Oguz Akin ⋅ Xi Peng
108. **VesselTok: Tokenizing Vessel-like 3D Biomedical Graph Representations for Reconstruction and Generation**  
   Chinmay Prabhakar ⋅ Bastian Wittmann ⋅ Tamaz Amiranashvili ⋅ Paul Büschl ⋅ Ezequiel De la Rosa ⋅ Julian McGinnis ⋅ Benedikt Wiestler ⋅ Bjoern Menze ⋅ Suprosanna Shit  
   [arXiv:2603.18797](https://arxiv.org/abs/2603.18797)
109. **Wavelet-Driven Cross-Domain Consistency for Mixed-Supervised 3D Tumor Segmentation**  
   Tianzhong Lan ⋅ Weili Jiang ⋅ Yisong Liu ⋅ Yi Zhou ⋅ Junqi Bai ⋅ Si Yeo ⋅ Xulei Yang ⋅ Min Zhu
110. **XSurfer: Reconstructing surface meshes of cerebral and cerebellar cortex from diverse MRI data using untrained neural networks**  
   Haoxiang Li ⋅ Mingxuan Liu ⋅ Divya Varadarajan ⋅ Zhangxuan Hu ⋅ Qiyuan Tian ⋅ Jonathan Polimeni
111. **λSplit: Self-Supervised Content-Aware Spectral Unmixing for Fluorescence Microscopy**  
   Federico Carrara ⋅ Mehdi Seifi ⋅ Florian Jug

## Remote Sensing & Earth Observation

*74 papers · 40 with links*

1. **3D-LENS: A 3D Lifting-based Elevated Novel-view Synthesis method for Single-View Aerial-Ground Re-Identification**  
   William Grolleau ⋅ Astrid Sabourin ⋅ Guillaume Lapouge ⋅ Catherine Achard
2. **AerialMetric: Benchmarking and Adapting UAV Monocular Metric Depth Estimation in the Real World**  
   Zhongqiang Song ⋅ Guanying Chen ⋅ Yuqi Zhang ⋅ Yin Zou ⋅ Chuanyu Fu ⋅ Zhiyuan Yuan ⋅ Chuan Huang ⋅ Shuguang Cui ⋅ Xiaochun Cao  
   [arXiv:2606.29716](https://arxiv.org/abs/2606.29716) · [project](https://kuieless.github.io/AerialMetric-ECCV2026-page/)
3. **AeroVLA: A Vision-Language-Action Model for UAV Navigation via Minimalist End-to-End Control**  
   Peng Xu ⋅ Zhengnan Deng ⋅ Jiayan Deng ⋅ Zonghua Gu ⋅ Peng Xu
4. **AirZoo: A Unified Large-Scale Dataset for Grounding Aerial Geometric 3D Vision**  
   Xiaoya Cheng ⋅ Rouwan Wu ⋅ Xinyi Liu ⋅ Zeyu Cui ⋅ Yan Liu ⋅ Na Zhao ⋅ Yu Liu ⋅ Maojun Zhang ⋅ Shen Yan  
   [arXiv:2604.26567](https://arxiv.org/abs/2604.26567) · [project](https://nudt-sawlab.github.io/AirZoo/)
5. **AutoWeather4D: Autonomous Driving Video Weather Conversion via G-Buffer Dual-Pass Editing**  
   Tianyu Liu ⋅ Weitao Xiong ⋅ Kunming Luo ⋅ Manyuan Zhang ⋅ Peng Li ⋅ Yuan Liu ⋅ Ping Tan  
   [arXiv:2603.26546](https://arxiv.org/abs/2603.26546) · [code](https://github.com/lty2226262/AutoWeather4D) · [project](https://lty2226262.github.io/autoweather4d/)
6. **AV2T-Gen: Aerial Visible to Thermal Generation with Environment and Vehicle State Guidance**  
   Kun Yang ⋅ Yuxiang Liu ⋅ Yihan Wang ⋅ Shen Yan ⋅ Maojun Zhang ⋅ Yu Liu ⋅ Xue Wang ⋅ Qing Wang
7. **Beyond Attention: Convolutional Global Context for Remote Sensing Change Detection**  
   Zhenyu Yang ⋅ Gensheng Pei ⋅ Junzhu Mao ⋅ Xinhao Cai ⋅ Tao Chen ⋅ Yazhou Yao
8. **Capturing Spectral and Spatial Patterns for Federated Remote Sensing Segmentation**  
   Yixin Xue ⋅ Wenke Huang ⋅ Haonan Guo ⋅ Bo Du
9. **Compact Low-Cost Hyperspectral Imaging via Angular-to-Spectral Diversity Conversion**  
   Kazuma Fujiwara ⋅ Takuya Funatomi ⋅ Kazuya Kitano ⋅ Yuki Fujimura ⋅ Yasuhiro Mukaigawa
10. **Constrained Rotation Optimization: Revisiting Crop-Based Gaze Estimation**  
   Riccardo Santambrogio ⋅ Jiawei Qin ⋅ Matteo Matteucci ⋅ Yusuke Sugano
11. **Context-Aware Joint Alignment for Cross-Scene Hyperspectral Image Classification**  
   Boshan Shi ⋅ JiaXin Chen ⋅ Yanbo Liu ⋅ Youqiang Zhang ⋅ Guo Cao
12. **Counting Trees from Satellite Imagery with Noisy Supervision**  
   Dimitri Gominski ⋅ Maurice Mugabowindekwe ⋅ Qiue XU ⋅ Xiaowei Tong ⋅ Martin Brandt ⋅ Hieu Le ⋅ Rasmus Fensholt ⋅ Dimitris Samaras ⋅ Loic Landrieu  
   [arXiv:2606.24786](https://arxiv.org/abs/2606.24786) · [code](https://github.com/dgominski/treematch)
13. **CRD-Net: Frequency-Adaptive Feature Injection and Change Decoupling for Building Damage Assessment**  
   Yao Zheng ⋅ Yuanxin Ye ⋅ Tan Shu ⋅ Liwei Cai
14. **CRISP: Calibration-Aware Visual State Space Duality for Remote Sensing Image Segmentation**  
   kangning wang ⋅ Haopeng Zhang ⋅ Zhiguo Jiang
15. **CROSS: Cascaded Distillation and Dual-Constraint Grounding for Remote Sensing Referring Segmentation**  
   Tingzhang Luo ⋅ Ruizhong Liu ⋅ Yichao Liu ⋅ Cheng Fan ⋅ Yu Liu ⋅ Jianyuan Guo
16. **DETR is Secretly a Multispectral Detector: Zero-Parameter Adaptation via Semantic Alignment**  
   Xiangyang Li ⋅ Zhiwei Jiang ⋅ Wushuai Jin ⋅ Pengyang Niu ⋅ Chunna Tian ⋅ Lingqiao Liu
17. **Environmental Change Detection for Real-World Change Analysis**  
   Kyusik Cho ⋅ Suhan Woo ⋅ Hongje Seong ⋅ Euntai Kim
18. **Estimating Individual Tree Height and Species from UAV Imagery**  
   Jannik Endres ⋅ Etienne Laliberté ⋅ David Rolnick ⋅ Arthur Ouaknine  
   [arXiv:2603.23669](https://arxiv.org/abs/2603.23669) · [project](https://RolnickLab.github.io/DINOvTree)
19. **Evaluating and Enhancing Negation Comprehension in Remote Sensing MLLMs**  
   Haochen Han ⋅ Jue Wang ⋅ Alex Jinpeng Wang ⋅ Fangming Liu  
   [arXiv:2606.20177](https://arxiv.org/abs/2606.20177)
20. **Filterless Snapshot Hyperspectral Imaging using Guided Patch Diffusion**  
   Dean Hazineh ⋅ Luca Sacchi ⋅ Davide Cassara ⋅ Federico Capasso ⋅ Todd Zickler  
   [arXiv:2412.02798](https://arxiv.org/abs/2412.02798)
21. **Foundation Model Selection for Remote Sensing via a Constraint-Aware Agent**  
   Binger Chen ⋅ Tacettin Bök ⋅ Behnood Rasti ⋅ Volker Markl ⋅ Begüm Demir  
   [arXiv:2511.17442](https://arxiv.org/abs/2511.17442) · [code](https://github.com/be-chen/REMSA)
22. **GeoSolver: Scaling Test-Time Reasoning in Remote Sensing with Fine-Grained Process Supervision**  
   Sun Lang ⋅ Ronghao Fu ⋅ Zhuoran Duan ⋅ Haoran Liu ⋅ Xueyan Liu ⋅ Bo Yang  
   [arXiv:2603.09551](https://arxiv.org/abs/2603.09551) · [code](https://github.com/yourname/GeoSolver)
23. **GroundSet: A Cadastral-Grounded Dataset for Spatial Understanding with Vector Data**  
   Roger Ferrod ⋅ Maël Lecene ⋅ Krishna Sapkota ⋅ George Leifman ⋅ Vered Silverman ⋅ Genady Beryozkin ⋅ Sylvain Lobry  
   [arXiv:2603.14609](https://arxiv.org/abs/2603.14609)
24. **GrowFields: Compositional 4D Neural Fields for Topology-Changing Plant Growth**  
   Joaquin Gajardo ⋅ Michele Volpi ⋅ Marko Mihajlovic ⋅ Siyu Tang ⋅ Lukas Roth ⋅ Sergey Prokudin  
   [arXiv:2607.03330](https://arxiv.org/abs/2607.03330) · [project](https://joaquin-gajardo.github.io/growfields/)
25. **Hierarchical Hyperbolic Representation Learning for Aerial-Ground Person Re-Identification**  
   QiWei Yang
26. **HUGE-Bench: A Benchmark for High-Level UAV Vision-Language-Action Tasks**  
   Jingyu Guo ⋅ Ziye Chen ⋅ Ziwen Li ⋅ Zhengqing Gao ⋅ Jiaxin Huang ⋅ Hanlue Zhang ⋅ Fengming Huang ⋅ Yu Yao ⋅ Tongliang Liu ⋅ Mingming Gong  
   [arXiv:2603.19822](https://arxiv.org/abs/2603.19822)
27. **Ice Cloud Geometry Retrieval with Calibrated Uncertainty from Passive Satellite Imagery**  
   Ayush Prasad
28. **Interpretation-Oriented Cloud Removal via Observation-Anchored Residual Flow with Geo-Contextual Alignment**  
   Ziyao Wang ⋅ Maonan Wang ⋅ Yucheng He ⋅ Xianping Ma ⋅ Ziyi Wang ⋅ Hongyang Zhang ⋅ Yirong Chen ⋅ Man On Pun  
   [arXiv:2607.02471](https://arxiv.org/abs/2607.02471) · [code](https://github.com/wzy6055/GACR)
29. **Keep Your Friends Close, and the Right Neighbours Closer: Disaster-Conditioned Kernel-Regularized Graph Attention for Building Damage Classification**  
   Fuad Hasan ⋅ Chul Min Yeum
30. **Learning Semantic-Robust Change Detection via Semantic-Invariant Self-Distillation**  
   Jiuhe Qu ⋅ Yingping Liang ⋅ Ying Fu  
   [arXiv:2607.19000](https://arxiv.org/abs/2607.19000) · [code](https://github.com/elecreak/SCDistill)
31. **Learning to Balance: Decoupled Siamese Diffusion Transformer for Reference-Based Remote Sensing Image Super-Resolution**  
   Bin Luo ⋅ Runmin Dong ⋅ Zhaoyang Luo ⋅ Jinxiao Zhang ⋅ Jiyao Zhao ⋅ Fan Wei ⋅ Haohuan Fu  
   [arXiv:2605.17980](https://arxiv.org/abs/2605.17980)
32. **Leaving the City: A Large-Scale Aerial Dataset for Cross-Season Localization in Unstructured Environments**  
   Michael Schleiss ⋅ Henry Hölzemann ⋅ Fahmi Rouatbi ⋅ Torsten Fiolka ⋅ Thomas Pany ⋅ Roger Förstner ⋅ Daniel Cremers
33. **Less Tokens, Better Forecasts: Sparse Residual Routing for Efficient Weather Prediction**  
   Janet Wang ⋅ Yunbei Zhang ⋅ Lin Zhao ⋅ Xi Xiao ⋅ Jihun Hamm ⋅ Xiao Wang  
   [arXiv:2607.02829](https://arxiv.org/abs/2607.02829)
34. **MapDreamer: Aerial Imagery Conditioned Latent Diffusion For Lane Level Map Generation**  
   Julian Brandes ⋅ Philipp Crocoll ⋅ Wolfram Burgard  
   [arXiv:2607.01370](https://arxiv.org/abs/2607.01370)
35. **MCVL: Multi-Space Cross-View Learning for Aerial-Ground Person Re-Identification**  
   Wajahat Khalid ⋅ Bin Liu ⋅ Xulin Li ⋅ Yubo Wang ⋅ MUHAMMAD SHER AFGAN
36. **Moonstone: A Multimodal Foundation Model and Benchmark for Lunar Remote Sensing**  
   Ayush Prasad ⋅ Swarnalee Mazumder  
   [arXiv:2607.03644](https://arxiv.org/abs/2607.03644) · [code](https://huggingface.co/datasets/ayushprd/Moonstone)
37. **Multi-label Instance-level Generalised Visual Grounding in Agriculture**  
   Mohammadreza Haghighat ⋅ Alzayat Saleh ⋅ Mostafa Azghadi  
   [arXiv:2603.06699](https://arxiv.org/abs/2603.06699)
38. **On-Orbit Real-Time Wildfire Detection Under On-Board Constraints**  
   Matthias Rötzer ⋅ Veronika Pörtge ⋅ Martin Ickerott ⋅ Jayendra Chorapalli ⋅ Dimitri Scheftelowitsch ⋅ Max Bereczky ⋅ Dmitry Rashkovetsky ⋅ Sai Appalla ⋅ Julia Gottfriedsen  
   [arXiv:2605.06273](https://arxiv.org/abs/2605.06273)
39. **OneHSI: A Unified Hyperspectral Foundation Model with Physical Consistency**  
   Yufei WEN ⋅ Jingdan KANG ⋅ SHUXIN ZHONG ⋅ Yuting Zhang ⋅ Yutong Feng ⋅ Jintai Chen ⋅ Kaishun Wu
40. **Online Segment 3D Gaussians via Launching Virtual Drones**  
   Liwei Liao ⋅ Rongjie Wang ⋅ Ronggang Wang  
   [arXiv:2607.01628](https://arxiv.org/abs/2607.01628)
41. **Open-Weather Robust 3D Detection via Dual-Critic Diffusion Alignment**  
   Shuyao Li ⋅ Chuanxing Geng ⋅ heyang sun ⋅ Qiang Zhou ⋅ Jingjing Gu  
   [arXiv:2607.01983](https://arxiv.org/abs/2607.01983)
42. **OpenEarthAgent: A Unified Framework for Tool-Augmented Geospatial Agents**  
   Akashah Shabbir ⋅ Muhammad Umer Sheikh ⋅ Muhammad Akhtar Munir ⋅ Hiyam Debary ⋅ Mustansar Fiaz ⋅ Muhammad Zaigham Zaheer ⋅ Paolo Fraccaro ⋅ Fahad Shahbaz Khan ⋅ Muhammad Haris Khan ⋅ Xiao Xiang Zhu ⋅ Salman Khan  
   [arXiv:2602.17665](https://arxiv.org/abs/2602.17665) · [code](https://github.com/mbzuai-oryx/OpenEarthAgent)
43. **OrthoTrack: Continuous 6-DoF UAV Trajectory Estimation Anchored in Public Orthophotos**  
   Oussema Dhaouadi ⋅ Zuria Bauer ⋅ Johannes Meier ⋅ Olaf Wysocki ⋅ Marc Pollefeys ⋅ Daniel Cremers  
   [arXiv:2606.25245](https://arxiv.org/abs/2606.25245) · [project](http://orthotrack.ethz.ch)
44. **Pixel Ignores, Superpixel Sees: Adverse Weather Image Restoration via Semantic-Center SSM**  
   Dayu Li ⋅ shihao zhou ⋅ SHU LEIZHI ⋅ Jin Wu ⋅ Chi Man VONG ⋅ Jufeng Yang  
   [arXiv:2608.01760](https://arxiv.org/abs/2608.01760)
45. **Pixel-wise Geo-registration of Drone and Satellite Images**  
   Qingyang Liu ⋅ David G Shatwell ⋅ Parth Parag Kulkarni ⋅ Shah Mubarak
46. **PMGC-SimVP: Parametric Multi-scale Gated Convolution for Global Ionospheric TEC Prediction**  
   Yu Xia ⋅ Yingkui Gong ⋅ Hao Zhang
47. **PriorEye: Geospatial Visual Priors for End-to-End Autonomous Driving**  
   Kyuhwan Yeon ⋅ Benjamin Ramtoula ⋅ Daniele De Martini  
   [arXiv:2606.31830](https://arxiv.org/abs/2606.31830) · [project](https://ori-mrg.github.io/PriorEye)
48. **ProSR: Semantic-Prototype-Guided Discrete Modeling for Physically Consistent SAR Super-Resolution**  
   Byoungwoo Kim ⋅ Munchurl Kim
49. **Pushing the Limits of High-Resolution Weather Forecasting through Data Scaling**  
   Yang Zhao ⋅ Peisong Niu ⋅ Tian Zhou ⋅ Ziqing Ma ⋅ Guanlong Ma ⋅ Rong Jin ⋅ Huiling Yuan ⋅ Liang Sun  
   [arXiv:2608.14652](https://arxiv.org/abs/2608.14652)
50. **QVAM: Query-guided View-aware Adaptive Modulation for Aerial-Ground Person Re-Identification**  
   Mengfei Zhou ⋅ Lin Wan
51. **RainODE: Continuous-Time Precipitation Forecasting with Latent Neural ODEs**  
   Yeeun Seong ⋅ Doyi Kim ⋅ Minseok Seo ⋅ Changick Kim  
   [arXiv:2606.29855](https://arxiv.org/abs/2606.29855) · [code](https://github.com/SeongYE/RainODE)
52. **Rectified Embedding Flow Learning for Aerial Multi-view&#xa0;&#xa0;Geo-localization**  
   Hao Ruan ⋅ Jinliang Lin ⋅ Yingxin Lai ⋅ Zhiming Luo ⋅ Shaozi Li ⋅ Yu Zang ⋅ Cheng Wang
53. **SARA: Structure-Aware Riemannian-Guided Alignment for Drone Image-Text Retrieval**  
   Keyu Lu ⋅ Qing Ma ⋅ Zhenyu Lu ⋅ Cong Bai
54. **SceneDiff: A Benchmark and Method for Multiview Object Change Detection**  
   Yuqun Wu ⋅ Chih-Hao Lin ⋅ Henry Che ⋅ Aditi Tiwari ⋅ Chuhang Zou ⋅ Shenlong Wang ⋅ Derek Hoiem  
   [arXiv:2512.16908](https://arxiv.org/abs/2512.16908) · [project](https://yuqunw.github.io/SceneDiff)
55. **SegFly: A 2D-3D-2D Paradigm for Aerial RGB-Thermal Semantic Segmentation at Scale**  
   Markus Gross ⋅ Sai Matha ⋅ Rui Song ⋅ Viswanathan Muthuveerappan ⋅ Conrad Christoph ⋅ Julius Huber ⋅ Daniel Cremers  
   [arXiv:2603.17920](https://arxiv.org/abs/2603.17920) · [code](https://github.com/markus-42/SegFly)
56. **Semantic-Aware, Physics-Informed, Geometry-Grounded Weather Synthesis**  
   Chenghao Qian ⋅ Nedko Savov ⋅ Lingdong Kong ⋅ Yeying Jin ⋅ Rui Song ⋅ Wenjing Li ⋅ Zhun Zhong ⋅ Jiaqi Ma ⋅ Gustav Markkula ⋅ Luc Van Gool
57. **Semantic-Geometric Dual Compression: Training-Free Visual Token Reduction for Ultra-High-Resolution Remote Sensing Understanding**  
   yueying li ⋅ Fengxiang Wang ⋅ Yan Li ⋅ Mingshuo Chen ⋅ Mengying Zhao ⋅ Long Lan  
   [arXiv:2604.11122](https://arxiv.org/abs/2604.11122)
58. **SemCityLoc: Aerial 6DoF Localization Using Semantic 3D City Models**  
   Jingfeng Mao ⋅ Xuyang Chen ⋅ Qilin Zhang ⋅ Oussema Dhaouadi ⋅ Guangming Wang ⋅ Brian Sheil ⋅ Daniel Cremers ⋅ Yan Xia ⋅ Olaf Wysocki  
   [arXiv:2606.27444](https://arxiv.org/abs/2606.27444) · [project](https://albertchen98.github.io/SemCityLoc)
59. **SFDATrack: Generalized Source-Free Domain Adaptive Tracking Under Adverse Weather Conditions**  
   Siyuan Yao ⋅ Ziqi Wang ⋅ Junqi Huang ⋅ Ruiqi Yu ⋅ Wenqi Ren ⋅ Xiaochun Cao  
   [arXiv:2607.00369](https://arxiv.org/abs/2607.00369) · [code](https://github.com/watcherBR0/sfdatrack)
60. **SGP2: Coarse-to-Fine Controllable Multimodal Remote Sensing Image Generation**  
   Pengyu Chen ⋅ Xi Yang ⋅ Nannan Wang
61. **Skyfall-GS: Synthesizing Immersive 3D Urban Scenes from Satellite Imagery**  
   Jie-Ying Lee ⋅ Yi-Ruei Liu ⋅ Shr-Ruei Tsai ⋅ Wei-Cheng Chang ⋅ Chung-Ho Wu ⋅ Jiewen Chan ⋅ Zhenjun Zhao ⋅ Chieh Hubert Lin ⋅ Yu-Lun Liu  
   [arXiv:2510.15869](https://arxiv.org/abs/2510.15869) · [project](https://skyfall-gs.jayinnn.dev/)
62. **SkySplat-OV: Generalizable Language Gaussian Splatting for Open-Vocabulary Scene Understanding from Sparse Satellite Views**  
   Xuejun Huang ⋅ Yi Wan ⋅ Lei Yu ⋅ Xinyi Liu ⋅ Zhi Zheng ⋅ Bin Zhang ⋅ Yingying Pei ⋅ Yi Liu ⋅ Changjun Zhu ⋅ Yi Liu ⋅ Xiangyuan Cai ⋅ Hongwei Hu ⋅ Xin Zhang ⋅ Yongjun Zhang
63. **STARLINC: Satellite Trail Artifact Removal using Inter-Frame Correlation**  
   Shingeon Kim ⋅ Hyeyoon Lee ⋅ Dain Kwon ⋅ Kanghyun Choi ⋅ SunJong Park ⋅ Mi-Ryang Kim ⋅ Jeong-Eun Lee ⋅ Jinho Lee
64. **StratoSplat: Taming Layered Regularities for Sparse Aerial 3D Gaussian Splatting**  
   Zihan Gao ⋅ Lingling Li ⋅ Licheng Jiao ⋅ Fang Liu ⋅ Wenping Ma ⋅ Yuwei Guo ⋅ Shuyuan Yang
65. **TerraDiT-Ω: Unified Spatial Control for Satellite Image Synthesis with Any Geospatial Primitive**  
   Brian Wei ⋅ Srikumar Sastry ⋅ Daniel Cher ⋅ Eric Xing ⋅ Nathan Jacobs  
   [arXiv:2606.31029](https://arxiv.org/abs/2606.31029) · [code](https://github.com/mvrl/TerraDiT)
66. **TerrainGraphNet: Terrain-Constrained Graph Reasoning for Landslide Segmentation**  
   SHAHID SHAFI DAR ⋅ Pranjal Pandey ⋅ Nagendra Kumar
67. **Tesselating The Earth**  
   Daniel Cher ⋅ Hamza Iqbal ⋅ Eric Xing ⋅ Brian Wei ⋅ Nathan Jacobs  
   [arXiv:2606.27514](https://arxiv.org/abs/2606.27514) · [code](https://github.com/mvrl/TTE)
68. **UnderOneFacade: Worldwide Facade Semantic Segmentation Benchmark Dataset**  
   Yi Wang ⋅ Fan Wang ⋅ Prabin Gyawali ⋅ Ziyang Xu ⋅ Anna Klimkowska ⋅ Yixiong Jing ⋅ Wanru Yang ⋅ Filip Biljecki ⋅ Christoph Holst ⋅ Benjamin Busam ⋅ Brian Sheil ⋅ Olaf Wysocki  
   [arXiv:2607.02018](https://arxiv.org/abs/2607.02018)
69. **VIGA: View-Conditioned and Identity-Guided Adaptation for Aerial-Ground Person Re-Identification**  
   XU ZHANG ⋅ Feng Yining ⋅ ZUYU ZHANG
70. **VVSim: A Large-Scale Aerial-Ground Dataset and Benchmark for Cooperative Perception**  
   Zengle Zhu ⋅ Zhen LI ⋅ Tianyi Huai ⋅ Tianshun Li ⋅ Zihang Xu ⋅ Liuqing Yang ⋅ Rongqing Zhang ⋅ Xinhu Zheng
71. **Weather-Conditioned Depth Anything**  
   Zhaoming Xu ⋅ Chan-Wei Hu ⋅ Kuan-Ru Huang ⋅ Zihao Zhu ⋅ Renjie Li ⋅ Yang Zhou ⋅ Zhengzhong Tu
72. **WeatherReasonSeg: A Benchmark for Weather-Aware Reasoning Segmentation in Visual Language Models**  
   Wanjun Du ⋅ Zifeng Yuan ⋅ Tingting Chen ⋅ Fucai Ke ⋅ Beibei Lin ⋅ Shunli Zhang  
   [arXiv:2603.17680](https://arxiv.org/abs/2603.17680)
73. **WildDepth: A Multimodal Dataset for 3D Wildlife Perception and Depth Estimation**  
   Muhammad Aamir ⋅ Naoya Muramatsu ⋅ Sangyun Shin ⋅ Matthew Wijers ⋅ Jia-Xing Zhong ⋅ Xinyu Hou ⋅ Amir Patel ⋅ Andrew Loveridge ⋅ Andrew Markham  
   [arXiv:2603.16816](https://arxiv.org/abs/2603.16816)
74. **WildProp: Visual Estimation of Wildlife Body Proportions at Scale**  
   Mustafa Chasmai ⋅ Aaron Sun ⋅ Subhransu Maji  
   [arXiv:2606.31125](https://arxiv.org/abs/2606.31125)

## Audio-Visual, Speech & Tactile Sensing

*57 papers · 46 with links*

1. **A First Exploration of Neuromorphic OT-CFM for Multi-Speaker VSR**  
   Lin Chen ⋅ Jingping Fang ⋅ Hairui Liu ⋅ Chenyang Xu ⋅ Junhao Chen ⋅ Xiaorui Li ⋅ Weidong Cai ⋅ Xiaoming Chen  
   [arXiv:2606.31225](https://arxiv.org/abs/2606.31225)
2. **AdaDexGrasp: Adaptive Dexterous Grasping via 3D Visuo-Tactile Representation Fusion**  
   Xirui Liang ⋅ Jingkai Xu ⋅ Jiaqi Liang ⋅ Yuran Wang ⋅ Ruochong Li ⋅ Yuanpei Chen ⋅ Masayoshi TOMIZUKA ⋅ Wei Zhan ⋅ Ruihai Wu  
   [arXiv:2608.07600](https://arxiv.org/abs/2608.07600)
3. **Audio-Visual Camera Pose Estimation with Passive Scene Sounds and In-the-Wild Video**  
   Ikechukwu D Adebi ⋅ Sagnik Majumder ⋅ Kristen Grauman  
   [arXiv:2512.12165](https://arxiv.org/abs/2512.12165) · [project](http://vision.cs.utexas.edu/projects/av_camera_pose)
4. **Audio-Visual Continual Test-Time Adaptation without Forgetting**  
   Sarthak Kumar Maharana ⋅ Akshay Mehra ⋅ Bhavya Ramakrishna ⋅ Yunhui Guo ⋅ Guan-Ming Su  
   [arXiv:2602.18528](https://arxiv.org/abs/2602.18528)
5. **AVTok: 1D Unified Tokenization for Holistic Audio-Video Generation**  
   Trung Kien Pham ⋅ I Chen ⋅ Qifeng Chen ⋅ Long Chen  
   [arXiv:2606.30811](https://arxiv.org/abs/2606.30811)
6. **Beyond Time Shifts: Adapting Omni-LLM as a Reference-Free Evaluator for Generative Audio-Visual Models**  
   Yijie Qian ⋅ Juncheng Wang ⋅ Chao Xu ⋅ Huihan Wang ⋅ Yuxiang Feng ⋅ Yang Liu ⋅ Baigui Sun ⋅ Yong Liu ⋅ Shujun Wang  
   [arXiv:2607.09091](https://arxiv.org/abs/2607.09091)
7. **C3ASD: Multi-Level Consistency-Driven Representation Learning for Robust Active Speaker Detection**  
   Jin Hong ⋅ Jisoo Park ⋅ Junseok Kwon
8. **Conditional Flow Matching for Visually-Guided Acoustic Highlighting**  
   Hugo Malard ⋅ Gael Le Lan ⋅ Daniel Wong ⋅ David Alon ⋅ YI-CHIAO WU ⋅ Sanjeel Parekh  
   [arXiv:2602.03762](https://arxiv.org/abs/2602.03762)
9. **Conversational Human Audio-visual Talking Dialogue Generation**  
   Junhao Song ⋅ Lluis Guasch ⋅ Xilin He ⋅ zhongyu yang ⋅ Yingfang Yuan ⋅ Weicheng Xie ⋅ Linlin Shen ⋅ Lin Haijun ⋅ Shizhe Liu ⋅ Wei Pang ⋅ Siyang Song  
   [arXiv:2607.02799](https://arxiv.org/abs/2607.02799)
10. **DAP: Doppler-aware Point Network for Heterogeneous mmWave Action Recognition**  
   Jiaying Lin ⋅ Shiman Wu ⋅ Jinfu Liu ⋅ Can Wang ⋅ Mengyuan Liu  
   [arXiv:2605.09604](https://arxiv.org/abs/2605.09604)
11. **DASH: Dynamic Audio-Driven Semantic Chunking for Efficient Omnimodal Token Compression**  
   Bingzhou Li ⋅ Tao Huang  
   [arXiv:2603.15685](https://arxiv.org/abs/2603.15685) · [code](https://github.com/laychou666/DASH)
12. **Deform360: A Massive Multi-view Visuotactile Dataset for Deformable World Models**  
   Hongyu Li ⋅ Wanjia Fu ⋅ Xiaoyan Cong ⋅ Zekun Li ⋅ Binghao Huang ⋅ Hanxiao Jiang ⋅ Xintong He ⋅ Yiqing Liang ⋅ Rao Fu ⋅ Tao Lu ⋅ Srinath Sridhar ⋅ Kevin Smith ⋅ George Konidaris ⋅ Yunzhu Li  
   [arXiv:2607.05390](https://arxiv.org/abs/2607.05390) · [project](https://deform360.lhy.xyz)
13. **Delayed Bidirectional Alignment via Disentangled Audio Semantics for Audio-Visual Segmentation**  
   Jingqi Tian ⋅ Yiheng Du ⋅ Haoji Zhang ⋅ Yuji Wang ⋅ Isaac Ning Lee ⋅ Xulong Bai ⋅ Tianrui Zhu ⋅ Jingxuan Niu ⋅ Yansong Tang  
   [arXiv:2512.20117](https://arxiv.org/abs/2512.20117) · [project](https://trilarflagz.github.io/DDAVS-page/)
14. **Don't Let the Video Speak: Audio-Contrastive Preference Optimization for Audio-visual Language Models**  
   Ami Baid ⋅ Zihui Xue ⋅ Kristen Grauman
15. **HiChor: Hierarchical Choreography Generation from Pop Music with Choreographic Primitives**  
   Jungsu Kim ⋅ Jungwoo Huh ⋅ Jeongwook Choi ⋅ Wen-Huang Cheng ⋅ Jian-Yu Jiang-Lin ⋅ Weisi Lin ⋅ Sanghoon Lee
16. **HolisticSemGes: Semantic Grounding of Holistic Co-Speech Gesture Generation with Contrastive Flow-Matching**  
   Lanmiao Liu ⋅ Esam Ghaleb ⋅ asli ozyurek ⋅ Zerrin Yumak
17. **HumanOmni-Speaker: Identifying Who said What and When**  
   Detao Bai ⋅ Xihan Wei ⋅ Zhiheng Ma  
   [arXiv:2603.21664](https://arxiv.org/abs/2603.21664)
18. **HybridSim: A Physics–Learning Hybrid Digital Twin for mmWave Human Sensing**  
   Weitao Xiong ⋅ Tianyu Liu ⋅ Peng Li ⋅ KOK CHUNG CHUA ⋅ Toa Khim ⋅ Pu Wang ⋅ Hongfei Xue  
   [arXiv:2607.15806](https://arxiv.org/abs/2607.15806) · [project](https://weitao-xiong.github.io/HybridSim/)
19. **ID-LoRA: Identity-Driven Audio-Video Personalization with In-Context LoRA**  
   Aviad Dahan ⋅ Moran Yanuka ⋅ Noa Kraicer ⋅ Lior Wolf ⋅ RAJA GIRYES  
   [arXiv:2603.10256](https://arxiv.org/abs/2603.10256)
20. **JAM-Flow: Joint Audio-Motion Synthesis with Flow Matching**  
   Mingi Kwon ⋅ Joonghyuk Shin ⋅ Jaeseok Jeong ⋅ Jaesik Park ⋅ Youngjung Uh  
   [arXiv:2506.23552](https://arxiv.org/abs/2506.23552) · [project](https://joonghyuk.com/jamflow-web)
21. **JoVA: Unified Multimodal Learning for Joint Video-Audio Generation and Editing**  
   Xiaohu Huang ⋅ Haoyang He ⋅ Hao Zhou ⋅ Qiangpeng Yang ⋅ Min Zheng ⋅ Kai Han  
   [arXiv:2512.13677](https://arxiv.org/abs/2512.13677) · [project](https://visual-ai.github.io/jova)
22. **MAVIN: Multi-Shot Audio-Visual Generation with Customized Narrative Control**  
   Kaiqi Liu ⋅ Yunyao Mao ⋅ Ziqi Cai ⋅ Zheng Geng ⋅ Jing Wang ⋅ Qiulin Wang ⋅ Xintao Wang ⋅ Pengfei Wan ⋅ Kun Gai ⋅ Shuchen Weng ⋅ Boxin Shi  
   [arXiv:2606.29473](https://arxiv.org/abs/2606.29473)
23. **MeanTalker: Efficient and Expressive Speech-Driven 3D Facial Animation via Geometric-Aware Mean Flow**  
   Zhongyuan Zhao ⋅ Zhihao Li ⋅ Qing Li ⋅ Leidong Fan ⋅ KANGLIN LIU
24. **Meric: A Unified Framework for Multimodal Music Generation and Retrieval via Representation Space Anchoring**  
   Xihua Wang ⋅ Yinbo Wang ⋅ Jingchao Zhang ⋅ Ruihua Song
25. **MGM-Omni: Scaling Omni LLMs to Personalized Long-Horizon Speech**  
   Chengyao Wang ⋅ Zhisheng Zhong ⋅ Bohao PENG ⋅ Senqiao Yang ⋅ Yuqi Liu ⋅ Haokun GUI ⋅ Bin Xia ⋅ Jingyao Li ⋅ Bei Yu ⋅ Jiaya Jia  
   [arXiv:2509.25131](https://arxiv.org/abs/2509.25131) · [code](https://github.com/dvlab-research/MGM-Omni)
26. **MindFlow: Harmonizing Cognitive Semantics and Acoustic Dynamics for Facial Animation Generation in Dyadic Conversations**  
   Hejia Chen ⋅ Haoxian Zhang ⋅ Xu He ⋅ Xiaoqiang Liu ⋅ Pengfei Wan ⋅ Shoulong Zhang ⋅ Shuai Li  
   [arXiv:2606.27779](https://arxiv.org/abs/2606.27779)
27. **MMControl: Unified Multi-Modal Control for Joint Audio-Video Generation**  
   Liyang Li ⋅ Wen Wang ⋅ Canyu Zhao ⋅ Tianjian Feng ⋅ Zhiyue Zhao ⋅ Hao Chen ⋅ Chunhua Shen  
   [arXiv:2604.19679](https://arxiv.org/abs/2604.19679) · [project](https://aim-uofa.github.io/MMControl/)
28. **Music-to-Dance Generation via Atomic Movements**  
   Xinhao Cai ⋅ Yixuan Sun ⋅ Minghang Zheng ⋅ Qingchao Chen ⋅ Xin Jin ⋅ Song-Chun Zhu ⋅ Yang Liu  
   [arXiv:2607.13978](https://arxiv.org/abs/2607.13978)
29. **MuSViT: A Foundation Vision Model for Sheet Music Representation**  
   Carlos Penarrubia ⋅ Antonio Rios-Vila ⋅ Eliseo Fuentes-Martinez ⋅ Juan Martinez-Sevilla ⋅ Francisco Castellanos ⋅ María Alfaro-Contreras ⋅ Jorge Calvo-Zaragoza  
   [arXiv:2606.31811](https://arxiv.org/abs/2606.31811)
30. **Objects as Audio-Visual Modal Sound Fields**  
   Zisen Shao ⋅ Zihao Wei ⋅ Derong Jin ⋅ Ruohan Gao  
   [arXiv:2608.05145](https://arxiv.org/abs/2608.05145) · [project](https://zisenshao.github.io/AV-MSF/)
31. **OmniForcing: Unleashing Real-time Joint Audio-Visual Generation**  
   Yaofeng Su ⋅ Yuming Li ⋅ Zeyue Xue ⋅ Jie Huang ⋅ Siming Fu ⋅ Haoran Li ⋅ Haoyang Huang ⋅ Nan Duan  
   [arXiv:2603.11647](https://arxiv.org/abs/2603.11647) · [project](https://omniforcing.com)
32. **OmniScript: Towards Audio-Visual Script Generation for Long-Form Cinematic Video**  
   JUNFU PU ⋅ Yuxin Chen ⋅ Teng Wang ⋅ Ying Shan  
   [arXiv:2604.11102](https://arxiv.org/abs/2604.11102) · [project](https://arcomniscript.github.io)
33. **Precise Video-to-Audio Generation with Cross-Modal Alignment in Latent Space**  
   Thanh V. T. Tran ⋅ Ngoc-Son Nguyen ⋅ Luong Tran ⋅ Long-Khanh Pham ⋅ Paarth Neekhara ⋅ Shehzeen Hussain ⋅ Van Nguyen  
   [arXiv:2607.06405](https://arxiv.org/abs/2607.06405)
34. **Q-TriM: Question-Guided Tri-Modal Attention for Audio–Visual Question Answering**  
   SungHun Kim ⋅ Seung Baek  
   [arXiv:2607.03825](https://arxiv.org/abs/2607.03825) · [code](https://github.com/Sunghun95/Q-TriM)
35. **Recognizing Co-Speech Gestures in-the-Wild**  
   Sindhu Hegde ⋅ K R Prajwal ⋅ Andrew ZISSERMAN  
   [arXiv:2605.31589](https://arxiv.org/abs/2605.31589) · [project](https://www.robots.ox.ac.uk/~vgg/research/grw)
36. **See &amp; Sniff: Learning Visuo-Olfactory Representations**  
   Seongyu Kim ⋅ Seungwoo Lee ⋅ Hyeonggon Ryu ⋅ Joon Son Chung ⋅ Arda Senocak
37. **Seeing Touch from Motion: A Unified Modality-Aware Visuo-Tactile Policy with Tactile Motion Correlation**  
   Shengqi Xu ⋅ Yang Liu ⋅ Guojin Zhong ⋅ Fanjie Wang ⋅ Hu Luo ⋅ Hanyu Zhou ⋅ WeiYao Zhang ⋅ Ziyi Ye ⋅ Zuxuan Wu ⋅ Yu-Gang Jiang  
   [arXiv:2606.29941](https://arxiv.org/abs/2606.29941) · [project](https://shengqi77.github.io/Seeing-Touch-from-Motion/)
38. **SICAGE: Speaker-Independent Culture-Aware Gesture Generation using TED4C-L Dataset**  
   Ariel Gjaci ⋅ Antonio Sgorbissa ⋅ Vittorio Murino  
   [arXiv:2606.30001](https://arxiv.org/abs/2606.30001)
39. **Sound-based Multi-Person 3D Pose Estimation**  
   Yusuke Oumi ⋅ Yuto Shibata ⋅ Go Irie ⋅ Akisato Kimura ⋅ Yoshimitsu Aoki ⋅ Mariko Isogawa
40. **SpEmoC: A Balanced Speaker-Segment Multimodal Emotion Benchmark**  
   Sania Bano ⋅ Shahzad Ahmad ⋅ Santosh Vipparthi ⋅ Sukalpa Chanda ⋅ Subrahmanyam Murala  
   [arXiv:2607.18109](https://arxiv.org/abs/2607.18109)
41. **Step-by-Step Video-to-Audio Synthesis via Negative Audio Guidance**  
   Akio Hayakawa ⋅ Masato Ishii ⋅ Takashi Shibuya ⋅ Yuki Mitsufuji  
   [arXiv:2506.20995](https://arxiv.org/abs/2506.20995) · [project](https://ahykw.github.io/sbsv2a/)
42. **StreamTalk: Streaming Co-Speech Gesture Generation with Key-Pose Anchoring**  
   Jianfang Li ⋅ Xiangyue Zhang ⋅ Jiaxu Zhang ⋅ Kaixing Yang ⋅ Steven Hoi  
   [arXiv:2608.01643](https://arxiv.org/abs/2608.01643) · [project](https://xiangyue-zhang.github.io/StreamTalk/)
43. **Structured-Noise Masked Modeling for Video, Audio and Beyond**  
   Aritra Bhowmik ⋅ Carlos Hinojosa ⋅ Fida Mohammad Thoker ⋅ Bernard Ghanem ⋅ Cees Snoek  
   [arXiv:2503.16311](https://arxiv.org/abs/2503.16311)
44. **SyncCache: Exploiting Asymmetric Dynamics for Fast Audio-Driven Portrait Animation**  
   Juncheng Ma ⋅ Yuxuan Du ⋅ Sun Yanan ⋅ Zhening Xing ⋅ Changlin Li ⋅ Zhenyu Tang ⋅ Bo Li ⋅ Peng-Tao Jiang ⋅ Li Yuan ⋅ Daquan Zhou ⋅ Yonghong Tian  
   [arXiv:2606.30849](https://arxiv.org/abs/2606.30849)
45. **Tac2Real: Reliable and GPU Visuotactile Simulation for Online Reinforcement Learning and Zero-shot Real-World Deployment**  
   Ningyu YAN ⋅ Shuai Wang ⋅ Xing Shen ⋅ Hui Wang ⋅ Hanqing Wang ⋅ Yang Xiang ⋅ Jiangmiao Pang  
   [arXiv:2603.28475](https://arxiv.org/abs/2603.28475) · [project](https://ningyurichard.github.io/tac2real-project-page/)
46. **Tactile Modality Fusion for Vision-Language-Action Models**  
   Charlotte Morissette ⋅ Amin Abyaneh ⋅ Wei-Di Chang ⋅ Anas Houssaini ⋅ David Meger ⋅ Hsiu-Chin Lin ⋅ Jonathan Tremblay ⋅ Gregory Dudek  
   [arXiv:2603.14604](https://arxiv.org/abs/2603.14604) · [project](https://charliem7.github.io/projects/TacFilm/)
47. **Text Dictates, Music Decorates: Energy-based Attention for Editable Dance Generation**  
   Seong Jong Yoo ⋅ Siyuan Peng ⋅ Felix Gu ⋅ Stratis Aloimonos ⋅ Cornelia Fermuller  
   [arXiv:2606.22726](https://arxiv.org/abs/2606.22726) · [code](https://github.com/SeongJong-Yoo/STREAM)
48. **Text-based Tactile Graphics Generation for the Visually Impaired**  
   Ruihan Gao ⋅ Joonghyuk Shin ⋅ Ava Pun ⋅ Jaesik Park ⋅ Wenzhen Yuan ⋅ Jun-Yan Zhu  
   [arXiv:2607.22674](https://arxiv.org/abs/2607.22674) · [project](https://ruihangao.github.io/Text2TactileGraphics/)
49. **Towards Flexible, Natural, Efficient Interaction for Conversational Talking Face Generation**  
   Baiqin Wang ⋅ Sen Chen ⋅ Jiankuo Zhao ⋅ Xiangyu Liu ⋅ Zhen Lei ⋅ Xiangyu Zhu  
   [arXiv:2606.31088](https://arxiv.org/abs/2606.31088) · [project](https://bq-wang0511.github.io/InterTalk/)
50. **Unison: Harmonizing Motion, Speech, and Sound for Human-Centric Audio-Video Generation**  
   Shihao Cheng ⋅ Jiaxu Zhang ⋅ Quanyue Song ⋅ Shansong Liu ⋅ Guo Zhi ⋅ Xiao-Lei Zhang ⋅ Chi Zhang ⋅ Xuelong Li ⋅ Zhigang Tu  
   [arXiv:2605.08729](https://arxiv.org/abs/2605.08729)
51. **UniTac: A Unified Multimodal Model for Cross-Sensor Tactile Understanding and Generation**  
   Jiahang Tu ⋅ Fengyu Yang ⋅ Chenyang Ma ⋅ Xihang Yu ⋅ Ziyao Zeng ⋅ Shaokai Wu ⋅ Hanbin Zhao ⋅ Zhi Tao ⋅ Chao Zhang ⋅ Hui Qian ⋅ Alex Wong  
   [arXiv:2606.31451](https://arxiv.org/abs/2606.31451)
52. **Video-HolmesV2: Can MLLMs Reason with Spatio-Temporal Audio-Visual Evidence in Long Videos?**  
   Zhaoyang Wei ⋅ Zipeng Wang ⋅ Yushe Cao ⋅ Chenhui Qiang ⋅ Shuaibing Cheng ⋅ Xuesong Yang ⋅ Sen Nie ⋅ Bowen Jiang ⋅ Wenchao Ding ⋅ Yanchao Hao ⋅ Zheng Wei ⋅ Xuehui Yu ⋅ Zhenjun Han
53. **VisTa3D: A Dataset and Benchmark for Vision, Tactile, and 3D Point Clouds-based Thin Object Reconstruction**  
   Shania Guo ⋅ Yeongsik Seo ⋅ Andrew Fu ⋅ Mei Hao ⋅ Iris Xia ⋅ Jiwon Lee ⋅ Xinyi Xie ⋅ Hyoungseob Park ⋅ Aaron Dollar ⋅ Alex Wong
54. **VoCa: Unified Autoregressive Modeling for Talking Audio-Video Generation**  
   Zhuofan Zong ⋅ Jiale Yuan ⋅ Yufei Liu ⋅ Dongzhi Jiang ⋅ Hao Shao ⋅ Zimu Lu ⋅ Ke Wang ⋅ Yunqiao Yang ⋅ Mingjie Zhan ⋅ Hongsheng LI
55. **Wake up for Touch! Mask-isolated Tactile Alignment Learning in MLLMs**  
   Yoonhyung Park ⋅ Minji Kim ⋅ Sungwon Moon ⋅ Jiyoung Lee  
   [arXiv:2607.00302](https://arxiv.org/abs/2607.00302) · [project](http://mmai.ewha.ac.kr/splash/)
56. **What Images Cannot Say: Language-Guided Olfactory Representation Learning**  
   Eleftherios Tsonis ⋅ Xi WANG ⋅ Vicky Kalogeiton  
   [arXiv:2607.06402](https://arxiv.org/abs/2607.06402) · [project](https://www.lix.polytechnique.fr/vista/projects/2026_scent_tsonis/)
57. **Whence the Voice? Self-supervised Dual-source Audio-Visual Localisation via Selective Convergence**  
   Han Hu ⋅ Dongheng Lin ⋅ Yuqi Hou ⋅ Haotian LI ⋅ Hyung Jin Chang ⋅ Jianbo Jiao  
   [arXiv:2608.05816](https://arxiv.org/abs/2608.05816)

# Unclassified


## Other / Uncategorized

*26 papers · 20 with links*

1. **AIMold: An Autonomous AI-based Pipeline for Complex Mold Design**  
   Pengyun Qiu ⋅ Shuo Wang ⋅ Zeyuan Chen ⋅ Yihao Zhi ⋅ Chongjie Ye ⋅ XIAOGUANG HAN  
   [arXiv:2608.00800](https://arxiv.org/abs/2608.00800) · [code](https://github.com/tb2-sy/AIMold)
2. **ARGENT: Adaptive Hierarchical Image-Text Representations**  
   Chuong Huynh ⋅ Hossein Souri ⋅ Abhinav Kumar ⋅ Vitali Petsiuk ⋅ Deen Dayal Mohan ⋅ Suren Kumar  
   [arXiv:2603.23311](https://arxiv.org/abs/2603.23311)
3. **Attention is Case-Sensitive**  
   Maximilian Dillitzer ⋅ Tin Stribor Sohn ⋅ Jason Corso ⋅ Michael Auerbach  
   [arXiv:2608.03711](https://arxiv.org/abs/2608.03711)
4. **Automatic Method Illustration Generation for AI Scientific Papers via Drawing Middleware Creation, Evolution, and Orchestration**  
   ZHUOLING Li ⋅ Jiarui Zhang ⋅ Ping Hu ⋅ Jason Kuen ⋅ Jiuxiang Gu ⋅ Hossein Rahmani ⋅ Jun Liu  
   [arXiv:2603.29590](https://arxiv.org/abs/2603.29590)
5. **AutoPhyX: Automatic Text-Condition Physics Property Generation**  
   Bei Huang ⋅ Yixin Chen ⋅ Hongbin Zha ⋅ Yuru Pei ⋅ Siyuan Huang
6. **Bottom-up modeling of repeated elements via single image analysis-by-synthesis**  
   syrine kalleli ⋅ Alexei Efros ⋅ Mathieu Aubry
7. **Bridging the Geometry Mismatch: Frequency-Aware Anisotropic Serialization for Thin-Structure SSMs**  
   Jin Bai ⋅ Huiyao Zhang ⋅ Qi Wen ⋅ Ningyang Li ⋅ Shengyang Li ⋅ Atta ur Rahman ⋅ Xiaolin Tian  
   [arXiv:2603.28503](https://arxiv.org/abs/2603.28503)
8. **Color Pass-Through via Camera-Display Coupling**  
   Ruikang Li ⋅ Molin Li ⋅ Jiarui Wu ⋅ Zhe Wei ⋅ Pengpeng Liu ⋅ Tianfan Xue  
   [arXiv:2607.12746](https://arxiv.org/abs/2607.12746) · [project](https://lyricccco.github.io/color-pass-through/)
9. **From Synchrony to Sequence: Exo-to-Ego Generation via Interpolation**  
   Mohammad Mahdi ⋅ Nedko Savov ⋅ Danda Paudel ⋅ Luc Van Gool  
   [arXiv:2604.13793](https://arxiv.org/abs/2604.13793)
10. **FUSE: A Flow-based Mapping Between Shapes**  
   Lorenzo Olearo ⋅ Giulio Viganò ⋅ Daniele Baieri ⋅ Filippo Maggioli ⋅ Simone Melzi  
   [arXiv:2511.13431](https://arxiv.org/abs/2511.13431)
11. **Generation Models Know Space: Unleashing Implicit 3D Priors for Scene Understanding**  
   Xianjin Wu ⋅ Dingkang Liang ⋅ Tianrui Feng ⋅ Kui Xia ⋅ Yumeng Zhang ⋅ Xiaofan Li ⋅ Xiao Tan ⋅ Xiang Bai  
   [arXiv:2603.19235](https://arxiv.org/abs/2603.19235) · [code](https://github.com/H-EmbodVis/VEGA-3D)
12. **Honey, I Shrunk the Arc de Triomphe!**  
   Yuanbo Xiangli ⋅ Hanyu Chen ⋅ Xueqing Tsang ⋅ Noah Snavely  
   [arXiv:2606.02379](https://arxiv.org/abs/2606.02379) · [project](https://metricscenes.github.io/)
13. **LangLoc: “Tell Me What You See”**  
   Shaurya Kishore Panwar ⋅ Roham Zendehdel Nobari ⋅ Shirley Lau ⋅ Abu Bakr Rahman Shaik ⋅ Manuel Günther ⋅ Marc Pollefeys ⋅ Daniel Barath  
   [arXiv:2607.05077](https://arxiv.org/abs/2607.05077)
14. **Lumina-OmniLV: A Unified Multimodal Framework for General Low-Level Vision**  
   Yuandong Pu ⋅ Le Zhuo ⋅ Kaiwen Zhu ⋅ Liangbin Xie ⋅ Wenlong Zhang ⋅ Xiangyu Chen ⋅ Peng Gao ⋅ Yu Qiao ⋅ Chao Dong ⋅ Yihao Liu  
   [arXiv:2504.04903](https://arxiv.org/abs/2504.04903)
15. **PuzLM: Solving Jigsaw Puzzles with Sequence-to-Sequence Language Models**  
   Gur Elkin ⋅ Ofir I Shahar ⋅ Ohad Ben-Shahar  
   [arXiv:2511.06315](https://arxiv.org/abs/2511.06315)
16. **Ray-Path-Aware Virtual Point Removal on 2D Layer-Wise Nearest Point Map**  
   DAEHYEON JEON ⋅ Kyungdon Joo ⋅ Jae-Young Sim
17. **SAMA: Factorized Semantic Anchoring and Motion Alignment for Instruction-Guided Video**  
   Xinyao Zhang ⋅ Wenkai Dong ⋅ YuXin Song ⋅ Bo Fang ⋅ Qi Zhang ⋅ Jing Wang ⋅ Fan Chen ⋅ Hui Zhang ⋅ Haocheng Feng ⋅ Yu Lu ⋅ Hang Zhou ⋅ Chun Yuan ⋅ Jingdong Wang  
   [arXiv:2603.19228](https://arxiv.org/abs/2603.19228)
18. **Task-driven Processing with Coarse-to-Fine Glimpse-based Active Perception**  
   Oleh Kolner ⋅ Thomas Ortner ⋅ Stanislaw Wozniak ⋅ Angeliki Pantazi
19. **Text-Conditioned Background Generation for Editable Multi-Layer Documents**  
   Taewon Kang ⋅ Joseph K J ⋅ Christopher Tensmeyer ⋅ Jihyung Kil ⋅ Wanrong Zhu ⋅ Ming C Lin ⋅ Vlad Morariu  
   [arXiv:2512.17151](https://arxiv.org/abs/2512.17151)
20. **The Dynamic Prior: Understanding 3D Structures for Casual Dynamic Videos**  
   Zhuoyuan Wu ⋅ Xurui Yang ⋅ Jiahui Huang ⋅ Yue Wang ⋅ Jun Gao  
   [arXiv:2512.05398](https://arxiv.org/abs/2512.05398) · [code](https://github.com/wuzy2115/DYNAPO)
21. **Trajectory Forcing: Structure-First Generation with Controllable Semantic Trajectories**  
   Merve Kocabas ⋅ Gege Gao ⋅ Bernhard Schölkopf ⋅ Andreas Geiger  
   [arXiv:2606.22527](https://arxiv.org/abs/2606.22527) · [project](https://mervekocabas.github.io/TrajectoryForcing/)
22. **Unsupervised Pixel-Level Semantic Left-Right Understanding of In-the-Wild Images**  
   Weikang Wang ⋅ Tobias Weißberg ⋅ Florian Bernard  
   [arXiv:2607.05006](https://arxiv.org/abs/2607.05006)
23. **Video2Reaction: Mapping Video to Audience Reaction Distribution in the Wild**  
   Trang Nguyen ⋅ Sidong Zhang ⋅ Shiv Shankar ⋅ Gauri Jagatap ⋅ Deepak Chandran ⋅ Andrea Fanelli ⋅ Madalina Fiterau  
   [arXiv:2607.06875](https://arxiv.org/abs/2607.06875) · [project](https://information-fusion-lab-umass.github.io/video2reaction-bench.github.io)
24. **VIGOR: VIdeo Geometry-Oriented Reward for Temporal Generative Alignment**  
   Tengjiao Yin ⋅ Jinglei Shi ⋅ Heng Guo ⋅ Xi WANG  
   [arXiv:2603.16271](https://arxiv.org/abs/2603.16271) · [project](https://vigor-geometry-reward.com/)
25. **VOID: Video Object and Interaction Deletion**  
   Saman Motamed ⋅ William Harvey ⋅ Benjamin Klein ⋅ Luc Van Gool ⋅ Zhuoning Yuan ⋅ Ta-Ying Cheng
26. **WALL-EVE: World Alignment with Rule Learning in Visual Environments**  
   Siyu Zhou ⋅ Tianyi Zhou ⋅ Yijun Yang ⋅ Deheng Ye ⋅ Chengqi Zhang ⋅ Jing Jiang ⋅ Guodong Long
