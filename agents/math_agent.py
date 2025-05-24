from agents.gemini import generate_response

def calculator_tool(expression: str) -> str:
    try:
        # Only evaluate if the expression contains only digits and math operators
        allowed_chars = set("0123456789+-*/(). ")
        if all(char in allowed_chars for char in expression):
            result = eval(expression)
            return f"The result is {result}"
    except:
        pass
    return None

def math_agent(query: str) -> str:
    simple_result = calculator_tool(query)
    
    if simple_result:
        return simple_result
    else:
        # Delegate complex expressions to the Gemini agent
        return generate_response(f"Help solve this math problem: {query}")
