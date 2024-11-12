# Sentiment Analysis for Product Reviews Using BeatifulSoup4(python), OpenAI and NextJS
A sentiment analysis tool for product reviews built with Python (BeautifulSoup for scraping, OpenAI for analysis) and Next.js for the frontend. It fetches reviews, analyzes sentiment, and displays results with ratings and emojis. A showcase project for web scraping, AI integration, and frontend development.

## Prerequisites

### Backend
1. Python 3.x
2. Install the required Python libraries by running:
   ```bash
   pip install -r backend/requirements.txt
3. You will need an OpenAI API key for sentiment analysis. You can obtain it by signing up at <a href="https://platform.openai.com/docs/overview">OpenAI.</a>

### Frontend
Node.js and npm (or yarn)
Install the required dependencies by running:
  ```bash
    cd frontend
    npm install
```
### Setting Up the Backend

1. In the backend/ folder, open app.py.
2. Modify the URL in the url = "your_product_reviews_url" line to the product review page you want to scrape.
3. Ensure your OpenAI API key is set up correctly in the SentimentAnalyzer class in the backend.
To run the backend, simply execute:
```bash
  python backend/app.py
```
This will fetch the reviews from the specified URL, analyze their sentiment, and print the results to the console ans also display then as  a json on your backend server

### Setting Up the Frontend
In the frontend/ folder, run the following to start the Next.js development server:
```bash
npm run dev
```
This will start the server at http://localhost:3000.

The frontend will display the scraped reviews and their sentiment analysis (rating and emoji) based on the backend's output.

### Deploying the Backend and Frontend
For deployment:

1. Backend: As the backend is not deployed, you can either run it locally or use a service like Heroku or PythonAnywhere to deploy it.
2. Frontend: You can deploy the Next.js frontend using platforms like Vercel or Netlify for easy hosting.

### How to Modify the Code
1. Scraping New Websites: To scrape a different website, modify the Scraper class inside backend/services/scraper.py to handle the new website's HTML structure.
2. Change Sentiment Model: If you want to change the sentiment analysis method, modify the SentimentAnalyzer class inside backend/services/sentiment_analyzer.py to use a different API or model.
3. Styling the Frontend: You can customize the look and feel of the frontend by editing the components in frontend/components/Review.js and adjusting the CSS styles in frontend/styles.

### Demo
here is how it looks like with an Example from TrustPilot after complete configuration
![image](https://github.com/user-attachments/assets/7ae655aa-5622-4379-b8e9-5494a1bf9ee4)

