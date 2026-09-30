# Speculative Decoding

Papers on speculative / draft-and-verify decoding and drafter designs for faster LLM inference.

| Paper | arXiv | Authors | Added | Summary |
|---|---|---|---|---|
| SpecStream: Resource-Efficient Speculative Decoding for Long-Context LLM Serving | [2609.33184](https://arxiv.org/abs/2609.33184) | Fei Li, Song Liu, Shiqiang Nie, Jinyu Wang, Weiguo Wu | 2026-09-30 | Starts target verification before full KV history is restored from CPU; streams KV chunks shared across queries within a verification round, with an online softmax preserving full-attention accuracy. Drafting runs concurrently in compute bubbles during KV transfers — everything on the same GPUs. 1.41x/1.32x output throughput vs offloading baseline; +55.4% throughput per GPU vs separate-GPU parallel spec decoding. |
| H-Spec: Parallel Speculative Decoding Without a Drafter-Side KV Cache | [2609.24197](https://arxiv.org/abs/2609.24197) | Weifan Jiang et al. | 2026-09-30 | Hybrid Mamba-attention parallel drafter reuses target KV and target hidden states directly, so it needs no separate drafter-side KV cache. +5.0–13.3% mean accepted length, +5.3–12.6% batch-1 latency speedup, and notably lower KV-cache utilization under concurrency. |

PDFs: [`../papers/`](../papers/)
