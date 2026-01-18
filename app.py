import json
import sqlite3
import matplotlib.pyplot as plt 

from matplotlib.figure import Figure
import base64
from io import BytesIO

import numpy as np
from flask import Flask, request, redirect, render_template

app = Flask(__name__)

def get_db(): 
    con = sqlite3.connect("zipcodes.db")
    con.row_factory = sqlite3.Row
    return con


with open ('house_prices.json') as j: 
    data_dict = json.load(j)


@app.route('/')
def index(): 
    con = get_db()
    c = con.cursor()
    rows = c.execute("SELECT DISTINCT(zipcode) FROM zipcodes").fetchall()
    zipcodes = [row[0] for row in rows]
    con.close()
    return render_template('index.html',zipcodes=zipcodes)


@app.route('/test', methods=['POST'])
def graph():
    zipcode = request.form.get('zipcode')
    con = get_db()
    c = con.cursor()
    rows = c.execute("SELECT median_price FROM zipcodes WHERE zipcode == ?", (zipcode,)).fetchall() 
    con.close()
    median_price = [row[0] for row in rows]
    print(median_price)
    return render_template('test.html', median_price=median_price)







# zipcode = input("Enter Zip: ")


# c.execute(query)
# rows = c.fetchall()



#114 zips per year


# rows = [row[0] for row in rows]

# x = np.arange(2000, 2026)
# h = zip(x, rows)
# print(tuple(h))
# plt.bar(x, rows)
# plt.xlabel("Years")
# plt.show()