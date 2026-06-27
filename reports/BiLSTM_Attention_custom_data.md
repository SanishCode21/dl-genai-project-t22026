# Smart MCQ Solver Challenge (Version 1)

## Deep Learning + PyTorch + GenAI Baseline

---

# Project Overview

This notebook represents my first end-to-end Deep Learning implementation for the **Smart MCQ Solver Challenge**.

The objective of this competition is to predict the **Top-3 most probable answers** for every multiple-choice question consisting of:

* Question Prompt
* Five Options (A, B, C, D, E)

The evaluation metric is:

> **Mean Average Precision @ 3 (MAP@3)**

Unlike standard classification tasks, this competition requires ranking answer choices according to confidence.

---

# Competition Objective

Input

Question

Option A

Option B

Option C

Option D

Option E

Output

Top-3 ranked options

Example

Correct Answer = B

Prediction

B A C  Highest Score

A B C  Lower Score

D C B  Much Lower Score

Therefore the model must learn ranking rather than simply predicting one class.

---

# My Objective

Instead of directly using large transformer models, I wanted to understand how Deep Learning models work internally.

Therefore I decided to build the complete pipeline manually using PyTorch.

The primary objective of this notebook was educational:

* understand NLP preprocessing
* understand pairwise ranking
* implement custom datasets
* build a neural network
* train from scratch
* evaluate using MAP@3
* generate Kaggle competition submissions

---

# Dataset

Training Questions : 2,000

Test Questions : 500

Each question contains

* Prompt
* Option A
* Option B
* Option C
* Option D
* Option E

Training data additionally contains

Correct Answer

---

# Dataset Transformation

Instead of treating the problem as a 5-class classifier, the dataset was converted into a binary ranking problem.

Original

Question

A

B

C

D

E

Answer = B

Converted into

Question + A → 0

Question + B → 1

Question + C → 0

Question + D → 0

Question + E → 0

Result

2000 Questions

↓

10000 Pairwise Samples

This allowed the model to independently score every answer option.

---

# Exploratory Data Analysis (EDA)

A complete EDA was performed before model development.

The analysis included:

## Dataset Overview

* Dataset shape
* Column information
* Data types
* Missing values
* Duplicate records
* Unique value counts

---

## Text Statistics

Calculated

* Prompt length
* Option lengths
* Combined text length
* Word counts
* Sentence counts
* Digit counts
* Punctuation counts

---

## Vocabulary Analysis

Observed

Vocabulary Size

3815

Total Tokens

299089

Vocabulary Coverage

99.97%

Rare Words

12

Rare Word Ratio

0.003

---

## Lexical Analysis

Calculated

Lexical Diversity

Stopword Ratio

Word Frequency

Most Frequent Words

Rare Words

---

## Visualizations

Created

* Answer Distribution
* Prompt Length Histogram
* Option Length Distribution
* Word Count Distribution
* Correlation Heatmaps
* Vocabulary Distribution
* Lexical Diversity Distribution
* Stopword Ratio Distribution

---

# Feature Engineering

Several handcrafted NLP features were explored.

Examples

Prompt Length

Option Length

Length Difference

Word Count

Sentence Count

TF-IDF Similarity

Jaccard Similarity

Embedding Similarity

Digit Overlap

Token Overlap

Topic Clustering

These features were mainly used for exploratory understanding rather than final neural network training.

---

# NLP Preprocessing Pipeline

Implemented manually.

Pipeline

Lowercase Conversion

↓

Cleaning

↓

Tokenization

↓

Vocabulary Building

↓

Integer Encoding

↓

Padding

↓

PyTorch Dataset

↓

DataLoader

---

# Vocabulary

A custom vocabulary was built entirely from the training dataset.

Special Tokens

<PAD>

<UNK>

Every word was assigned a unique integer index.

Unknown words were mapped to

<UNK>

---

# Tokenization

Implemented a custom tokenizer using regular expressions.

Steps

Lowercase

Remove unnecessary spaces

Split punctuation

Split words

Convert to token IDs

Pad sequences

---

# Train Validation Split

Performed using Question IDs to prevent leakage.

Train Questions

1600

Validation Questions

400

Resulting Samples

Train

8000

Validation

2000

---

# PyTorch Dataset

Created a custom Dataset class.

Responsibilities

Load input IDs

Load labels

Return Question IDs

Return Option Labels

Support batching

---

# DataLoader

Implemented

Custom collate function

Batch loading

Padding

Efficient GPU transfer

---

# Neural Network Architecture

Implemented completely in PyTorch.

Architecture

Embedding Layer

↓

Bidirectional LSTM

↓

Attention Layer

↓

Dropout

↓

Fully Connected Layer

↓

ReLU

↓

Dropout

↓

Output Layer

↓

Sigmoid

The model predicts a probability indicating how likely an option is the correct answer.

---

# Attention Mechanism

Instead of using the last hidden state, an attention layer was implemented.

Benefits

* Better contextual representation
* Weighted focus on important words
* Improved sequence representation

---

# Training Pipeline

Implemented

Binary Cross Entropy Loss

Adam Optimizer

Learning Rate Scheduler

Mixed Precision Training

Gradient Clipping

Early Stopping

Checkpoint Saving

Training History Logging

---

# Evaluation

Implemented

Binary Accuracy

Validation Loss

Training Loss

MAP@3

The MAP@3 implementation was written manually according to the competition rules.

---

# Inference Pipeline

Implemented

Pairwise Test Dataset

↓

Tokenization

↓

Encoding

↓

Padding

↓

Prediction Scores

↓

Ranking

↓

Top-3 Selection

↓

Submission Generation

---

# Competition Submission

Submission format

ID

Prediction

Example

1,A B C

2,C D A

3,B A E

---

# Final Model

Model

BiLSTM + Attention

Framework

PyTorch

Task

Binary Pairwise Ranking

Evaluation

MAP@3

---

# Leaderboard Result

Public Leaderboard Score

0.45760

---

# Why was the score relatively low?

Although the notebook achieved nearly perfect training performance, leaderboard performance remained limited.

Main reasons

## 1. Small Dataset

Only 2000 training questions.

Deep neural networks generally require much larger datasets.

---

## 2. Random Word Embeddings

Embedding layer was initialized randomly.

The model needed to learn language representations from scratch.

Modern NLP models instead begin with pretrained embeddings.

---

## 3. No External Knowledge

The model only learned from the provided dataset.

It had no pretrained understanding of

language

reasoning

facts

semantics

---

## 4. Overfitting

Training MAP@3 approached 1.0

Leaderboard MAP@3 remained much lower.

This indicates limited generalization.

---

## 5. Model Capacity

Although BiLSTM + Attention is an important NLP architecture, recent transformer-based models significantly outperform recurrent neural networks on reasoning-heavy MCQ tasks.

---

# Key Learnings

This notebook greatly improved my understanding of Deep Learning and NLP.

Major concepts learned

* Pairwise Ranking
* Binary Ranking Models
* NLP Preprocessing
* Vocabulary Construction
* Tokenization
* Integer Encoding
* Sequence Padding
* Custom Dataset
* DataLoader
* BiLSTM
* Attention Mechanism
* Binary Classification
* MAP@3 Evaluation
* Mixed Precision Training
* Early Stopping
* Model Checkpointing
* Competition Submission Pipeline

---

# Challenges Faced

Throughout this project I encountered and solved many implementation issues.

Examples

* Dataset transformation
* Pairwise ranking conversion
* Tokenization bugs
* Vocabulary encoding issues
* DataLoader multiprocessing errors
* Shape mismatch errors
* Tensor dimension errors
* Submission formatting issues
* Inference pipeline debugging
* Validation leakage checks
* MAP@3 implementation

Each debugging step helped strengthen my understanding of PyTorch and NLP workflows.

---

# Limitations

Current notebook limitations

Random embeddings

Small dataset

No pretrained language model

No transformer encoder

No cross encoder

No retrieval augmentation

No ensemble

No pseudo-labeling

No knowledge distillation

---

# Future Improvements (Version 2)

The next notebook will focus on stronger architectures and improved generalization.

Planned experiments

* Sentence Transformers
* MiniLM
* MPNet
* Cross Encoder Models
* DeBERTa
* RoBERTa
* BERT Fine-tuning
* Pairwise Transformer Ranking
* Learning Rate Warmup
* Better Negative Sampling
* Ensemble Methods
* Retrieval-Augmented Ranking
* Advanced Data Augmentation

The goal is to significantly improve leaderboard performance while gaining a deeper understanding of modern NLP systems.

---

# Final Reflection

This notebook was not just about achieving a leaderboard score.

It was primarily a learning project that helped me understand the complete lifecycle of building a Deep Learning NLP system from scratch.

From raw text to preprocessing, dataset creation, model design, training, evaluation, inference, and competition submission, every stage was implemented manually using PyTorch.

Although the leaderboard score leaves room for improvement, the knowledge gained from building this pipeline provides a strong foundation for future experiments with transformer-based architectures and advanced GenAI techniques.

This notebook serves as Version 1 of the Smart MCQ Solver project and establishes the baseline for all future improvements.
