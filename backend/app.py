# backend/app.py
from flask_cors import CORS
from flask import Flask, jsonify
from services.scraper import Scraper
from services.sentiment_analyzer import SentimentAnalyzer

app = Flask(__name__)
CORS(app)

class SentimentAnalysisApp:
    def __init__(self, url: str):
        self.url = url
        self.scraper = Scraper(url)
        self.sentiment_analyzer = SentimentAnalyzer()

    def get_reviews_with_sentiment(self):
        reviews = self.scraper.get_reviews()
        reviews_with_sentiment = []
        
        for review in reviews:
            sentiment = self.sentiment_analyzer.analyze_sentiment(review.review_text)
            # Format each review with sentiment details as a dictionary
            reviews_with_sentiment.append({
                "product_name": review.product_name,
                "reviewer_name": review.reviewer or "Anonymous",
                "review_text": review.review_text,
                "sentiment_rating": sentiment.rating,
                "emoji": sentiment.emoji
            })
        
        return reviews_with_sentiment

# Create an instance of SentimentAnalysisApp
url = "your-url-for-reviews-here"  # Replace with actual review page URL
sentiment_app = SentimentAnalysisApp(url)

# Define the endpoint to serve reviews
@app.route('/reviews', methods=['GET'])
def get_reviews():
    reviews_data = sentiment_app.get_reviews_with_sentiment()
    return jsonify(reviews_data)  # Return the list of reviews as JSON

if __name__ == "__main__":
    app.run(debug=True, port=8000)
