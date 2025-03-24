'''from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
import os

Token=os.getenv("HUGGINGFACEHUB_API_TOKEN")

load_dotenv()
llm=HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text_generation",
    huggingfacehub_api_token=Token
    )

model=ChatHuggingFace(llm=llm)
result=model.invoke('what is the capital of france')
print(result.content)'''

import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

# Load environment variables
load_dotenv()
huggingface_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

if not huggingface_token:
    raise ValueError("Hugging Face API token is missing. Please check your .env file.")

# Initialize Hugging Face LLM
llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text_generation",
)
huggingfacehub_api_token=huggingface_token

model = ChatHuggingFace(llm=llm)

# Define the generate_response function
def generate_response(prompt):
    result = model.invoke(prompt)
    return result.content

