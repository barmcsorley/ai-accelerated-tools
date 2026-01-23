import os
import chromadb
from chromadb.utils import embedding_functions
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Configuration (Env vars for GitOps compliance)
CHROMA_HOST = os.getenv("CHROMA_HOST", "chromadb")
CHROMA_PORT = os.getenv("CHROMA_PORT", "8000")
OLLAMA_HOST = os.getenv("OLLAMA_BASE_URL", "http://ollama:11434/api/embeddings")

def ingest_docs():
    print(f"🚀 Connecting to Vector DB at {CHROMA_HOST}:{CHROMA_PORT}...")
    
    # 1. Initialize Client
    client = chromadb.HttpClient(host=CHROMA_HOST, port=CHROMA_PORT)
    
    # 2. Define Embedding Function (Ollama)
    # Using the standard OpenAI-compatible endpoint or dedicated Ollama func
    ollama_ef = embedding_functions.OllamaEmbeddingFunction(
        url=f"{OLLAMA_HOST}",
        model_name="nomic-embed-text"
    )

    # 3. Create/Get Collection
    collection = client.get_or_create_collection(
        name="engineering_docs", 
        embedding_function=ollama_ef
    )

    # 4. Load Documents
    print("📂 Loading documents from /data/docs...")
    loader = DirectoryLoader('/data/docs', glob="**/*.md", loader_cls=TextLoader)
    docs = loader.load()

    # 5. Split Text (Chunking strategy is key for RAG)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)

    # 6. Upsert to DB
    print(f"🧠 Embedding {len(splits)} chunks...")
    for i, split in enumerate(splits):
        collection.upsert(
            documents=[split.page_content],
            metadatas=[split.metadata],
            ids=[f"doc_{i}"]
        )
    
    print("✅ Ingestion Complete. Knowledge Base updated.")

if __name__ == "__main__":
    ingest_docs()
