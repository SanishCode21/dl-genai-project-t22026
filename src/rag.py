"""
src/rag.py

Retrieval-Augmented Generation (FAISS)
"""

import faiss
import numpy as np
import pandas as pd

from sentence_transformers import SentenceTransformer


class RAGRetriever:

    def __init__(
        self,
        embedding_model_path,
        faiss_path,
        corpus_path
    ):

        self.model = SentenceTransformer(
            embedding_model_path
        )

        self.index = faiss.read_index(
            faiss_path
        )

        self.corpus = pd.read_csv(
            corpus_path
        )

    def encode(
        self,
        text
    ):

        embedding = self.model.encode(
            text,
            convert_to_numpy=True,
            normalize_embeddings=True
        )

        return np.array([embedding])


    def retrieve(
        self,
        query,
        top_k=3
    ):

        embedding = self.encode(
            query
        )

        scores, indices = self.index.search(
            embedding,
            top_k + 5
        )

        retrieved = self.corpus.iloc[
            indices[0]
        ].copy()

        retrieved["similarity"] = scores[0]

        retrieved = retrieved.drop_duplicates(
            subset="mcq_text"
        )

        retrieved = retrieved.sort_values(
            by="similarity",
            ascending=False
        )

        retrieved = retrieved.head(
            top_k
        )

        return retrieved.reset_index(
            drop=True
        )

    def retrieve_one(
        self,
        query
    ):

        return self.retrieve(
            query,
            top_k=1
        )


    def corpus_size(
        self
    ):

        return len(
            self.corpus
        )

