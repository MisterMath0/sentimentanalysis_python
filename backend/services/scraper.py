# backend/services/scraper.py

import requests
from bs4 import BeautifulSoup
from models.review import Review

class Scraper:
    def __init__(self, url: str):
        self.url = url

    def get_reviews(self) -> list:
        """Scrapes reviews from a webpage and returns a list of Review objects."""
        reviews = []
        
        response = requests.get(self.url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # This selector will need to be customized based on your target webpage structure
            review_elements = soup.select('.your-actual-html-tag-for-reviews')  # Replace .review with actual HTML tag for reviews(TIP: you can use chatGPT to analyse a page structure and give you this values as output
            
            for element in review_elements:
                product_name = soup.select_one('.your-actual-html-tag-for-product-name').text.strip() # Replace with actual class
                review_text = element.select_one('.your-actual-html-tag-for-review-text').text  if element.select_one('.your-actual-html-tag-for-reviews-text') else "No review text available"  # Replace with actual class
                reviewer = element.select_one('your-actual-html-tag-for-reviewer-name').text if element.select_one('your-actual-html-tag-for-reviewer-name') else "None"
                
                review = Review(product_name=product_name, review_text=review_text, reviewer=reviewer)
                reviews.append(review)
                print(f"Scraped Review: {review}")
        else:
            print(f"Failed to retrieve webpage: {response.status_code}")

        return reviews
