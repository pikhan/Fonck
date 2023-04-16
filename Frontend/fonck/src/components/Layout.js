import React from "react";
import { Outlet } from "react-router-dom";
import { Link } from "react-router-dom";
import "./Layout.css";
import AccountCircleIcon from "@mui/icons-material/AccountCircle";
import logo from "../assets/ItineroLogo.png";
import { PreferencesProvider } from "../context/preferencesContext";
import { Typography } from "@mui/material";
import { UXProvider } from "../context/UXContext";
import { WebProvider } from "../context/WebContext";

const Layout = () => {
  return (
    
      <UXProvider>
        <PreferencesProvider>
        <WebProvider>
        <main>
          <nav className="nav-el">
            <ul>
              <li className="logo-item">
                <Link to="/Home">
                  <img src={logo} alt="Itinero logo" className="logo-img" />
                </Link>
              </li>
              <li className="itinerary-item">
                <Link to="/BuildItinerary">
                  <button className="itinerary-btn">
                    <Typography variant="h6">Create Itinerary</Typography>
                  </button>
                </Link>
              </li>
              <li>
                <Link to="/Profile">
                  <AccountCircleIcon
                    className="profile-icon"
                    sx={{ fontSize: 60 }}
                    htmlColor="#00AFB9"
                  />
                </Link>
              </li>
            </ul>
          </nav>

          <div className="page-container">
            <Outlet />
          </div>

          <footer></footer>
        </main>
        </WebProvider>
      
    </PreferencesProvider>
    </UXProvider>
  );
};

export default Layout;
