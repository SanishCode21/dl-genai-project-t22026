"""
pages/prediction.py

Prediction Page
"""

import os
import streamlit as st
import pandas as pd

from .preprocessing import build_prediction_text, build_rag_text
from .inference import MCQPredictor
from .rag import RAGRetriever
from .utils import (
    SENTENCE_TRANSFORMER_DIR,
    TFIDF_PATH,
    LOGISTIC_PATH,
    FAISS_PATH,
    CORPUS_PATH
)

from .styles import load_css, main_title, sub_title

# Cache Models
@st.cache_resource(show_spinner=False)
def load_predictor():
    return MCQPredictor(
        TFIDF_PATH,
        LOGISTIC_PATH
    )


@st.cache_resource(show_spinner=False)
def load_retriever():

    return RAGRetriever(
        embedding_model_path=SENTENCE_TRANSFORMER_DIR,
        faiss_path=FAISS_PATH,
        corpus_path=CORPUS_PATH,
    )

# Load Models
predictor = load_predictor()

retriever = load_retriever()


# Helper Functions
def build_option_dictionary(
    option_a,
    option_b,
    option_c,
    option_d,
    option_e
):
    """
    Convert option letters to option text.
    """

    return {
        "A": option_a,
        "B": option_b,
        "C": option_c,
        "D": option_d,
        "E": option_e
    }

def show():
    load_css()

    def validate_inputs(
        question,
        option_a,
        option_b,
        option_c,
        option_d,
        option_e
    ):
        """
        Validate all fields.
        """

        return all([
            question.strip(),
            option_a.strip(),
            option_b.strip(),
            option_c.strip(),
            option_d.strip(),
            option_e.strip()
        ])


    # Header
    main_title("🧠 Prediction")
    st.caption("TF-IDF + Logistic Regression")
    st.divider()


    # Model Information
    m1, m2, m3 = st.columns(3)
    m1.metric("Prediction Model", "TF-IDF + Logistic Regression")
    m2.metric("Retriever", "FAISS")
    m3.metric("Top-K", "3")

    st.divider()


    # Input Form
    with st.form("prediction_form", clear_on_submit=False):

        question = st.text_area(
            "Question",
            height=140,
            placeholder="Enter the MCQ question..."
        )

        left, right = st.columns(2)

        with left:

            option_a = st.text_area(
                "Option A",
                height=100
            )

            option_b = st.text_area(
                "Option B",
                height=100
            )

            option_c = st.text_area(
                "Option C",
                height=100
            )

        with right:

            option_d = st.text_area(
                "Option D",
                height=100
            )

            option_e = st.text_area(
                "Option E",
                height=100
            )

        submit = st.form_submit_button(
            "Predict",
            width="stretch"
        )

    # Input Validation
    if submit:

        if not validate_inputs(
            question,
            option_a,
            option_b,
            option_c,
            option_d,
            option_e
        ):

            st.error("Please complete every field before prediction.")

            st.stop()

        option_lookup = build_option_dictionary(
            option_a,
            option_b,
            option_c,
            option_d,
            option_e
        )

        prediction_text = build_prediction_text(
            question,
            option_a,
            option_b,
            option_c,
            option_d,
            option_e,
        )

        rag_text = build_rag_text(
            question,
            option_a,
            option_b,
            option_c,
            option_d,
            option_e
        )

        # Prediction logic will be added in Part 2
        try:
            # RoBERTa Prediction
            with st.spinner("Running TF-IDF + Logistic Regression prediction..."):
                labels, scores = predictor.predict(
                    prediction_text,
                    top_k=3
                )

            # FAISS Retrieval
            with st.spinner("Searching similar questions..."):

                retrieved = retriever.retrieve(
                    rag_text,
                    top_k=10          # retrieve extra, remove duplicates later
                )

            # Remove duplicate questions
            if "mcq_text" in retrieved.columns:
                retrieved = (
                    retrieved
                    .drop_duplicates(subset="mcq_text")
                    .head(3)
                    .reset_index(drop=True)

                )

            # Prediction Section
            st.divider()
            sub_title("🏆 Top-3 Predictions")
            prediction_columns = st.columns(3)
            medals = [
                "🥇",
                "🥈",
                "🥉"
            ]

            for i in range(3):
                with prediction_columns[i]:
                    label = labels[i]
                    confidence = scores[i] * 100
                    option_text = option_lookup[label]

                    st.markdown(
                        f"""
                            <div class="prediction-card">
                            <div class="prediction-title">
                            {medals[i]} Prediction {i+1}
                            </div>
                            <div class="prediction-answer">
                                {label}
                            </div>
                            <div class="prediction-score">
                            Confidence : {confidence:.2f}%
                            </div>
                            <div class="option-box">
                            {option_text}
                            </div>
                            </div>
                        """,
                        unsafe_allow_html=True
                    )

            best = scores[0]

            if best >= 0.90:
                st.success("🟢 Very High Confidence")
            elif best >= 0.70:
                st.info("🟡 High Confidence")
            elif best >= 0.50:
                st.warning("🟠 Medium Confidence")
            else:
                st.error("🔴 Low Confidence")

            # Confidence Bar Chart
            st.divider()

            sub_title("Confidence Scores")

            confidence_df = pd.DataFrame({
                "Answer": labels,
                "Confidence": [round(s * 100, 2) for s in scores],
            })

            st.bar_chart(
                confidence_df,
                x="Answer",
                y="Confidence",
                width="stretch",
            )

            # Save retrieved dataframe
            # Used in Part 3
            st.session_state["labels"] = labels
            st.session_state["scores"] = scores
            st.session_state["retrieved_questions"] = retrieved
            st.session_state["option_lookup"] = option_lookup

        except Exception as e:
            st.error("Prediction failed.")
            st.exception(e)


    ############# Part - 3
    # Retrieved Similar Questions
    if "retrieved_questions" in st.session_state:
        retrieved = st.session_state["retrieved_questions"]
        st.divider()
        sub_title("Similar Questions")

        if len(retrieved) == 0:
            st.info("No similar questions found.")
        else:
            for idx, row in retrieved.iterrows():
                with st.container(border=True):
                    st.markdown(f"### 🔹 Question {idx+1}")

                    if "similarity" in row:
                        st.progress(min(float(row["similarity"]),1.0))
                        st.caption(f"Similarity Score : {row['similarity']:.4f}")

                    if "answer" in row:
                        st.success(f"Correct Answer : {row['answer']}")

                    st.markdown("**Retrieved Question**")
                    st.write(row["prompt"])
                    st.markdown("### Options")
                    st.write(f"**A.** {row['A']}")
                    st.write(f"**B.** {row['B']}")
                    st.write(f"**C.** {row['C']}")
                    st.write(f"**D.** {row['D']}")
                    st.write(f"**E.** {row['E']}")
                    st.success(
                        f"Correct Answer : {row['answer']}"
                    )
                    st.info(
                        f"Similarity : {row['similarity']:.4f}"
                    )

    # Prediction Summary
    if "labels" in st.session_state:
        st.divider()
        sub_title("Prediction Summary")
        summary = []
        option_lookup = st.session_state["option_lookup"]
        labels = st.session_state["labels"]
        scores = st.session_state["scores"]

        for label, score in zip(labels, scores):
            summary.append({
                "Answer": label,
                "Confidence (%)": round(score*100,2),
                "Answer Text": option_lookup[label]
            })

        st.dataframe(summary,width="stretch",hide_index=True)
        summary_df = pd.DataFrame(summary)

        st.download_button(
            "📥 Download Prediction",
            summary_df.to_csv(index=False),
            file_name="prediction.csv",
            mime="text/csv"
        )

    # Tips
    st.divider()

    with st.expander("Guidelines"):
        st.markdown("""
    - Enter complete MCQ statements.
    - Enter meaningful answer choices.
    - The model predicts the **Top-3** most probable answers.
    - Retrieved questions provide supporting context.
    - Similar questions are retrieved using FAISS.

    """)
        

    # Footer
    st.divider()
    left,right = st.columns([3,1])

    with left:
        st.caption(
            "🧠 Smart MCQ Solver | TF-IDF + Logistic Regression | Sentence Transformers | FAISS | Streamlit | Hugging Face"
        )
        st.caption("Version 1.0")

    with right:
        st.markdown("---")
        c1,c2,c3=st.columns(3)

        with c1:
            st.caption("Prediction Engine")
            st.write("TF-IDF + Logistic Regression")

        with c2:
            st.caption("Retriever")
            st.write("Sentence Transformers + FAISS")

        with c3:
            st.caption("Developer")
            st.write("Sanish Kumar")

        st.markdown("---")

        st.caption(
            "© 2026 Smart MCQ Solver • Streamlit • Hugging Face • PyTorch"
        )


if __name__ == "__main__":
    show()
