# Speculative Decoding

Papers on speculative / draft-and-verify decoding and drafter designs for faster LLM inference.

| Paper | arXiv | Authors | Added | Summary |
|---|---|---|---|---|
| SpecStream: Resource-Efficient Speculative Decoding for Long-Context LLM Serving | [2609.33184](https://arxiv.org/abs/2609.33184) | Fei Li, Song Liu, Shiqiang Nie, Jinyu Wang, Weiguo Wu | 2026-09-30 | Starts target verification before full KV history is restored from CPU; streams KV chunks shared across queries within a verification round, with an online softmax preserving full-attention accuracy. Drafting runs concurrently in compute bubbles during KV transfers — everything on the same GPUs. 1.41x/1.32x output throughput vs offloading baseline; +55.4% throughput per GPU vs separate-GPU parallel spec decoding. |
| H-Spec: Parallel Speculative Decoding Without a Drafter-Side KV Cache | [2609.24197](https://arxiv.org/abs/2609.24197) | Weifan Jiang et al. | 2026-09-30 | Hybrid Mamba-attention parallel drafter reuses target KV and target hidden states directly, so it needs no separate drafter-side KV cache. +5.0–13.3% mean accepted length, +5.3–12.6% batch-1 latency speedup, and notably lower KV-cache utilization under concurrency. |
| Accelerating Large Language Model Decoding with Speculative Sampling | [2302.01318](https://arxiv.org/abs/2302.01318) | Charlie Chen et al. | 2026-09-30 | the DeepMind speculative-decoding paper underlying all speculative decoding in serving stacks. |
| Faster LLM Inference via Sequential Monte Carlo | [2604.15672](https://arxiv.org/abs/2604.15672) | Yahya Emara et al. | 2026-09-30 | sequential Monte Carlo speculative decoding (SMC-SD): replaces token-level rejection with importance-weighted resampling over a population of draft particles; 2.36x over speculative decoding and 5.2x over autoregressive decoding, within 3% of target accuracy on reasoning, instruction-following, and coding benchmarks. Code: github.com/abdelfattah-lab/smcsd. Added 2026-09-21 at user request; queued as the 2026-09-22 daily ML paper. |
| DSpark: Confidence-Scheduled Speculative Decoding with Semi-Autoregressive Generation | [2607.05147](https://arxiv.org/abs/2607.05147) | Xin Cheng et al. | 2026-09-30 | semi-autoregressive drafting + confidence-scheduled verification; +60–85% per-user serving speedup on V4-Flash in production. |

PDFs: [`../papers/`](../papers/)
