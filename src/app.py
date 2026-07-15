import streamlit as st
import os
from preprocessing import build_roberta_text, build_rag_text
from inference import RobertaPredictor
from rag import RAGRetriever
from utils import (
    ROBERTA_DIR,
    LABEL_MAPPING,
    RAG_DIR,
    SENTENCE_TRANSFORMER_DIR
)


predictor = RobertaPredictor(model_path=ROBERTA_DIR, label_path=LABEL_MAPPING)

retriever = RAGRetriever(

    embedding_model_path=SENTENCE_TRANSFORMER_DIR,

    faiss_path=os.path.join(
        RAG_DIR,
        "mcq_rag_index.faiss"
    ),

    corpus_path=os.path.join(
        RAG_DIR,
        "knowledge_corpus.csv"
    )

)

# Page Config
st.set_page_config(
    page_title="Smart MCQ Solver",
    page_icon="🧠",
    layout="wide"
)


# Cache Models
@st.cache_resource
def load_predictor():
    return RobertaPredictor(
        ROBERTA_DIR,
        LABEL_MAPPING
    )


@st.cache_resource
def load_retriever():
    return RAGRetriever(
        embedding_model_path=SENTENCE_TRANSFORMER_DIR,
        faiss_path=os.path.join(
            RAG_DIR,
            "mcq_rag_index.faiss"
        ),
        corpus_path=os.path.join(
            RAG_DIR,
            "knowledge_corpus.csv"
        )
    )


predictor = load_predictor()
retriever = load_retriever()

# Header
st.title("🧠 Smart MCQ Solver")

st.caption(
    "Fine-tuned RoBERTa + Retrieval-Augmented Generation (FAISS)"
)

st.divider()


# Input Form
with st.form("mcq_form"):

    question = st.text_area(
        "Question",
        height=140
    )

    col1, col2 = st.columns(2)

    with col1:

        option_a = st.text_input("Option A")

        option_b = st.text_input("Option B")

        option_c = st.text_input("Option C")

    with col2:

        option_d = st.text_input("Option D")

        option_e = st.text_input("Option E")

    submit = st.form_submit_button(
        "Predict"
    )


# Prediction
if submit:

    if not all([
        question,
        option_a,
        option_b,
        option_c,
        option_d,
        option_e
    ]):

        st.warning(
            "Please fill every field."
        )

        st.stop()

    # Build input for RoBERTa
    roberta_text = build_roberta_text(
        question,
        option_a,
        option_b,
        option_c,
        option_d,
        option_e,
        predictor.tokenizer      # uses </s> separator
    )

    # Build input for FAISS Retrieval
    rag_text = build_rag_text(
        question,
        option_a,
        option_b,
        option_c,
        option_d,
        option_e
    )

    with st.spinner("Running RoBERTa..."):

        labels, scores = predictor.predict(
            roberta_text
        )

    with st.spinner("Searching similar questions..."):

        retrieved = retriever.retrieve(
            rag_text,
            top_k=3
        )

    st.divider()

    st.subheader("🏆 Top-3 Predictions")

    cols = st.columns(3)

    medals = [
        "🥇",
        "🥈",
        "🥉"
    ]

    for i in range(3):

        cols[i].metric(
            label=f"{medals[i]} Rank {i+1}",
            value=labels[i],
            delta=f"{scores[i]*100:.2f}%"
        )

    st.divider()

    st.subheader("Similar Questions")

    for idx, row in retrieved.iterrows():

        with st.expander(
            f"Question {idx+1}"
        ):

            st.write(row["mcq_text"])

            if "label" in row:

                st.success(
                    f"Correct Answer : {row['label']}"
                )

            st.info(
                f"Similarity : {row['similarity']:.4f}"
            )

    st.divider()

    st.caption(
        "Powered by FacebookAI RoBERTa • SentenceTransformers • FAISS • Streamlit"
    )


