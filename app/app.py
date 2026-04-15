from fastapi import FastAPI
from pydantic import BaseModel
from agents.agent import agent_decision

app = FastAPI()

# 👇 This tells FastAPI to expect JSON
class InputText(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "AI NLP Agent Running"}

@app.post("/predict/")
def get_prediction(data: InputText):
    result = agent_decision(data.text)
    return {"result": result}