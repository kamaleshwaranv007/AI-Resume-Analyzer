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
        /* Import Google Fonts - Poppins for headings, Inter for body */
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600;700;800&family=Inter:wght@400;500;600&display=swap');

        /* Overall app background */
        .stApp {
            background-color: #ffffff;
            font-family: 'Inter', sans-serif;
        }

        /* Main title styling - distinct heading font */
        h1 {
            font-family: 'Poppins', sans-serif;
            font-weight: 800;
            color: #10143d;
            padding-bottom: 0px;
        }

        h2, h3 {
            font-family: 'Poppins', sans-serif;
            font-weight: 700;
            color: #10143d;
            border-bottom: 1px solid #e0e6f0;
            padding-bottom: 6px;
            margin-top: 24px;
        }

        /* Brighter, higher-contrast body text */
        p, span, label, li, div {
            color: #1c1c1c;
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
            font-family: 'Poppins', sans-serif;
            font-size: 26px;
            font-weight: 700;
            color: #1e6fd9;
        }

        div[data-testid="stMetricLabel"] {
            color: #2b3a5c;
            font-weight: 500;
        }

        /* Buttons (including Download button) */
        .stButton > button,
        .stDownloadButton > button {
            background-color: #1e6fd9 !important;
            color: white !important;
            border-radius: 8px;
            border: none;
            padding: 8px 20px;
            font-weight: 600;
            transition: all 0.2s ease-in-out;
        }
        .stButton > button:hover,
        .stDownloadButton > button:hover {
            background-color: #1859ad !important;
            transform: translateY(-1px);
            box-shadow: 0 4px 10px rgba(30,111,217,0.3);
        }

        /* Success / warning / error boxes */
        div[data-testid="stAlert"] {
            border-radius: 8px;
            padding: 14px;
        }
        div[data-testid="stAlert"] p {
            color: #1c1c1c;
            font-weight: 500;
        }

        /* Progress bars */
        div[data-testid="stProgress"] > div > div {
            background-color: #1e6fd9;
            border-radius: 6px;
        }

        /* File uploader dropzone box */
        section[data-testid="stFileUploaderDropzone"] {
            background-color: #f5f8ff;
            border: 1.5px dashed #b8cdf0;
            border-radius: 10px;
        }
        section[data-testid="stFileUploaderDropzone"] * {
            color: #1c1c1c !important;
        }

        /* Uploaded file "chip" that shows after upload */
        div[data-testid="stFileUploaderFile"] {
            background-color: #f5f8ff !important;
            border: 1px solid #d6e0f5 !important;
            border-radius: 8px !important;
            color: #1c1c1c !important;
        }
        div[data-testid="stFileUploaderFile"] * {
            color: #1c1c1c !important;
        }
        div[data-testid="stFileUploaderFile"] small {
            color: #2b3a5c !important;
        }

        /* Text area / input boxes */
        textarea, .stTextArea textarea {
            background-color: #ffffff !important;
            border: 1px solid #d6e0f5 !important;
            border-radius: 8px !important;
            color: #10143d !important;
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
    
