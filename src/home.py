"""
src/home.py
Home Page
"""

import streamlit as st

from src.styles import load_css, main_title, sub_title

def show():
    main_title("Welcome to Smart MCQ Solver")

    st.markdown(
        """
        ### AI-Powered Multiple Choice Question Solver

        Smart MCQ Solver combines a fine-tuned **FacebookAI/RoBERTa-v3-base**
        transformer with **Retrieval-Augmented Generation (RAG)** to predict
        the most likely answers while retrieving similar questions for
        additional context.
        """
    )

    st.markdown("---")
    sub_title("Key Features")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.info(
            """
            ### Transformer Prediction
            
            • Fine-tuned FacebookAI/RoBERTa-v3-base
            
            • Predicts Top-3 Answers
            
            • Confidence Scores

            """
        )

    with col2:
        st.success(
            """
            ### Retrieval-Augmented Generation

            • Sentence Transformers
            
            • FAISS Vector Search
            
            • Similar Question Retrieval

            """
        )

    with col3:
        st.warning(
            """
            ### Deployment
            
            • Streamlit
            
            • Docker
            
            • Hugging Face Spaces
            """
        )

    st.markdown("---")
    sub_title("System Architecture")
    st.code(
        """
                                                        User Question
                                                            │
                                                            ▼
                                                Fine-tuned FacebookAI/RoBERTa
                                                            │
                                                            ▼
                                                    Top-3 Predictions
                                                            │
                                                            ▼
                                                Sentence Transformer Embedding
                                                            │
                                                            ▼
                                                    FAISS Retrieval
                                                            │
                                                            ▼
                                                Similar Questions + Answers
        """,
        language="text"
    )

    st.markdown("---")
    sub_title("Project Statistics")
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Prediction Model",
            "RoBERTa-v3"
        )

    with c2:
        st.metric(
            "Embedding",
            "BGE-base"
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
    sub_title("Technology Stack")
    left, right = st.columns(2)

    with left:
        st.markdown(
            """
            #### AI & Machine Learning

            - FacebookAI/RoBERTa-v3-base
            
            - Sentence Transformers
            
            - FAISS
            
            - PyTorch
            
            - Transformers
            
            """
        )

    with right:
        st.markdown(
            """

            #### Deployment

            - Streamlit
            
            - Docker
            
            - Hugging Face Spaces
            
            - GitHub

            """
        )

    st.markdown("---")
    sub_title("How It Works")
    st.markdown(
        """
        **Step 1**
        Enter your multiple-choice question.

        **Step 2**
        The RoBERTa model predicts the Top-3 most probable answers.

        **Step 3**
        The question is converted into embeddings using a Sentence Transformer.

        **Step 4**
        FAISS retrieves the most similar questions from the knowledge base.

        **Step 5**
        The retrieved questions and their answers are displayed as supporting evidence.
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
            "Smart MCQ Solver • Deep Learning & Generative AI Project • IIT Madras BS Degree"
            </div>
            """,
            unsafe_allow_html=True
    )
      

