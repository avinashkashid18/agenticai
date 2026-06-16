from langchain.tools import tool
@tool("check_weather", return_direct=True)
def check_weather(location: str) -> str:
    """Check the current weather for a given location."""
    return f"The current weather in {location} is sunny with a temperature of 100°C."
