import React from 'react';
import lightLogo from '../../assets/LightItineroLogo.png';
import { Link } from 'react-router-dom';
import "./Home.css";

const Home = () => {

  
    return (
      <main id="home-hero-img">
        <div className="header-content">
          <img src={lightLogo}/>
          <h1>
            Plan your next vacation with ease!
          </h1>
          <Link to="/BuildItinerary"><button id="run-away-btn">
            Run away today!
          </button></Link>
          </div>
      </main>
    );
  };

export default Home;