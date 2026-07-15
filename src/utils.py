"""
utils.py
"""

import os

from huggingface_hub import snapshot_download


HF_MODEL_REPO = "SanishKumarSingh/smart-mcq-solver-models"

CACHE_DIR = os.path.join(
    os.path.expanduser("~"),
    ".cache",
    "smart-mcq-solver"
)


def download_models():

    model_path = snapshot_download(
        repo_id=HF_MODEL_REPO,
        repo_type="model",
        local_dir=CACHE_DIR,
        allow_patterns=[
            "roberta-finetuned/*",
            "sentence-transformer/*",
            "rag-faiss/*"
        ]
    )

    return model_path


MODEL_DIR = download_models()


ROBERTA_DIR = os.path.join(
    MODEL_DIR,
    "roberta-finetuned"
)

LABEL_MAPPING = os.path.join(
    ROBERTA_DIR,
    "label_mapping.joblib"
)

RAG_DIR = os.path.join(
    MODEL_DIR,
    "rag-faiss"
)

SENTENCE_TRANSFORMER_DIR = os.path.join(
    MODEL_DIR,
    "sentence-transformer"
)


