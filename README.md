# LlamaIndex Agentic RAG Assistant

An Agentic Retrieval-Augmented Generation (RAG) system built using LlamaIndex, HuggingFace embeddings, and Groq LLMs that can answer questions directly from PDF documents.

This project demonstrates how an AI system can read documents, understand context, retrieve relevant information, and generate accurate answers using modern agentic RAG architecture.

## Features

📄 Load and read PDF documents

🔍 Semantic search using vector embeddings

🧠 Agentic reasoning powered by LlamaIndex

🤗 HuggingFace embedding model (BGE)

⚡ Fast inference using Groq LLMs

🧩 Simple and clean project structure

🔐 Secure API key handling using .env

## Architecture (How it Works)

PDF documents are loaded from the data/ folder

Text is converted into vector embeddings using BAAI/bge-base-en-v1.5

Vectors are stored in an in-memory vector index

User query is embedded and matched with relevant document chunks

Retrieved context is passed to Groq LLM

Final answer is generated using RAG (Retrieval + Generation)

## Tech Stack
Component	                   Technology
Framework          	            LlamaIndex
Embeddings	                    HuggingFace (BAAI/bge-base-en-v1.5)
LLM	Groq                        (OpenAI-compatible API)
Language	                       Python
Documents	                       PDF
Vector Store	                   In-Memory (LlamaIndex)
## Project Structure
    
    LlamaIndex-Agentic-RAG-Assistant/
    │
    ├── data/
    │   └── NIPS-2017-attention-is-all-you-need-Paper.pdf
    │
    ├── main.py
    ├── requirements.txt
    ├── .env.example
    ├── .gitignore
    └── README.md

## Setup & Installation
### 1️ Clone the Repository
    git clone https://github.com/sahilshore/LlamaIndex-Agentic-RAG-Assistant.git
    cd LlamaIndex-Agentic-RAG-Assistant

### 2️ Create Virtual Environment (Recommended)
    python -m venv venv


##### Activate:

Windows

    venv\Scripts\activate


Mac / Linux

    source venv/bin/activate

### 3️ Install Dependencies
    pip install -r requirements.txt

### 4️ Setup Environment Variables

Create a .env file:

    cp .env.example .env


Edit .env and add your Groq API key:

    GROQ_API_KEY=your_groq_api_key_here

### >>> How to Run
    python main.py


You should see an answer generated from the PDF document.

### Example Query
    response = query_engine.query(
        "What did the author do growing up?"
    )


Output:

    The model generates an answer based on retrieved document context.

### Main Purpose of This Project

This project demonstrates:

. How Agentic RAG systems work

. How to combine retrieval + reasoning

. How LLMs can understand and answer from documents

. Practical use of LlamaIndex + Groq

This is ideal for:

. Generative AI portfolios

. AI Engineer interviews

. Document QA systems

. RAG-based assistants

### Security Notes

. Do NOT commit .env

.  Use .env.example for sharing configuration

 . Never push API keys to GitHub

### Future Improvements

 . Add conversational memory
  
 . Support multiple PDFs
  
 . Add web UI (Streamlit / Chainlit)
  
 . Persist vectors using FAISS or Chroma
  
 .  Convert into a chatbot interface
