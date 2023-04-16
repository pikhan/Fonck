import Searchbar from "./Searchbar/Searchbar";
import Preferences from "./Preferences/Preferences";
import "./BuildItinerary.css";
import React from "react";
import ItineraryCards from "../../components/itinerary-card/ItineraryCards";
import cloudbg from "../../assets/createItinerary-bg.png";
import PopUp from "../../components/PopUp";

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
      <div className="form-wrapper">
        <Searchbar />
        <div className="pref-and-searchResults-wrapper">
          <div className="side-column">
            <Preferences />
          </div>
          <PopUp trigger={true}/>
          <div className="main-column">
            <h1>We've generated 3 itineraries for you!</h1>
            <ItineraryCards itineraries={itineraries} />
          </div>
        </div>
      </div>
    </div>
  );
};

export default BuildItinerary;
