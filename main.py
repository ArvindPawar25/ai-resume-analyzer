# main.py
import csv
import os
import json
from resume_parser import extract_resume_text
from analyzer import clean_text, extract_skills, calculate_similarity

# Load job description
with open("jd_input.txt", "r", encoding="utf-8") as f:
    jd_text = f.read()

# Load skill keywords
if os.path.exists("skills.json"):
    with open("skills.json", "r") as f:
        skill_keywords = json.load(f)
else:
    # Default skill set
    skill_keywords = ["python", "sql", "pandas", "communication", "teamwork", "machine learning", "data analysis"]

print("----- AI Resume Analyzer -----")
results = []

# Analyze each resume in 'resumes' folder
for file in os.listdir("resumes"):
    if file.endswith(".pdf"):
        file_path = os.path.join("resumes", file)
        resume_text = extract_resume_text(file_path)

        if resume_text.strip():
            resume_clean = clean_text(resume_text)
            jd_clean = clean_text(jd_text)

            score = calculate_similarity(resume_clean, jd_clean)
            skills = extract_skills(resume_clean, skill_keywords)

            # 🔽 Determine match level here
            if score >= 75:
                level = "Excellent"
            elif score >= 50:
                level = "Good"
            elif score >= 25:
                level = "Average"
            else:
                level = "Low"

            # 🔽 Print results
            print(f"\n📄 Resume: {file}")
            print(f"✅ Match Score: {score:.2f}% ({level})")
            print(f"🛠️ Skills Found: {', '.join(skills) if skills else 'None'}")
            print("-" * 40)
            print(f"\n--- Resume Content ({file}) ---\n")
            print(resume_clean[:500])  # Show first 500 characters
            print("\n--- JD Content ---\n")
            print(jd_clean)

            # 🔽 Save to results list
            results.append({
                "Resume Name": file,
                "Match Score (%)": f"{score:.2f}",
                "Match Level": level,
                "Skills Found": ", ".join(skills) if skills else "None"
            })
        else:
            print(f"⚠️ Could not read content from {file_path}")

# Save the results to a CSV file
os.makedirs("reports", exist_ok=True)  # Ensure the reports folder exists

with open("reports/resume_analysis.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["Resume Name", "Match Score (%)", "Match Level", "Skills Found"])
    writer.writeheader()
    writer.writerows(results)

print("\n📁 Analysis saved to reports/resume_analysis.csv")
