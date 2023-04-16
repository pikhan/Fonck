import React from 'react';
import "./Profile.css"
import { Box, Typography } from "@mui/material";
import AccountCircleIcon from "@mui/icons-material/AccountCircle";


const Profile = () => {
    return(
        <Box className="bg-container" id="create-pg">
            <Box className="profile-container">
                <Box className="profile-info">
                    <Box sx={{}}>
                        <Typography variant="h1" sx={{fontSize: '50px'}}> Hello World</Typography>
                        <AccountCircleIcon className="profile-icon" sx={{fontSize:''}}/>
                    </Box>
                    <Typography> </Typography>
                    <Typography> </Typography>
                    
                </Box>
                <div className="inner-profile-container">
                    <Box className="user-pref"></Box>
                    <Box className="user-itineraries"></Box>
                </div>
            </Box>
        </Box>
        
    );
};

export default Profile;