import Preferences from "./Preferences/Preferences";
import "./BuildItinerary.css";
import React from "react";
import ItineraryCards from "../../components/itinerary-card/ItineraryCards";
import cloudbg from "../../assets/createItinerary-bg.png";
import Quiz from "../../components/Quiz/Quiz";

const itineraries = [
  {
    id: 1,
    title: "To Kill a Mockingbird",
  },
  {
    id: 2,
    title: "1984",
  },
  {
    id: 3,
    title: "Pride and Prejudice",
  },
];

const BuildItinerary = () => {
  return (
    <div className="pg-content" id="create-pg">
        <div className="pref-and-searchResults-wrapper">
          <div className="side-column">
            <Preferences />
          </div>
          <Quiz/>
          <div className="main-column">
            <h1>We've generated 3 itineraries for you!</h1>
            <ItineraryCards itineraries={itineraries} />
          </div>
        </div>
      </div>
  );
};

export default BuildItinerary;
