CREATE TABLE IF NOT EXISTS zipcodes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    'year' TEXT NOT NULL,
    zipcode TEXT NOT NULL,
    houses_sold INT,
    median_price INT,
    mean_price INT,
    price_per_sqrft INT,
    total_volume INT,
    bedrooms_1 INT, 
    bedrooms_2 INT,
    bedrooms_3 INT, 
    bedrooms_over_3 INT,
    CONSTRAINT uq_zipcodes UNIQUE ('year', zipcode)
)
