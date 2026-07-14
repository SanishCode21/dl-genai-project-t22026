# DL & GenAI Project T22026
## Smart MCQ Solver Challenge
- Title: Smart MCQ Solver Challenge
- Name: Sanish Kumar
- Email ID: 23f3001252@ds.study.iitm.ac.in
- Kaggle & GitHub Email ID: sanishbux42@gmail.com


## Project Overview
We are required to build machine learning or AI based systems capable of solving complex multiple choice questions. Each question contains a prompt along with five possible answer options labeled A, B, C, D, and E. The objective is to predict the top three most likely correct answers in ranked order.

The challenge focuses on evaluating a model’s ability to understand context, reason across options, and rank answers effectively. Participants are encouraged to experiment with a variety of approaches including transformer architectures, retrieval based pipelines, fine tuned language models, ensemble strategies, and efficient inference techniques.


## Project Folder Structure
```Bash
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
│   ├── app.py
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
├── README.md
├── requirements.txt
├── Dockerfile
├── .dockerignore
└── .gitignore
```
