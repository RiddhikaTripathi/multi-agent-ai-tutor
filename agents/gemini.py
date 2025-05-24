import os
from google.generativeai import GenerativeModel, configure

# Configure Gemini API
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise EnvironmentError("GEMINI_API_KEY not found in environment variables")

configure(api_key=api_key)

# Load Gemini model
model = GenerativeModel("gemini-1.5-flash")

def generate_response(prompt: str) -> str:
    try:
        response = model.generate_content(prompt)
        if response and hasattr(response, "text"):
            return response.text.strip()
        else:
            return "Gemini returned no response."
    except Exception as e:
        return f"Gemini API Error: {e}"
