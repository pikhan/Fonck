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

  useEffect(() => {
    console.log("quizResultsChanged", quizResults);
}, [quizResults]);

  return (
    <UXContext.Provider value={[quizResults, setQuizResults]}>
      {children}
    </UXContext.Provider>
  );
}
