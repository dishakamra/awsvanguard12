from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_aws import ChatBedrock

chat = ChatBedrock(
    region_name="us-east-1",
    model_id="anthropic.claude-3-sonnet-20240229-v1:0",
    model_kwargs={
        "temperature": 1,
        "top_k": 250,
        "top_p": 0.999,
        "anthropic_version": "bedrock-2023-05-31",
        # "max_tokens": 512,  # uncomment to cap output length
    },
)

prompt = PromptTemplate.from_template(
    "Create a list of the main metrics tracked in the reports of {company}. "
    "Only return the metric names as a bullet list."
)

chain = prompt | chat | StrOutputParser()

if __name__ == "__main__":
    print("Vanguard:\n", chain.invoke({"company": "Vanguard"}))
    print("\nAWS:\n", chain.invoke({"company": "AWS"}))