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

- `GET /` - Home page with market overview  
- `GET /details?zipcode=15239` - Detailed market analysis for zipcode  
- `GET /api/details?zipcode=15239` - JSON response with market data  

# Deployment

This app is deployed on Railway:  

- **Live:** [alleghanyhouses.up.railway.app](https://alleghanyhouses.up.railway.app)  
- Auto-deploys from the main branch on GitHub  

# Requirements

See `requirements.txt` for full list. Key packages:  

- Flask 3.1.2  
- Matplotlib 3.10.8  
- Plotly 6.5.2  
- Gunicorn 25.0.2  

# License

MIT License - feel free to use for personal or educational projects  

# Author

Nicolas Fiore - [GitHub](https://github.com/nicolas-fiore)
