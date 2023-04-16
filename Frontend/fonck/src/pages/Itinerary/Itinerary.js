import React from 'react';
import "./Itinerary.css"

import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import itineraryData from './itineraryData.js';
import AllItineraryData from './itineraryObj.js';


function Day({dayIndex, date, dayData} ) {
  return (
    <TableContainer component={Paper}>
      <Table sx={{ minWidth: 650 }} aria-label="simple table">
        <TableHead>
        <TableRow>
              <TableCell align="center" colSpan={2}>
                Day {dayIndex+1} - {date}
              </TableCell>
            
            </TableRow>
          <TableRow>
            <TableCell>Time</TableCell>
            <TableCell>Location</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {dayData.map((dayRow) => (
            <TableRow
              key={dayRow.time}
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >
              <TableCell>{dayRow.time}</TableCell>
              <TableCell component="th" scope="row">
                {dayRow.name} - {dayRow.address}
              </TableCell>
              
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}


const Itinerary = () => {
    return(
        <div className="pg-content" id="itinerary-pg">
            <div className="itinerary-title-wrapper"><h1>Itinerary</h1></div>
            
            {Object.entries(itineraryData).map(([key, value], index) => (
              <Day dayIndex={index} date={key} dayData={value}/>
      ))}

            

        </div>
    )
};

export default Itinerary;