import EventNoteIcon from '@mui/icons-material/EventNote';
import Checkbox from '@mui/material/Checkbox';
import FavoriteBorder from '@mui/icons-material/FavoriteBorder';
import Favorite from '@mui/icons-material/Favorite';
import "./ItineraryCards.css"
import itinerary1 from "../../assets/itinerary1.png"
import itinerary2 from "../../assets/itinerary2.png"
import itinerary3 from "../../assets/itinerary3.png"

import React from "react";

const label = { inputProps: { 'aria-label': 'Checkbox demo' } };

const ItineraryCard = ({cardInfo, num}) => {

    const itineraryPhotos = [itinerary1, itinerary2, itinerary3]

    return(
        <div className="card-container">
            <img src={itineraryPhotos[num-1]}/>
            <div className="card-info">
                <h2>Itinerary {num}</h2>
                <Checkbox {...label} icon={<FavoriteBorder />} checkedIcon={<Favorite />} className="checkbox"/>
            </div>
        </div>
    )
};

const ItineraryCards = ({itineraries}) =>{
    return(
        <>
            {itineraries.map((item, index) => (
                <ItineraryCard cardInfo={item} num={index+1}/>
            ))}
        </>
    )
};

export default ItineraryCards;