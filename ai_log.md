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


combining_data.py:

# for the frontend button change:
/* ...existing code... */
.screen:not(#home) button {
  border-color: navy;
  color: navy;
}
/* ...existing code... */

# to add images to the border of the whole application
/* Full-page decorative borders */
body::before,
body::after {
    content: "";
    position: fixed;
    top: 0;
    bottom: 0;
    width: 65px;

    background: url("images/Border-image.jpg") center / cover no-repeat;

    pointer-events: none;
    z-index: 10;
}

/* Left border */
body::before {
    left: 0;
}

/* Right border */
body::after {
    right: 0;
}