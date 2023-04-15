import { TextField } from '@mui/material';
import { TimePicker } from '@mui/x-date-pickers';
import dayjs from 'dayjs';
import Rank from "./Rank";
import Options from "./Options"
import Prices from "./Prices"

import {useContext, useState} from "react";
import { PreferencesContext } from '../../../context/preferencesContext';


const Preferences = () => {
    const [,, location, setLocation, boundingTimes, setBoundingTimes, food, setFood, attractions, setAttractions, price, setPrice] = useContext(PreferencesContext);
    
    return(
        <section>
            <h3>Preferences</h3>
            <TextField id="outlined-basic" label="Location" variant="standard" />
            <Rank options={Options.cuisines}/>
            <Rank options={Options.attractions}/>
            <Prices/>

            {/* <TimePicker
                label="Controlled picker"
                value={dayjs('2022-04-17T15:30')}
                // onChange={(newValue) => setValue(newValue)}
            /> */}
        </section>
    )
}

export default Preferences;