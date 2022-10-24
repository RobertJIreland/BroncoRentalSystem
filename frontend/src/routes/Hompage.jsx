// IMPORTS
import React from "react";
import hero2 from '../images/hero2.jpg';

//Material UI IMPORTS
import Grid from "@mui/material/Grid";

// COMPONENT IMPORTS
import Navbar from "../components/Navbar";
import VehicleSearch from "../components/VehicleSearch";


export default function Homepage() {
  return (
    <>
      <Navbar />
      <Grid container
        sx={{
          justifyContent: 'center',
          alignItems: 'center',
        }}>
        <img className="jumbotron" src={hero2} />
      <Grid item
        sx={{
          zIndex: 1,
          position: 'absolute',
          marginTop: 30
        }}>
        <VehicleSearch />
      </Grid>
      </Grid>
    </>
  );
}


