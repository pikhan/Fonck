import React from 'react';
import lightLogo from '../../assets/LightItineroLogo.png';
import { Link } from 'react-router-dom';
import "./Home.css";
import { useContext, useState } from "react";
import { WebContext } from "../../context/WebContext";

const Home = () => {

  const [popUp, setPopUp] = useContext(WebContext);

    return (
      <main id="home-hero-img">
        <div className="header-content">
          <img src={lightLogo}/>
          <h1>
            Plan your next vacation with ease!
          </h1>
          <Link to="/BuildItinerary"><button onClick={setPopUp(true)} id="run-away-btn">
            Run away today!
          </button></Link>
          </div>
      </main>
    );
  };

export default Home;