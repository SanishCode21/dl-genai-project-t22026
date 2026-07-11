# Milestone 3 – Retrieval-Augmented Generation (RAG)

## Overview

This milestone focused on understanding the complete Retrieval-Augmented Generation (RAG) pipeline and evaluating how external knowledge influences Large Language Model (LLM) predictions. The project explored semantic retrieval using vector embeddings, document re-ranking with Cross-Encoders, and the impact of both relevant and incorrect retrieved context on model performance.

## Learning Objectives

* Build a searchable knowledge base from the training dataset.
* Generate semantic embeddings using `all-MiniLM-L6-v2`.
* Create and query a FAISS vector index for efficient document retrieval.
* Perform zero-shot classification using `facebook/bart-large-mnli`.
* Improve retrieval quality with the `cross-encoder/ms-marco-MiniLM-L-6-v2` reranker.
* Measure retrieval effectiveness using Hit Rate.
* Evaluate end-to-end RAG performance using MAP@3.
* Demonstrate the risks of incorrect retrieval through an Adversarial RAG experiment.

## Technologies Used

* Python
* FAISS
* Sentence Transformers
* Hugging Face Transformers
* Cross-Encoder
* BART Large MNLI (Zero-Shot Classification)
* Pandas
* NumPy
* Scikit-learn

## Pipeline Implemented

1. Create a knowledge base using the correct answers from the dataset.
2. Generate dense embeddings with `all-MiniLM-L6-v2`.
3. Index embeddings using FAISS.
4. Retrieve the Top-K most relevant documents.
5. Re-rank retrieved documents using a Cross-Encoder.
6. Construct an augmented prompt with retrieved context.
7. Perform zero-shot classification using the augmented prompt.
8. Evaluate retrieval quality and prediction performance.

## Experiments Performed

* Zero-shot classification without retrieval.
* Semantic retrieval using FAISS.
* Cross-Encoder re-ranking.
* Context window (Top-K) retrieval analysis.
* Retrieval Hit Rate evaluation.
* MAP@3 evaluation on a RAG pipeline.
* Adversarial RAG using intentionally incorrect context.

## Key Takeaways

* Vector search enables fast semantic retrieval but may not always return the most relevant document first.
* Cross-Encoders significantly improve retrieval quality by re-ranking candidate documents.
* High-quality retrieved context can improve prediction confidence and accuracy.
* Incorrect or irrelevant retrieved context can mislead the model, demonstrating the "Garbage In, Garbage Out" principle.
* Effective RAG systems depend on both accurate retrieval and careful context selection.

## Outcome

This milestone provided practical experience in designing, evaluating, and analyzing modern RAG systems. It established a strong foundation for building knowledge-grounded AI applications and understanding how retrieval quality directly impacts the performance and reliability of Large Language Models.

