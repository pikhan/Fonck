import { TextField } from "@mui/material";
import { AdapterDateFns } from "@mui/x-date-pickers/AdapterDateFns";
import { Stack } from "@mui/material";
import { TimePicker, StaticTimePicker } from "@mui/x-date-pickers";

import dayjs from "dayjs";
import ScoreCuisines from "./ScoreCuisines";
import Prices from "./Prices";
import React from "react";
import { useContext, useState } from "react";
import { PreferencesContext } from "../../../context/preferencesContext";
import "./Preferences.css";


import { LocalizationProvider, DateField } from "@mui/x-date-pickers";
import { AdapterDayjs } from "@mui/x-date-pickers/AdapterDayjs";


const today = dayjs();
const tomorrow = dayjs().add(1, "day");

const Preferences = () => {
  const [dates,setDates,
    location,
    setLocation,
    boundingTimes,
    setBoundingTimes,
    food,
    setFood,
    price,
    setPrice,
    handleSearchSubmit,
  ] = useContext(PreferencesContext);
  const [startTime, setStartTime] = useState(null);
  const [endTime, setEndTime] = useState(null);
  return (
    <div className="pref-container">
      <h3>Preferences</h3>

    <section>


    <h4 className="sectionTitle">Location:</h4>

    <TextField
        label="Location"
        // variant="standard"
        onChange={(event) => setLocation(event.target.value)}
      />

    <h4 className="sectionTitle">Dates:</h4>


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
          onChange={(newValue) =>
            setDates((prevState) => ({
              ...prevState,
              startDate: newValue,
            }))}

          
        />
        <DateField
          className="Searchbar-item"
          minDate={tomorrow}
          label="End Date"
          variant="filled"
          InputProps={{
            style: { backgroundColor: "#FFFFFF" },
          }}

          onChange={(newValue) =>
            setDates((prevState) => ({
              ...prevState,
              endDate: newValue,
            }))
          }

        />
      </LocalizationProvider>


      <h4 className="sectionTitle"> Time Bounds: </h4>
      <div className="time-pickers">
            <LocalizationProvider dateAdapter={AdapterDateFns}>
              <Stack spacing={4} sx={{ witdh: "250px" }}>
                <table>
                  <tbody>
                    <tr>
                      <td>
                        <TimePicker
                          label="Start Bound"
                          renderInput={(params) => <TextField {...params} />}
                          value={boundingTimes.startTime}
                          onChange={(newValue) =>
                            setBoundingTimes((prevState) => ({
                              ...prevState,
                              startTime: newValue,
                            }))
                          }
                        />
                      </td>
                      <td>
                        <TimePicker
                          label="End Bound"
                          renderInput={(params) => <TextField {...params} />}
                          value={boundingTimes.endTime}
                          onChange={(newValue) =>
                            setBoundingTimes((prevState) => ({
                              ...prevState,
                              endTime: newValue,
                            }))
                          }
                        />
                      </td>
                    </tr>
                  </tbody>
                </table>
              </Stack>
            </LocalizationProvider>
          </div>

    </section>


      <section>
        <h4 className="sectionTitle">Score Cuisines</h4>
        <ScoreCuisines/>
      </section>


    
    <h4 className="sectionTitle">Price:</h4>
    <div> <Prices /></div>
   




      <button className="Searchbar-item" id="search-btn" onClick={handleSearchSubmit}>
        <h1>Search</h1>
      </button>
    </div>
  );
};

export default Preferences;
