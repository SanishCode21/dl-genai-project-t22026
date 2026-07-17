"""
src/utils.py

Utility paths and model downloading.
"""

import os

from huggingface_hub import snapshot_download


# Root Directory
ROOT_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

CACHE_DIR = os.path.join(
    os.path.expanduser("~"),
    ".cache",
    "smart-mcq-solver"
)


# Hugging Face Repository
HF_REPO = "SanishKumarSingh/smart-mcq-solver-models"


# Download Models
snapshot_download(

    repo_id=HF_REPO,

    repo_type="model",

    local_dir=CACHE_DIR,

    allow_patterns=[
        "roberta-finetuned/*",
        "sentence-transformer/*",
        "rag-faiss/*"
    ]

)

MODEL_DIR = CACHE_DIR


# RoBERTa
ROBERTA_DIR = os.path.join(

    MODEL_DIR,

    "roberta-finetuned"

)


LABEL_MAPPING = os.path.join(
    ROBERTA_DIR,
    "label_mapping.joblib"
)


# RAG
RAG_DIR = os.path.join(
    MODEL_DIR,
    "rag-faiss"
)


# Sentence Transformer
SENTENCE_TRANSFORMER_DIR = os.path.join(
    MODEL_DIR,
    "sentence-transformer"
)
