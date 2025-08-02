import re
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Auto-download spaCy model if missing
import subprocess
import sys
try:
    nlp = spacy.load('en_core_web_sm')
except OSError:
    subprocess.run([sys.executable, "-m", "spacy", "download", "en_core_web_sm"])
    nlp = spacy.load('en_core_web_sm')

def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)  # Remove extra whitespaces
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)  # Remove special chars
    return text

def extract_skills(text: str, skill_keywords: list) -> list:
    found_skills = []
    for skill in skill_keywords:
        if skill.lower() in text.lower():
            found_skills.append(skill.lower())
    return found_skills

def calculate_similarity(resume_text: str, jd_text: str) -> float:
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_text, jd_text])
    similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    return round(similarity * 100, 2)  # Return as percentage
