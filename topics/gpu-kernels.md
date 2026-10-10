# GPU Kernels & Performance Engineering

Classic and current GPU kernel literature: performance models, GEMM/scan kernel case studies, kernel programming languages, and benchmarks for LLM-generated kernels.

| Paper | arXiv | Authors | Added | Summary |
|---|---|---|---|---|
| Roofline: An Insightful Visual Performance Model for Multicore Architectures | [CACM 2009](https://users.cs.duke.edu/~lkw34/papers/roofline-cacm2008.pdf) | Samuel Williams, Andrew Waterman, David A. Patterson | 2026-10-10 | The roofline model: attainable performance bounded by peak compute and memory bandwidth via arithmetic intensity; the basic visual tool for kernel bottleneck analysis. |
| Benchmarking GPUs to Tune Dense Linear Algebra | [SC 2008](https://mc.stanford.edu/cgi-bin/images/6/65/SC08_Volkov_GPU.pdf) | Vasily Volkov, James W. Demmel | 2026-10-10 | Shows dense linear algebra on GPUs is bound by measured hardware behavior (register/memory throughput) rather than occupancy folklore; foundation of empirical GEMM tuning. |
| Single-pass Parallel Prefix Scan with Decoupled Look-back | [NVIDIA 2016](https://research.nvidia.com/sites/default/files/pubs/2016-03_Single-pass-Parallel-Prefix/nvr-2016-002.pdf) | Duane Merrill, Michael Garland | 2026-10-10 | Work-efficient single-pass scan using decoupled look-back across thread blocks; the scan primitive behind cub/Thrust-style implementations. |
| Triton: An Intermediate Language and Compiler for Tiled Neural Network Computations | [MAPL 2019](https://www.eecs.harvard.edu/~htk/publication/2019-mapl-tillet-kung-cox.pdf) | Philippe Tillet, H. T. Kung, David Cox | 2026-10-10 | The original Triton paper: a blocked-programming intermediate language and compiler for writing tiled GPU kernels at near-cuBLAS performance. |
| KernelBench: Can LLMs Write Efficient GPU Kernels? | [2502.10517](https://arxiv.org/abs/2502.10517) | Anne Ouyang et al. | 2026-10-10 | Benchmark of 250 PyTorch-to-CUDA kernel-writing tasks for evaluating LLM-generated GPU kernels against strong baselines. |
| KernelBench-Verified: Do LLM-Generated Kernels Actually Beat PyTorch? | [2607.16241](https://arxiv.org/abs/2607.16241) | Yunxiang Zhang et al. | 2026-10-10 | Hardened re-evaluation of KernelBench with stronger correctness tests and baseline parity, checking which LLM kernel speedups actually hold. |

PDFs: [`../papers/`](../papers/)
