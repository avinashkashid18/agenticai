from langchain_ollama import ChatOllama
from model.llm import get_llm

query = input("Press Enter to send a query to the model...")
llm = get_llm()
response = llm.invoke(query)
print(response.content)