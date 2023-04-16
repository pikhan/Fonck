import EventNoteIcon from '@mui/icons-material/EventNote';
import "./ItineraryCards.css"
import itinerary1 from "../../assets/itinerary1.png"
import itinerary2 from "../../assets/itinerary2.png"
import itinerary3 from "../../assets/itinerary3.png"
import React from "react";

const ItineraryCard = ({cardInfo, num}) => {

    const itineraryPhotos = [itinerary1, itinerary2, itinerary3]
    const cardImgPath = `../../assets/itinerary${num}.png`;
    console.log(cardImgPath)
    return(
        <div className="card-container">
            <img src={itineraryPhotos[num-1]}/>
          
            <div className="card-info">
                <h3>Option {num}</h3>
                <h1><EventNoteIcon fontSize="large"/></h1>
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