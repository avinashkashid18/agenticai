from langchain.agents import create_agent
from model.llm import llm

from tools.weather import check_weather
agent = create_agent(model=llm, tools=[check_weather], system_prompt="You are a helpful assistant.")
inputs = {"messages": [{"role": "user", "content": "What's the weather like in New York?"}]}
result = agent.invoke(inputs)
print(result)