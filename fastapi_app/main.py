from fastapi import FastAPI
from pydantic import BaseModel
from shared.utils import summarize, sentiment_analysis

app = FastAPI()

class InputText(BaseModel):
    text: str

@app.post("/analyze")
def analyze(input: InputText):
    summary = summarize(input.text)
    sentiment = sentiment_analysis(input.text)

    return {
        "summary": summary,
        "sentiment": sentiment
    }