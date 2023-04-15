import Searchbar from "./Searchbar/Searchbar";
import Preferences from "./Preferences/Preferences";
import "./BuildItinerary.css"
import React from 'react';
import ItineraryCards from "../../components/itinerary-card/ItineraryCards";

const itineraries = [
    {
      id: 1,
      title: 'To Kill a Mockingbird',
    },
    {
      id: 2,
      title: '1984',
    },
    {
      id: 3,
      title: 'Pride and Prejudice',
    }
];

const BuildItinerary = () => {
    return(
        <>
        <Searchbar/>
        <div className="pref-and-searchResults-wrapper">
            <div className="side-column">
                <Preferences/>
            </div>
        
        <div className="main-column">
            <h3>We've generated 3 itineraries for you!</h3>
            <ItineraryCards itineraries={itineraries}/>
        </div>

        </div>
            </>
    )
};

export default BuildItinerary;