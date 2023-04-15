import { LocalizationProvider, DateField } from "@mui/x-date-pickers";
import { AdapterDayjs } from "@mui/x-date-pickers/AdapterDayjs";
import dayjs from "dayjs";
import { TextField } from "@mui/material";
import { useContext, useState } from "react";
import { PreferencesContext } from "../../../context/preferencesContext";
import React from "react"
import "./Searchbar.css"


const today = dayjs();
const tomorrow = dayjs().add(1, "day");


const Searchbar = () => {
  const [searchInput, setSearchInput] = useContext(PreferencesContext);

  return (
    <div className="Searchbar-wrapper">

      <LocalizationProvider dateAdapter={AdapterDayjs}>
        <DateField className="Searchbar-item" defaultValue={today} minDate={tomorrow} label="Start Date" />
        <DateField className="Searchbar-item" minDate={tomorrow} label="End Date" />
      </LocalizationProvider>
      
      <TextField className="Searchbar-item" id="outlined-basic" label="User Input" variant="outlined" />
      <button className="Searchbar-item" id="search-btn">Search</button>
    </div>
  );
};

export default Searchbar;
