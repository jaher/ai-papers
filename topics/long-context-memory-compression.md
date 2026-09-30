# Long-Context Memory Compression

Papers on compressing long input contexts into compact memory embeddings for inference.

| Paper | arXiv | Authors | Added | Summary |
|---|---|---|---|---|
| Compressing Long Context into Answer-Aligned Memory Embeddings for LLM Inference | [2609.25537](https://arxiv.org/abs/2609.25537) | Md Mostafizer Rahman et al. | 2026-09-30 | Context-to-Answer-Aligned Memory Compression (CMC): compresses long input contexts into Context Memory Embeddings (CMEs) aligned to any frozen decoder's embedding space; a two-tier KV cache combines question-guided CME selection with a local context window; compressor trained by answer-targeted distillation from a frozen LLM — no decoder weight changes. Up to +7.3 EM / +4.0 F1 on SQuAD; inference time and energy down up to 20%, peak reserved GPU memory down up to 50% at 3,000 generation tokens. |
| DeepSeek-OCR: Contexts Optical Compression | [2510.18234](https://arxiv.org/abs/2510.18234) | Haoran Wei et al. | 2026-09-30 | compressing long contexts by rendering them as images for a vision encoder. |
| Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models | [2601.07372](https://arxiv.org/abs/2601.07372) | Xin Cheng et al. | 2026-09-30 | the Engram paper: O(1)-lookup conditional-memory module; its ~197 GB tables are what the V4.1-Flash DGX Spark deployment offloads to NVMe. |
| DeepSeek-OCR 2: Visual Causal Flow | [2601.20552](https://arxiv.org/abs/2601.20552) | Haoran Wei et al. | 2026-09-30 | follow-up encoder design for visual context compression. |

| Landmark Attention: Random-Access Infinite Context Length for Transformers | [2305.16300](https://arxiv.org/abs/2305.16300) | Amirkeivan Mohtashami et al. | 2026-09-30 | While Transformers have shown remarkable success in natural language processing, their attention mechanism's large memory requirements have limited their ability to handle longer contexts |
| Lost in the Middle: How Language Models Use Long Contexts | [2307.03172](https://arxiv.org/abs/2307.03172) | Nelson F. Liu et al. | 2026-09-30 | While recent language models have the ability to take long contexts as input, relatively little is known about how well they use longer context |
| LongLLMLingua: Accelerating and Enhancing LLMs in Long Context Scenarios via Prompt Compression | [2310.06839](https://arxiv.org/abs/2310.06839) | Huiqiang Jiang et al. | 2026-09-30 | In long context scenarios, large language models (LLMs) face three main challenges: higher computational cost, performance reduction, and position bias |
| LongRoPE: Extending LLM Context Window Beyond 2 Million Tokens | [2402.13753](https://arxiv.org/abs/2402.13753) | Yiran Ding et al. | 2026-09-30 | Large context window is a desirable feature in large language models (LLMs) |
| Leave No Context Behind: Efficient Infinite Context Transformers with Infini-attention | [2404.07143](https://arxiv.org/abs/2404.07143) | Tsendsuren Munkhdalai et al. | 2026-09-30 | This work introduces an efficient method to scale Transformer-based Large Language Models (LLMs) to infinitely long inputs with bounded memory and computation |
PDFs: [`../papers/`](../papers/)
