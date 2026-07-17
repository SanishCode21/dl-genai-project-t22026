import streamlit as st

PAGE_STYLE = """
    <style>

    .main-title{
        font-size:40px;
        font-weight:bold;
        color:#1f77b4;
        text-align:center;
        padding-bottom:2rem;
    }

    .sub-title{
        font-size:28px;
        font-weight:600;
        color:#444;
        text-align:center;
        padding-bottom:2rem;
    }

    </style>
"""

def main_title(text):
    st.markdown(
        f'<h1 class="main-title">{text}</h1>',
        unsafe_allow_html=True,
    )

def sub_title(text):
    st.markdown(
        f'<h2 class="sub-title">{text}</h2>',
        unsafe_allow_html=True,
    )


def load_css():

    st.markdown(
        """
        <style>

        /* Main Page */
        
        .block-container{
            padding-top:2rem;
            padding-bottom:2rem;
            max-width:1250px;
        }

        /* Metric Cards */
        div[data-testid="metric-container"]{

            border-radius:18px;

            padding:18px;

            border:1px solid rgba(255,255,255,0.08);

            background:rgba(30,30,35,.45);

            box-shadow:0 5px 15px rgba(0,0,0,.20);

        }

        /* Buttons */
        .stButton>button{

            width:100%;

            height:48px;

            border-radius:12px;

            font-weight:600;

        }

        /* Text Inputs */
        .stTextInput>div>div>input{

            border-radius:10px;

        }


        textarea{

            border-radius:10px !important;

        }

        /* Expanders */
        .streamlit-expanderHeader{

            font-weight:600;

        }


        /* Prediction Cards */
        .prediction-card{

            padding:20px;

            border-radius:16px;

            background:#1E293B;              /* Dark slate */

            border:1px solid #334155;

            margin-bottom:18px;

            box-shadow:0 4px 12px rgba(0,0,0,0.15);

        }


        /* Card Title */
        .prediction-title{

            font-size:22px;

            font-weight:700;

            color:#F8FAFC;                   /* Nearly white */

            margin-bottom:8px;

        }


        /* Confidence Score */
        .prediction-score{

            font-size:18px;

            font-weight:600;

            color:#22C55E;                   /* Green */

            margin-bottom:12px;

        }


        /* Option Box */
        .option-box{

            background:#334155;              /* Slightly lighter than card */

            color:#E2E8F0;                   /* Light gray text */

            padding:12px;

            border-radius:12px;

            border-left:4px solid #3B82F6;   /* Blue accent */

            margin-top:10px;

        }

        /* Footer */
        .footer{

            text-align:center;

            color:gray;

            margin-top:40px;

            font-size:14px;

        }


        /* Sidebar */
        section[data-testid="stSidebar"]{

            border-right:1px solid rgba(255,255,255,.06);

        }


        /* Success */
        .stSuccess{

            border-radius:12px;

        }


        /* Info */
        .stInfo{

            border-radius:12px;

        }


        /* Warning */
        .stWarning{

            border-radius:12px;

        }


        /* Spinner */
        .stSpinner{

            text-align:center;

        }

        </style>
                """,
                unsafe_allow_html=True

    )

