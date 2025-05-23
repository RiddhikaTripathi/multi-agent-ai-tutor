from agents.gemini import generate_response

def calculator_tool(expression: str) -> str:
    try:
        result = eval(expression)
        return f"The result is {result}"
    except:
        return "Sorry, I couldn't evaluate that expression."

def math_agent(query: str) -> str:
    if any(op in query for op in ['+', '-', '*', '/']):
        return calculator_tool(query)
    return generate_response(f"Solve this math question: {query}")
