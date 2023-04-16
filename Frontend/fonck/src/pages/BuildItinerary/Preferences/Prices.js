import * as React from 'react';
import Radio from '@mui/material/Radio';
import RadioGroup from '@mui/material/RadioGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import FormControl from '@mui/material/FormControl';
import FormLabel from '@mui/material/FormLabel';

import {useContext, useState} from "react";
import { PreferencesContext } from '../../../context/preferencesContext';

const Prices= () => {
  const [,,,,,,,, price, setPrice] = useContext(PreferencesContext);
  const handleChange = (event) => {
    setPrice(event.target.value);
  };

  return (
    <FormControl>
      <RadioGroup
        row
        aria-labelledby="price-preference"
        name="price-preference"
        value={price}
        onChange={handleChange}

      >
        <FormControlLabel value="$" control={<Radio />} label="$" />
        <FormControlLabel value="$$" control={<Radio />} label="$$" />
        <FormControlLabel value="$$$" control={<Radio />} label="$$$" />
      </RadioGroup>
    </FormControl>
  );
}

export default Prices;