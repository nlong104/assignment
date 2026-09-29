import pandas as pd

# Load the BOM dataset
data = pd.read_csv("combined_data.csv")

# Assign the Noongar season
def assign_season(month):
    if month == 12 or month == 1:
        return "Birak"
    elif month == 6 or month == 7:
        return "Makuru"
    elif month == 10 or month == 11:
        return "Kambarang"
    else:
        return "Other"

data["Season"] = data["Month"].apply(assign_season)

# Create the season year
def get_season_year(row):
    if row["Season"] == "Birak":
        if row["Month"] == 12:
            return f"{row['Year']}-{str(row['Year'] + 1)[-2:]}"
        elif row["Month"] == 1:
            return f"{row['Year'] - 1}-{str(row['Year'])[-2:]}"
    else:
        return str(row["Year"])

data["Season_Year"] = data.apply(get_season_year, axis=1)

# Update the CURRENT CSV file
data.to_csv("combined_data.csv", index=False)

print("BOM data successfully updated!")