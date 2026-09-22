import streamlit as st

def apply_professional_theme():
    """
    Call this ONCE at the very top of app.py, right after
    st.set_page_config(...). This only changes the LOOK of the
    app - fonts, colors, spacing, card styling. It does not touch
    any of your existing logic or variables.
    """

    st.markdown("""
        <style>
        /* Overall app background */
        .stApp {
            background-color: #ffffff;
        }

        /* Main title styling */
        h1 {
            font-family: 'Segoe UI', sans-serif;
            font-weight: 700;
            color: #1a1a2e;
            padding-bottom: 0px;
        }

        h2, h3 {
            font-family: 'Segoe UI', sans-serif;
            font-weight: 600;
            color: #1a1a2e;
            border-bottom: 1px solid #e0e6f0;
            padding-bottom: 6px;
            margin-top: 24px;
        }

        p, span, label, li {
            color: #333333;
        }

        /* Metric cards (Resume Score, ATS Score etc.) */
        div[data-testid="stMetric"] {
            background-color: #f5f8ff;
            border: 1px solid #d6e0f5;
            border-radius: 10px;
            padding: 16px 12px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.06);
        }

        div[data-testid="stMetricValue"] {
            font-size: 26px;
            font-weight: 700;
            color: #1e6fd9;
        }

        div[data-testid="stMetricLabel"] {
            color: #5a6b8c;
        }

        /* Buttons */
        .stButton > button {
            background-color: #1e6fd9;
            color: white;
            border-radius: 8px;
            border: none;
            padding: 8px 20px;
            font-weight: 600;
            transition: all 0.2s ease-in-out;
        }
        .stButton > button:hover {
            background-color: #1859ad;
            transform: translateY(-1px);
            box-shadow: 0 4px 10px rgba(30,111,217,0.3);
        }

        /* Success / warning / error boxes */
        div[data-testid="stAlert"] {
            border-radius: 8px;
            padding: 14px;
        }

        /* Progress bars */
        div[data-testid="stProgress"] > div > div {
            background-color: #1e6fd9;
            border-radius: 6px;
        }

        /* File uploader box */
        section[data-testid="stFileUploaderDropzone"] {
            background-color: #f5f8ff;
            border: 1.5px dashed #b8cdf0;
            border-radius: 10px;
        }

        /* Text area / input boxes */
        textarea, .stTextArea textarea {
            background-color: #ffffff !important;
            border: 1px solid #d6e0f5 !important;
            border-radius: 8px !important;
            color: #1a1a2e !important;
        }

        /* DataFrames / tables */
        div[data-testid="stDataFrame"] {
            border: 1px solid #d6e0f5;
            border-radius: 8px;
            overflow: hidden;
        }

        /* Sidebar */
        section[data-testid="stSidebar"] {
            background-color: #f5f8ff;
            border-right: 1px solid #d6e0f5;
        }

        /* Divider lines between sections */
        hr {
            border-color: #e0e6f0;
        }
        </style>
    """, unsafe_allow_html=True)


def section_card_start():
    """Optional: wrap a section in a card-like container. Use with section_card_end()."""
    st.markdown(
        '<div style="background-color:#f5f8ff; border:1px solid #d6e0f5; '
        'border-radius:10px; padding:18px; margin-bottom:16px;">',
        unsafe_allow_html=True
    )


def section_card_end():
    st.markdown('</div>', unsafe_allow_html=True)
    



