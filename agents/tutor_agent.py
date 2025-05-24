from agents.math_agent import math_agent
from agents.physics_agent import physics_agent
from agents.gemini import generate_response

def classify_subject(query: str) -> str:
    prompt = f"""
You are an intelligent AI that classifies questions into subjects. 

Classify the following query into one of the following categories:
- "math"
- "physics"
- "unknown"

Query: "{query}"
Respond with only one word: math, physics, or unknown.
"""
    classification = generate_response(prompt).lower().strip()
    return classification

def tutor_agent(query: str) -> str:
    subject = classify_subject(query)

    if subject == "math":
        return math_agent(query)
    elif subject == "physics":
        return physics_agent(query)
    else:
        return (
            "Sorry, I couldn't determine the subject of your question. "
            "Please ask something related to math or physics."
        )
