import boto3
import json
bedrock_rt = boto3.client(service_name='bedrock-runtime')
prompt = "Difference between zero-shot and few-shot prompt"
configs= {
"inputText": prompt,
"textGenerationConfig": {
"maxTokenCount": 4096,
"stopSequences": [],
"temperature":0.9,
"topP":0.7
}
}
body=json.dumps(configs)
modelId = 'amazon.titan-tg1-large'
accept = 'application/json'
contentType = 'application/json'
response = bedrock_rt.invoke_model(
     body=body,
     modelId=modelId,
     accept=accept,
     contentType=contentType
)
response_body = json.loads(response.get('body').read())
print(response_body.get('results')[0].get('outputText'))