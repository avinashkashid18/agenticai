from langchain.tools import tool
@tool
def check_weather(location: str) -> str:
    """Check the current weather for a given location."""
    return f"The current weather in {location} is sunny with a temperature of 100°C."
