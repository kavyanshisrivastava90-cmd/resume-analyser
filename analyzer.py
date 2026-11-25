import PyPDF2

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text.lower()

def extract_text_from_txt(file):
    return file.read().decode('utf-8').lower()

def analyze_resume(resume_text, job_desc):
    skills = ["html","css","javascript","python","java","excel","communication","drawing","english","photoshop","sql","react"]
    matched = []
    missing = []
    for skill in skills:
        if skill in job_desc:
            if skill in resume_text:
                matched.append(skill)
            else:
                missing.append(skill)
    
    total = len(matched) + len(missing)
    score = round((len(matched)/total)*100) if total > 0 else 0
    
    return {
        "score": score,
        "matched": matched,
        "missing": missing
    }