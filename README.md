# SkillBridge — AI-Powered Career Gap Analyzer

![SkillBridge Banner](https://img.shields.io/badge/SkillBridge-AI%20Career%20Analyser-2dd4bf?style=for-the-badge&logo=bolt&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8+-3b82f6?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Backend-2dd4bf?style=for-the-badge&logo=flask&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-Llama%203.3%2070B-3b82f6?style=for-the-badge&logo=meta&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

> Know exactly what's standing between you and your dream job.

SkillBridge is a full-stack AI web application that analyses your CV against any job description and delivers a comprehensive, personalised career gap report — for **any role in any industry**.

---

## 📸 Preview

![SkillBridge Demo](https://via.placeholder.com/1200x600/0a0c10/2dd4bf?text=SkillBridge+AI+Demo)

> *Upload your CV · Paste the job description · Get your roadmap in 15 seconds*

---

## ✨ Features

- **Instant Skill Gap Analysis** — See exactly which skills you have and which you're missing for the target role
- **Overall Match Score** — A 0–100% compatibility score with an animated visual ring
- **Personalised Learning Roadmap** — Step-by-step plan with free and paid resources, real links, and time estimates
- **CV Improvement Tips** — Specific, actionable advice to strengthen your CV for the exact role
- **Salary Insights** — Realistic salary ranges for entry through senior levels
- **Career Advice** — 5 tailored career strategy tips
- **Experience Gap Analysis** — Honest assessment of your experience vs what's required
- **Alternative Role Suggestions** — Similar roles you might be a stronger match for
- **Works for ANY industry** — Tech, medicine, law, finance, engineering, arts, education, hospitality and more
- **User Authentication** — Register and sign in with email and password
- **Dark / Light Mode** — Sleek dark UI by default with light mode toggle
- **PDF & DOCX Support** — Upload your CV in any format
- **Fully Responsive** — Works on desktop and mobile

---

## 🛠 Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | HTML5, CSS3, Tailwind CSS, Vanilla JavaScript |
| Backend | Python, Flask, Flask-CORS |
| AI Model | Llama 3.3 70B via Groq API |
| PDF Parsing | PyMuPDF (fitz) |
| DOCX Parsing | python-docx |
| Fonts | Plus Jakarta Sans (Google Fonts) |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- A free [Groq API key](https://console.groq.com) (takes 2 minutes to get)

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/YOUR-USERNAME/skillbridge.git
cd skillbridge
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Add your Groq API key**

Open `run.py` and replace the placeholder with your key:
```python
os.environ['GROQ_API_KEY'] = 'your-groq-api-key-here'
```

**4. Run the app**
```bash
python run.py
```

**5. Open in your browser**
```
http://localhost:5000
```

---

## 📁 Project Structure

```
skillbridge/
├── app.py              # Flask backend — routes, PDF parsing, AI analysis
├── run.py              # Entry point — sets API key and starts server
├── index.html          # Frontend — full UI (single file)
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

---

## 🔑 Getting a Free Groq API Key

1. Go to [console.groq.com](https://console.groq.com)
2. Sign up for a free account
3. Navigate to **API Keys** → **Create API Key**
4. Copy the key and paste it into `run.py`

Groq's free tier is generous — more than enough for personal use and demos.

---

## 🤖 How the AI Works

When you submit a CV and job description, the app sends both to **Llama 3.3 70B** (Meta's most powerful open model, served via Groq) with a detailed prompt instructing it to act as a world-class career coach. The model returns a structured JSON object containing all analysis fields, which the frontend renders into the results dashboard.

The AI is instructed to:
- Tailor advice to the **specific industry** (never generic)
- Be **honest** about gaps while remaining encouraging
- Suggest **real, named resources** relevant to the field
- Provide **concrete, actionable** next steps

---

## 💡 Usage

1. **Upload your CV** — drag and drop a PDF/DOCX/TXT or paste the text directly
2. **Enter the job** — paste the full job description for best results, or just a job title
3. **Click Analyse** — wait 15–20 seconds for the AI to process
4. **Review your results** — match score, gaps, roadmap, CV tips, salary data and more

---

## 🔒 Privacy

- No CV data is stored on any server
- All analysis happens in real-time and is discarded after the response
- User accounts (name, email, hashed password) are stored in your browser's localStorage only — nothing is sent to a database

---

## 📋 Requirements

```txt
flask
flask-cors
groq
pymupdf
python-docx
python-dotenv
```

---

## 🗺 Roadmap

- [ ] Export analysis as PDF report
- [ ] Save and compare multiple analyses
- [ ] LinkedIn profile URL input (auto-parse CV)
- [ ] Job board integration (auto-fetch job descriptions)
- [ ] Email analysis results
- [ ] Backend database for user accounts

---

## 👨‍💻 Author

**Angel Egwaoje**

- LinkedIn: [linkedin.com/in/your-profile](https://www.linkedin.com/in/angel-egwaoje-416927280/)

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgements

- [Groq](https://groq.com) for ultra-fast LLM inference
- [Meta AI](https://ai.meta.com) for the Llama 3.3 model
- [Tailwind CSS](https://tailwindcss.com) for styling utilities
- [Font Awesome](https://fontawesome.com) for icons
- [Plus Jakarta Sans](https://fonts.google.com/specimen/Plus+Jakarta+Sans) for typography

---

<div align="center">
  <p>Built with ❤️ by Angel Egwaoje</p>
  <p>⭐ Star this repo if it helped you!</p>
</div>
