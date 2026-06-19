from langchain.agents import create_agent
from model.llm import get_llm
from dotenv import load_dotenv

from tools.weather import check_weather
from tools.calculator import calculate
from format.dataformat import format_response
from langchain_tavily import TavilySearch
load_dotenv()

search_tool = TavilySearch(
    max_results=3,
    topic="general"
)
llm = get_llm()
agent = create_agent(model=llm, tools=[check_weather, calculate, search_tool])
inputs = {"messages": [("user", "Who is Sachin Tendulkar? and add 2 and 3")]}
result = agent.invoke(inputs)
print(result)
print(format_response(result))