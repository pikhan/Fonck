import React from "react";
import { useState } from "react";
import "./PopUp.css";
import Quiz from "../pages/BuildItinerary/Quiz/Quiz"
import CancelIcon from '@mui/icons-material/Cancel';


//let popUp = true;

// function exit() {
//     popUp = false;
// }

const PopUp = () => {
    const [popUp, setPopUp] = useState(true);
    return(popUp) ? (
        <div className="pop-up-container">
                <button className="cancel-btn" onClick={() => setPopUp(false)}> <CancelIcon /> </button>
                <Quiz/>
                <button className="submit-btn" onClick={() => setPopUp(false)}> <h2>Submit</h2> </button>
        </div>
    ): "";
};


export default PopUp;