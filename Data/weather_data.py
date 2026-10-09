
import csv

# Defining the seasons
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
    return None  # If we reach this line, no season matched this month


# Loading the data from combined data file
def load_weather_data(filepath):
    """
    Reads combined_data.csv and returns a list of dictionaries, one per row.

    Expected columns: Year, Month, Temperature, Precipitation
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
                continue
    return records



# Analysing the data 
def get_season_summary(records, season_name):
    season_records = [r for r in records if r["season"] == season_name]
    if not season_records:
        return None  
    total_records = len(season_records)
    avg_temp = sum(r["Temperature"] for r in season_records) / total_records
    avg_precip = sum(r["Precipitation"] for r in season_records) / total_records
    # round(x, 1) rounds a number to 1 decimal place
    return {
        "season": season_name,
        "records_count": total_records,
        "average_temperature": round(avg_temp, 1),
        "average_precipitation": round(avg_precip, 1),
    }


def get_all_season_summaries(records):
    return [
        get_season_summary(records, season)

        for season in SEASON_MONTHS
        if get_season_summary(records, season) is not None
    ]



# Checking that it all works by running the script directly
if __name__ == "__main__":
    data = load_weather_data("combined_data.csv")

    print(f"Loaded {len(data)} rows of data.\n")

    for summary in get_all_season_summaries(data):
        print(summary)