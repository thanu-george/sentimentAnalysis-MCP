from pydantic import BaseModel
from fastapi import FastAPI
from textblob import TextBlob

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.post("/analyze")
def analyze_sentiment(input: TextInput):
    blob = TextBlob(input.text)
    sentiment = blob.sentiment
    return {
       "polarity":round(sentiment.polarity,2),
       "subjectivity":round(sentiment.subjectivity,2),
       "assessment":"positive" if sentiment.polarity > 0 else "negative" if sentiment.polarity < 0 else "neutral"
   }
