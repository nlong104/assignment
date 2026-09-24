"""
weather_data.py

This file does three simple things:
1. Loads temperature and precipitation data from combined_data.csv
2. Works out which Nyoongar season each row belongs to (based on the month)
3. Gives you simple functions to get useful info back out (averages, totals)

You can import this file into your app later and just call the functions.
"""

import csv


# ---------------------------------------------------------------------------
# STEP 1: Define your seasons
# ---------------------------------------------------------------------------
# Adjust the month numbers below to match the three seasons you're using.
# Months are numbers: January = 1, February = 2, ... December = 12
# Example below uses three of the six Nyoongar seasons - change as needed.

SEASON_MONTHS = {
    "Kambarang": [10, 11],        # October-November
    "Makuru": [6, 7],        # June-July
    "Birak": [12, 1],        # December-January
}


def get_season_for_month(month_number):
    """
    Given a month number (1-12), return which season it belongs to.
    Returns None if the month isn't in any of your three chosen seasons.
    """
    for season_name, months in SEASON_MONTHS.items():
        if month_number in months:
            return season_name
    return None


# ---------------------------------------------------------------------------
# STEP 2: Load the data from file
# ---------------------------------------------------------------------------

def load_weather_data(filepath):
    """
    Reads combined_data.csv and returns a list of dictionaries, one per row.

    Expected columns: year, month, temperature, precipitation
    """
    records = []

    with open(filepath, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            try:
                year = int(row["Year"])
                month = int(row["Month"])
                temperature = float(row["Temperature"])
                precipitation = float(row["Precipitation"])

                record = {
                    "Year": year,
                    "Month": month,
                    "season": get_season_for_month(month),
                    "Temperature": temperature,
                    "Precipitation": precipitation,
                }
                records.append(record)

            except (ValueError, KeyError):
                # If a row is badly formatted or has missing/text values,
                # skip it rather than crashing the whole app
                continue

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
    season_records = [r for r in records if r["season"] == season_name]

    if not season_records:
        return None  # no data for this season - handle this in your app!

    total_records = len(season_records)
    avg_temp = sum(r["Temperature"] for r in season_records) / total_records
    avg_precip = sum(r["Precipitation"] for r in season_records) / total_records

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