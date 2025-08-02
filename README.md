
🧠 **AI Resume Analyzer**

A **Streamlit-based web application** that allows users to upload resumes and analyze how well they match a given job description. It uses **NLP techniques** to extract relevant skills, calculate a match score, and label resumes as Excellent, Good, Average, or Low match.

### 📌 Features

* 📄 Upload PDF resumes
* ✍️ Paste or type in a Job Description
* 🔍 Extracts key skills using NLP
* ✅ Calculates match score (TF-IDF similarity)
* 🎯 Labels resumes as: Excellent, Good, Average, or Low match
* 📊 Displays extracted text and JD side-by-side
* 🌐 Deployed on Streamlit Cloud (public link)

### 🛠️ Tech Stack

* **Python**
* **Streamlit** – frontend interface
* **pdfminer.six** – PDF parsing
* **scikit-learn** – TF-IDF and cosine similarity
* **spaCy** – natural language preprocessing


### 📁 Folder Structure
```
resume_analyzer/
├── app.py                # Streamlit web app
├── analyzer.py           # NLP logic (cleaning, skill extraction, similarity)
├── resume_parser.py      # PDF text extraction
├── requirements.txt      # All dependencies for deployment
├── skills.json           # List of target skills (or fallback to default)
├── resumes/              # Folder to store sample resumes
├── reports/              # Output CSVs from CLI version
└── jd_input.txt          # Sample job description (optional for CLI)
```

---

### 🚀 How to Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/ai-resume-analyzer.git
   cd ai-resume-analyzer
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:

   ```bash
   streamlit run app.py
   ```

4. Visit `http://localhost:8501` in your browser.

---

### 🌍 Live Demo

🔗 **[Click here to view the deployed app on Streamlit Cloud](https://your-deployed-link.streamlit.app)**
*(Replace with your actual link after deployment)*

---

### 📌 Use Cases

* HR screening tools
* Resume optimization
* Career counselling portals
* Final-year mini project

---

### 👤 Author

**Arvind Pawar**
[GitHub](https://github.com/your-username) · [LinkedIn](#)

---

### 📄 License

MIT License – Free to use, modify, and distribute with credit.
