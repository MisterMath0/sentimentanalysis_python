# backend/models/sentiment_analysis.py

class SentimentAnalysis:
    def __init__(self, score: float):
        self.score = score
        self.rating = self._get_rating()
        self.emoji = self._get_emoji()

    def _get_rating(self) -> int:
        """Converts the sentiment score to a 1-10 rating."""
        return min(max(int((self.score + 1) * 5), 1), 10)  # Normalize score to 1-10

    def _get_emoji(self) -> str:
        """Returns an emoji based on the sentiment rating."""
        if self.rating >= 8:
            return "😃"
        elif self.rating >= 5:
            return "😐"
        else:
            return "😡"

    def __repr__(self):
        return f"<SentimentAnalysis(score={self.score}, rating={self.rating}, emoji={self.emoji})>"
