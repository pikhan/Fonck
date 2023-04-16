import EventNoteIcon from '@mui/icons-material/EventNote';
import React from "react";


const ItineraryCard = ({cardInfo, num}) => {
    return(
        <div className="card-container">
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