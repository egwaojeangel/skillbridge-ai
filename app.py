"""
SkillBridge AI - Flask Backend
Powered by Groq (Llama 3.3 70B)
"""

import os
import json
import re
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from groq import Groq

try:
    import fitz
    PDF_OK = True
except ImportError:
    PDF_OK = False

try:
    from docx import Document
    DOCX_OK = True
except ImportError:
    DOCX_OK = False

app = Flask(__name__, static_folder='.')
CORS(app)

GROQ_API_KEY = os.environ.get('GROQ_API_KEY', '')
client = Groq(api_key=GROQ_API_KEY) if GROQ_API_KEY else None

print("=" * 50)
print("SkillBridge AI")
print(f"API: {'Groq Connected' if client else 'MISSING KEY - check run.py'}")
print(f"PDF: {'Yes' if PDF_OK else 'No'} | DOCX: {'Yes' if DOCX_OK else 'No'}")
print("=" * 50)


def extract_pdf(b):
    if not PDF_OK: return ""
    try:
        doc = fitz.open(stream=b, filetype="pdf")
        return "\n".join(p.get_text() for p in doc).strip()
    except: return ""


def extract_docx(b):
    if not DOCX_OK: return ""
    try:
        import io
        doc = Document(io.BytesIO(b))
        return "\n".join(p.text for p in doc.paragraphs).strip()
    except: return ""


def analyse(cv_text, job_desc, job_title=""):
    prompt = f"""You are SkillBridge, a world-class career coach and talent analyst with deep expertise across ALL industries — technology, medicine, law, finance, marketing, design, education, engineering, arts, hospitality, and more.

Analyse this person's CV against the job they want. Be thorough, honest, specific, and genuinely helpful.

CV / RESUME:
{cv_text if cv_text else "No CV provided — give general advice based on the job description only."}

TARGET JOB:
{f"Job Title: {job_title}" if job_title else ""}
{f"Job Description: {job_desc}" if job_desc else ""}

You MUST respond with ONLY a valid JSON object. No markdown, no backticks, no explanation, no text before or after the JSON. Just the raw JSON object starting with {{ and ending with }}.

{{
  "overall_match": <integer 0-100>,
  "job_title": "<detected or provided job title>",
  "industry": "<detected industry>",
  "summary": "<2-3 sentence honest summary of their candidacy>",

  "strengths": [
    {{"skill": "<skill name>", "level": <integer 0-100>, "note": "<why this is a strength>"}}
  ],

  "gaps": [
    {{"skill": "<missing skill>", "importance": "critical|important|nice-to-have", "note": "<why it matters for this role>"}}
  ],

  "experience_advice": {{
    "years_needed": "<e.g. 2-3 years or Entry level OK>",
    "current_estimate": "<estimate from CV or Unknown>",
    "advice": "<honest advice about experience gap>"
  }},

  "roadmap": [
    {{
      "step": <number>,
      "title": "<skill or area to develop>",
      "why": "<why this step matters>",
      "duration": "<realistic time estimate>",
      "resources": [
        {{"name": "<resource name>", "type": "course|book|project|certification|youtube|practice", "url": "<real URL if known, else empty string>", "free": <true|false>, "note": "<brief note>"}}
      ]
    }}
  ],

  "career_advice": [
    "<actionable career advice point 1>",
    "<actionable career advice point 2>",
    "<actionable career advice point 3>",
    "<actionable career advice point 4>",
    "<actionable career advice point 5>"
  ],

  "cv_advice": [
    "<specific CV improvement tip 1 — quantify achievements, fix formatting, add keywords etc>",
    "<specific CV improvement tip 2>",
    "<specific CV improvement tip 3>",
    "<specific CV improvement tip 4>",
    "<specific CV improvement tip 5>",
    "<specific CV improvement tip 6>"
  ],

  "alternative_roles": [
    {{"title": "<alternative job title>", "match": <integer 0-100>, "reason": "<why this suits them>"}}
  ],

  "salary_insight": {{
    "range": "<realistic salary range>",
    "entry": "<entry level salary>",
    "senior": "<senior level salary>",
    "note": "<relevant context about salary>"
  }},

  "next_steps": [
    "<concrete immediate action they can take this week>",
    "<second immediate action>",
    "<third immediate action>"
  ]
}}

Be honest but encouraging. Tailor everything specifically to the industry and role — never give generic tech advice for a nursing, law, or arts role. Make resources real and relevant to the specific field."""

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are a world-class career coach. You always respond with valid JSON only — no markdown, no backticks, no extra text. Just raw JSON."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7,
            max_tokens=4000,
        )

        raw = response.choices[0].message.content.strip()

        # Strip any markdown fences if model adds them
        raw = re.sub(r'^```json\s*', '', raw)
        raw = re.sub(r'^```\s*', '', raw)
        raw = re.sub(r'\s*```$', '', raw)

        # Find the JSON object if there's any extra text
        match = re.search(r'\{.*\}', raw, re.DOTALL)
        if match:
            raw = match.group()

        return json.loads(raw)

    except json.JSONDecodeError as e:
        print(f"JSON error: {e}")
        print(f"Raw response: {raw[:500]}")
        return {"error": "Failed to parse response. Please try again."}
    except Exception as e:
        print(f"API error: {e}")
        return {"error": str(e)}


@app.route('/')
def index():
    return send_from_directory('.', 'index.html')


@app.route('/api/analyse', methods=['POST'])
def api_analyse():
    try:
        if not client:
            return jsonify({"error": "API key missing. Check run.py"}), 500

        cv_text   = ""
        job_desc  = request.form.get('job_description', '').strip()
        job_title = request.form.get('job_title', '').strip()

        if 'cv_file' in request.files:
            f = request.files['cv_file']
            b = f.read()
            name = f.filename.lower()
            if name.endswith('.pdf'):
                cv_text = extract_pdf(b)
            elif name.endswith(('.docx', '.doc')):
                cv_text = extract_docx(b)
            elif name.endswith('.txt'):
                cv_text = b.decode('utf-8', errors='ignore')

        if not cv_text:
            cv_text = request.form.get('cv_text', '').strip()

        if not job_desc and not job_title:
            return jsonify({"error": "Please provide a job description or job title."}), 400

        result = analyse(cv_text, job_desc, job_title)
        if "error" in result:
            return jsonify(result), 500
        return jsonify(result)

    except Exception as e:
        import traceback; traceback.print_exc()
        return jsonify({"error": str(e)}), 500


@app.route('/api/health')
def health():
    return jsonify({"status": "ok", "model": "llama-3.3-70b-versatile", "api": "groq"})


if __name__ == '__main__':
    print("\nRunning at http://localhost:5000\n")
    app.run(debug=True, host='0.0.0.0', port=5000)