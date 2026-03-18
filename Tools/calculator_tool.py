import numexpr
from langchain_core.tools import tool

@tool("calculator", description="Evaluate a mathematical expression")
def calculator(expression:str) -> str:
    try:
        result = numexpr.evaluate(expression)
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"