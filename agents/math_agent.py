from agents.gemini import generate_response

def calculator_tool(expression: str) -> str:
    try:
        # Only allow digits, spaces, and basic math symbols
        allowed = set("0123456789+-*/(). ")
        if all(char in allowed for char in expression):
            result = eval(expression)
            return f"The result is {result}"
        else:
            return None
    except:
        return None

def math_agent(query: str) -> str:
    # Try to evaluate simple math expressions
    calculated = calculator_tool(query)
    if calculated:
        return calculated
    
    # Otherwise, ask Gemini to handle it
    return generate_response(f"Please solve this math question: {query}")
