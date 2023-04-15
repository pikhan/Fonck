import React from 'react';
import logo from './logo.svg';
import './App.css';
import {Routes, Route } from 'react-router-dom';
import Layout from "./components/Layout";
import Home from "./pages/Home/Home";
import Profile from "./pages/Profile/Profile";
import BuildItinerary from "./pages/BuildItinerary/BuildItinerary";

function App() {
  return (
    <div className="App">
        <Routes>
            <Route path="/" element={<Layout/>}> 
              <Route index path="Home" element={<Home/>}/>       
              <Route path="BuildItinerary" element={<BuildItinerary/>}/> 
              <Route path="Profile" element={<Profile/>}/>
            </Route>
        </Routes>
    </div>
  );
}

export default App;
