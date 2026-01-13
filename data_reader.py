import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import json, re, sys

#//zip code
#//price
#//data of sale 
#TODO: linaer regression the point is to predict house prices
#//CLASS[R] - for residential only
#//NEED [01-01-2025] - [12-31-2025] dates just for grpah 
#///TODO: sq foot per area {price \ sqft} FINISHEDLIVINGAREA
#///TODO: get median
#TODO: user asks for 1 - 20 compare zip and makes chart (maybe)
#TODO: maybe group zip code with how many bedrooms
#TODO: factor in previous sale price to see if zipcodes have "fell off" or vice versa (maybe)
#///TODO: make a sql table

# pd.set_option('display.max_rows', None)
# df = pd.read_csv("houses_test.csv")
df = pd.read_csv("houses.csv")


df['SALEDATE'] = pd.to_datetime(df['SALEDATE'])
df = df.loc[(df['SALEDATE'] >= '2023-01-01') & (df['SALEDATE'] <= '2025-12-31')]

df = df.loc[(df['SALEDESC'] == "VALID SALE") & (df['CLASS'] == 'R')]
df = df[['PROPERTYZIP', 'SALEPRICE', 'CLASS', 'FAIRMARKETTOTAL', 'PREVSALEPRICE', 'SALEDESC', 'SALEDATE', 'FINISHEDLIVINGAREA', 'BEDROOMS', 'PROPERTYADDRESS' ]].dropna()


df['PROPERTYZIP'] = df['PROPERTYZIP'].astype('Int64').astype('str')
df['SALEPRICE'] = df['SALEPRICE'].astype('Int64')
print(df)



#overall total
def print_overall(): 
    total_price = df['SALEPRICE'].sum()
    count = df['SALEPRICE'].count()
    mean = total_price / count
    print("--------------------------------------")
    print(f"Total amount of houses: {count:,}")
    print(f"Sum of all sale prices: ${total_price:,}")
    print(f"Median: ${int(df['SALEPRICE'].median()):,}")
    print(f"Mean: ${mean:,.3f}")
    print(f"Price/Sqft: ${total_price / df['FINISHEDLIVINGAREA'].sum():,.3f}")
    print("--------------------------------------")




zipcodes = df['PROPERTYZIP'].value_counts().to_dict()
# print(f"\nZIPCODE DICT:\n-------------\n{zipcodes}")
years = df['SALEDATE'].dt.year.value_counts().to_dict()
years = dict(sorted(years.items()))
print(json.dumps(years, indent=4))



price_dict = {} 
for year in years: 
    price_dict[year] = {}
    for zip in zipcodes:
        tmp = df.loc[(df['SALEDATE'].dt.year == year) &(df['PROPERTYZIP'] == zip)]
    
        if tmp['SALEPRICE'].count() == 0: 
            price_dict[year][zip] ={
           
                "houses_sold": 0, 
                "median_price:": 0, 
                "mean_price": 0, 
                "price_per_sqrft": 0, 
                "total_volume": 0
            }
            continue    

        total,count, median  = tmp['SALEPRICE'].sum(), tmp['SALEPRICE'].count(), tmp['SALEPRICE'].median()
        sqrft = total / tmp['FINISHEDLIVINGAREA'].sum()
       
        price_dict[year][zip] ={
           
                "houses_sold": int(count), 
                "median_price:": int(median), 
                "mean_price": int(total / count), 
                "price_per_sqrft":int(sqrft), 
                "total_volume": int(total)
            }     



with open("house_prices.json", "w") as j: 
    j.write(json.dumps(price_dict, indent=4))

#?print(price_dict[2025]["15239"]) acces the dict

# y = [price_dict[2025]["15239"]["mean_price"], price_dict[2024]["15239"]["mean_price"]]
# x = ["2025", "2024"]
# plt.bar(x, y)
# plt.yticks(np.arange(250000,280000,1000))
# print(2025,price_dict[2025]["15239"]["mean_price"])
# plt.show()
print_overall()




from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route("/")
def index(): 
    return render_template("index.html", df2=df)


