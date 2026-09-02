import streamlit as st
import re
from io import BytesIO

# PDF and DOCX readers
from pypdf import PdfReader
from docx import Document


# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")
st.write("Analyze your resume, identify skills and check job compatibility.")


# ---------------- SKILLS DATABASE ----------------
skills = [
    "Python", "Java", "C", "C++",
    "HTML", "CSS", "JavaScript",
    "SQL", "MySQL", "MongoDB",
    "Flask", "Django",
    "Git", "GitHub",
    "Machine Learning",
    "Data Science",
    "Artificial Intelligence",
    "React", "Node.js",
    "REST API",
    "AWS", "Azure",
    "Power BI",
    "Excel"
]


# ---------------- RESUME TEXT EXTRACTION ----------------
def extract_text(uploaded_file):

    file_name = uploaded_file.name.lower()

    # PDF
    if file_name.endswith(".pdf"):
        reader = PdfReader(uploaded_file)
        text = ""

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

        return text

    # DOCX
    elif file_name.endswith(".docx"):
        document = Document(BytesIO(uploaded_file.getvalue()))

        text = ""

        for paragraph in document.paragraphs:
            text += paragraph.text + "\n"

        return text

    # TXT
    elif file_name.endswith(".txt"):
        return uploaded_file.getvalue().decode("utf-8", errors="ignore")

    return ""


# ---------------- FILE UPLOAD ----------------
uploaded_file = st.file_uploader(
    "Upload your Resume",
    type=["pdf", "docx", "txt"]
)


# ---------------- JOB DESCRIPTION ----------------
job_description = st.text_area(
    "💼 Paste Job Description (Optional)",
    placeholder="Example: We are looking for a Python Developer with Flask, SQL and Git skills..."
)


# ---------------- ANALYSIS ----------------
if uploaded_file is not None:

    text = extract_text(uploaded_file)

    if not text.strip():
        st.error("Unable to extract text from this resume.")
        st.stop()

    st.success("✅ Resume uploaded and analyzed successfully!")

    # ---------------- SKILL DETECTION ----------------
    found_skills = []

    for skill in skills:

        pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"

        if re.search(pattern, text, re.IGNORECASE):
            found_skills.append(skill)

    # ---------------- RESUME SCORE ----------------
    skill_score = min(len(found_skills) * 4, 40)

    project_score = 20 if re.search(
        r"\b(project|projects)\b",
        text,
        re.IGNORECASE
    ) else 0

    education_score = 20 if re.search(
        r"\b(education|degree|b\.e|b\.tech|bachelor|master)\b",
        text,
        re.IGNORECASE
    ) else 0

    contact_score = 20 if re.search(
        r"@|phone|mobile|contact",
        text,
        re.IGNORECASE
    ) else 0

    score = min(
    skill_score + project_score + education_score + contact_score,
    100
        )
        # ---------------- DASHBOARD ----------------

st.divider()
st.subheader("📊 Resume Performance")

# Top metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📄 Resume Score", f"{score}/100")

with col2:
    st.metric("🛠️ Skills Found", len(found_skills))

with col3:
    st.metric("📝 Resume Words", len(text.split()))

st.markdown("### 📈 Score Breakdown")

# Score cards
b1, b2 = st.columns(2)

with b1:
    st.write("🛠️ **Technical Skills**")
    st.progress(skill_score / 40)
    st.caption(f"{skill_score}/40 points")

with b2:
    st.write("📁 **Projects**")
    st.progress(project_score / 20)
    st.caption(f"{project_score}/20 points")

b3, b4 = st.columns(2)

with b3:
    st.write("🎓 **Education**")
    st.progress(education_score / 20)
    st.caption(f"{education_score}/20 points")

with b4:
    st.write("📧 **Contact Information**")
    st.progress(contact_score / 20)
    st.caption(f"{contact_score}/20 points")

st.markdown("---")

# Overall score
st.write("🏆 **Overall Resume Score**")
st.progress(score / 100)

if score >= 80:
    st.success(f"Excellent Resume — {score}/100")
elif score >= 60:
    st.info(f"Good Resume — {score}/100")
else:
    st.warning(f"Needs Improvement — {score}/100")


    # ---------------- DETECTED SKILLS ----------------
    st.subheader("🛠️ Detected Skills")

    if found_skills:

        skill_text = " • ".join(
            ["✅ " + skill for skill in found_skills]
        )

        st.write(skill_text)

    else:
        st.warning("No matching technical skills found.")


    # ---------------- JOB MATCHING ----------------
    if job_description.strip():

        st.divider()
        st.subheader("🎯 Job Compatibility Analysis")

        job_skills = []

        for skill in skills:

            pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"

            if re.search(
                pattern,
                job_description,
                re.IGNORECASE
            ):
                job_skills.append(skill)

        matched_skills = [
            skill for skill in job_skills
            if skill in found_skills
        ]

        missing_skills = [
            skill for skill in job_skills
            if skill not in found_skills
        ]

        if job_skills:

            match_percentage = int(
                len(matched_skills) /
                len(job_skills) * 100
            )

        else:
            match_percentage = 0


        st.metric(
            "🎯 Job Match",
            f"{match_percentage}%"
        )


        st.write("### ✅ Matching Skills")

        if matched_skills:

            for skill in matched_skills:
                st.write("✅", skill)

        else:
            st.write("No matching skills found.")


        st.write("### ❌ Missing Skills")

        if missing_skills:

            for skill in missing_skills:
                st.write("❌", skill)

        else:
            st.success("🎉 No major skills are missing!")


    # ---------------- JOB ROLE RECOMMENDATION ----------------
    st.divider()

    st.subheader("💼 Recommended Job Roles")

    recommendations = []

    if "Python" in found_skills:
        recommendations.append("Python Developer")

    if "Java" in found_skills:
        recommendations.append("Java Developer")

    if "HTML" in found_skills and "CSS" in found_skills:
        recommendations.append("Web Developer")

    if "JavaScript" in found_skills:
        recommendations.append("Frontend Developer")

    if "SQL" in found_skills or "MySQL" in found_skills:
        recommendations.append("Database Developer")

    if "Machine Learning" in found_skills:
        recommendations.append("Machine Learning Engineer")

    if "Data Science" in found_skills:
        recommendations.append("Data Scientist")

    if "React" in found_skills:
        recommendations.append("React Developer")

    if "Flask" in found_skills:
        recommendations.append("Python Backend Developer")


    if recommendations:

        for role in recommendations:
            st.write("🔹", role)

    else:

        st.info(
            "Add more technical skills to get better job recommendations."
        )


    # ---------------- SUGGESTIONS ----------------
    st.divider()

    st.subheader("💡 Resume Improvement Suggestions")

    suggestions = []

    if len(found_skills) < 5:
        suggestions.append(
            "Add more relevant technical skills."
        )

    if not re.search(
        r"\b(project|projects)\b",
        text,
        re.IGNORECASE
    ):
        suggestions.append(
            "Add your academic or personal projects."
        )

    if not re.search(
        r"\b(education|degree|b\.e|b\.tech|bachelor|master)\b",
        text,
        re.IGNORECASE
    ):
        suggestions.append(
            "Add your education details."
        )

    if not re.search("@", text):
        suggestions.append(
            "Add a professional email address."
        )

    if not suggestions:

        st.success(
            "🎉 Your resume contains the important basic sections!"
        )

    else:

        for suggestion in suggestions:
            st.write("🔹", suggestion)


    # ---------------- RESUME PREVIEW ----------------
    with st.expander("📄 View Extracted Resume Text"):
        st.text(text)
