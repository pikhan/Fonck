import React from "react";
import { useContext, useState } from "react";
import { UXContext } from "../../context/UXContext";
import RadioGroupRating from "./Rating";

import "./Quiz.css";
import CancelIcon from '@mui/icons-material/Cancel';
import { capitalize } from "@mui/material";



const QuizCard = ({ quizKey}) => {
  return (
    <>
      <h3>{quizKey}</h3>
    <RadioGroupRating quizKey={quizKey}/>
    </>
  );
};





const Quiz = () => {

  const [popUp, setPopUp] = useState(true);

  const [quizResults, ,submit, handleSubmit] = useContext(UXContext);

  const quizKeys = Object.keys(quizResults)

  return (popUp) ?(

    <div className="pop-up-container">
    <button className="cancel-btn" onClick={() => setPopUp(false)}> <CancelIcon /> </button>

    <div>
      <h1>
        Hello! You seem new here...To build you a personalized itinerary, please
        let us know more about you!
      </h1>
      <h2>Rate your experience at each of the following:&nbsp;</h2>
      <br></br>

      {Object.keys(quizResults).map((key) => {
        // title case for key
        key = capitalize(key);
        return <QuizCard quizKey={key}/>;
      })}

    </div>
    <button id="submit-btn" onClick={handleSubmit}>Submit</button>
    </div>
  ): "";
};

export default Quiz;
