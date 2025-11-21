# lcmemory.py
# pip install -U langchain-core langchain-community langchain-aws boto3

import boto3
from langchain_aws import ChatBedrock
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory


# Create the Bedrock runtime client
bedrock_client = boto3.client("bedrock-runtime", region_name="us-east-1")

# Initialize the model
chat = ChatBedrock(
    client=bedrock_client,
    model="amazon.titan-tg1-large",
    temperature=0.7,
)

# Create message history store
store = {}

def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

# Define the prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful travel assistant."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

# Combine prompt, model, and parser into a runnable pipeline
chain = prompt | chat | StrOutputParser()

# Wrap the chain with message history
chain_with_history = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
)

def ask(question: str):
    """Ask a question and update the memory."""
    result = chain_with_history.invoke(
        {"input": question},
        config={"configurable": {"session_id": "default"}}
    )
    return result

if __name__ == "__main__":
    print(ask("Hi! I’m in Los Angeles. What are some popular sightseeing places?"))
    print(ask("What’s the closest beach I can go to?"))
    print(ask("What’s the weather like in Los Angeles in December?"))
