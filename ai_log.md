weather_data.py:
    Loads weather data from a CSV, tags each row with a Nyoongar season, and gives you simple summary stats (avg temperature, avg precipitation) per season.

    Input file
        combined_data.csv needs these columns: Year, Month, Temperature, Precipitation. Bad or missing rows are skipped automatically.
    Seasons mapped
        Season	Months
            Kambarang	Oct, Nov
            Makuru	Jun, Jul
            Birak	Dec, Jan
    Functions
        load_weather_data(filepath) — reads the CSV, returns a list of row dictionaries (each tagged with its season).
        get_season_summary(records, season_name) — returns avg temp, avg precipitation, and record count for one season.
        get_all_season_summaries(records) — same, but for every mapped season.
