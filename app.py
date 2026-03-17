import streamlit as st
import random
import pdfplumber

st.set_page_config(page_title="AI Career Assistant", layout="centered")
st.title("🎯 AI Career Assistant")
st.write("Boost your internship journey with smart resume feedback, interview prep, and motivation!")

menu = st.sidebar.selectbox(
    "📌 Choose a Feature:",
    ["💬 General Chat", "📄 Resume Tips", "📎 Upload Resume", "🎤 Interview Prep", "💡 Motivation"]
)

# Session-based chat memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# 💬 General Chat
if menu == "💬 General Chat":
    st.subheader("💬 General Chat")
    user_input = st.text_input("Ask me anything:")
    if user_input:
        response = random.choice([
            "Keep going, you're doing great! Explore open source and network on LinkedIn.",
            "Focus on your fundamentals, contribute to GitHub, and learn in public!",
            "Start small projects and showcase them on your resume and LinkedIn."
        ])
        st.session_state.messages.append({"user": user_input, "bot": response})
    for chat in st.session_state.messages:
        st.write(f"👤 {chat['user']}")
        st.write(f"🤖 {chat['bot']}")

# 📄 Resume Tips
elif menu == "📄 Resume Tips":
    st.subheader("📄 Resume Tips")
    resume_text = st.text_area("Paste your resume summary or description:")
    if resume_text:
        st.markdown("### ✅ Suggestions:")
        word_count = len(resume_text.split())
        score = 0

        if any(skill in resume_text.lower() for skill in ["c", "java", "python", "sql"]):
            st.write("• Good job including programming languages!")
            score += 1
        if "team" in resume_text.lower() or "collaborated" in resume_text.lower():
            st.write("• Strong teamwork mentioned.")
            score += 1
        if "intern" in resume_text.lower():
            st.write("• Mention your learnings from the internship.")
            score += 1
        if "lead" in resume_text.lower():
            st.write("• Great! Highlight impact of your leadership.")
            score += 1

        if word_count < 50:
            st.warning("Try expanding with specific achievements.")
        else:
            st.success("Looks like a solid summary!")

        st.write(f"📝 Word Count: {word_count}")
        st.progress(score / 4)
        st.write(f"Resume Strength Score: **{int((score / 4) * 100)}%**")

# 📎 Upload Resume (PDF)
elif menu == "📎 Upload Resume":
    st.subheader("📎 Upload Resume")
    uploaded_file = st.file_uploader("Upload your resume (PDF)", type="pdf")
    if uploaded_file:
        with pdfplumber.open(uploaded_file) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text()
        st.text_area("Extracted Resume Text", text, height=200)
        st.info("Now paste this text into 'Resume Tips' for personalized feedback.")

# 🎤 Interview Prep
elif menu == "🎤 Interview Prep":
    st.subheader("🎤 Interview Prep")
    question = st.selectbox("Choose a question:", [
        "Tell me about yourself.",
        "What are your strengths and weaknesses?",
        "Describe a project you're proud of.",
        "How do you handle challenges in a team?",
        "Why should we hire you?"
    ])
    st.markdown(f"**Selected Question:** {question}")
    user_answer = st.text_area("✍️ Type your answer:")
    if user_answer:
        st.write("🤖 Structure it as: Intro → Skill → Example → Impact")
        if "team" in user_answer.lower():
            st.write("✅ You mentioned teamwork. Nice!")
        if "challenge" in user_answer.lower() or "problem" in user_answer.lower():
            st.write("✅ Good job discussing a challenge.")
        if "project" in user_answer.lower():
            st.write("✅ Project experience is always valuable.")

# 💡 Motivation
elif menu == "💡 Motivation":
    st.subheader("💡 Daily Motivation")
    quotes = [
        "Believe you can and you're halfway there. – Roosevelt",
        "Stay hungry, stay foolish. – Steve Jobs",
        "Push yourself, because no one else will.",
        "Your limitation—it's only your imagination.",
        "Success is not final. Keep going."
    ]
    st.success(random.choice(quotes))
    user_quote = st.text_input("💬 Your motivational thought today:")
    if user_quote:
        st.write("⭐ Stay inspired:", user_quote)