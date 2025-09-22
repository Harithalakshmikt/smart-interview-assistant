from transformers import pipeline
from langchain.embeddings import HuggingFaceEmbeddings

def load_llm(model_name="google/flan-t5-base"):
    """
    Load a lightweight instruction-tuned model for text generation.
    """
    return pipeline("text2text-generation", model=model_name)

def load_embedding_model(model_name="sentence-transformers/all-MiniLM-L6-v2"):
    """
    Load a sentence transformer for embedding resume chunks.
    """
    return HuggingFaceEmbeddings(model_name=model_name)
