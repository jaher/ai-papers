# Serving Engines

Papers on LLM serving engines: PagedAttention/vLLM, SGLang RadixAttention, continuous batching, and scheduler design.

| Paper | arXiv | Authors | Added | Summary |
|---|---|---|---|---|
| Efficient Memory Management for Large Language Model Serving with PagedAttention | [2309.06180](https://arxiv.org/abs/2309.06180) | Woosuk Kwon et al. | 2026-09-30 | PagedAttention KV-cache paging plus continuous batching; the serving engine the DGX Spark stack itself runs on. |
| SGLang: Efficient Execution of Structured Language Model Programs | [2312.07104](https://arxiv.org/abs/2312.07104) | Lianmin Zheng et al. | 2026-09-30 | RadixAttention prefix caching and zero-overhead scheduler; the other major serving engine alongside vLLM. |

PDFs: [`../papers/`](../papers/)
