from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Prompt(BaseModel):
    prompt: str

class CompassUpdate(BaseModel):
    transparency: Optional[int] = 0
    equity: Optional[int] = 0
    mindfulness: Optional[int] = 0
    accountability: Optional[int] = 0
    dataEthics: Optional[int] = 0
    humanOversight: Optional[int] = 0

conversation_history = []
ethical_compass = {
    "transparency": 0,
    "equity": 0,
    "mindfulness": 0,
    "accountability": 0,
    "dataEthics": 0,
    "humanOversight": 0,
}

@app.get("/")
def read_root():
    return {"message": "AI Literacy RPG is running!"}

@app.post("/ask")
def ask(prompt: Prompt):
    reply = f"You asked: {prompt.prompt}. The world responds with uncertainty..."
    conversation_history.append(prompt.prompt)
    return {"response": reply}

@app.get("/conversation")
def get_conversation():
    return {"history": conversation_history}

@app.post("/reset")
def reset_conversation():
    conversation_history.clear()
    return {"message": "Conversation reset."}

@app.post("/update_compass")
def update_compass(update: CompassUpdate):
    for key in ethical_compass:
        ethical_compass[key] += getattr(update, key, 0)
    return {"message": "Compass updated."}
