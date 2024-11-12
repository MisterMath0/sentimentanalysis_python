# backend/models/review.py

class Review:
    def __init__(self, product_name: str, review_text: str, reviewer: str = None):
        self.product_name = product_name
        self.review_text = review_text
        self.reviewer = reviewer

    def __repr__(self):
        return f"<Review(product_name={self.product_name},review_text={self.review_text}, reviewer={self.reviewer})>"
    
    
