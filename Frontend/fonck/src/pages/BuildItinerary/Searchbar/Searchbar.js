import { LocalizationProvider, DateField } from "@mui/x-date-pickers";
import { AdapterDayjs } from "@mui/x-date-pickers/AdapterDayjs";
import dayjs from "dayjs";
import { TextField } from "@mui/material";
import { useContext, useState } from "react";
import { PreferencesContext } from "../../../context/preferencesContext";
import React from "react";
import "./Searchbar.css";

const today = dayjs();
const tomorrow = dayjs().add(1, "day");

const Searchbar = () => {
  const [searchInput, setSearchInput] = useContext(PreferencesContext);

  return (
    <div className="Searchbar-wrapper">
      <LocalizationProvider dateAdapter={AdapterDayjs}>
        <DateField
          className="Searchbar-item"
          defaultValue={today}
          minDate={tomorrow}
          label="Start Date"
          variant="filled"
          InputProps={{
            style: { backgroundColor: "#FFFFFF" },
          }}
        />
        <DateField
          className="Searchbar-item"
          minDate={tomorrow}
          label="End Date"
          variant="filled"
          InputProps={{
            style: { backgroundColor: "#FFFFFF" },
          }}
        />
      </LocalizationProvider>
      <TextField
        label="Location"
        InputProps={{
          style: { backgroundColor: "#FFFFFF" },
        }}
        variant="filled"
      />

      <button className="Searchbar-item" id="search-btn">
        <h1>Search</h1>
      </button>
    </div>
  );
};

export default Searchbar;
