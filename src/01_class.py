from langchain_ollama import ChatOllama
from model.llm import llm

query = input("Press Enter to send a query to the model...")
response = llm.invoke(query)
print(response.content)