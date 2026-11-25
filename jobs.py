def recommend_jobs(resume_text):
    jobs = []
    if "python" in resume_text or "sql" in resume_text or "excel" in resume_text:
        jobs.append({"title": "Data Analyst", "company": "TCS", "match": "92%"})
    if "html" in resume_text or "css" in resume_text or "javascript" in resume_text:
        jobs.append({"title": "Web Developer", "company": "Infosys", "match": "88%"})
    if "drawing" in resume_text or "photoshop" in resume_text:
        jobs.append({"title": "UI/UX Designer", "company": "Zomato", "match": "85%"})
    if "java" in resume_text or "python" in resume_text:
        jobs.append({"title": "Software Developer", "company": "Wipro", "match": "90%"})
    
    if not jobs:
        jobs.append({"title": "Fresher - Internship", "company": "Internshala", "match": "70%"})
    return jobs