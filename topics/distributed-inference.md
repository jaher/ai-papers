# Distributed Inference

Papers on distributed and disaggregated inference: prefill/decode splitting, phase splitting, model parallelism, and AI-HPC cluster design.

| Paper | arXiv | Authors | Added | Summary |
|---|---|---|---|---|
| Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism | [1909.08053](https://arxiv.org/abs/1909.08053) | Mohammad Shoeybi et al. | 2026-09-30 | tensor/pipeline parallelism; the foundation of distributed training and model-parallel inference. |
| ZeRO: Memory Optimizations Toward Training Trillion Parameter Models | [1910.02054](https://arxiv.org/abs/1910.02054) | Samyam Rajbhandari et al. | 2026-09-30 | sharded data parallelism; the memory-optimization standard for training and inference offload. |
| Splitwise: Efficient generative LLM inference using phase splitting | [2311.18677](https://arxiv.org/abs/2311.18677) | Pratyush Patel et al. | 2026-09-30 | Microsoft's phase-splitting onto heterogeneous hardware; ISCA'24. |
| DistServe: Disaggregating Prefill and Decoding for Goodput-optimized Large Language Model Serving | [2401.09670](https://arxiv.org/abs/2401.09670) | Yinmin Zhong et al. | 2026-09-30 | prefill/decode disaggregation with per-phase parallelism plans; OSDI'24. |
| Fire-Flyer AI-HPC: A Cost-Effective Software-Hardware Co-Design for Deep Learning | [2408.14158](https://arxiv.org/abs/2408.14158) | Wei An et al. | 2026-09-30 | DeepSeek's cost-effective AI-HPC cluster design: hardware-software co-design for training/inference clusters. |
| DeepSeek Elastic Compute (DSec): A Sandbox Infrastructure for Effective Agentic Training at Scale | [2609.22978](https://arxiv.org/abs/2609.22978) | Jialiang Huang et al. | 2026-09-30 | DeepSeek's production agent-RL sandbox platform: 380k concurrent sandboxes, 3M/day, >5k creations/sec; fleet-scale infra for agentic training and evaluation. |

PDFs: [`../papers/`](../papers/)
