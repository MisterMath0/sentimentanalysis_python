// app/page.tsx
'use client';

import React, { useEffect, useState } from 'react';
import { fetchReviews } from '../utils/api';
import ReviewCard from '../components/ReviewCard';
import './page.css';

const HomePage = () => {
  const [reviews, setReviews] = useState([]);

  useEffect(() => {
    const getReviews = async () => {
      const fetchedReviews = await fetchReviews();
      console.log('Fetched Reviews:', fetchedReviews); // Log the response to check if it's correct
      setReviews(fetchedReviews);
    };

    getReviews();
  }, []);

  return (
    <div>
      <h1>Product Reviews</h1>
      <div className="reviews-container">
        {reviews.length === 0 ? (
          <p>No reviews available</p> // Display a message if no reviews are available
        ) : (
          reviews.map((review, index) => (
            <ReviewCard key={index} review={review} />
          ))
        )}
      </div>
    </div>
  );
};

export default HomePage;
