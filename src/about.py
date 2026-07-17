"""
src/about.py

About Page
"""

import streamlit as st
from src.styles import load_css, main_title, sub_title

def show():
    main_title("About")
    st.markdown(
        """
        Smart MCQ Solver is an end-to-end Deep Learning and
        Retrieval-Augmented Generation application developed
        for the IIT Madras BS Degree Deep Learning & GenAI Project.
        """
    )

    st.markdown("---")
    sub_title("Project Goal")

    st.write(
        """
        The objective of this project is to build an intelligent
        Multiple Choice Question Solver capable of:

        • Predicting Top-3 Answers
        
        • Understanding contextual information
        
        • Retrieving similar questions
        
        • Providing confidence scores
        
        • Delivering explainable predictions
        
        """
    )

    st.markdown("---")
    sub_title("Developer")
    
    c1,c2=st.columns([1,3])

    with c1:
        st.title("👨‍💻")

    with c2:
        st.write("**Name**")
        st.write("Sanish Kumar")
        st.write("**Program**")
        st.write("BS Degree in Data Science")
        st.write("**Institute**")
        st.write("Indian Institute of Technology Madras")

    st.markdown("---")

    sub_title("Technologies Used")
    left,right=st.columns(2)

    with left:
        st.success("Python")
        st.success("PyTorch")
        st.success("Transformers")
        st.success("Sentence Transformers")
        st.success("Git & GitHub")

    with right:
        st.info("Kaggle Notebook")
        st.info("RAG + FAISS")
        st.info("Streamlit")
        st.info("Docker")
        st.info("Hugging Face Spaces")

    st.markdown("---")

    sub_title("Project Highlights")

    col1,col2,col3,col4=st.columns(4)
    col1.metric("Prediction","Top-3")
    col2.metric("Architecture","RoBERTa + RAG")
    col3.metric("Retriever","FAISS")
    col4.metric("Deployment","Docker")
    st.markdown("---")
    sub_title("Contacts")
    st.write("Email")
    st.code("sanishbux42@gmail.com")
    st.write("GitHub")
    st.code("https://github.com/SanishCode21")
    st.write("Hugging Face")
    st.code("https://huggingface.co/SanishKumarSingh")
    st.write("LinkedIn")
    st.code("https://www.linkedin.com/in/sanish-kumar-singh-163679289")
    st.write("Kaggle Profile")
    st.code("https://www.kaggle.com/code/sanishkumarsingh")
    st.markdown("---")
    sub_title("License")
    st.info(
        """
        This project is developed for educational and research purposes.
        The implementation demonstrates the use of Deep Learning,
        Transformers, Sentence Embeddings, Retrieval-Augmented Generation,
        and FAISS for intelligent MCQ solving.
        """
    )

    st.markdown("---")

    st.caption(
        "© 2026 Smart MCQ Solver • Developed by Sanish Kumar"
    )

