import fitz  # PyMuPDF

def extract_resume_text(file_path):
    try:
        doc = fitz.open(file_path)
        text = ""
        for page in doc:
            text += page.get_text()
        return text
    except Exception as e:
        print(f"Error: {e}")
        return ""
