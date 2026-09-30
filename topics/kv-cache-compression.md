# KV-Cache Compression

Papers on compressing the KV cache — unified/token-type-aware schemes, low-rank compression, and joint bit-rank allocation.

| Paper | arXiv | Authors | Added | Summary |
|---|---|---|---|---|
| UniCache: Task- and Type-Aware KV Cache Compression for Unified Multimodal Models | [2609.32831](https://arxiv.org/abs/2609.32831) | Wanqi Yang et al. | 2026-09-30 | Task- and token-type-aware KV compression for unified multimodal (text-image) models. 5x KV-cache compression for understanding/editing, 2.5x for generation, negligible quality loss; up to 1.78x throughput in long-context settings. |
| KV-COBRA: Co-Optimized Bit-Rank Allocation for Efficient KV Cache Compression | [2609.24298](https://arxiv.org/abs/2609.24298) | Sihyeon Ha, Jaeho Lee, Yo-Seb Jeon | 2026-09-30 | Jointly co-optimizes bit-width and rank allocations across KV heads and layers: adaptive per-head bit-rank schedule under a global budget pushes capacity toward the most error-sensitive heads. Best accuracy at low bit budgets (0.5–4 bits/dim); no per-token compute overhead at inference. |
| MILO: Efficient Many-shot In-Context Learning with Block-wise Low-rank Compression | [2609.29913](https://arxiv.org/abs/2609.29913) | Youpeng Zhao et al. | 2026-09-29 | Block-wise low-rank KV-cache compression at demonstration-example granularity, with per-block rank budgets set by information entropy (critical blocks preserved, redundant ones compressed hard). Up to 50% KV-cache memory reduction and 1.8x throughput on Qwen2.5 with negligible degradation. |

PDFs: [`../papers/`](../papers/)
