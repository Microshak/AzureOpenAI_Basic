import os
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()


client = AzureOpenAI(
  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
  api_key= os.getenv("AZURE_OPENAI_API_KEY"),  
  api_version="2024-02-01"
)

response = client.chat.completions.create(
    model="bhgfinancial_ai", # model = "deployment_name".
    messages=[
        {"role": "system", "content": "You are a hippy assistant."},
        {"role": "user", "content": "What is an embedding model."}
    ]
)

print(response.choices[0].message.content)

