from flask import Flask, render_template, request
from analyzer import extract_text_from_pdf, extract_text_from_txt, analyze_resume
from jobs import recommend_jobs

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['resume']
    job_desc = request.form['job_desc'].lower()
    
    text = ""
    if file.filename.endswith('.pdf'):
        text = extract_text_from_pdf(file)
    elif file.filename.endswith('.txt'):
        text = extract_text_from_txt(file)
    else:
        return "Please upload PDF or TXT only!"

    result = analyze_resume(text, job_desc)
    jobs = recommend_jobs(text)

    return render_template('index.html', 
                           result=result, 
                           jobs=jobs, 
                           resume_text=text, 
                           job_desc=job_desc)

if __name__ == '__main__':
    app.run(debug=True)