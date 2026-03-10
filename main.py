from fastapi import FastAPI
from textblob import TextBlob

app = FastAPI()


@app.get("/analyze/{text}")
def get_sentiment(text: str):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    # Determine label based on score
    if polarity > 0:
        sentiment = "positive"
    elif polarity < 0:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    return {
        "text": text,
        "sentiment": sentiment,
        "score": round(polarity, 2)
    }
