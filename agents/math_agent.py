from agents.gemini import generate_response

def calculator_tool(expression: str) -> str:
    try:
        # Only evaluate if the expression has digits and math symbols (no letters)
        allowed_chars = set("0123456789+-*/(). ")
        if all(char in allowed_chars for char in expression):
            result = eval(expression)
            return f"The result is {result}"
    except:
        pass
    return None

def math_agent(query: str) -> str:
    # Strip query of spaces for validation (optional)
    simple_math_result = calculator_tool(query)
    if simple_math_result:
        return simple_math_result

    # If not evaluable, let Gemini solve it
    return generate_response(f"Can you help with this math problem: {query}")
