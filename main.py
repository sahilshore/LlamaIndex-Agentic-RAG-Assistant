import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.groq import Groq
from dotenv import load_dotenv

load_dotenv()
# Load documents
documents = SimpleDirectoryReader("data").load_data()

# Embeddings
Settings.embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-base-en-v1.5"
)

# Groq LLM (UPDATED MODEL)
Settings.llm = Groq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)

# Build index
index = VectorStoreIndex.from_documents(documents)

# Query
query_engine = index.as_query_engine()
response = query_engine.query(
"What problem does the Transformer architecture solve?"
)

print(response)
