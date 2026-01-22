import sqlite3, json, jsonify
import matplotlib.pyplot as plt 
from graph import house_x_median
from matplotlib.figure import Figure
import base64
from io import BytesIO

import numpy as np
from flask import Flask, request, redirect, render_template

app = Flask(__name__)

ZIPCODES = ['15003', '15005', '15006', '15007', '15014', '15015', '15017', '15018', '15020', '15024', 
            '15025', '15026', '15028', '15030', '15031', '15034', '15035', '15037', '15044', '15045', 
            '15046', '15047', '15049', '15051', '15056', '15057', '15063', '15064', '15065', '15068', 
            '15071', '15075', '15076', '15082', '15083', '15084', '15085', '15086', '15088', '15089', 
            '15090', '15101', '15102', '15104', '15106', '15108', '15110', '15112', '15116', '15120', 
            '15122', '15126', '15129', '15131', '15132', '15133', '15135', '15136', '15137', '15139', 
            '15140', '15142', '15143', '15144', '15145', '15146', '15147', '15148', '15201', '15202', 
            '15203', '15204', '15205', '15206', '15207', '15208', '15209', '15210', '15211', '15212', 
            '15213', '15214', '15215', '15216', '15217', '15218', '15219', '15220', '15221', '15222', 
            '15223', '15224', '15225', '15226', '15227', '15228', '15229', '15232', '15233', '15234', 
            '15235', '15236', '15237', '15238', '15239', '15241', '15243', '15321', '15332', '15642', 
            '15668', '16046', '16059', '16229']


def get_db(): 
    con = sqlite3.connect("zipcodes.db")
    con.row_factory = sqlite3.Row
    return con


with open ('house_prices.json') as j: 
    data_dict = json.load(j)
    
y= []
for i in data_dict.values(): 
    x = []
    for j in i.values(): 
        x.append(j['median_price'])
    y.append(x)



@app.route('/')
def index(): 
    return render_template('index.html',zipcodes=ZIPCODES)


@app.route('/test', methods=['POST'])
def graph():

    #get zipcode
    zipcode = request.form.get('zipcode')
    if zipcode not in ZIPCODES: 
        return render_template('error.html')
    
    #connect db
    con = get_db()
    c = con.cursor()

    #fetch houses_sold and median_price from entered zipcode
    x1 = c.execute("SELECT houses_sold FROM zipcodes WHERE zipcode == ?", (zipcode,)).fetchall() 
    x2 = c.execute("SELECT median_price FROM zipcodes WHERE zipcode == ?", (zipcode,)).fetchall() 
    info = c.execute("SELECT AVG(mean_price), AVG(price_per_sqrft) FROM zipcodes WHERE zipcode == ?", (zipcode,)).fetchone()
    con.close()
    
    #assign houses_sold to (x1) and median_price to (x2)
    x1 = [i[0] for i in x1]
    x2 = [j[0] for j in x2]
    graph = house_x_median(x1, x2, zipcode)
    for value in info: 
        print(value)
    
    print(list(zip(x1, x2)))
    return render_template('test.html', graph=graph, info=info)
