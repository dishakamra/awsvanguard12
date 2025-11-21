import boto3
from langchain.tools import tool
from langchain_aws import ChatBedrock

@tool
def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

# Create the Bedrock runtime client
bedrock_client = boto3.client("bedrock-runtime", region_name="us-east-1")

# Initialize the model with tool support
llm = ChatBedrock(
    client=bedrock_client,
    model="anthropic.claude-3-sonnet-20240229-v1:0",
    temperature=0.7,
)

# Bind tools to the LLM
llm_with_tools = llm.bind_tools([get_weather])

# Invoke the model directly
response = llm_with_tools.invoke("what is the weather in sf")
print(response)