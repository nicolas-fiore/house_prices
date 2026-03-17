# Description

Self taught flask, pandas, matplotlib, and ploty, and sqlite for this personal project

Mostly made this for some experience with pandas and backend development with flask and python

My css skills arent the best but I didnt want to spend too much time learning how to create a pretty website as I would rather spend time learning something else.

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


# Website Photos

<img width="1889" height="897" alt="Screenshot 2026-03-17 142519" src="https://github.com/user-attachments/assets/c9c2ae3b-1777-40bd-9aa9-49f2acce5fb5" />

# route: /details?zipcode=15239
<img width="1889" height="904" alt="Screenshot 2026-03-17 142555" src="https://github.com/user-attachments/assets/50518a5b-7e49-45a8-964e-4a2797c268e5" />


<img width="1885" height="902" alt="Screenshot 2026-03-17 142602" src="https://github.com/user-attachments/assets/6b34aafe-b386-4975-b9c6-6a6253952977" />

# route: /api/details?zipcode=15239
<img width="1665" height="634" alt="Screenshot 2026-03-17 142607" src="https://github.com/user-attachments/assets/c648d2b7-f118-49e5-ac37-a049f5143325" />



