"""
rag.py
"""

import faiss
import pandas as pd
import numpy as np

from sentence_transformers import SentenceTransformer


class RAGRetriever:

    def __init__(self, embedding_model_path, faiss_path, corpus_path):

        self.model = SentenceTransformer(
            embedding_model_path
        )

        self.index = faiss.read_index(
            faiss_path
        )

        self.corpus = pd.read_csv(
            corpus_path
        )

    def retrieve(self, query, top_k=3):

        embedding = self.model.encode(
            query,
            convert_to_numpy=True,
            normalize_embeddings=True
        )

        scores, indices = self.index.search(
            np.array([embedding]),
            top_k
        )

        retrieved = self.corpus.iloc[
            indices[0]
        ].copy()

        retrieved["similarity"] = scores[0]

        return retrieved.reset_index(drop=True)
    
