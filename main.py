from fastapi import FastAPI
from pydantic import BaseModel
from agents.tutor_agent import tutor_agent
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="AI Tutor Agent",
    description="A multi-agent AI Tutor system using Gemini API",
    version="1.0.0"
)

class Question(BaseModel):
    query: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Tutor Agent API!"}

@app.post("/ask")
def ask_question(q: Question):
    response = tutor_agent(q.query)
    return {"question": q.query, "answer": response}
