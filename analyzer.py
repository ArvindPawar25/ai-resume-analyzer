import re
import sys
import subprocess
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load or download spaCy model
try:
    import spacy
    nlp = spacy.load("en_core_web_sm")
except (OSError, ImportError):
    subprocess.run([sys.executable, "-m", "spacy", "download", "en_core_web_sm"])
    import spacy
    nlp = spacy.load("en_core_web_sm")


def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text.strip()


def extract_skills(text: str, skill_keywords: list) -> list:
    return [skill.lower() for skill in skill_keywords if skill.lower() in text.lower()]


def calculate_similarity(resume_text: str, jd_text: str) -> float:
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_text, jd_text])
    similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    return round(similarity * 100, 2)
