import * as React from "react";
import Box from "@mui/material/Box";
import MenuItem from "@mui/material/MenuItem";
import { useContext, useState } from "react";
import { PreferencesContext } from "../../../context/preferencesContext";
import InputLabel from "@mui/material/InputLabel";
import FormControl from "@mui/material/FormControl";
import Select from "@mui/material/Select";


const ScoreCuisines = () => {
  const [, , , , , ,food, setFood] = useContext(PreferencesContext);

  const score = ["1", "2", "3", "4", "5"];

  return (
    <>
      <Box sx={{ minWidth: 120 }}>
        <FormControl fullWidth>
          <InputLabel id="demo-simple-select-label">American</InputLabel>
          <Select
            labelId="demo-simple-select-label"
            id="demo-simple-select"
            value={food.American}
            label="American"
            onChange={(event) =>
              setFood((prevState) => ({
                ...prevState,
                American: event.target.value,
              }))
            }
          >
            {score.map((item, index) => (
              <MenuItem key={index} value={item}>{item}</MenuItem>
            ))}
          </Select>
        </FormControl>
      </Box>

      <Box sx={{ minWidth: 120 }}>
        <FormControl fullWidth>
          <InputLabel id="demo-simple-select-label">Asian</InputLabel>
          <Select
            labelId="demo-simple-select-label"
            id="demo-simple-select"
            value={food.Asian}
            label="Asian"
            onChange={(event) =>
              setFood((prevState) => ({
                ...prevState,
                Asian: event.target.value,
              }))
            }
          >
            {score.map((item, index) => (
              <MenuItem key={index} value={item}>{item}</MenuItem>
            ))}
          </Select>
        </FormControl>
      </Box>

      <Box sx={{ minWidth: 120 }}>
        <FormControl fullWidth>
          <InputLabel id="demo-simple-select-label">Mediterranean</InputLabel>
          <Select
            labelId="demo-simple-select-label"
            id="demo-simple-select"
            value={food.Mediterranean}
            label="Mediterranean"
            onChange={(event) =>
              setFood((prevState) => ({
                ...prevState,
                Mediterranean: event.target.value,
              }))
            }
          >
            {score.map((item, index) => (
              <MenuItem key={index} value={item}>{item}</MenuItem>
            ))}
          </Select>
        </FormControl>
      </Box>

      <Box sx={{ minWidth: 120 }}>
        <FormControl fullWidth>
          <InputLabel id="demo-simple-select-label">Latin</InputLabel>
          <Select
            labelId="demo-simple-select-label"
            id="demo-simple-select"
            value={food.Latin}
            label="Latin"
            onChange={(event) =>
              setFood((prevState) => ({
                ...prevState,
                Latin: event.target.value,
              }))
            }
          >
            {score.map((item, index) => (
              <MenuItem key={index} value={item}>{item}</MenuItem>
            ))}
          </Select>
        </FormControl>
      </Box>


      <Box sx={{ minWidth: 120 }}>
        <FormControl fullWidth>
          <InputLabel id="demo-simple-select-label">European</InputLabel>
          <Select
            labelId="demo-simple-select-label"
            id="demo-simple-select"
            value={food.European}
            label="European"
            onChange={(event) =>
              setFood((prevState) => ({
                ...prevState,
                European: event.target.value,
              }))
            }
          >
            {score.map((item, index) => (
              <MenuItem key={index} value={item}>{item}</MenuItem>
            ))}
          </Select>
        </FormControl>
      </Box>
    </>
  );
};

export default ScoreCuisines;
