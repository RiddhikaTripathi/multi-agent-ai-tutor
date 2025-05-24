from agents.gemini import generate_response

def chemistry_agent(query: str) -> str:
    return generate_response(f"Answer this chemistry question: {query}")
