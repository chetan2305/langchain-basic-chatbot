# from langchain.prompts import ChatPromptTemplate
from langchain_core.prompts import ChatPromptTemplate


basic_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "{question}")
])
