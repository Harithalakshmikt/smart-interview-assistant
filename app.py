from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

class Query(BaseModel):
    query: str

@app.post("/ask")
async def ask(query: Query):
    return {"response": f"You asked: {query.query}"}

@app.get("/")
def home():
    return {"message": "Welcome to the API!"}

