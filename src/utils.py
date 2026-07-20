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


# Local Cache Directory
CACHE_DIR = os.path.join(
    os.path.expanduser("~"),
    ".cache",
    "smart-mcq-solver"
)


# Hugging Face Repository
HF_REPO = "SanishKumarSingh/smart-mcq-solver-models"


# Local Paths
MODEL_DIR = CACHE_DIR

RAG_DIR = os.path.join(
    MODEL_DIR,
    "rag-faiss"
)

SENTENCE_TRANSFORMER_DIR = os.path.join(
    MODEL_DIR,
    "sentence-transformer"
)

TFIDF_PATH = os.path.join(
    RAG_DIR,
    "tfidf_vectorizer.joblib"
)

LOGISTIC_PATH = os.path.join(
    RAG_DIR,
    "logistic_regression.joblib"
)

FAISS_PATH = os.path.join(
    RAG_DIR,
    "mcq_rag_index.faiss"
)

CORPUS_PATH = os.path.join(
    RAG_DIR,
    "knowledge_corpus.csv"
)

# Download Models (Only Once)
required_files = [
    TFIDF_PATH,
    LOGISTIC_PATH,
    FAISS_PATH,
    CORPUS_PATH,
    os.path.join(
        SENTENCE_TRANSFORMER_DIR,
        "model.safetensors"
    ),
]

if not all(os.path.exists(file) for file in required_files):

    print("Downloading models from Hugging Face...")

    snapshot_download(
        repo_id=HF_REPO,
        repo_type="model",
        local_dir=CACHE_DIR,
        allow_patterns=[
            "sentence-transformer/*",
            "rag-faiss/*"
        ],
        local_dir_use_symlinks=False,
    ) # type: ignore

    print("Download complete.")

else:
    print("Using cached models.")
