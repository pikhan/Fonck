import Searchbar from "./Searchbar/Searchbar";
import Preferences from "./Preferences/Preferences";
import "./BuildItinerary.css"
import React from 'react';

const BuildItinerary = () => {
    return(
        <>
        <Searchbar/>
        <div className="pref-and-searchResults-wrapper">
            <div className="side-column">
                <Preferences/>
            </div>
        
        <div className="main-column">
            BuildItinerary
        </div>

        </div>
            </>
    )
};

export default BuildItinerary;