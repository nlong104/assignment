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

# for the map inclusion in the home page

.map-source {
    font-size: 0.8rem;
}

  </div>
    <section class="map-section" aria-labelledby="map-heading">
        <div class="map-intro">
            <h2 id="map-heading">The Noongar Regions enclosed in our study area</h2>
            <p>These maps show the Whadjuk Noongar and Gnaala Karla Booja regions. These are the regions owned by the Indigenous people of Australia in which our activity areas are located (Hillarys to Rockingham).</p>
        </div>
        <div class="map-row">
            <figure>
              <img src="images/whadjuk%20noongar%20map.png" alt="Map showing Whadjuk Country around Perth">
              <figcaption>Whadjuk Noongar Area Map</figcaption>
            </figure>
            <figure>
              <img src="images/G.K.B%20noongar%20map.png" alt="Map showing the broader Noongar region in south-western Western Australia">
              <figcaption>Gnaala Karla Booja Noongar Map</figcaption>
            </figure>
        </div>
                <p class="map-source">Source: https://www.wa.gov.au/government/publications/maps-of-noongar-native-title-agreement-groups-the-settlement</p>

    </section>