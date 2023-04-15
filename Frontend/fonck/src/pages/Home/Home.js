import React from 'react';
import beachImage from '../../assets/beach.png';

const Home = () => {
    const backgroundStyle = {
      backgroundImage: `url(${beachImage})`,
      backgroundSize: "cover",
      height: "100vh",
      position: "relative",
    };
  
    const textStyle = {
      position: "absolute",
      top: "50%",
      left: "50%",
      transform: "translate(-50%, -50%)",
      textAlign: "center",
      color: "white",
      textShadow: "0 0 10px black",
    };
  
    return (
      <div style={backgroundStyle}>
        <div style={textStyle}>
          <h1 style={{ fontSize: "4rem" }}>itinero</h1>
          <h3 style={{ fontSize: "2rem" }}>
            Plan your next vacation with ease!
          </h3>
          <button style={{ fontSize: "1.5rem", padding: "1rem 2rem" }}>
            Run away today!
          </button>
        </div>
      </div>
    );
  };

export default Home;