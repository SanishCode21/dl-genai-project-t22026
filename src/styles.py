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


        /* Prediction Card */
        .prediction-card{

            padding:22px;

            border-radius:18px;

            background:linear-gradient(145deg,#1E293B,#0F172A);

            border:1px solid #334155;

            margin-bottom:22px;

            box-shadow:0 8px 24px rgba(0,0,0,.25);

            transition:all .35s ease;

            overflow:hidden;

            position:relative;

        }

        /* Top Glow */

        .prediction-card::before{

            content:"";

            position:absolute;

            left:0;
            top:0;

            width:100%;
            height:4px;

            background:linear-gradient(
                90deg,
                #3B82F6,
                #06B6D4,
                #22C55E
            );

        }

        /* Hover Effect */

        .prediction-card:hover{

            transform:translateY(-6px);

            box-shadow:0 18px 36px rgba(37,99,235,.30);

            border-color:#3B82F6;

        }


        /* Prediction Title */
        .prediction-title{

            font-size:24px;

            font-weight:700;

            color:#F8FAFC;

            margin-bottom:8px;

        }

        .prediction-answer{
            font-size:52px;
            font-weight:800;
            color:#3B82F6;
            text-align:center;
            margin:12px 0;
        }

        /* Confidence Score Badge */
        .prediction-score{

            display:inline-block;

            padding:8px 18px;

            border-radius:999px;

            background:rgba(34,197,94,.12);

            border:1px solid rgba(34,197,94,.35);

            color:#22C55E;

            font-size:16px;

            font-weight:700;

            margin-bottom:18px;

        }


        /* Option Box */

        .option-box{

            background:#334155;

            color:#E2E8F0;

            padding:14px 16px;

            border-radius:12px;

            border-left:5px solid #3B82F6;

            margin-top:12px;

            transition:all .30s ease;

        }


        /* Hover */

        .option-box:hover{

            background:#3F4F63;

            transform:translateX(6px);

            border-left-color:#22C55E;

        }


        /* Option Label */
        .option-label{

            color:#60A5FA;

            font-weight:700;

        }


        /* Rank Badge */

        .rank-badge{

            display:inline-block;

            padding:6px 14px;

            border-radius:999px;

            background:#2563EB;

            color:white;

            font-size:14px;

            font-weight:700;

            margin-bottom:10px;

        }


        @keyframes fadeIn{

            from{

                opacity:0;

                transform:translateY(20px);

            }

            to{

                opacity:1;

                transform:translateY(0);

            }

        }

        .prediction-card{

            animation:fadeIn .45s ease;

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

