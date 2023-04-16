import React from "react";
import { useContext, useState } from "react";
import { UXContext } from "../../context/UXContext";
import RadioGroupRating from "./Rating";



import "./Quiz.css";
import CancelIcon from '@mui/icons-material/Cancel';

const QuizCard = ({ quizKey}) => {
  return (
    <>
      <h3>Rate your average experience at a {quizKey}</h3>
    <RadioGroupRating quizKey={quizKey}/>
    </>
  );
};





const Quiz = () => {

  const [popUp, setPopUp] = useState(true);

  const [quizResults] = useContext(UXContext);

  const quizKeys = Object.keys(quizResults)

  return (popUp) ?(

    <div className="pop-up-container">
    <button className="cancel-btn" onClick={() => setPopUp(false)}> <CancelIcon /> </button>

    <div>
      <h1>
        Hello! You seem new here...To build you a personalized itinerary, please
        let us know more about you!
      </h1>

      {Object.keys(quizResults).map((key) => {
        return <QuizCard quizKey={key}/>;
      })}

    </div>
    </div>
  ): "";
};

export default Quiz;
