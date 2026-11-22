# AI Papers

A living collection of AI research papers, organized by topic: inference, pre-training, and post-training (RL, RLHF, preference optimization). Updated daily from the morning arXiv sweep — new papers land in the topic file that matches their primary angle, with the PDF in [`papers/`](papers/).

## Topics

- [Speculative Decoding](topics/speculative-decoding.md) — draft-and-verify decoding, drafter designs (162 papers)
- [KV-Cache Compression](topics/kv-cache-compression.md) — unified/token-type-aware schemes, low-rank compression, bit-rank allocation (131 papers)
- [KV-Cache Eviction & Management](topics/kv-cache-eviction.md) — eviction scoring, adaptive budgets, capacity planning (65 papers)
- [Quantization](topics/quantization.md) — weight/activation/state quantization for inference (328 papers)
- [Long-Context Memory Compression](topics/long-context-memory-compression.md) — compressing long contexts into memory embeddings (45 papers)
- [Distributed Inference](topics/distributed-inference.md) — disaggregated serving, phase splitting, model parallelism, AI-HPC cluster design (106 papers)
- [Serving Engines](topics/serving-engines.md) — vLLM, SGLang, PagedAttention, schedulers (154 papers)
- [Attention Kernels](topics/attention-kernels.md) — FlashAttention, FlashInfer, IO-aware attention (54 papers)
- [GPU Kernels & Performance Engineering](topics/gpu-kernels.md) — roofline model, GEMM/scan kernel classics, Triton, LLM kernel-generation benchmarks (84 papers)
- [Recurrent & Looped Architectures](topics/recurrent-architectures.md) — looped/recurrent transformers, latent reasoning, adaptive depth (108 papers)
- [Model & Technical Reports](topics/model-reports.md) — model reports with inference-relevant findings (MLA lineage, sparse attention, MoE, open-weight families) (141 papers)
- [Foundational & Frequently-Cited Works](topics/foundational.md) — transformer architecture, pretraining/scaling, efficient-attention lineage, surveys (5,001 papers)
- [LoRA & Adapters](topics/lora.md) — LoRA serving, multi-tenant adapter kernels, adapter formats (48 papers)
- [Weight-Space Programming](topics/weight-space-programming.md) — LLMs that read and write neural network weights: weight-space learning, parameter generation, and model editing and merging in weight space (55 papers)
- [Structured & Constrained Decoding](topics/structured-decoding.md) — guided/constrained generation, FSM logit masking (12 papers)
- [Tokenizers](topics/tokenizers.md) — tokenizer design and its impact on inference (24 papers)
- [Model Compression](topics/model-compression.md) — pruning, sparsity, distillation (288 papers)
- [Pre-Training](topics/pre-training.md) — scaling laws, compute-optimal training, large training runs (564 papers)
- [Post-Training](topics/post-training.md) — instruction tuning, RLHF/RLAIF, preference optimization, RL methods (1308 papers)
- [Harnesses](topics/harnesses.md) — agent harnesses and orchestration runtimes, tool-use loops, decision/context reuse, harness self-improvement, token/cost efficiency of agent scaffolding (2505 papers)

## Adding papers

Each paper goes in `papers/` (kebab-case filename with arXiv ID) and gets a row in its primary topic's table with an arXiv link, authors, date added, an Importance score (see below), and a one-line summary. Entries are not constrained to arXiv: a work published only as a technical blog post, report, or other primary source gets a row linking that source, with no PDF required. Insert the row in the table's reading order: by Importance first, then foundational-before-recent within the same tier.

## Importance

Every paper carries an Importance score for a reader working through LLM inference engineering, and each topic table is sorted in reading order — most important first, with foundational/canonical works ahead of later papers within the same tier.

- ★★★★★ — field-defining: introduced the technique, or the canonical reference later work builds on
- ★★★★☆ — major: widely cited or adopted, benchmark-setting, or used in production systems
- ★★★☆☆ — solid: a real method or result worth reading
- ★★☆☆☆ — incremental: a small improvement, or narrow in scope/applicability
- ★☆☆☆☆ — tangential: marginal relevance to inference engineering

## Stats

- 11,183 papers across 20 topics as of 2026-11-22
- 8,348 PDFs in papers/
