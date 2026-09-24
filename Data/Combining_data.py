# Import pandas so we can work with the CSV data
import pandas as pd


# Load the temperature dataset from the data folder
temperature = pd.read_csv("data/monthly temperature.csv")

# Load the precipitation dataset from the data folder
precipitation = pd.read_csv("data/monthly precipitation.csv")


# Print the first 5 rows of the temperature dataset
# This lets us check that the file has loaded correctly
print("Temperature data:")
print(temperature.head())


# Print the first 5 rows of the precipitation dataset
# This lets us check that the file has loaded correctly
print("\nPrecipitation data:")
print(precipitation.head())


# Select only the columns we need from the temperature dataset
# We don't need the product code, station number or quality columns
# Year and Month will be used to match the two datasets
temperature = temperature[
    ["Year", "Month", "Mean maximum temperature (°C)"]
]


# Select only the columns we need from the precipitation dataset
# We don't need the product code, station number or quality columns
# Year and Month will be used to match the two datasets
precipitation = precipitation[
    ["Year", "Month", "Monthly Precipitation Total (millimetres)"]
]


# Rename the temperature column to make it shorter and easier to use
# The original column name is "Mean maximum temperature (°C)"
temperature = temperature.rename(
    columns={"Mean maximum temperature (°C)": "Temperature"}
)


# Rename the precipitation column to make it shorter and easier to use
# The original column name is "Monthly Precipitation Total (millimetres)"
precipitation = precipitation.rename(
    columns={"Monthly Precipitation Total (millimetres)": "Precipitation"}
)


# Combine the temperature and precipitation datasets
# Year and Month are used to match the correct rows together
# For example, temperature data from January 1993 will be matched
# with precipitation data from January 1993
data = pd.merge(
    temperature,
    precipitation,
    on=["Year", "Month"]
)


# Print the first 5 rows of the combined dataset
# This lets us check that the two datasets have been combined correctly
print("\nCombined data:")
print(data.head())


# Print the size of the combined dataset
# The first number is the number of rows
# The second number is the number of columns
print("\nDataset size:")
print(data.shape)


# Print the names of all the columns in the combined dataset
# We should now have four columns:
# Year, Month, Temperature and Precipitation
print("\nColumn names:")
print(data.columns)

# Save the combined dataset as a new CSV file
data.to_csv("data/combined_data.csv", index=False)