import EventNoteIcon from '@mui/icons-material/EventNote';
import "./ItineraryCards.css"
import React from "react";

const ItineraryCard = ({cardInfo, num}) => {

    const cardImgPath = `../../assets/itinerary${num}.png`;
    return(
        <div className="card-container">
            <img src={`../../assets/itinerary${num}.png`}/>
            <h1><EventNoteIcon fontSize="large"/></h1>
            <div className="card-info">
                <h3>Option {num}</h3>
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