import pandas as pd
import json, cpi 

df = pd.read_csv("houses.csv")

df['SALEDATE'] = pd.to_datetime(df['SALEDATE'])
df = df.loc[(df['SALEDATE'] >= '2000-01-01') & (df['SALEDATE'] <= '2025-12-31')] #year data is taken

#checks for VALID SALES AND R(residential) CLASS TYPES ONLY
df = df.loc[(df['SALEDESC'] == "VALID SALE") & (df['CLASS'] == 'R')]
df['YEAR'] = df['SALEDATE'].dt.year #creates collumn of only year
df = df[['PROPERTYZIP', 'SALEPRICE', 'SALEDESC', 'SALEDATE', 'FINISHEDLIVINGAREA', 'YEAR' ]].dropna()
df['PROPERTYZIP'] = df['PROPERTYZIP'].astype('Int64').astype('str')
df['SALEPRICE'] = df['SALEPRICE'].astype('Int64')

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


# returns a dict with changed values 
def compute_price(df):
    zipcodes = df['PROPERTYZIP'].value_counts().to_dict()
    # print(f"\nZIPCODE DICT:\n-------------\n{zipcodes}")
    years = df['SALEDATE'].dt.year.value_counts().to_dict()
    years = dict(sorted(years.items()))
    print(json.dumps(years, indent=4))

    price_dict = {} 
    for year in years: #for each year in year dict
        price_dict[year] = {}
        year_df = df.loc[(df['YEAR'] == year)] #makes copy for matching year
        
        for zip in zipcodes: #for each zip in zipcode
            tmp = year_df.loc[(year_df['PROPERTYZIP'] == zip)] #checks each value against zip
            
            #if no sold houses in that zip all values are zero
            if tmp['SALEPRICE'].count() == 0: 
                price_dict[year][zip] ={
            
                    "houses_sold": 0, 
                    "median_price": 0, 
                    "mean_price": 0, 
                    "price_per_sqrft": 0, 
                    "total_volume": 0
                }
                continue    

            print('.', end='', flush=True)

            #caluclates inflation
            inflation = cpi.inflate(tmp['SALEPRICE'], year, items='Housing')
            total,count, median  = inflation.sum(), inflation.count(), inflation.median()
            sqrft = total / tmp['FINISHEDLIVINGAREA'].sum()
        
            #converts values to ints in dict
            price_dict[year][zip] ={
            
                    "houses_sold": int(count), 
                    "median_price": int(median), 
                    "mean_price": int(total / count), 
                    "price_per_sqrft":int(sqrft), 
                    "total_volume": int(total)
                }   
        print("Year done")  
    return price_dict
    
price_dict = compute_price(df)
print()
print_overall()

#writes to json file
def write_json(price_dict):
    print("Writing JSON file!......")
    with open("house_prices.json", "w") as j: 
        j.write(json.dumps(price_dict, indent=4))
write_json(price_dict) 


