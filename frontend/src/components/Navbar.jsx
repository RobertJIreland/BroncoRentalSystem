// Imports
import React from 'react';
import {Link} from 'react-router-dom';
import Login from './Login'

// Material.UI Imports
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Grid from '@mui/material/Grid'
import Paper from '@mui/material/Paper'
import Appbar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import AppBar from '@mui/material/AppBar';
import CarRentalIcon from '@mui/icons-material/CarRental';


export default function Navbar () {
       return (
        <Grid container 
            sx={{
                alignItems: 'center',
            }}>
        <Grid item>
        <Box
        sx={{
            flexgrow: 1,
            boxShadow: 1,
            width: '100vw',
        }}>
            <AppBar 
            position='static'
            elevation={24}
            square={false}
            sx={{
            backgroundColor: '#255dcc',
            borderBottomLeftRadius: 5,
            borderBottomRightRadius: 5,
            }}>
                <Toolbar>
                    <CarRentalIcon 
                    sx={{
                        fontSize: 50,
                    }}/>
                    <Typography
                    className='logo-title'
                    variant='h1'
                    component='div'
                    sx={{
                        flexGrow: 1,
                        fontSize: 50,
                    }}>
                        <Link to='/'
                        style={{
                            textDecoration: 'none',
                            color: 'white',
                            backgroundColor: null,
                        }}>
                            Bronco Rental System
                        </Link>
                    </Typography>
                    <Login />
                </Toolbar>
            </AppBar>
        </Box>
        </Grid>
        </Grid>
       )
}

