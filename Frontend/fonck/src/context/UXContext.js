import { createContext, useState, useEffect } from "react";
import React from "react";

export const UXContext = createContext();

export function UXProvider({ children }) {
  const [quizResults, setQuizResults] = useState({
    "art gallery": 3,
    "bar": 3,
    "clothing store": 3,
    "museum": 3,
    "park": 3,
    "shopping mall": 3,
    "tourist attraction": 3,
    "zoo": 3,
  });

  const [submit, setSubmit] = useState(false)

  const handleSubmit = () => {
    console.log("submitted", quizResults)
    //Code for what you want to do when quiz is submitted
    setSubmit(true)
  }

  useEffect(() => {
    console.log("quizResultsChanged", quizResults);
}, [quizResults]);

  return (
    <UXContext.Provider value={[quizResults, setQuizResults, submit, handleSubmit]}>
      {children}
    </UXContext.Provider>
  );
}
