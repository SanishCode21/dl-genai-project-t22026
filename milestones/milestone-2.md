# DL & GenAI Project – Milestone 2

## Transformers, Context-Aware Embeddings & Zero-Shot Learning

## Overview

This milestone marks the transition from **classical Natural Language Processing (NLP)** techniques to **modern Deep Learning and Generative AI** approaches. Instead of relying on sparse representations such as TF-IDF, this milestone focuses on understanding how Transformer-based models capture semantic meaning through contextual embeddings and attention mechanisms.

The primary objective was to explore the **Hugging Face ecosystem**, understand Transformer architectures, generate dense sentence embeddings, perform zero-shot classification, compare Softmax and Sigmoid probabilities, and experiment with Small Language Models (SLMs) for generative question answering.

---

# Objectives

* Learn the Hugging Face `datasets` library.
* Work with pre-trained Transformer models.
* Understand tokenization using BERT.
* Explore the Attention Mechanism.
* Generate context-aware sentence embeddings.
* Compare TF-IDF with Transformer embeddings.
* Perform Zero-Shot Classification.
* Understand Softmax vs Independent Sigmoid probabilities.
* Prompt a Small Language Model (FLAN-T5).

---

# Technologies Used

* Python
* Hugging Face Transformers
* Hugging Face Datasets
* Sentence Transformers
* PyTorch
* Scikit-learn
* NumPy

---

# Concepts Covered

## 1. Hugging Face Datasets

Instead of using Pandas, the dataset was loaded using the Hugging Face `datasets` library.

### Learned Concepts

* Loading CSV datasets
* Dataset objects
* Column operations
* `.map()` function
* Efficient preprocessing pipelines

Example:

```python
dataset = load_dataset("csv", data_files={"train": "train.csv"})
train_ds = dataset["train"]

train_ds = train_ds.map(
    lambda x: {
        "combined_text": x["prompt"] + " " + x["A"]
    }
)
```

---

# 2. BERT Tokenizer

Initialized the `bert-base-uncased` tokenizer and explored its configuration.

### Learned

* Vocabulary size
* Special tokens
* Token IDs
* `[CLS]`
* `[SEP]`
* Padding
* Truncation
* Maximum sequence length

---

# 3. Tokenization

Tokenized the entire dataset simultaneously.

Configuration used:

```python
padding="max_length"
truncation=True
max_length=128
return_tensors="pt"
```

Learned:

* Batch tokenization
* Attention masks
* Input IDs
* Tensor shapes

---

# 4. Transformer Architecture

Studied the architecture of BERT.

### Concepts

* Hidden size (768)
* Number of attention heads (12)
* Head dimension (64)
* Encoder blocks
* Feed Forward Networks
* Residual connections
* Layer Normalization

---

# 5. Attention Mechanism

Explored self-attention inside Transformer models.

Learned:

* Query (Q)
* Key (K)
* Value (V)
* Self-attention
* Multi-head attention
* Context-aware representations

Extracted:

* Last layer attention matrix
* Individual attention heads
* Attention weights between tokens

---

# 6. Context-Aware Embeddings

Generated semantic sentence embeddings using:

```
sentence-transformers/all-MiniLM-L6-v2
```

Generated embeddings for:

* Prompt
* Option A
* Option B
* Option C
* Option D
* Option E

Compared embeddings using cosine similarity.

---

# 7. Cosine Similarity

Used

```python
sentence_transformers.util.cos_sim()
```

to compute semantic similarity between:

* Prompt
* Answer options

This ranking forms the basis of the semantic retrieval pipeline.

---

# 8. TF-IDF vs Transformer Embeddings

Implemented two complete ranking pipelines.

## Pipeline 1

Traditional NLP

* TF-IDF
* Cosine Similarity

## Pipeline 2

Deep Learning

* MiniLM embeddings
* Cosine Similarity

Compared both using MAP@3.

---

# 9. MAP@3 Evaluation

Evaluated ranking quality using Mean Average Precision at Top-3.

Computed:

* TF-IDF MAP@3
* MiniLM MAP@3

Also measured:

* Number of questions improved by MiniLM over TF-IDF.

---

# 10. Zero-Shot Classification

Used:

```
facebook/bart-large-mnli
```

Performed classification without additional training.

Learned:

* Natural Language Inference (NLI)
* Candidate labels
* Entailment
* Label ranking
* Confidence scores

---

# 11. Softmax vs Independent Sigmoid

Compared two probability formulations.

## Softmax

* Probabilities sum to 1
* Best for single-label prediction

## Independent Sigmoid

* Independent probabilities
* Used in multi-label classification

Observed the probability difference experimentally.

---

# 12. Small Language Models (SLMs)

Prompted

```
google/flan-t5-small
```

using instruction-based prompting.

Example prompt:

```
Question: ...
Is the correct answer A or B?
Answer with just the letter.
```

Learned:

* Prompt engineering
* Instruction following
* Conditional text generation

---

# Experimental Pipeline

```
Dataset
      │
      ▼
Hugging Face Dataset
      │
      ▼
BERT Tokenizer
      │
      ▼
Transformer Models
      │
      ├───────────────► Attention Analysis
      │
      ├───────────────► Context Embeddings
      │
      ├───────────────► Zero-shot Classification
      │
      └───────────────► FLAN-T5 Prompting
```

---

# Key Learning Outcomes

By completing this milestone, I learned:

* Hugging Face ecosystem
* Transformer-based NLP
* BERT architecture
* Self-attention mechanism
* Context-aware embeddings
* Sentence Transformers
* Semantic similarity
* MAP@3 evaluation
* Zero-shot learning
* Multi-label vs single-label classification
* Small Language Models
* Prompt engineering fundamentals

---

# Skills Developed

* Transformer inference
* Tokenization
* Embedding generation
* Attention visualization
* Semantic search
* Zero-shot prediction
* Ranking systems
* Retrieval-based NLP
* Generative AI experimentation

---

# Milestone Summary

This milestone successfully transitioned the project from traditional NLP methods toward modern Transformer-based Deep Learning approaches. It demonstrated how contextual embeddings significantly improve semantic understanding compared to sparse TF-IDF representations and introduced powerful pre-trained models for retrieval, classification, and generation without task-specific training.

The knowledge gained in this milestone establishes the foundation for future work involving Transformer fine-tuning, Retrieval-Augmented Generation (RAG), advanced ranking models, and Large Language Models (LLMs) in subsequent milestones.

---

# Next Milestone

Future work will focus on:

* Fine-tuning Transformer models
* Advanced ranking architectures
* Retrieval-Augmented Generation (RAG)
* Large Language Models (LLMs)
* Improved Top-3 prediction accuracy
* Competition leaderboard optimization

---

## 👨‍💻 Author

**Sanish Kumar**

**Project:** Smart MCQ Solver – Deep Learning & Generative AI Project

**Academic Program:** IIT Madras – BS Degree in Data Science and Applications
