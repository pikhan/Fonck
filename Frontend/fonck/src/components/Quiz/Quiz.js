import React from "react";
import { useContext, useState } from "react";
import { UXContext } from "../../context/UXContext";
import RadioGroupRating from "./Rating";
import CloseIcon from '@mui/icons-material/Close';
import "./Quiz.css";
import { WebContext } from "../../context/WebContext";

const QuizCard = ({ quizKey }) => {
  return (
    <>
      <h3>{quizKey}</h3>
      <RadioGroupRating quizKey={quizKey} />
    </>
  );
};

const Quiz = () => {
  const [popUp, setPopUp] = useContext(WebContext);

  const [quizResults, , submit, handleSubmit] = useContext(UXContext);

  const quizKeys = Object.keys(quizResults);

  return popUp ? (
    <div className="pop-up-container">
        <CloseIcon className="cancel-btn" onClick={() => setPopUp(false)}/>
      <div>
        <h1>Hello! You seem new here...Please let tell us more about you!</h1>
        <h2>Rate your experience at each of the following:&nbsp;</h2>
        <br></br>

        {quizKeys.map((item) => (
          <QuizCard quizKey={item} />
        ))}
      </div>
      <button
        id="submit-btn"
        onClick={() => {
          handleSubmit();
          setPopUp(false);
        }}
      >
        Submit
      </button>
    </div>
  ) : (
    ""
  );
};

export default Quiz;
