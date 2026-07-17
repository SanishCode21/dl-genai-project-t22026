"""
src/model_info.py

Model Information Page
"""

import streamlit as st
from src.styles import load_css, main_title, sub_title

def show():

    main_title("Model Information")

    st.markdown(
        """
        Learn about the deep learning models, retrieval pipeline,
        and technologies powering Smart MCQ Solver.
        """
    )

    st.markdown("---")

    sub_title("Prediction Model")

    c1, c2 = st.columns([1,2])

    with c1:
        st.metric("Model", "RoBERTa-v3")
        st.metric("Framework", "PyTorch")
        st.metric("Task", "MCQ Classification")

    with c2:

        st.info(
        """
        **FacebookAI/RoBERTa-v3-base**

        ✔ Fine-tuned on MCQ dataset

        ✔ Context-aware Transformer Encoder

        ✔ Predicts Top-3 Answers
        
        ✔ Softmax Confidence Scores
        
        ✔ HuggingFace Transformers

        """
        )

    st.markdown("---")
    sub_title("Retrieval-Augmented Generation")
    c1, c2 = st.columns([1,2])

    with c1:
        st.metric("Embedding", "BGE-base")
        st.metric("Retriever", "FAISS")
        st.metric("Top K", "3")

    with c2:
        st.success(
        """

        **Sentence Transformer**

        • BAAI/bge-base-en-v1.5
        
        • Dense Vector Embeddings
        
        • FAISS Similarity Search
        
        • Context Retrieval

        """
        )

    st.markdown("---")
    sub_title("Inference Pipeline")
    st.code(
        """
                                                User Question
                                                    │
                                                    ▼
                                                Preprocessing
                                                    │
                                                    ▼
                                                RoBERTa-v3 Prediction
                                                    │
                                                    ▼
                                                Top-3 Answers
                                                    │
                                                    ▼
                                                Sentence Transformer
                                                    │
                                                    ▼
                                                FAISS Retrieval
                                                    │
                                                    ▼
                                                Similar Questions
        """,

language="text"
    )
    st.markdown("---")
    sub_title("Project Components")
    left,right=st.columns(2)
    with left:
        st.markdown("""
                    
            ### Models

            - FacebookAI/RoBERTa-v3-base
            
            - BAAI/bge-base-en-v1.5
                    
            - FAISS Index
                    
            """
            )

    with right:

        st.markdown("""
            ### Libraries

            - Transformers
                    
            - Sentence Transformers
            
            - PyTorch
            
            - FAISS
                    
            - Streamlit
                    
            """
                    )

    st.markdown("---")

    sub_title("Deployment Stack")

    c1,c2,c3,c4=st.columns(4)
    c1.metric("Frontend","Streamlit")
    c2.metric("Container","Docker")
    c3.metric("Hosting","HF Spaces")
    c4.metric("Repository","GitHub")

    st.markdown("---")
    st.caption("Model Version : v1.0")

