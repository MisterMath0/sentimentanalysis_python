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
            review_elements = soup.select('.styles_cardWrapper__LcCPA')  # Replace .review with actual HTML tag for reviews
            
            for element in review_elements:
                product_name = soup.select_one('h1.title_title__i9V__ span').text.strip() # Replace with actual class
                review_text = element.select_one('.styles_reviewContent__0Q2Tg p').text  if element.select_one('.styles_reviewContent__0Q2Tg p') else "No review text available"  # Replace with actual class
                reviewer = element.select_one('.link_internal__7XN06 link_wrapper__5ZJEx styles_consumerDetails__ZFieb span').text if element.select_one('.link_internal__7XN06 link_wrapper__5ZJEx styles_consumerDetails__ZFieb span') else "None"
                
                review = Review(product_name=product_name, review_text=review_text, reviewer=reviewer)
                reviews.append(review)
                print(f"Scraped Review: {review}")
        else:
            print(f"Failed to retrieve webpage: {response.status_code}")

        return reviews
