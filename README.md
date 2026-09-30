# LLM Inference Papers

A living collection of LLM inference research papers, organized by topic. Updated daily from the morning arXiv sweep — new papers land in the topic file that matches their primary angle, with the PDF in [`papers/`](papers/).

## Topics

- [Speculative Decoding](topics/speculative-decoding.md) — draft-and-verify decoding, drafter designs
- [KV-Cache Compression](topics/kv-cache-compression.md) — unified/token-type-aware schemes, low-rank compression, bit-rank allocation
- [KV-Cache Eviction & Management](topics/kv-cache-eviction.md) — eviction scoring, adaptive budgets, management policies
- [Quantization](topics/quantization.md) — weight/activation/state quantization for inference
- [Long-Context Memory Compression](topics/long-context-memory-compression.md) — compressing long contexts into memory embeddings

## Adding papers

Each paper goes in `papers/` (kebab-case filename with arXiv ID) and gets a row in its primary topic's table with an arXiv link, authors, date added, and a one-line summary.

## Stats

- 9 papers as of 2026-09-30
