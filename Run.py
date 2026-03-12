import os

# Paste your Groq API key here
os.environ['GROQ_API_KEY'] = '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'

from app import app

if __name__ == '__main__':
    print("\n" + "="*50)
    print("  SkillBridge AI")
    print("  Open: http://localhost:5000")
    print("="*50 + "\n")
    app.run(debug=True, host='0.0.0.0', port=5000)