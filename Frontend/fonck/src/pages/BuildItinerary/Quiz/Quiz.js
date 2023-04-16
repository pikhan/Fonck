import React from "react";

import RadioGroupRating from "./Rating";

const quizCat = [
  {
    category: "art_gallery",
    rating: "",
  },
  {
    category: "bar",
    rating: "",
  },
  {
    category: "clothing_store",
    rating: "",
  },
  {
    category: "museum",
    rating: "",
  },
  {
    category: "park",
    rating: "",
  },
  {
    category: "shopping_mall",
    rating: "",
  },
  {
    category: "tourist_attraction",
    rating: "",
  },
  {
    category: "zoo",
    rating: "",
  },
];

const QuizCard = ({item, num}) => {
  return (
  <>
    <h3>Rate your average experience at a {item.category}</h3>
    <RadioGroupRating/>
  </>
  )
};

const Quiz = () => {
  return (
    <div>
      <h1>
        Hello! You seem new here...To build you a personalized itinerary, please
        let us know more about you!
      </h1>

      {quizCat.map((item, index) => (
                <QuizCard item={item} num={index}/>
        ))}

    </div>
  );
};

export default Quiz;