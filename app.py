"""
app.py

Smart MCQ Solver
Main Controller
"""

import streamlit as st
from streamlit_option_menu import option_menu

from src.home import show as home_page
from src.prediction import show as prediction_page
from src.model_info import show as model_info_page
from src.about import show as about_page


# Page Configuration
st.set_page_config(
    page_title="Smart MCQ Solver",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# Load Custom CSS
from src.styles import load_css, PAGE_STYLE, main_title, sub_title
load_css()

st.markdown(PAGE_STYLE, unsafe_allow_html=True)

try:
    with open("assets/style.css") as css:
        st.markdown(
            f"<style>{css.read()}</style>",
            unsafe_allow_html=True
        )
except FileNotFoundError:
    pass

# Navigation Bar
selected = option_menu(
    menu_title=None,

    options=[
        "Home",
        "Prediction",
        "Models",
        "About"
    ],

    icons=[
        "house-fill",
        "cpu-fill",
        "diagram-3-fill",
        "person-fill"
    ],

    menu_icon="cast",
    default_index=0,
    orientation="horizontal",

    styles={
        "container": {
            "padding": "0!important",
            "background-color": "#C6E16E"
        },

        "icon": {
            "color": "#00B4D8",
            "font-size": "18px"
        },

        "nav-link": {
            "font-size": "16px",
            "text-align": "center",
            "margin": "2px",
            "--hover-color": "#C95555"
        },

        "nav-link-selected": {
            "background-color": "#2563EB",
            "color": "white"
        }
    }
)


st.divider()

# Page Router
if selected == "Home":
    home_page()

elif selected == "Prediction":
    prediction_page()

elif selected == "Models":
    model_info_page()

elif selected == "About":
    about_page()



# Footer
st.divider()

st.markdown(
    """
    <div style="text-align:center;color:gray;font-size:15px;">
    © 2026 Smart MCQ Solver • Built with using
    TF-IDF + Logistic Regression • MiniLM • FAISS • Streamlit
    </div>
    """,
    unsafe_allow_html=True
)

