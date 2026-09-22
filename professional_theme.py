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
            background-color: #0e1117;
        }

        /* Main title styling */
        h1 {
            font-family: 'Segoe UI', sans-serif;
            font-weight: 700;
            color: #ffffff;
            padding-bottom: 0px;
        }

        h2, h3 {
            font-family: 'Segoe UI', sans-serif;
            font-weight: 600;
            color: #e6e6e6;
            border-bottom: 1px solid #2d2d3a;
            padding-bottom: 6px;
            margin-top: 24px;
        }

        /* Metric cards (Resume Score, ATS Score etc.) */
        div[data-testid="stMetric"] {
            background-color: #1a1d24;
            border: 1px solid #2d2d3a;
            border-radius: 10px;
            padding: 16px 12px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.25);
        }

        div[data-testid="stMetricValue"] {
            font-size: 26px;
            font-weight: 700;
            color: #4CAF50;
        }

        div[data-testid="stMetricLabel"] {
            color: #a0a0b0;
        }

        /* Buttons */
        .stButton > button {
            background-color: #4CAF50;
            color: white;
            border-radius: 8px;
            border: none;
            padding: 8px 20px;
            font-weight: 600;
            transition: all 0.2s ease-in-out;
        }
        .stButton > button:hover {
            background-color: #43a047;
            transform: translateY(-1px);
            box-shadow: 0 4px 10px rgba(76,175,80,0.35);
        }

        /* Success / warning / error boxes */
        div[data-testid="stAlert"] {
            border-radius: 8px;
            padding: 14px;
        }

        /* Progress bars */
        div[data-testid="stProgress"] > div > div {
            background-color: #4CAF50;
            border-radius: 6px;
        }

        /* File uploader box */
        section[data-testid="stFileUploaderDropzone"] {
            background-color: #1a1d24;
            border: 1.5px dashed #3a3a4a;
            border-radius: 10px;
        }

        /* Text area / input boxes */
        textarea, .stTextArea textarea {
            background-color: #1a1d24 !important;
            border: 1px solid #2d2d3a !important;
            border-radius: 8px !important;
            color: #e6e6e6 !important;
        }

        /* DataFrames / tables */
        div[data-testid="stDataFrame"] {
            border: 1px solid #2d2d3a;
            border-radius: 8px;
            overflow: hidden;
        }

        /* Sidebar */
        section[data-testid="stSidebar"] {
            background-color: #12141a;
            border-right: 1px solid #2d2d3a;
        }

        /* Divider lines between sections */
        hr {
            border-color: #2d2d3a;
        }
        </style>
    """, unsafe_allow_html=True)


def section_card_start():
    """Optional: wrap a section in a card-like container. Use with section_card_end()."""
    st.markdown(
        '<div style="background-color:#1a1d24; border:1px solid #2d2d3a; '
        'border-radius:10px; padding:18px; margin-bottom:16px;">',
        unsafe_allow_html=True
    )


def section_card_end():
    st.markdown('</div>', unsafe_allow_html=True)
  
