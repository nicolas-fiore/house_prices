import sqlite3, json
from graph import house_x_median, zipcodes_x_median, piechart
import numpy as np
from flask import Flask, request, redirect, render_template

app = Flask(__name__)

def get_db(): 
    con = sqlite3.connect("zipcodes.db")
    con.row_factory = sqlite3.Row
    return con


def get_zipcodes():
    con = get_db()
    c = con.cursor()
    zipcode = c.execute("SELECT DISTINCT(zipcode) FROM zipcodes").fetchall()
    con.close()    
    zipcode = [i[0] for i in zipcode]
    return zipcode


@app.route('/')
def index(): 
    zipcodes = get_zipcodes()
    #connect db
    con = get_db()
    c = con.cursor()
    #get median prices
    median = c.execute("SELECT median_price from zipcodes").fetchall()
    con.close()
    #get 0'th item from list of tuples [..,]
    median = [i[0] for i in median]
    print("THIS IS THE Median", len(median))
    print("-----------------")
    graph = zipcodes_x_median(median, zipcodes)
    return render_template('index.html',zipcodes=zipcodes, graph=graph)




@app.route('/details')
def details():
    #get zipcode
    zipcode = request.args.get('zipcode')
    zipcodes = get_zipcodes()
    if zipcode not in zipcodes: 
        return render_template('error.html')
    
    #connect db
    con = get_db()
    c = con.cursor()

    #fetch houses_sold and median_price from entered zipcode and details
    
    rows = c.execute(
        "SELECT houses_sold, median_price, bedrooms_1, bedrooms_2, bedrooms_3, bedrooms_over_3 "
        "FROM zipcodes WHERE zipcode = ?", 
        (zipcode,)
    ).fetchall()
    
    info = c.execute(
        "SELECT AVG(mean_price), AVG(price_per_sqrft), AVG(houses_sold), AVG(total_volume) "
        "FROM zipcodes WHERE zipcode = ? AND year BETWEEN 2020 AND 2025", 
        (zipcode,)
    ).fetchone()

    con.close()
    
    x1 = [r[0] for r in rows] #houses_sold
    x2 = [r[1] for r in rows] #median_price
    bedrooms_counts = [(r[2], r[3], r[4], r[5]) for r in rows]
    
    barchart = house_x_median(x1, x2, zipcode)
    #piechart = piechart(bedroom_counts)

    print(bedrooms_counts)
    for value in info: 
        print(value)
    print('-------------------')
    print("this is data: ")
    print(list(zip(x1, x2)))
    
    return render_template('details.html', 
                           barchart=barchart, 
                           info=info,
                           display=zipcode,
                           zipcodes=zipcodes)


@app.route('/api/details')
def get_api(): 
    zipcode = request.args.get('zipcode')
    zipcodes = get_zipcodes()
    if zipcode not in zipcodes: 
        return render_template('error.html')
    
    with open ('house_prices.json') as j: 
        data_dict = json.load(j)

    zip_data = {
        year: year_dict.get(zipcode)
        for year, year_dict in data_dict.items()
    }

    return zip_data