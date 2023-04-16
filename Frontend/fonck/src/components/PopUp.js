import React from "react";
import "./PopUp.css";


const PopUp = (props) => {
    return(props.trigger) ? (
        <div className="pop-up-container">
                <p> Hello World</p>
        </div>
    ): "";
};


export default PopUp;