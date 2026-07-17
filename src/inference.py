"""
src/inference.py

RoBERTa Prediction Engine
"""

import joblib
import numpy as np
import torch

from scipy.special import softmax

from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification
)


class RobertaPredictor:

    def __init__(
        self,
        model_path,
        label_path
    ):

        self.device = torch.device(
            "cuda"
            if torch.cuda.is_available()
            else "cpu"
        )

        # Tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(
            model_path
        )

        # Model
        self.model = AutoModelForSequenceClassification.from_pretrained(
            model_path
        )

        self.model.to(
            self.device
        )

        self.model.eval()


        # Label Mapping
        mapping = joblib.load(
            label_path
        )

        self.id2label = mapping["ID2LABEL"]
        self.label2id = mapping["LABEL2ID"]


    def preprocess(
        self,
        text
    ):

        encoded = self.tokenizer(
            text,
            truncation=True,
            padding=True,
            max_length=512,
            return_tensors="pt"
        )

        encoded = {
            k: v.to(self.device)
            for k, v in encoded.items()
        }

        return encoded


    def predict(
        self,
        text,
        top_k=3
    ):
        inputs = self.preprocess(
            text
        )

        with torch.no_grad():
            outputs = self.model(
                **inputs
            )

        probabilities = softmax(
            outputs.logits.cpu().numpy(),
            axis=1
        )[0]

        ranking = np.argsort(
            -probabilities
        )[:top_k]

        labels = [
            self.id2label[idx]
            for idx in ranking
        ]

        scores = [
            float(probabilities[idx])
            for idx in ranking
        ]

        return labels, scores


    def predict_proba(
        self,
        text
    ):
        inputs = self.preprocess(
            text
        )

        with torch.no_grad():
            outputs = self.model(
                **inputs
            )

        probabilities = softmax(
            outputs.logits.cpu().numpy(),
            axis=1
        )[0]

        return probabilities

    
    def predict_one(
        self,
        text
    ):

        labels, scores = self.predict(
            text,
            top_k=1
        )

        return labels[0], scores[0]
    
