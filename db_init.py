import sqlite3
import json

#Database ranges from 2000-01-01 to 2025-12-31
con = sqlite3.connect("zipcodes.db")

with open ('schema.sql') as f: 
    con.executescript(f.read())

with open ('house_prices.json') as j: 
    data_dict = json.load(j)

con.row_factory = sqlite3.Row
c = con.cursor()
for year, data in data_dict.items():

    print(f"{year}---{data} END")
    for z, v in data.items(): 
        print(f"{z} - THIS IS V: {v.items()}")

        c.execute("""INSERT INTO zipcodes (year, zipcode, houses_sold, median_price, mean_price, price_per_sqrft, total_volume) 
                VALUES (?, ?, ?, ?, ?, ?, ?)"""
                ,(year, z, *v.values()))
        

con.commit()
con.close()



