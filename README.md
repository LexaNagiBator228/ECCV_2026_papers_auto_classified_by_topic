# ECCV 2026 Accepted Papers — Auto-Classified by Topic

All **2,864 ECCV 2026 accepted papers**, grouped into 30 topics under 8 super-groups, with
arXiv / project-page / code links resolved automatically.

> The source list is preliminary, pending publisher checks.

## Files

| File | What it is |
|---|---|
| [`papers_by_topic.md`](papers_by_topic.md) | Everything in one browsable document: linked table of contents, a recommended-reading section, then all papers grouped by topic with authors and links |
| [`papers_by_topic.csv`](papers_by_topic.csv) | Same data as a table — `group, topic, title, authors, arxiv_url, code_url, project_url, doi` — for filtering and sorting |
| [`topics/`](topics/) | 30 plain-text files, one per topic, alphabetized |
| [`papers_list.txt`](papers_list.txt) | The raw scraped source list |
| [`scripts/`](scripts/) | The classifier and link-resolution pipeline |

## Topic distribution

| Group | Topics (paper count) |
|---|---|
| Generation & Editing | Image Gen/Diffusion 178 · Video Gen/World Models 131 · Editing 88 · 3D Gen 49 |
| Multimodal & Video | MLLM/VLM 283 · Video Understanding 104 · Document/OCR 33 · Retrieval 18 |
| 3D, Geometry & Imaging | 3D Recon/Gaussian Splatting 313 · Depth/Geometry/Pose 129 · Low-Level Vision 100 · Point Cloud 57 · Computational Imaging 27 |
| Recognition & Perception | Detection/Segmentation 150 · Anomaly/OOD 52 · Tracking 31 · Classification 15 |
| Humans, Agents & Autonomy | Human Pose/Motion/Avatars 181 · Embodied/Robotics 148 · Driving 81 · Face/Identity 38 |
| Learning, Efficiency & Trust | Efficiency 103 · Trustworthy AI 89 · Representation/SSL 82 · Transfer/Adaptation 80 · Benchmarks 36 |
| Application Domains | Medical 111 · Remote Sensing 74 · Audio-Visual/Tactile 57 |
| Unclassified | 26 |

## Link coverage

| | Count | Share |
|---|---|---|
| arXiv preprint | 1,725 | 60% |
| Project page | 489 | 17% |
| Code repository | 406 | 14% |

## Method

**Classification** is a weighted keyword/regex scorer over paper titles
([`scripts/classify.py`](scripts/classify.py)). Each topic carries strong signals (weight 6) and
weak ones (weight 2–3); a paper is assigned to its single highest-scoring topic, with ties broken
by a specificity ordering that puts application domains first. Abstracts were not available from
the source page, so titles are the only input.

**Links** were resolved by querying every title against the arXiv API (OR-batched, 10 titles per
request at arXiv's requested 3-second interval), with OpenAlex filling in additional matches. A
match requires ≥0.92 normalized-title similarity; matches cluster tightly at ratio 1.0, so false
positives are unlikely. Project and code URLs are scraped from arXiv abstracts and author comments.

## Known limitations

- **Single-label assignment.** Many papers legitimately span topics, but each is filed under one.
  "Video anomaly detection" lands in Anomaly/OOD, not Video Understanding; the two
  privacy-in-visual-localization papers land in different topics.
- **"Localization" is overloaded.** The Depth/Geometry topic absorbs a handful of papers on
  temporal action localization and forgery/tamper localization, which are unrelated tasks.
- **40% of papers have no link.** Those have no preprint findable on arXiv or OpenAlex — expected
  for freshly-accepted papers, not a lookup failure.
- **Recommendations are title-based judgement,** not a reading of the papers.

## Reproducing

```bash
python3 scripts/classify.py       # titles -> topic labels
python3 scripts/lookup_arxiv.py   # batched arXiv title matching
python3 scripts/fetch_abstracts.py# abstracts -> project/code URLs
python3 scripts/emit_links.py     # render markdown / CSV / per-topic files
```

Paths at the top of each script point at a working directory holding the intermediate JSON.
