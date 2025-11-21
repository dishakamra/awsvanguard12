from langchain_aws import ChatBedrock as Bedrock
from langchain_core.messages import HumanMessage

chat = Bedrock(model_id="anthropic.claude-3-sonnet-20240229-v1:0", model_kwargs={"temperature":0.1})

messages = [
     HumanMessage(
          content="I would like to try Indian food, what do you suggest should I try?"
     )
]
print(chat.invoke(messages))