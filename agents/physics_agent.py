from agents.gemini import generate_response

CONSTANTS = {
    "speed of light": "299,792,458 m/s",
    "gravitational constant": "6.67430 × 10^-11 m^3 kg^-1 s^-2"
}

def lookup_constants(query: str) -> str:
    for key in CONSTANTS:
        if key in query.lower():
            return f"The {key} is {CONSTANTS[key]}"
    return None

def physics_agent(query: str) -> str:
    constant_info = lookup_constants(query)
    if constant_info:
        return constant_info
    return generate_response(f"Answer this physics question: {query}")
