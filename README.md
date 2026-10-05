# AI Papers

A living collection of AI research papers, organized by topic: inference, pre-training, and post-training (RL, RLHF, preference optimization). Updated daily from the morning arXiv sweep — new papers land in the topic file that matches their primary angle, with the PDF in [`papers/`](papers/).

## Topics

- [Speculative Decoding](topics/speculative-decoding.md) — draft-and-verify decoding, drafter designs
- [KV-Cache Compression](topics/kv-cache-compression.md) — unified/token-type-aware schemes, low-rank compression, bit-rank allocation
- [KV-Cache Eviction & Management](topics/kv-cache-eviction.md) — eviction scoring, adaptive budgets, capacity planning
- [Quantization](topics/quantization.md) — weight/activation/state quantization for inference
- [Long-Context Memory Compression](topics/long-context-memory-compression.md) — compressing long contexts into memory embeddings
- [Distributed Inference](topics/distributed-inference.md) — disaggregated serving, phase splitting, model parallelism, AI-HPC cluster design
- [Serving Engines](topics/serving-engines.md) — vLLM, SGLang, PagedAttention, schedulers
- [Attention Kernels](topics/attention-kernels.md) — FlashAttention, FlashInfer, IO-aware attention
- [Recurrent & Looped Architectures](topics/recurrent-architectures.md) — looped/recurrent transformers, latent reasoning, adaptive depth
- [Model & Technical Reports](topics/model-reports.md) — model reports with inference-relevant findings (MLA lineage, sparse attention, MoE, open-weight families)
- [Foundational & Frequently-Cited Works](topics/foundational.md) — transformer architecture, pretraining/scaling, efficient-attention lineage, surveys
- [LoRA & Adapters](topics/lora.md) — LoRA serving, multi-tenant adapter kernels, adapter formats
- [Structured & Constrained Decoding](topics/structured-decoding.md) — guided/constrained generation, FSM logit masking
- [Tokenizers](topics/tokenizers.md) — tokenizer design and its impact on inference
- [Model Compression](topics/model-compression.md) — pruning, sparsity, distillation
- [Pre-Training](topics/pre-training.md) — scaling laws, compute-optimal training, large training runs
- [Post-Training](topics/post-training.md) — instruction tuning, RLHF/RLAIF, preference optimization, RL methods

## Adding papers

Each paper goes in `papers/` (kebab-case filename with arXiv ID) and gets a row in its primary topic's table with an arXiv link, authors, date added, and a one-line summary.

## Stats

- 393 papers as of 2026-10-04
