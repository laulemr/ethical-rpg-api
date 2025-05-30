from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

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

# Ethical compass can be kept static or reset after each request to stay stateless
DEFAULT_COMPASS = {
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
    return {"response": reply}

@app.post("/update_compass")
def update_compass(update: CompassUpdate):
    updated_compass = DEFAULT_COMPASS.copy()
    for key in updated_compass:
        updated_compass[key] += getattr(update, key, 0)
    return {"updatedCompass": updated_compass}
