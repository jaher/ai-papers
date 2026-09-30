# KV-Cache Eviction & Management

Papers on KV-cache eviction scoring, adaptive budgets, and management policies — which entries to keep and how much memory to give each request.

| Paper | arXiv | Authors | Added | Summary |
|---|---|---|---|---|
| ActKV: Efficient LLM Agents through Action-Guided KV Cache Management | [2609.31395](https://arxiv.org/abs/2609.31395) | Zihan Wang et al. | 2026-09-29 | First KV-cache compression framework tailored for agentic LLM inference: action-oriented eviction retains entries critical to future *action* generation; confidence-driven adaptive budget allocation grows/shrinks per-request KV budget with model confidence; page-aware compression with customized kernels plugs into paged-memory serving. 98.53% of FullKV accuracy with 25.98% of its peak KV memory; 3.97x token / 3.58x task throughput vs FullKV. |
| Beyond Mean Attention: Diversity-Aware, Layer-Wise Scoring for KV Cache Eviction | [2609.30738](https://arxiv.org/abs/2609.30738) | Tianfang Xie, Wei Zhu | 2026-09-30 | Eviction scoring beyond mean attention: score = μ_i + λ1σ_i + λ2·corr(i,S) — attention dispersion plus redundancy vs already-selected tokens (MMR-style, no extra forward passes). On 16 LongBench datasets at 64 entries/layer, a single global diversification constant improves 13/16; per-dataset search finds a mid-layer sign flip on passage retrieval worth +9.6. A cheap drop-in for SnapKV/PyramidKV-style eviction stacks. |

PDFs: [`../papers/`](../papers/)
