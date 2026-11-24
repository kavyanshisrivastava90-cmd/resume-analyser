import streamlit as st
import PyPDF2

st.set_page_config(page_title="AI Resume Analyser", page_icon="📄", layout="centered")

st.title("📄 AI Resume Analyser")
st.write("Upload your Resume and get your AI Score!")

job_role = st.selectbox("Select Job Role", ["Python Developer", "Web Developer", "Data Analyst"])

jobs_skills = {
    "Python Developer": ["python", "sql", "django", "flask", "api", "git", "machine learning"],
    "Web Developer": ["html", "css", "javascript", "react", "python", "git", "sql"],
    "Data Analyst": ["python", "sql", "excel", "power bi", "pandas", "statistics", "tableau"]
}

uploaded_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])

if uploaded_file is not None:
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    text_lower = text.lower()
    required = jobs_skills[job_role]
    found = [s for s in required if s in text_lower]
    missing = [s for s in required if s not in text_lower]
    score = int(len(found) / len(required) * 100)
    st.divider()
    st.subheader(f"🎯 Resume Score: {score} / 100")
    st.progress(score / 100)
    if score >= 70:
        st.success("Excellent! You are ready for this job! 🎉")
    elif score >= 40:
        st.warning("Good Start! You need to learn a few more skills. 💪")
    else:
        st.error("Keep working hard! You can improve. 📚")
    col1, col2 = st.columns(2)
    with col1:
        st.write("✅ **Skills Found:**")
        for s in found:
            st.write(f"- {s}")
    with col2:
        st.write("❌ **Missing Skills:**")
        for s in missing:
            st.write(f"- {s}")
    report = f"Job Role: {job_role}\nScore: {score}/100\nFound: {found}\nMissing: {missing}"
    st.download_button("📥 Download Report", report, file_name="resume_report.txt")