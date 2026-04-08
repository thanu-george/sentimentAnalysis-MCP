from textblob import TextBlob

def summarize(text: str) -> str:
    return text[:80] + "..." if len(text) > 80 else text

def sentiment_analysis(text: str) -> dict:
    blob = TextBlob(text)
    sentiment = blob.sentiment

    return {
        "polarity": round(sentiment.polarity, 2),
        "subjectivity": round(sentiment.subjectivity, 2),
        "assessment": (
            "positive" if sentiment.polarity > 0
            else "negative" if sentiment.polarity < 0
            else "neutral"
        )
    }