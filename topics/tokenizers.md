# Tokenizers

Tokenizer design and its impact on inference.

| Paper | Importance | arXiv | Authors | Added | Summary |
|---|---|---|---|---|---|
| Neural Machine Translation of Rare Words with Subword Units | ★★★★★ | [1508.07909](https://arxiv.org/abs/1508.07909) | Rico Sennrich et al. | 2026-09-30 | Neural machine translation (NMT) models typically operate with a fixed vocabulary, but translation is an open-vocabulary problem |
| SentencePiece: A simple and language independent subword tokenizer and detokenizer for Neural Text Processing | ★★★★★ | [1808.06226](https://arxiv.org/abs/1808.06226) | Taku Kudo et al. | 2026-09-30 | This paper describes SentencePiece, a language-independent subword tokenizer and detokenizer designed for Neural-based text processing, including Neural Machine Translation |
| Subword Regularization: Improving Neural Network Translation Models with Multiple Subword Candidates | ★★★★☆ | [1804.10959](https://arxiv.org/abs/1804.10959) | Taku Kudo | 2026-09-30 | Subword units are an effective way to alleviate the open vocabulary problems in neural machine translation (NMT) |
| Delta Tokenizer: Reference-Identical Tokenization of Session Deltas and Segment-Parallelism for Long Prompts on Multicore CPUs | ★★★☆☆ | [2610.19801](https://arxiv.org/abs/2610.19801) | Zhenyu Zhang, Zhichao Cao | 2026-10-15 | CPU front end that tokenizes only the appended session delta (joined at a provably stable split, output identical to full tokenization) and splits long prompts across cores; in SGLang, median chat TTFT down 59% at 100K tokens and agent-session P99 TTFT down up to 23x under front-end load. |
