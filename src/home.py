"""
src/home.py

Home Page
"""

import streamlit as st

from src.styles import main_title, sub_title


def show():
    main_title("Welcome to Smart MCQ Solver")
    st.markdown(
        """
        ### AI-Powered Multiple Choice Question Solver

        Smart MCQ Solver combines a lightweight
        **TF-IDF + Logistic Regression** prediction model with
        **Retrieval-Augmented Generation (RAG)** to predict the
        most likely answers while retrieving semantically similar
        questions from the knowledge base for additional context.
        """
    )

    st.markdown("---")

    # Key Features
    sub_title("Key Features")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.info(
            """
            ### Prediction Engine

            • TF-IDF Vectorization

            • Logistic Regression

            • Top-3 Answer Prediction

            • Confidence Scores
            """
        )

    with col2:

        st.success(
            """
            ### Retrieval-Augmented Generation

            • MiniLM Sentence Transformer

            • FAISS Vector Search

            • Similar Question Retrieval
            """
        )

    with col3:

        st.warning(
            """
            ### Deployment

            • Streamlit

            • Hugging Face Hub

            • Lightweight Models
            """
        )

    st.markdown("---")

    # Architecture
    sub_title("System Architecture")

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
                                        Similar Questions + Context
        """,
        language="text",
    )

    st.markdown("---")

    # Project Statistics
    sub_title("Project Statistics")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Prediction Model",
            "TF-IDF + LR"
        )

    with c2:
        st.metric(
            "Embedding",
            "MiniLM"
        )

    with c3:
        st.metric(
            "Vector Search",
            "FAISS"
        )

    with c4:
        st.metric(
            "Predictions",
            "Top-3"
        )

    st.markdown("---")

    # Technology Stack
    sub_title("Technology Stack")

    left, right = st.columns(2)

    with left:

        st.markdown(
            """
            #### AI & Machine Learning

            - TF-IDF Vectorizer

            - Logistic Regression

            - Sentence Transformers

            - FAISS

            - Scikit-Learn
            """
        )

    with right:

        st.markdown(
            """
            #### Deployment

            - Streamlit

            - Hugging Face Hub

            - GitHub
            """
        )

    st.markdown("---")

    # How It Works
    sub_title("How It Works")

    st.markdown(
        """
        **Step 1**

        Enter your multiple-choice question and answer options.

        **Step 2**

        The question is converted into TF-IDF features.

        **Step 3**

        A Logistic Regression model predicts the Top-3 most probable answers with confidence scores.

        **Step 4**

        The same question is converted into semantic embeddings using the MiniLM Sentence Transformer.

        **Step 5**

        FAISS retrieves the most similar questions from the knowledge base.

        **Step 6**

        The retrieved questions and their correct answers are displayed as supporting context.
        """
    )

    st.markdown("---")

    st.success(
        "👉 Select **Prediction** from the navigation bar above to start solving MCQs."
    )

    st.markdown("---")

    st.markdown(
        """
        <div style="text-align:center;color:gray;font-size:15px;">
        Smart MCQ Solver • Deep Learning & Generative AI Project • IIT Madras BS Degree
        </div>
        """,
        unsafe_allow_html=True,
    )
