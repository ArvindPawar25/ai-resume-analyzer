# analyzer.py

import re
import spacy # type: ignore
from sklearn.feature_extraction.text import TfidfVectorizer # type: ignore
from sklearn.metrics.pairwise import cosine_similarity # type: ignore
import subprocess
import sys

try:
    nlp = spacy.load('en_core_web_sm')
except OSError:
    subprocess.run([sys.executable, "-m", "spacy", "download", "en_core_web_sm"])
    nlp = spacy.load('en_core_web_sm')

nlp = spacy.load('en_core_web_sm')

def clean_text(text):
    """Remove extra spaces and lowercase the text."""
    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)  # remove special characters
    return text.lower()

def extract_skills(text, skill_keywords):
    """Extract known skills from resume text."""
    doc = nlp(text)
    found_skills = [token.text.lower() for token in doc if token.text.lower() in skill_keywords]
    return list(set(found_skills))

def calculate_similarity(resume_text, jd_text):
    vectorizer = TfidfVectorizer(stop_words='english')
    vectors = vectorizer.fit_transform([resume_text, jd_text])
    return cosine_similarity(vectors[0:1], vectors[1:2])[0][0] * 100
