# Smart MCQ Solver Challenge - Exploratory Data Analysis (EDA)

## Overview

Before designing any Deep Learning model, a comprehensive Exploratory Data Analysis (EDA) was conducted to understand the dataset characteristics, identify potential data quality issues, analyze text distributions, and make informed preprocessing and modeling decisions.

Unlike traditional Machine Learning projects where feature engineering is the primary objective, the goal of EDA in this project is to understand the nature of the textual data and optimize the preprocessing pipeline for Neural Networks.

---

# Dataset Overview

## Training Dataset

* Total Samples: **2000**
* Features: **8**

| Column | Description                |
| ------ | -------------------------- |
| id     | Unique question identifier |
| prompt | MCQ question               |
| A      | Option A                   |
| B      | Option B                   |
| C      | Option C                   |
| D      | Option D                   |
| E      | Option E                   |
| answer | Correct option             |

---

## Test Dataset

* Total Samples: **500**
* Features: **7**
* The test dataset does not contain the answer column.

---

# Data Quality Analysis

## Missing Values

### Observation

* Missing values in Train Dataset: **0**
* Missing values in Test Dataset: **0**

### Insight

The dataset is completely clean.

### Decision

No missing value imputation was required.

---

## Duplicate Analysis

### Entire Duplicate Rows

* **0**

### Duplicate Prompts

* **242**

### Duplicate Question + Options

* **183**

### Duplicate IDs

* **0**

### Observation

Several prompts appear multiple times because the same knowledge is tested using different instructions such as:

* Pick the best answer
* Select the correct option
* Identify the most accurate statement

However, complete duplicate rows do not exist.

### Insight

These duplicated prompts introduce linguistic diversity rather than redundant data.

### Decision

Duplicate prompts were retained because they improve model robustness.

---

# Target Variable Analysis

## Correct Answer Distribution

| Answer | Count |
| ------ | ----: |
| A      |   369 |
| B      |   490 |
| C      |   459 |
| D      |   358 |
| E      |   324 |

### Observation

The dataset is reasonably balanced.

Although option **B** appears most frequently, the difference between the largest and smallest class is relatively small.

### Insight

No severe class imbalance exists.

### Decision

* No oversampling
* No undersampling
* No SMOTE

A stratified train-validation split will be sufficient.

---

# Prompt Analysis

## Prompt Length Statistics

| Statistic |             Value |
| --------- | ----------------: |
| Mean      | 117.67 characters |
| Minimum   |                19 |
| Maximum   |               337 |

## Prompt Word Count

| Statistic |       Value |
| --------- | ----------: |
| Mean      | 18.15 words |
| Minimum   |           3 |
| Maximum   |          51 |

### Observation

Most questions contain between 15 and 25 words.

The histogram shows only a few long questions.

### Insight

Questions have consistent length and do not contain excessive outliers.

### Decision

No filtering of long questions was required.

---

# Combined Question + Options Analysis

To understand the complete input size presented to the model, all options were combined with the corresponding prompt.

## Combined Length Statistics

| Statistic |           Value |
| --------- | --------------: |
| Mean      |  947 characters |
| Maximum   | 2608 characters |

## Combined Word Statistics

| Statistic |        Value |
| --------- | -----------: |
| Mean      | 149.54 words |
| Maximum   |    457 words |

### Observation

Most samples fall between 100 and 200 words.

Very few samples exceed 400 words.

### Insight

The dataset contains moderate-length sequences suitable for sequence models.

### Decision

Padding and truncation will be applied instead of removing long samples.

---

# Token Length Analysis

Token length analysis is critical for selecting the maximum sequence length (`MAX_LEN`) during preprocessing.

| Percentile | Tokens |
| ---------- | -----: |
| 50%        |    133 |
| 75%        |    202 |
| 90%        |    257 |
| 95%        |    322 |
| 99%        |    412 |
| Maximum    |    457 |

### Observation

95% of all samples contain fewer than 322 words.

### Insight

Using a sequence length of 512 would waste memory because most samples are significantly shorter.

### Decision

The project uses:

**MAX_LEN = 320**

This value captures approximately 95% of the dataset while improving computational efficiency.

---

# Option Length Analysis

Average word count of each option:

| Option | Mean Words |
| ------ | ---------: |
| A      |      26.15 |
| B      |      26.52 |
| C      |      26.55 |
| D      |      26.00 |
| E      |      26.19 |

### Observation

All five options have nearly identical average lengths.

### Insight

There is no positional or length bias.

The model cannot rely on option length as a shortcut.

### Decision

All options are treated equally during training.

---

# Vocabulary Analysis

## Vocabulary Size

* Unique Words: **3815**

## Total Tokens

* **299089**

### Most Frequent Words

Examples include:

* the
* of
* a
* is
* and
* in
* to
* that

### Observation

The vocabulary is relatively small compared to many NLP datasets.

### Insight

The dataset contains a stable and repetitive vocabulary.

### Decision

Vocabulary size was limited to:

**5000 words**

No extremely large vocabulary is required.

---

# Rare Word Analysis

Rare words (frequency = 1):

* **12**

Rare Word Ratio:

* **0.0031**

### Observation

Almost every word appears multiple times.

### Insight

The dataset has very little vocabulary noise.

### Decision

No rare-word removal was required.

---

# Lexical Diversity

Average lexical diversity:

**0.416**

### Observation

Many questions share domain-specific terminology.

### Insight

This is expected because the dataset covers educational MCQs where concepts are repeatedly discussed.

---

# Stopword Analysis

Average stopword ratio:

**0.424**

### Observation

Approximately 42% of words are common English stopwords.

### Insight

Stopwords contribute to sentence meaning and grammatical structure.

### Decision

Stopwords were retained.

---

# Train-Test Vocabulary Coverage

Vocabulary coverage:

**99.97%**

### Observation

Almost every word appearing in the test set is already present in the training set.

### Insight

There is virtually no vocabulary shift between training and testing data.

### Decision

No domain adaptation techniques are required.

---

# Correlation Analysis

Strong positive correlations were observed between:

* Prompt Length ↔ Prompt Words
* Combined Length ↔ Combined Words

### Observation

Character length and word count measure nearly the same information.

### Decision

Word count is preferred over character count for subsequent analyses.

---

# Semantic Similarity Analysis

Sentence embeddings were generated using **all-MiniLM-L6-v2**.

Average similarity:

* Correct Option: **0.5827**
* Incorrect Option: **0.5744**

### Observation

The similarity gap is very small.

### Insight

Correct answers are not easily distinguishable using semantic similarity alone.

The challenge requires contextual reasoning rather than simple sentence matching.

### Decision

A ranking-based neural network is more suitable than relying solely on similarity features.

---

# Key Insights from EDA

1. The dataset is completely clean with no missing values.
2. Duplicate prompts are intentional and improve linguistic diversity.
3. The target distribution is reasonably balanced.
4. Question lengths are consistent with only a few long outliers.
5. Sequence lengths suggest **MAX_LEN = 320** as an efficient choice.
6. Option lengths are evenly distributed, preventing positional bias.
7. Vocabulary size is compact (3815 words), allowing a vocabulary of 5000 tokens.
8. Rare words are almost nonexistent, indicating a stable corpus.
9. Train and test datasets have almost identical vocabularies (99.97% overlap).
10. Semantic similarity alone is insufficient for solving the task.

---

# Decisions Taken for Deep Learning Pipeline

Based on the EDA findings, the following decisions were made:

* No missing value treatment.
* No duplicate removal.
* No stemming or lemmatization.
* No stopword removal.
* No punctuation removal.
* Vocabulary size fixed at **5000**.
* Maximum sequence length fixed at **320**.
* Stratified train-validation split.
* Pairwise ranking formulation adopted instead of direct multiclass classification.
* PyTorch selected as the Deep Learning framework.
* BiLSTM with Attention chosen as the initial neural network architecture.
* Model evaluation based on **Mean Average Precision at 3 (MAP@3)**, matching the competition metric.

---

# Conclusion

The EDA demonstrates that the Smart MCQ Solver dataset is clean, balanced, and well-structured for Deep Learning. Rather than relying on handcrafted features, the analysis focused on understanding sequence lengths, vocabulary characteristics, semantic complexity, and answer distributions. These observations guided every preprocessing and modeling decision, resulting in a robust pipeline optimized for pairwise answer ranking and MAP@3 evaluation.
