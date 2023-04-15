<<<<<<< HEAD
import Searchbar from "./Searchbar/Searchbar";
import Preferences from "./Preferences/Preferences";
import "./BuildItinerary.css"

=======
import React from 'react';
>>>>>>> f5ffbae40862da17400916b1d531c233e125ff85
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