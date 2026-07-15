"""
metrics.py
"""

import numpy as np


def map_at_3(y_true, top3_predictions):

    score = 0

    for truth, pred in zip(y_true, top3_predictions):

        if truth == pred[0]:
            score += 1

        elif truth == pred[1]:
            score += 0.5

        elif truth == pred[2]:
            score += 1 / 3

    return score / len(y_true)


