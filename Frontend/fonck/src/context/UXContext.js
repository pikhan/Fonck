import { createContext, useContext, useState, useEffect } from "react";
import React from "react";

export const UXContext = createContext();

export function UXProvider({ children }) {
  const [quizResults, setQuizResults] = useState({
    "movie theater": 3,
    "art gallery": 3,
    "clothing store": 3,
    "university": 3,
    "bar": 3,
    "shopping mall": 3,
    "museum": 3,
    "stadium": 3,
    "zoo": 3,
    "tourist attraction": 3,
    "park": 3,
  });

  const [attractions, setAttractions] = useState([]);

  const [submit, setSubmit] = useState(false)

  const handleSubmit = async () => {
    // console.log("submitted", quizResults)
    //Code for what you want to do when quiz is submitted
    try {
      const response = await fetch('http://localhost:5000/getActivities', {
        method: 'POST',
        headers: {
          'Access-Control-Allow-Origin': '*',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(quizResults) 
      });
      // get recommended attractions json
      const data = await response.json();
      console.log(data);
      setAttractions(data);
  
    } catch (error) {
      console.log(error);
    }
    setSubmit(true)
  }

  useEffect(() => {
    // console.log("quizResultsChanged", quizResults);
}, [quizResults]);

  return (
    <UXContext.Provider value={[quizResults, setQuizResults, submit, handleSubmit, attractions]}>
      {children}
    </UXContext.Provider>
  );
}
