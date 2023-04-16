import { TextField } from "@mui/material";
import { LocalizationProvider } from "@mui/x-date-pickers";
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



const Preferences = () => {
  const [,,
    location,
    setLocation,
    boundingTimes,
    setBoundingTimes,
    food,
    setFood,
    price,
    setPrice,
  ] = useContext(PreferencesContext);
  const [startTime, setStartTime] = useState(null);
  const [endTime, setEndTime] = useState(null);
  return (
    <div className="pref-container">
      <h3>Preferences</h3>
      <section>
    
          <h4 className="sectionTitle">Price:</h4>
          <Prices />
        <div>
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
        </div>
      </section>
      <section>
        <h4 className="sectionTitle">Score Cuisines</h4>
        <ScoreCuisines/>
      </section>
    </div>
  );
};

export default Preferences;
