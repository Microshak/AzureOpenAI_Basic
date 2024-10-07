import os
import weave
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

weave.init("microshak/azureopenai_basic")

client = AzureOpenAI(
  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
  api_key= os.getenv("AZURE_OPENAI_API_KEY"),  
  api_version="2024-02-01"
)

@weave.op()
def get_response():
    response = client.chat.completions.create(
        model="bhgfinancial_ai", # model = "deployment_name".
        messages=[
            {"role": "system", "content": "You are a happy assistant."},
            {"role": "user", "content": "Hi My name is mike"},
            {"role": "assistant", "content": "Hi Mike"},
            {"role": "user", "content": "What is my name"}

        ]
    )
    return response

print(get_response().choices[0].message.content)

