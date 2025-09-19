from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

# Load a small Hugging Face model
generator = pipeline("text-generation", model="google/gemma-2b-it")  # lightweight and free

class Query(BaseModel):
    query: str

@app.post("/ask")
async def ask(query: Query):
    result = generator(query.query, max_length=200, do_sample=True)[0]["generated_text"]
    return {"response": result}

@app.get("/")
def home():
    return {"message": "Welcome to the Smart Interview Assistant API!"}
