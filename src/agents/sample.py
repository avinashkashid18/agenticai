from langchain.agents import create_agent
from model.llm import get_llm

from tools.weather import check_weather
from tools.calculator import calculate
from dotenv import load_dotenv
from langchain_tavily import TavilySearch
from langchain.tools import tool
load_dotenv()
tool = TavilySearch(
    max_results=5,
    topic="general"
)
llm = get_llm()
agent = create_agent(model=llm, tools=[check_weather, calculate])
inputs = {"messages": [("user", "what is addition of 50 and 30?")]}
result = agent.invoke(inputs)
print(result["messages"][-1].content)
#print(result)