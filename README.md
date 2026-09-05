# DL & GenAI Project T22026
## Smart MCQ Solver Challenge
### Deep Learning & Generative AI Project | IIT Madras BS Degree

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)
![SentenceTransformers](https://img.shields.io/badge/SentenceTransformers-MiniLM-green)
![FAISS](https://img.shields.io/badge/FAISS-Vector%20Search-purple)
![License](https://img.shields.io/badge/License-MIT-success)

---
- Title: Smart MCQ Solver Challenge
- Name: Sanish Kumar
- Email ID: 23f3001252@ds.study.iitm.ac.in
- Kaggle & GitHub Email ID: sanishbux42@gmail.com

# Project Overview

Smart MCQ Solver is an end-to-end Artificial Intelligence system developed as part of the **Deep Learning & Generative AI Project** in the **IIT Madras BS Degree** program.

The objective of this project is to automatically predict the **Top-3 most probable answers** for Multiple Choice Questions (MCQs) while also retrieving similar historical questions to improve explainability.

Unlike traditional MCQ classifiers that only predict an answer, this project combines **Machine Learning** and **Retrieval-Augmented Generation (RAG)** techniques to provide both predictions and supporting evidence.

The project represents several weeks of experimentation involving traditional Machine Learning, Deep Learning, Transformer models, Vector Databases, and deployment optimization.

---

# Problem Statement

Given an MCQ consisting of

- Question
- Five answer choices (A–E)

predict the **Top-3 most probable answers** ranked by confidence.

The evaluation metric used throughout the project is

> **MAP@3 (Mean Average Precision @ 3)**

which rewards correct ranking rather than only the first prediction.

---

# Project Objectives

The primary objectives of this project were

- Learn complete Deep Learning workflow
- Apply Natural Language Processing to MCQ solving
- Compare multiple Machine Learning models
- Train Transformer models
- Implement Retrieval-Augmented Generation (RAG)
- Build a FAISS vector database
- Track experiments using Weights & Biases
- Deploy the complete application
- Optimize models for real-world deployment

---

# Project Journey

This project was developed incrementally through multiple notebooks.

Instead of directly building a final model, every major concept was explored individually.

The complete workflow consisted of

```
EDA
      ↓

Baseline MAP@3

      ↓

TF-IDF + Logistic Regression

      ↓

Random Forest

      ↓

LightGBM

      ↓

XGBoost

      ↓

Neural Networks

      ↓

BiLSTM + Attention

      ↓

DistilBERT

      ↓

DeBERTa

      ↓

FacebookAI RoBERTa

      ↓

Sentence Transformers

      ↓

FAISS

      ↓

RAG

      ↓

Deployment
```

Each notebook introduced a new concept while preserving previous learnings.

---

# Repository Structure

```
Smart-MCQ-Solver/
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_baseline_tfidf.ipynb
│   ├── 03_bilstm_attention.ipynb
│   ├── 04_deberta_finetuning.ipynb
│   ├── 05_ensemble.ipynb
│   ...
│
├── milestones/
│   ├── milestone-1.ipynb
│   ├── milestone-2.ipynb
│   ├── milestone-3.ipynb
│   ├── milestone-4.ipynb
│   ├── milestone-5.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── metrics.py
│   ├── inference.py
│   ├── utils.py
│   ├── prediction.py
│   ├── rag.py
│   ├── home.py
│   │   ...
│
├── models/     --->  (Exclude this from GitHub - It contains large files)
│   ├── Roberta-finetuned/    
│   │   ├── config.json
│   │   ├── model.safetensors
│   │   ├── tokenizer.json
│   │   ...
│   │
│   ├── sentence-transformer/
│   │   ├── model.safetensors
│   │   ├── tokenizer.json
│   │   ├── tokenizer_config.json
│   │   ...
│   │
│   ├── rag-faiss/
│   │   ├── mcq_rag_index.faiss
│   │   ├── knowledge_corpus.csv
│   │   ├── metadata.joblib
│       ...
│
├── reports/
│   ├── Smart-mcq-solver.pdf
│
├── assets/
│   ├── wandb_run1.png
│   ├── wandb_run2.png
│   ├── eda.png
│   ...
│
│
├── app.py
├── README.md
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitattributes
└── .gitignore
```

---

# Final Pipeline

The final lightweight pipeline became

```
User Question

↓

TF-IDF Vectorizer

↓

Logistic Regression

↓

Top-3 Predictions

↓

Sentence Transformer

↓

FAISS Retrieval

↓

Similar Questions

↓

Display Results
```

This architecture balances

- Speed
- Memory
- Explainability
- Deployment feasibility

---

# Experiment Tracking

Weights & Biases (W&B) was used throughout the project.

Tracked information included

- Training Loss
- Validation Loss
- Accuracy
- MAP@3
- Learning Rate
- Epochs
- Model Comparison

---

# Evaluation

Primary metric

```
MAP@3
```

Other metrics

- Accuracy
- Precision
- Recall
- Macro F1

Multiple models were compared before selecting the final deployment pipeline.

---

# Deployment

The application was built using

- Streamlit
- Gradio on Hugging face
- Hugging Face Hub
- FAISS
- Sentence Transformers

Initially deployment used

- FacebookAI RoBERTa
- BGE-base

This exceeded free memory limits.

Therefore deployment was optimized using

- TF-IDF
- Logistic Regression
- MiniLM
- FAISS

---

# Challenges Faced

Major challenges included

- GPU memory limitations
- Hugging Face authentication
- Large model downloads
- Transformer deployment
- Dependency conflicts
- Free-tier RAM restrictions
- Model version compatibility
- Scikit-learn serialization warnings
- Streamlit deployment failures
- Hugging Face Space memory limits

Each issue was investigated and resolved through iterative debugging and optimization.

---

# Key Learnings

This project provided practical experience in

- Natural Language Processing
- Deep Learning
- Transformer models
- Retrieval-Augmented Generation
- FAISS indexing
- Experiment tracking
- Model deployment
- Performance optimization
- Cloud deployment
- Debugging production ML systems

---

# Future Improvements

Potential future work includes

- LoRA fine-tuning
- ONNX optimization
- Quantized transformer models
- Better retrieval reranking
- Larger training datasets
- Hybrid dense + sparse retrieval
- Cloud GPU deployment
- Better explainability techniques

---

# Technologies Used

### Languages

- Python

### Machine Learning

- Scikit-Learn

### Deep Learning

- PyTorch

### NLP

- Transformers
- Sentence Transformers

### Retrieval

- FAISS

### Visualization

- Matplotlib
- Seaborn
- Plotly

### Experiment Tracking

- Weights & Biases

### Deployment

- Streamlit
- Hugging Face Hub
- Docker

---

# Author

**Sanish Kumar**

Deep Learning & Generative AI Project

IIT Madras BS Degree

- Email: sanishbux42@gmail.com
- Linkedin: https://www.linkedin.com/in/sanish-kumar-singh-163679289
- Kaggle Notebook: https://www.kaggle.com/code/sanishkumarsingh/
- GitHub: https://github.com/SanishCode21
- Hugging Face: https://huggingface.co/SanishKumarSingh
- Live Project link: https://sanishkumarsingh-smart-mcq-solver-1.hf.space 

---

# ⭐ Acknowledgements

This project was completed as part of the **Deep Learning & Generative AI** course under the **IIT Madras BS Degree Program**.

The project integrates concepts learned throughout the course, including classical machine learning, deep learning, transformer architectures, Retrieval-Augmented Generation, experiment tracking, and deployment optimization.

---


