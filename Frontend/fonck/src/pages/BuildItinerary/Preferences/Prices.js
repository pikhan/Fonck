import * as React from 'react';
import Radio from '@mui/material/Radio';
import RadioGroup from '@mui/material/RadioGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import FormControl from '@mui/material/FormControl';
import FormLabel from '@mui/material/FormLabel';

const Prices= () => {
  return (
    <FormControl>
      <FormLabel id="demo-row-radio-buttons-group-label">Price</FormLabel>
      <RadioGroup
        row
        aria-labelledby="demo-row-radio-buttons-group-label"
        name="row-radio-buttons-group"
      >
        <FormControlLabel value="$" control={<Radio />} label="$" />
        <FormControlLabel value="$$" control={<Radio />} label="$$" />
        <FormControlLabel value="$$$" control={<Radio />} label="$$$" />
      </RadioGroup>
    </FormControl>
  );
}

export default Prices;