from agents.gemini import generate_response
from sympy import symbols, Eq, solve
import re

def calculator_tool(expression: str) -> str:
    try:
        result = eval(expression)
        return f"The result is {result}"
    except:
        return "Sorry, I couldn't evaluate that expression."

def solve_equation(expression: str) -> str:
    try:
        # Match patterns like "x^2 - 5x + 6 = 0"
        x = symbols('x')
        expression = expression.replace("^", "**")
        equation_match = re.search(r'([-+*/^x0-9\s]+)=\s*0', expression)
        if equation_match:
            lhs = equation_match.group(1).strip()
            eq = Eq(eval(lhs), 0)
            solution = solve(eq, x)
            return f"The solution(s) to the equation are: {solution}"
        return None
    except Exception as e:
        return f"Sorry, I couldn't solve the equation. ({str(e)})"

def math_agent(query: str) -> str:
    # Try solving as symbolic equation
    if "equation" in query or "=" in query:
        result = solve_equation(query)
        if result:
            return result

    # Try evaluating arithmetic expressions
    if any(op in query for op in ['+', '-', '*', '/']):
        return calculator_tool(query)

    # Fallback to Gemini for other math-related queries
    return generate_response(f"Solve this math question: {query}")
