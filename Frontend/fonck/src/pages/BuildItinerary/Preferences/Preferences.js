import { TextField } from '@mui/material';
import { TimePicker } from '@mui/x-date-pickers';
import dayjs from 'dayjs';
import Rank from "./Rank";
import Options from "./Options"
import Prices from "./Prices"
import React from "react"
import {useContext, useState} from "react";
import { PreferencesContext } from '../../../context/preferencesContext';
import "./Preferences.css";


const Preferences = () => {
    const [,, location, setLocation, boundingTimes, setBoundingTimes, food, setFood, attractions, setAttractions, price, setPrice] = useContext(PreferencesContext);
    
    return(
        <div className="pref-container">
            <h3>Preferences</h3>
            <section>
                <div className="pref-field">
                    <h4 className="sectionTitle">Location:</h4>
                    <TextField id="outlined-basic" label="Location" variant="standard" />
                </div>
                <div className="pref-field">
                    <h4 className="sectionTitle">Price:</h4>
                    <Prices/>
                </div>
            </section>
            <section>
                <h4 className="sectionTitle">Rank Food Categories</h4>
                <Rank options={Options.cuisines}/>
            </section>

            <section>
                <h4 className="sectionTitle">Rank Attractions</h4>
                <Rank options={Options.attractions}/>
            </section>
            

        </div>
    )
}

export default Preferences;