# CarrerCoachAssistant
The AI Career Assistant is a centralized hub for career development. It allows users to upload their resumes, receive structured feedback on their professional summaries, and practice high-stakes interview questions using the STAR (Situation, Task, Action, Result) method framework.

Key Features:
1. General Chat: A conversational interface providing tips on networking, LinkedIn presence, and open-source contributions.
2.Resume Analyzer: A scoring engine that evaluates resume summaries based on keywords like "leadership," "collaboration," and specific technical skills (C, Java, Python, SQL).
3.PDF Resume Parser: Integration with pdfplumber to extract raw text from PDF files for instant review.
4.Interview Prep: A guided module for common interview questions that prompts users to structure their answers with "Intro → Skill → Example → Impact".
5.Daily Motivation: A library of curated quotes to keep users inspired during the job search process.

Tech Stack:
Language: Python 
Framework: Streamlit (>= 1.34.0) 
PDF Processing: pdfplumber (>= 0.10.2) 

Installation & Setup
Clone the Repository:
Bash
git clone https://github.com/YOUR_USERNAME/career-coach-assistant.git
cd career-coach-assistant
Create a Virtual Environment (Optional but Recommended):
Bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies:
Bash
pip install -r requirements.txt
Launch the Application:
Bash
streamlit run app.py

 How It Works
The application uses session-based chat memory to track your conversation during the general chat session. The Resume Tips feature calculates a "Strength Score" by checking for specific industry-standard keywords and length requirements to ensure your summary is impactful.
