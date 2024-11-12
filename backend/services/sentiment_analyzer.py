# backend/services/sentiment_analyzer.py
from dotenv import load_dotenv
from openai import OpenAI # type: ignore
import os
from models.sentiment_analysis import SentimentAnalysis

class SentimentAnalyzer:
    def __init__(self):
        load_dotenv() 
        OpenAI.api_key = os.getenv("OPENAI_API_KEY")

    def analyze_sentiment(self, review_text: str) -> SentimentAnalysis:
        """Analyzes the sentiment of a review text using OpenAI and returns a SentimentAnalysis object."""
        client = OpenAI()
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {   "role": "system", 
                    "content": "You are a helpful assistant. You analy Reviews and rate the sentiments given the users requests and return the score requested. note: you only returna  float value"
                    },
                {
                    "role": "user",
                    "content": f"Rate the sentiment of this review from -1 (very negative) to 1 (very positive): {review_text}",
                }
            ]
           
            )
        print(response.choices[0].message.content)
        score = float(response.choices[0].message.content)
        return SentimentAnalysis(score=score)
