// app/components/ReviewCard.js
'use client';

import React from 'react';
import './ReviewCard.css';

const ReviewCard = ({ review }) => {
  console.log('Review in ReviewCard:', review); // Log the review data to see if it's passed correctly

  return (
    <div className="review-card">
      <h3 className="product-name">{review.product_name}</h3>
      <div className="emoji">{review.emoji}</div>
      <p className="review-text">{review.review_text.trim()}</p>
      <p className="reviewer-name">{review.reviewer_name.trim()}</p>
      <p className="sentiment-rating">Rating: {review.sentiment_rating}</p>
    </div>
  );
};

export default ReviewCard;
