import axios from 'axios';

export const fetchReviews = async () => {
  try {
    const response = await axios.get('http://127.0.0.1:7000/reviews'); // Replace with your backend URL
    return response.data;
  } catch (error) {
    console.error("Error fetching reviews:", error);
    return [];
  }
};
