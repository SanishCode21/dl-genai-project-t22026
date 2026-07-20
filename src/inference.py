"""
src/inference.py

TF-IDF + Logistic Regression Prediction Engine
"""

import joblib
import numpy as np


class MCQPredictor:

    def __init__(
        self,
        vectorizer_path,
        model_path
    ):

        self.vectorizer = joblib.load(
            vectorizer_path
        )

        self.model = joblib.load(
            model_path
        )

        self.labels = np.array(
            ["A", "B", "C", "D", "E"]
        )


    def predict_proba(
        self,
        text
    ):

        X = self.vectorizer.transform(
            [text]
        )

        probabilities = self.model.predict_proba(
            X
        )[0]

        return probabilities


    def predict(
        self,
        text,
        top_k=3
    ):

        probabilities = self.predict_proba(
            text
        )

        ranking = np.argsort(
            -probabilities
        )[:top_k]

        labels = self.labels[
            ranking
        ].tolist()

        scores = probabilities[
            ranking
        ].tolist()

        return labels, scores


    def predict_one(
        self,
        text
    ):

        labels, scores = self.predict(
            text,
            top_k=1
        )

        return labels[0], scores[0]
    
