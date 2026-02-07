# Description
Mostly made this for some experience with pandas and backend development with flask and python

I did use ai for some of the colors and *aesthetic cause I dont know color theory and Im not trying to get a frontend job! Did write the intial css though

I would like to do more with this but spent way too much time on it a lot of it learning new stuff but would like to start something new 

Hopefully this is a good starting place


- **Website Live:** [alleghanyhouses.up.railway.app](https://alleghanyhouses.up.railway.app) 


# House Prices in Alleghany Country
<h5>Data taken from the Westren Pennsylvania Regional Data Center</h5>

Dataset found [here](https://data.wprdc.org/dataset/property-assessments)
 
# Alleghany Houses

A Flask web application that visualizes real estate market data for Pittsburgh-area zipcodes (2000-2025).

## Features

- **Interactive Market Dashboard** - Explore housing data across 114 Western Pennsylvania zipcodes
- **Price & Volume Analysis** - Dual-axis charts showing median prices and houses sold over 25 years
- **Bedroom Distribution** - Pie charts breaking down available listings by bedroom count
- **Market Statistics** - Average prices, price per sq ft, and annual transaction volume
- **Responsive Design** - Clean, dark-themed interface optimized for all devices

## Tech Stack

- **Backend:** Flask (Python)
- **Database:** SQLite (zipcodes.db with 2,850 records)
- **Visualization:** Matplotlib, Plotly
- **Frontend:** Jinja2 templates, CSS
- **Deployment:** Railway

# API Endpoints

- `GET /` 
- `GET /details?zipcode=15239` 
- `GET /api/details?zipcode=15239` 






