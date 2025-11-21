import boto3
client = boto3.client("bedrock-runtime")
modelId = 'amazon.nova-lite-v1:0'

# Inference parameters to use.
temperature = 0.5
top_p = 0.9

inference_config={"temperature": temperature,"topP": top_p}

# Setup the system prompts and messages to send to the model.

# Define system prompts and add as 'system' message
system_prompts = [{"text": "You are a helpful assistant. Please answer the query politely."}]
conversation = [
    {"role": "system", "content": system_prompts[0]["text"]},
    {
        "role": "user",
        "content": [{"text": "Hello, what is the capital of France?"}]
    }
]
# Use converse API
response = client.converse(
    modelId=modelId,
    messages=conversation,
    inferenceConfig=inference_config
)
print(response['output']['message']["content"][0]["text"])