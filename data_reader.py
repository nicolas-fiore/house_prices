import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import json, re

#//zip code
#//price
#//data of sale 
#TODO: linaer regression the point is to predict house prices
#//CLASS[R] - for residential only
#//NEED [01-01-2025] - [12-31-2025] dates just for grpah 
#TODO: sq foot per area {price \ sqft} FINISHEDLIVINGAREA
#TODO: get median
#TODO: maybe group zip code with how many bedrooms


# pd.set_option('display.max_rows', None)
# df = pd.read_csv("houses_test.csv")
df = pd.read_csv("houses.csv")




match = r"([0-9][0-9]|[0-9])-([0-9][0-9]|[0-9])-2025"
clean = df[df["SALEDATE"].str.contains(match, regex=True, na=False)]
clean = clean.loc[(clean["SALEDESC"] == "VALID SALE") & (clean["CLASS"] == "R")]
clean = clean[["PROPERTYZIP", "SALEPRICE", "CLASS", "FAIRMARKETTOTAL", "PREVSALEPRICE", "SALEDESC", "SALEDATE", "FINISHEDLIVINGAREA", "BEDROOMS", "PROPERTYADDRESS" ]].dropna()

clean["PROPERTYZIP"] = clean["PROPERTYZIP"].astype('Int64').astype('str')
filterd = clean[clean["SALEPRICE"] > 0]
clean["SALEPRICE"] = clean["SALEPRICE"].astype('Int64')

print(clean)



zipcodes = {}
for zip in clean["PROPERTYZIP"]: 
    if zip in zipcodes: 
        zipcodes[zip] += 1
    else: 
        zipcodes[zip] = 1 
print("")
print(f"ZIPCODE DICT:\n-------------\n{zipcodes}")




#overall total
def overall(): 
    total_price = clean["SALEPRICE"].sum()
    count = clean["SALEPRICE"].count()
    mean = total_price / count
    print("--------------------------------------")
    print(f"Total amount of houses: {count:,}")
    print(f"Sum of all sale prices: ${total_price:,}")
    print(f"Mean: {mean:,.3f}")
    print("--------------------------------------")



#test total for one zip code only
#exmaple {15222: total, mean}
#if (zip == propzip):total =+ saleprice
price_dict = {} 
for zip in zipcodes:
    tmp = clean.loc[clean["PROPERTYZIP"] == zip]
    total, count = tmp["SALEPRICE"].sum(), tmp["SALEPRICE"].count()
    price_dict[zip] = {"count": int(count), "mean_price": int(total / count), "total_volume": int(total)}
print(price_dict)





with open("house_prices.json", "w") as j: 
    j.write(json.dumps(price_dict, indent=4))


overall()








from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route("/")
def index(): 
    return render_template("index.html", df2=clean)



