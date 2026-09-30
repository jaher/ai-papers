# LoRA & Adapters

Low-rank adapters for inference: LoRA serving, multi-tenant adapter kernels (Punica, S-LoRA), and adapter formats (DoRA, VeRA).

| Paper | arXiv | Authors | Added | Summary |
|---|---|---|---|---|
| Parameter-Efficient Transfer Learning for NLP | [1902.00751](https://arxiv.org/abs/1902.00751) | Neil Houlsby et al. | 2026-09-30 | Fine-tuning large pre-trained models is an effective transfer mechanism in NLP |
| Prefix-Tuning: Optimizing Continuous Prompts for Generation | [2101.00190](https://arxiv.org/abs/2101.00190) | Xiang Lisa Li et al. | 2026-09-30 | Fine-tuning is the de facto way to leverage large pretrained language models to perform downstream tasks |
| The Power of Scale for Parameter-Efficient Prompt Tuning | [2104.08691](https://arxiv.org/abs/2104.08691) | Brian Lester et al. | 2026-09-30 | In this work, we explore "prompt tuning", a simple yet effective mechanism for learning "soft prompts" to condition frozen language models to perform specific downstream tasks |
| LoRA: Low-Rank Adaptation of Large Language Models | [2106.09685](https://arxiv.org/abs/2106.09685) | Edward J. Hu et al. | 2026-09-30 | An important paradigm of natural language processing consists of large-scale pre-training on general domain data and adaptation to particular tasks or domains |
| BitFit: Simple Parameter-efficient Fine-tuning for Transformer-based Masked Language-models | [2106.10199](https://arxiv.org/abs/2106.10199) | Elad Ben-Zaken et al. | 2026-09-30 | We introduce BitFit, a sparse-finetuning method where only the bias-terms of the model (or a subset of them) are being modified |
| VeRA: Vector-based Random Matrix Adaptation | [2310.11454](https://arxiv.org/abs/2310.11454) | Dawid J. Kopiczko et al. | 2026-09-30 | Low-rank adapation (LoRA) is a popular method that reduces the number of trainable parameters when finetuning large language models, but still faces acute storage challenges when scaling to even larger models or deploying numer... |
| Punica: Multi-Tenant LoRA Serving | [2310.18547](https://arxiv.org/abs/2310.18547) | Lequn Chen et al. | 2026-09-30 | Low-rank adaptation (LoRA) has become an important and popular method to adapt pre-trained models to specific domains |
| S-LoRA: Serving Thousands of Concurrent LoRA Adapters | [2311.03285](https://arxiv.org/abs/2311.03285) | Ying Sheng et al. | 2026-09-30 | The "pretrain-then-finetune" paradigm is commonly adopted in the deployment of large language models |
| DoRA: Weight-Decomposed Low-Rank Adaptation | [2402.09353](https://arxiv.org/abs/2402.09353) | Shih-Yang Liu et al. | 2026-09-30 | Among the widely used parameter-efficient fine-tuning (PEFT) methods, LoRA and its variants have gained considerable popularity because of avoiding additional inference costs |
| FlexLLM: Token-Level Co-Serving of LLM Inference and Finetuning with SLO Guarantees | [2402.18789](https://arxiv.org/abs/2402.18789) | Gabriele Oliaro et al. | 2026-09-30 | Finetuning large language models (LLMs) is essential for task adaptation, yet today's serving stacks isolate inference and finetuning on separate GPU clusters -- wasting resources and under-utilizing hardware |
