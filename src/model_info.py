"""
src/model_info.py

Model Information Page
"""

import streamlit as st
from src.styles import main_title, sub_title


def show():

    main_title("Model Information")

    st.markdown(
        """
        Learn about the machine learning models, retrieval pipeline,
        and technologies powering Smart MCQ Solver.
        """
    )

    st.markdown("---")

    # Prediction Model
    sub_title("Prediction Model")

    c1, c2 = st.columns([1, 2])

    with c1:

        st.metric("Model", "TF-IDF + Logistic Regression")
        st.metric("Framework", "Scikit-Learn")
        st.metric("Task", "MCQ Classification")

    with c2:

        st.info(
            """
            **TF-IDF + Logistic Regression**

            ✔ TF-IDF text vectorization

            ✔ Logistic Regression classifier

            ✔ Predicts Top-3 Answers

            ✔ Probability-based Confidence Scores

            ✔ Fast CPU Inference
            """
        )

    st.markdown("---")

    # Retrieval Pipeline
    sub_title("Retrieval-Augmented Generation")

    c1, c2 = st.columns([1, 2])

    with c1:

        st.metric("Embedding", "all-MiniLM-L6-v2")
        st.metric("Retriever", "FAISS")
        st.metric("Top K", "3")

    with c2:

        st.success(
            """
            **Sentence Transformer**

            • all-MiniLM-L6-v2

            • Dense Semantic Embeddings

            • FAISS Similarity Search

            • Retrieves Similar MCQs
            """
        )

    st.markdown("---")

    # Pipeline
    sub_title("Inference Pipeline")

    st.code(
        """
                                            User Question
                                                │
                                                ▼
                                            Text Preprocessing
                                                │
                                                ▼
                                        TF-IDF Vectorization
                                                │
                                                ▼
                                    Logistic Regression
                                                │
                                                ▼
                                        Top-3 Predictions
                                                │
                                                ▼
                                    SentenceTransformer (MiniLM)
                                                │
                                                ▼
                                        FAISS Retrieval
                                                │
                                                ▼
                                        Similar Questions
        """,
        language="text",
    )

    st.markdown("---")


    # Components
    sub_title("Project Components")

    left, right = st.columns(2)

    with left:

        st.markdown(
            """
            ### Models

            - TF-IDF Vectorizer

            - Logistic Regression

            - SentenceTransformer (MiniLM)

            - FAISS Index
            """
        )

    with right:

        st.markdown(
        """
            ### Libraries

            - Scikit-Learn

            - Sentence Transformers

            - FAISS

            - Hugging Face Hub

            - Streamlit
        """
        )

    st.markdown("---")

    # Deployment
    sub_title("Deployment Stack")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Frontend", "Streamlit")
    c2.metric("ML", "Scikit-Learn")
    c3.metric("Retriever", "FAISS")
    c4.metric("Models", "HF Hub")

    st.markdown("---")

    st.caption("Model Version: v2.0")
