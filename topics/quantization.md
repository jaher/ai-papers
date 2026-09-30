# Quantization

Papers on weight/activation/state quantization for inference — including KV-cache quantization and recurrent-state quantization.

| Paper | arXiv | Authors | Added | Summary |
|---|---|---|---|---|
| Low-Bit Recurrent States in Hybrid Language Models | [2609.30950](https://arxiv.org/abs/2609.30950) | Hongren Chen, Jiayang He | 2026-09-30 | Quantizes the fixed-size recurrent states of hybrid LMs below 8 bits: distortion weights from the observability Gramian plus normalized state ranges for mixed-precision bit allocation — no calibration data, no rotation, no training. 4-bit mean payload cuts excess NLL 3.3–27.9x vs the best of seven baselines across three hybrid models; 6 bits lands within 0.005 nats of the FP32-state baseline. Directly relevant to serving Kimi-Linear/MiniMax-style hybrids on Spark clusters. |

PDFs: [`../papers/`](../papers/)
