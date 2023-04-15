import { LocalizationProvider, DateField } from '@mui/x-date-pickers';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { TextField } from '@mui/material';
import {useContext, useState} from "react";
import { PreferencesContext } from '../../../context/preferencesContext';
import React from "react"

const Searchbar = () => {
    const [searchInput, setSearchInput] = useContext(PreferencesContext);

    return(
        <div className="Searchbar-wrapper">
            <LocalizationProvider dateAdapter={AdapterDayjs}>
                <DateField label="Start Date" />
                <DateField label="End Date" />
            </LocalizationProvider>
            <TextField id="outlined-basic" label="User Input" variant="outlined" />
            
        </div>
    )
};

export default Searchbar;