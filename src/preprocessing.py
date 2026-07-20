"""
preprocessing.py
"""

#def build_roberta_text(question, option_a, option_b, option_c, option_d, option_e, tokenizer):
def build_prediction_text(question, a, b, c, d, e):
    return (
        f"{question}\n\n"
        f"A. {a}\n"
        f"B. {b}\n"
        f"C. {c}\n"
        f"D. {d}\n"
        f"E. {e}"
    )

def build_rag_text(question, option_a, option_b, option_c, option_d, option_e):
    """
    Build exactly the same input used for
    SentenceTransformer + FAISS.
    """

    return (
        f"Question: {question}\n\n"
        f"A. {option_a}\n"
        f"B. {option_b}\n"
        f"C. {option_c}\n"
        f"D. {option_d}\n"
        f"E. {option_e}"
    )

