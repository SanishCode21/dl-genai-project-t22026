"""
inference.py
"""

import os
import joblib
import numpy as np
import torch

from scipy.special import softmax

from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification
)

from utils import (
    ROBERTA_DIR,
    LABEL_MAPPING
)

class RobertaPredictor:

    def __init__(self, model_path, label_path):

        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        self.tokenizer = AutoTokenizer.from_pretrained(
            model_path
        )

        self.model = AutoModelForSequenceClassification.from_pretrained(
            model_path
        )

        self.model.to(self.device)

        self.model.eval()

        mapping = joblib.load(label_path)

        self.id2label = mapping["ID2LABEL"]

    def predict(self, text, top_k=3):

        inputs = self.tokenizer(
            text,
            truncation=True,
            padding=True,
            max_length=512,
            return_tensors="pt"
        )

        inputs = {
            k: v.to(self.device)
            for k, v in inputs.items()
        }

        with torch.no_grad():

            outputs = self.model(**inputs)

        probs = softmax(
            outputs.logits.cpu().numpy(),
            axis=1
        )[0]

        order = np.argsort(-probs)[:top_k]

        labels = [
            self.id2label[i]
            for i in order
        ]

        scores = probs[order]

        return labels, scores
    

predictor = RobertaPredictor(ROBERTA_DIR, LABEL_MAPPING)

