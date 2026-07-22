from pinecone import Pinecone, ServerlessSpec
import os
from dotenv import load_dotenv

load_dotenv(override=True)

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

index_name = "langchain"

def create_index():
    if not pc.has_index(index_name):
        print(f"Creating index {index_name}..")
        pc.create_index_for_model(
            name=index_name,
            cloud="aws",
            region="us-east-1",
            embed={
                "model":"llama-text-embed-v2",
                "field_map":{"text": "chunk_text"}
            }
        )
        print(f"Index {index_name} is created :)")
    else:
        print(f"Index {index_name} already exists")