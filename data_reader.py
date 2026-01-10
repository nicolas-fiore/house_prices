import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#zip code 
#price
#data of sale 
#linaer regression the point is to predict house prices
#CLASS[R] - for residential only

pd.set_option('display.max_rows', None)
df = pd.read_csv("houses.csv", nrows= 100)
 

zip = df["PROPERTYZIP"].astype("str")

df2 = df.loc[df["CLASS"] == "R"] 

df2 = df2[["PROPERTYZIP", "SALEPRICE", "CLASS"]].dropna()


print(df2)

# print(df[["PROPERTYZIP", "SALEPRICE"]])
# print(df["PROPERTYZIP"])





from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route("/")
def index(): 
    return render_template("index.html", df2=df2)