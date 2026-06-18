from langchain.tools import tool

@tool
def calculate(operation: str, a: float, b: float) -> float:
    """Perform a calculation based on the specified operation. like addition, subtract, multiply, or divide."""
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b if b != 0 else float("inf")
    else:
        raise ValueError(f"Unsupported operation: {operation}")    