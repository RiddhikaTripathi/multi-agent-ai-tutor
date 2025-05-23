from agents.math_agent import math_agent
from agents.physics_agent import physics_agent

def tutor_agent(query: str) -> str:
    if any(keyword in query.lower() for keyword in ["math", "solve", "equation", "+", "-", "*", "/"]):
        return math_agent(query)
    elif any(keyword in query.lower() for keyword in ["physics", "force", "law", "velocity", "constant"]):
        return physics_agent(query)
    else:
        return "Sorry, I couldn't determine the subject of your question. Please ask something related to math or physics."
