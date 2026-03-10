# Description
Mostly made this for some experience with pandas and backend development with flask and python

My css skills arent the best but I didnt want to spend too much time learning how to create a pretty website as I would rather spend time learning something else.

I would like to do more with this but spent way too much time on it a lot of it learning new stuff but would like to start something new 

Hopefully this is a good starting place

**IMPORTANT: Changed the hosting from railway to render beacuse railway only offers 30 day free trial
This is only temporary for now as the website runs very slowly BUT STILL WORKS** 
- **Website Live:** [house-prices-cwyv.onrender.com](https://house-prices-cwyv.onrender.com/)


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
- **Deployment:** Render (was railway) 

# API Endpoints

- `GET /` 
- `GET /details?zipcode=15239` 
- `GET /api/details?zipcode=15239` 






