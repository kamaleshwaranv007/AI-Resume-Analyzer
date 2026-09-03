import streamlit as st
import re
from io import BytesIO

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
    "Power BI", "Excel"
]


# ---------------- RESUME TEXT EXTRACTION ----------------
def extract_text(uploaded_file):

    file_name = uploaded_file.name.lower()

    if file_name.endswith(".pdf"):
        reader = PdfReader(uploaded_file)
        text = ""

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

        return text

    elif file_name.endswith(".docx"):
        document = Document(BytesIO(uploaded_file.getvalue()))
        text = ""

        for paragraph in document.paragraphs:
            text += paragraph.text + "\n"

        return text

    elif file_name.endswith(".txt"):
        return uploaded_file.getvalue().decode(
            "utf-8",
            errors="ignore"
        )

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

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("📄 Resume Score", f"{score}/100")

    with col2:
        st.metric("🛠️ Skills Found", len(found_skills))

    with col3:
        st.metric("📝 Resume Words", len(text.split()))


    # ---------------- SCORE BREAKDOWN ----------------
    st.markdown("### 📊 Score Breakdown")

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


    # =========================================================
    #                    ATS ANALYSIS
    # =========================================================

    st.divider()
    st.subheader("📋 ATS Resume Analysis")

    ats_score = 0
    ats_suggestions = []

    # Contact Information
    has_email = bool(
        re.search(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            text
        )
    )

    has_phone = bool(
        re.search(
            r"(\+91[\s-]?)?[6-9]\d{9}",
            text
        )
    )

    if has_email:
        ats_score += 10
    else:
        ats_suggestions.append(
            "Add a professional email address."
        )

    if has_phone:
        ats_score += 10
    else:
        ats_suggestions.append(
            "Add a valid phone number."
        )


    # Resume Sections
    section_patterns = {
        "Education": r"\b(education|academic|qualification)\b",
        "Projects": r"\b(project|projects)\b",
        "Skills": r"\b(skills|technical skills|technologies)\b",
        "Experience": r"\b(experience|work experience|employment)\b",
        "Summary": r"\b(summary|profile|objective|career objective)\b"
    }

    section_results = {}

    for section, pattern in section_patterns.items():

        found = bool(
            re.search(
                pattern,
                text,
                re.IGNORECASE
            )
        )

        section_results[section] = found

        if found:
            ats_score += 10


    # Suggestions for missing sections
    if not section_results["Summary"]:
        ats_suggestions.append(
            "Add a professional summary or career objective."
        )

    if not section_results["Skills"]:
        ats_suggestions.append(
            "Add a dedicated Technical Skills section."
        )

    if not section_results["Projects"]:
        ats_suggestions.append(
            "Add relevant academic or personal projects."
        )

    if not section_results["Education"]:
        ats_suggestions.append(
            "Add your education details."
        )

    if not section_results["Experience"]:
        ats_suggestions.append(
            "Consider adding internship, work or practical experience."
        )


    # Keyword / Action Word Check
    action_words = [
        "developed",
        "created",
        "designed",
        "implemented",
        "managed",
        "built",
        "analyzed",
        "optimized",
        "improved",
        "developed"
    ]

    action_word_found = any(
        re.search(
            r"\b" + word + r"\b",
            text,
            re.IGNORECASE
        )
        for word in action_words
    )

    if action_word_found:
        ats_score += 10
    else:
        ats_suggestions.append(
            "Use strong action words such as Developed, Built, Designed and Implemented."
        )


    # Final ATS score
    ats_score = min(ats_score, 100)


    # ---------------- ATS SCORE DISPLAY ----------------
    ats_col1, ats_col2 = st.columns(2)

    with ats_col1:
        st.metric(
            "📋 ATS Score",
            f"{ats_score}/100"
        )

    with ats_col2:

        if ats_score >= 80:
            st.success("🟢 ATS Friendly Resume")

        elif ats_score >= 60:
            st.warning("🟡 Resume can be improved")

        else:
            st.error("🔴 Resume needs improvement")


    st.progress(ats_score / 100)


    # ---------------- ATS SECTION CHECK ----------------
    st.write("### 📑 Resume Sections")

    section_col1, section_col2 = st.columns(2)

    for index, (section, found) in enumerate(
        section_results.items()
    ):

        column = (
            section_col1
            if index % 2 == 0
            else section_col2
        )

        with column:

            if found:
                st.write(f"✅ {section}")

            else:
                st.write(f"❌ {section}")


    # ---------------- ATS SUGGESTIONS ----------------
    st.write("### 💡 ATS Improvement Suggestions")

    if ats_suggestions:

        for suggestion in ats_suggestions:
            st.write("🔹", suggestion)

    else:

        st.success(
            "🎉 Your resume is well structured for ATS!"
        )


    # =========================================================
    #                    JOB MATCHING
    # =========================================================

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
            skill
            for skill in job_skills
            if skill in found_skills
        ]

        missing_skills = [
            skill
            for skill in job_skills
            if skill not in found_skills
        ]


        if job_skills:

            match_percentage = int(
                len(matched_skills)
                / len(job_skills)
                * 100
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

            st.success(
                "🎉 No major skills are missing!"
            )

     # ---------------- SKILL GAP ANALYSIS ----------------

        st.write("### 📊 Skill Gap Analysis")

        skill_gap = 100 - match_percentage

        gap_col1, gap_col2 = st.columns(2)

        with gap_col1:
            st.metric(
                "📈 Skill Match",
                f"{match_percentage}%"
            )

        with gap_col2:
            st.metric(
                "📉 Skill Gap",
                f"{skill_gap}%"
            )

        st.progress(match_percentage / 100)

        # Skill gap message
        if match_percentage >= 80:
            st.success(
                "🎉 Excellent skill match! Your resume is highly suitable for this job."
            )

        elif match_percentage >= 60:
            st.warning(
                "👍 Good match, but adding some missing skills can improve your chances."
            )

        else:
            st.error(
                "⚠️ There is a significant skill gap. Consider learning the missing skills."
            )

        # Missing skills priority
        if missing_skills:

            st.write("### 🎯 Skills You Should Consider Learning")

            for skill in missing_skills:
                st.write("🔴", skill)

        else:

            st.success(
                "✅ No important skills are missing from the job description!"
            )
    # =========================================================
    #                JOB ROLE RECOMMENDATION
    # =========================================================

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


    # =========================================================
    #                  RESUME SUGGESTIONS
    # =========================================================

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

    # =========================================================
    #             SMART RESUME IMPROVEMENT
    # =========================================================

    st.divider()
    st.subheader("🤖 Smart Resume Improvement")

    smart_suggestions = []

    # Summary check
    has_summary = bool(
        re.search(
            r"\b(summary|profile|objective|career objective)\b",
            text,
            re.IGNORECASE
        )
    )

    if not has_summary:
        smart_suggestions.append(
            ("⚠️ Professional Summary",
             "Add a 2–3 line professional summary highlighting your skills, career goal and strengths.")
        )
    else:
        smart_suggestions.append(
            ("✅ Professional Summary",
             "A professional summary is present in your resume.")
        )


    # Skills check
    if len(found_skills) < 5:
        smart_suggestions.append(
            ("⚠️ Technical Skills",
             "Add more relevant technical skills based on the job you are targeting.")
        )
    else:
        smart_suggestions.append(
            ("✅ Technical Skills",
             f"Your resume contains {len(found_skills)} technical skills.")
        )


    # Project check
    has_projects = bool(
        re.search(
            r"\b(project|projects)\b",
            text,
            re.IGNORECASE
        )
    )

    if not has_projects:
        smart_suggestions.append(
            ("⚠️ Projects",
             "Add academic, personal or internship projects with technologies used and results achieved.")
        )
    else:
        smart_suggestions.append(
            ("✅ Projects",
             "Projects section detected. Try describing your contribution and measurable results.")
        )


    # Experience check
    has_experience = bool(
        re.search(
            r"\b(experience|work experience|employment|internship)\b",
            text,
            re.IGNORECASE
        )
    )

    if not has_experience:
        smart_suggestions.append(
            ("⚠️ Experience",
             "Add internship, freelance, volunteer or practical experience if available.")
        )
    else:
        smart_suggestions.append(
            ("✅ Experience",
             "Experience section detected. Use action verbs and measurable achievements.")
        )


    # Action words
    action_words = [
        "developed",
        "created",
        "designed",
        "implemented",
        "managed",
        "built",
        "analyzed",
        "optimized",
        "improved",
        "tested",
        "deployed"
    ]

    action_word_count = sum(
        len(
            re.findall(
                r"\b" + word + r"\b",
                text,
                re.IGNORECASE
            )
        )
        for word in action_words
    )

    if action_word_count < 2:
        smart_suggestions.append(
            ("⚠️ Action Words",
             "Use strong action words such as Developed, Implemented, Designed, Built and Deployed.")
        )
    else:
        smart_suggestions.append(
            ("✅ Action Words",
             f"Good use of action-oriented words detected ({action_word_count}).")
        )


    # Contact information
    if not has_email:
        smart_suggestions.append(
            ("⚠️ Contact Information",
             "Add a professional email address.")
        )

    if not has_phone:
        smart_suggestions.append(
            ("⚠️ Contact Information",
             "Add a valid phone number.")
        )


    # Display suggestions
    for title, message in smart_suggestions:

        if title.startswith("✅"):
            st.success(f"{title}\n\n{message}")

        else:
            st.warning(f"{title}\n\n{message}")


    # Professional summary template
    st.write("### ✨ Professional Summary Template")

    st.info(
        "Recent graduate with skills in "
        + ", ".join(found_skills[:5])
        + ". Passionate about developing practical solutions and "
          "applying technical knowledge to real-world projects."
    )
    # =========================================================
    #                    RESUME PREVIEW
    # =========================================================

    with st.expander("📄 View Extracted Resume Text"):
        st.text(text)

        
