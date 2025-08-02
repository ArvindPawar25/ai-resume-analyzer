# app.py
import streamlit as st
import os
import json
from resume_parser import extract_resume_text
from analyzer import clean_text, extract_skills, calculate_similarity

# Title
st.set_page_config(page_title="AI Resume Analyzer", layout="centered")
st.title("📄 AI Resume Analyzer")

# Upload resume
uploaded_file = st.file_uploader("Upload your resume (PDF only)", type=["pdf"])

# Job description input
jd_text = st.text_area("Paste the Job Description here")

# Load skill keywords
if os.path.exists("skills.json"):
    with open("skills.json", "r") as f:
        skill_keywords = json.load(f)
else:
    skill_keywords = ["python", "sql", "pandas", "communication", "teamwork", "machine learning", "data analysis"]

# Analyze button
if uploaded_file and jd_text:
    with st.spinner("Analyzing resume..."):
        # Save uploaded file temporarily
        with open("temp_resume.pdf", "wb") as f:
            f.write(uploaded_file.read())

        # Extract and process
        resume_text = extract_resume_text("temp_resume.pdf")

        if resume_text.strip():
            resume_clean = clean_text(resume_text)
            jd_clean = clean_text(jd_text)

            score = calculate_similarity(resume_clean, jd_clean)
            skills_found = extract_skills(resume_clean, skill_keywords)

            # Match Level
            if score >= 75:
                level = "🟢 Excellent"
            elif score >= 50:
                level = "🟡 Good"
            elif score >= 25:
                level = "🟠 Average"
            else:
                level = "🔴 Low"

            # Display Results
            st.subheader("✅ Analysis Results")
            st.write(f"**Match Score:** `{score:.2f}%`")
            st.write(f"**Match Level:** {level}")
            st.write("**Skills Found:**", ", ".join(skills_found) if skills_found else "None")

            with st.expander("📄 View Extracted Resume Text"):
                st.text(resume_clean[:1500])

            with st.expander("📌 View Job Description"):
                st.text(jd_clean)
        else:
            st.error("❌ Could not extract text from the uploaded resume.")
else:
    st.info("Upload a resume and paste a job description to begin.")
