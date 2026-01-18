CREATE TABLE IF NOT EXISTS zipcodes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    'year' TEXT NOT NULL,
    zipcode TEXT NOT NULL,
    houses_sold INT,
    median_price INT,
    mean_price INT,
    price_per_sqrft INT,
    total_volume INT,
    CONSTRAINT uq_zipcodes UNIQUE ('year', zipcode)
)
