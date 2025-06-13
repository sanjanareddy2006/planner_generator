import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Load your API key from .env file
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def create_prompt(goal, duration, level):
    return f"""
    You are an expert AI tutor. Create a detailed {duration} study plan for a {level} learner who wants to {goal}.
    Break the plan into daily or weekly tasks.
    Make sure it's structured, goal-oriented, and easy to follow.
    """

def generate_study_plan(goal, duration, level):
    prompt = create_prompt(goal, duration, level)

    model = genai.GenerativeModel("models/gemini-1.5-flash")  # Use valid model
    response = model.generate_content(prompt)

    return response.text
