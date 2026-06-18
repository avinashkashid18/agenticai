from langchain_ollama import ChatOllama

def get_llm():
    llm = ChatOllama(model="gpt-oss:120b-cloud")
    return llm