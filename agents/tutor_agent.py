from agents.math_agent import math_agent
from agents.physics_agent import physics_agent

def tutor_agent(query: str) -> str:
    query_lower = query.lower()

    math_keywords = ["math", "solve", "equation", "+", "-", "*", "/", "^"]
    physics_keywords = ["physics", "force", "law", "velocity", "constant", "mass", "acceleration","gravity"]

    if any(keyword in query_lower for keyword in math_keywords):
        return math_agent(query)
    elif any(keyword in query_lower for keyword in physics_keywords):
        return physics_agent(query)
    else:
        return (
            "Sorry, I couldn't determine the subject of your question. "
            "Please ask something related to math or physics."
        )
