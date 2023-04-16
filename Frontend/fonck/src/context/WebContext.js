import { createContext, useState, useEffect } from "react";
import React from "react";

export const WebContext = createContext();

export function WebProvider({ children }) {
  const [popUp, setPopUp] = useState(false);

  return (
    <WebContext.Provider value={[popUp, setPopUp]}>
      {children}
    </WebContext.Provider>
  );
}
