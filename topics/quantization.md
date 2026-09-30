# Quantization

Papers on weight/activation/state quantization for inference — including KV-cache quantization and recurrent-state quantization.

| Paper | arXiv | Authors | Added | Summary |
|---|---|---|---|---|
| Low-Bit Recurrent States in Hybrid Language Models | [2609.30950](https://arxiv.org/abs/2609.30950) | Hongren Chen, Jiayang He | 2026-09-30 | Quantizes the fixed-size recurrent states of hybrid LMs below 8 bits: distortion weights from the observability Gramian plus normalized state ranges for mixed-precision bit allocation — no calibration data, no rotation, no training. 4-bit mean payload cuts excess NLL 3.3–27.9x vs the best of seven baselines across three hybrid models; 6 bits lands within 0.005 nats of the FP32-state baseline. Directly relevant to serving Kimi-Linear/MiniMax-style hybrids on Spark clusters. |
| GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers | [2210.17323](https://arxiv.org/abs/2210.17323) | Elias Frantar et al. | 2026-09-30 | one-shot 3–4-bit weight-only quantization; the canonical PTQ baseline. |
| SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models | [2211.10438](https://arxiv.org/abs/2211.10438) | Guangxuan Xiao et al. | 2026-09-30 | activation-outlier smoothing enabling W8A8 INT8 inference. |
| AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration | [2306.00978](https://arxiv.org/abs/2306.00978) | Ji Lin et al. | 2026-09-30 | activation-aware 4-bit weight quantization; widely deployed in serving engines. |

PDFs: [`../papers/`](../papers/)
