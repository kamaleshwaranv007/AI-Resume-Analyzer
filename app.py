import streamlit as st
import re

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")
st.write("Analyze your resume and discover your skills.")

uploaded_file = st.file_uploader(
    "Upload your Resume",
    type=["txt"]
)

if uploaded_file is not None:

    text = uploaded_file.read().decode("utf-8")

    st.success("Resume uploaded successfully!")

    skills = [
        "Python", "Java", "C", "C++",
        "HTML", "CSS", "JavaScript",
        "SQL", "MySQL", "Flask",
        "Django", "Git", "GitHub",
        "Machine Learning", "Data Science"
    ]

    found_skills = []

    for skill in skills:
        if re.search(r"\b" + re.escape(skill) + r"\b",
                     text, re.IGNORECASE):
            found_skills.append(skill)

    st.subheader("🛠️ Detected Skills")

    if found_skills:
        for skill in found_skills:
            st.write("✅", skill)
    else:
        st.warning("No matching skills found.")

    score = min(len(found_skills) * 5, 100)

    st.subheader("📊 Resume Score")
    st.progress(score / 100)
    st.write(f"### {score}/100")

    st.subheader("💡 Suggestions")

    if len(found_skills) < 5:
        st.write("• Add more technical skills")
        st.write("• Include academic projects")
        st.write("• Mention relevant tools and technologies")
    else:
        st.write("✅ Your resume contains a good number of technical skills.")
