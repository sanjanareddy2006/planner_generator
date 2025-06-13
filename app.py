import streamlit as st
from backend import generate_study_plan
import random

# ✅ Config
st.set_page_config(page_title="AI Study Plan Generator", page_icon="📚")

# ✅ Sidebar
with st.sidebar:
    st.image("my_background.jpg", use_column_width=True)
    st.title("📘 About")
    st.markdown("""
    This AI-powered tool creates a custom study plan based on your learning goal, level, and duration.

    **Made by:** Sanju Reddy  
    **Powered by:** Gemini AI
    """)
    st.markdown("---")
    st.markdown("📬 *Stay consistent. Check in daily.*")

# ✅ AI Daily Tip Generator (can be expanded via Gemini API)
daily_tips = [
    "💡 *Consistency beats intensity. Show up every day!*",
    "🧠 *Learning is a marathon, not a sprint. Keep going.*",
    "📊 *Track your progress. Small wins lead to big gains.*",
    "📚 *Teach what you learn – it's the fastest way to grow.*",
    "💬 *Ask questions. AI loves curiosity.*",
    "📝 *Write a summary of what you learned today.*"
]
st.markdown(f"""
    <div style='font-size:18px; color:#00ffff; padding:10px; background-color:rgba(0,0,0,0.6); border-radius:10px;'>
    🌟 <b>AI Tip of the Day:</b> {random.choice(daily_tips)}
    </div>
""", unsafe_allow_html=True)

# ✅ Background and Styling
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("my_background.jpg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        font-family: 'Segoe UI', sans-serif;
        color: #00ffff;
    }}
    h1, h2, h3, h4, label, div, p {{
        color: #00ffff !important;
    }}
    .stButton>button {{
        background-color: #111;
        color: #00ffff;
        font-weight: bold;
        border-radius: 10px;
        box-shadow: 0 0 12px #00ffff;
        transition: all 0.3s ease-in-out;
    }}
    .stButton>button:hover {{
        background-color: #00ffff;
        color: black;
        box-shadow: 0 0 20px #00ffff;
    }}
    .fade-in {{
        animation: fadeIn 2s;
    }}
    @keyframes fadeIn {{
        0% {{opacity: 0; transform: translateY(20px);}}
        100% {{opacity: 1; transform: translateY(0);}}
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ✅ Title
st.title("🎓 AI-Powered Study Plan Generator")

# ✅ User Inputs
goal = st.text_input("🎯 Enter your learning goal (e.g., Learn Python)", key="goal_input")
duration = st.selectbox("⏳ Select your timeframe", ["1 week", "2 weeks", "4 weeks", "8 weeks"], key="duration_input")
level = st.radio("📌 Your current level", ["Beginner", "Intermediate", "Advanced"], key="level_input")

# ✅ State Initialization for Progress
if "study_plan" not in st.session_state:
    st.session_state.study_plan = []
    st.session_state.checked = []

# ✅ Generate Button
if st.button("🚀 Generate Study Plan"):
    if goal.strip() == "":
        st.warning("⚠️ Please enter a learning goal.")
    else:
        with st.spinner("🔄 Generating your personalized plan..."):
            try:
                result = generate_study_plan(goal, duration, level)
                plan_lines = result.strip().split('\n')
                st.session_state.study_plan = [line for line in plan_lines if line.strip()]
                st.session_state.checked = [False] * len(st.session_state.study_plan)
                st.success("✅ Plan generated! Scroll down to start tracking.")
            except Exception as e:
                st.error(f"⚠️ Something went wrong:\n\n{e}")

# ✅ Progress Tracker
if st.session_state.study_plan:
    st.markdown("### ✅ Your Study Plan Progress", unsafe_allow_html=True)
    for i, task in enumerate(st.session_state.study_plan):
        st.session_state.checked[i] = st.checkbox(task, value=st.session_state.checked[i], key=f"chk_{i}")

    completed = sum(st.session_state.checked)
    total = len(st.session_state.study_plan)
    st.progress(completed / total)
    st.info(f"📘 {completed} of {total} tasks completed.")

