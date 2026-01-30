import sqlite3
import json

#Database ranges from 2000-01-01 to 2025-12-31
#id's up to 2964
#Database complies very fast /NOTE
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

        c.execute("""INSERT OR IGNORE INTO zipcodes (year, zipcode, houses_sold, median_price, mean_price, price_per_sqrft, total_volume, bedrooms_1, bedrooms_2, bedrooms_3, bedrooms_over_3) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
                ,(year, z, *v.values()))
        
con.commit()
test = c.execute("SELECT COUNT(id) FROM zipcodes").fetchone()
print(f"if {[i for i in test]} == 2964, we chillin!")

con.close()



