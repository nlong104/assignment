"""
weather_data.py

# This file does three simple things:
# 1. Loads temperature and precipitation data from combined_data.csv
# 2. Works out which Nyoongar season each row belongs to (based on the month)
# 3. Gives you simple functions to get useful info back out (averages, totals)

# You can import this file into your app later and just call the functions.
#

import csv


# ---------------------------------------------------------------------------
# STEP 1: Define your seasons
# ---------------------------------------------------------------------------
# This dictionary is the "key" that links calendar months to season names.

SEASON_MONTHS = {
    "Kambarang": [10, 11],        # October-November
    "Makuru": [6, 7],        # June-July
    "Birak": [12, 1],        # December-January
}


def get_season_for_month(month_number):
    """
    #Given a month number (1-12), return which season it belongs to.
    #Returns None if the month isn't in any of your three chosen seasons.    """
    for season_name, months in SEASON_MONTHS.items():
        if month_number in months:
            return season_name
    return None # If we reach this line, no season matched this month


# ---------------------------------------------------------------------------
# STEP 2: Load the data from file
# ---------------------------------------------------------------------------

def load_weather_data(filepath):
    """
    Reads combined_data.csv and returns a list of dictionaries, one per row.

    Expected columns: Year, Month, Temperature, Precipitation
    """
    records = []     # This empty list will collect every row we successfully read
# "with open(...)" opens the file and automatically closes it again
# when we're done - you don't need to worry about closing it yourself

    with open(filepath, newline="", encoding="utf-8") as f:
        # DictReader reads the CSV so each row becomes a dictionary,
        # using the column headers (Year, Month, Temperature, Precipitation)
        # as the keys. This is much easier to work with than raw text.
        reader = csv.DictReader(f)

        for row in reader: # Go through the file one row at a time
            # try/except means: "attempt this code, but if something goes
            # wrong (like a missing or broken value), don't crash the whole
            # program - just skip this one row and move to the next"
            try:
                # Convert the text from the CSV into actual numbers.
                # CSV files store everything as text by default, so we need
                # int() for whole numbers and float() for decimal numbers.
                year = int(row["Year"])
                month = int(row["Month"])
                temperature = float(row["Temperature"])
                precipitation = float(row["Precipitation"])
                # Build one clean dictionary for this row of data,
                # including which season this month belongs to
                record = {
                    "Year": year,
                    "Month": month,
                    "season": get_season_for_month(month),
                    "Temperature": temperature,
                    "Precipitation": precipitation,
                }
                records.append(record)         # Add this row's dictionary to our overall list


            except (ValueError, KeyError):
                # If a row is badly formatted or has missing/text values,
                # skip it rather than crashing the whole app
                 # ValueError = a value couldn't be converted to a number
                #              (e.g. the cell was blank or had text in it)
                # KeyError   = a column name we expected wasn't found
                # Either way, we just skip this row and keep going -
                # this is what "handles invalid input" for your data loading
                continue


    # Once every row has been processed, hand back the full list

    return records


# ---------------------------------------------------------------------------
# STEP 3: Analyse the data - simple summary stats per season
# ---------------------------------------------------------------------------

def get_season_summary(records, season_name):
    """
    Given the full list of records and a season name,
    return a dictionary of simple stats for that season:
    average temperature, average precipitation, number of records.
    """
    # This line is called a "list comprehension" - it's a compact way of
    # writing a loop. It means: "give me every record r from records,
    # but only keep the ones where r's season matches the one we want."
    season_records = [r for r in records if r["season"] == season_name]
 # If no rows matched this season, there's nothing to calculate -
    # return None so the app can handle this gracefully (e.g. show a
    # "no data available" message instead of crashing)
    if not season_records:
        return None  # no data for this season - handle this in your app!

 # How many rows of data we found for this season
    total_records = len(season_records)
     # sum(...) adds up a list of numbers.
    # Here we're pulling out just the temperature value from every record
    # in season_records, adding them all up, then dividing by the count
    # to get the average (mean).
    avg_temp = sum(r["Temperature"] for r in season_records) / total_records
    avg_precip = sum(r["Precipitation"] for r in season_records) / total_records
# round(x, 1) rounds a number to 1 decimal place, just to keep the
    # output tidy (e.g. 18.34999 becomes 18.3)
    return {
        "season": season_name,
        "records_count": total_records,
        "average_temperature": round(avg_temp, 1),
        "average_precipitation": round(avg_precip, 1),
    }


def get_all_season_summaries(records):
    """Returns a summary for every season you've defined, ready to display."""
    return [
        get_season_summary(records, season)
            # Go through each season name we defined at the top of the file

        for season in SEASON_MONTHS
        if get_season_summary(records, season) is not None
    ]


# ---------------------------------------------------------------------------
# Quick test - run this file directly to check it works
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    data = load_weather_data("combined_data.csv")

    print(f"Loaded {len(data)} rows of data.\n")

    for summary in get_all_season_summaries(data):
        print(summary)