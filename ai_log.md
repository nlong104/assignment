
# weather_data.py:
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

# automated tests 
// reusable assertion function for testing that compares actual and expected values and logs the result
    function assertEqual(actual, expected, testName) {
      if (actual === expected) {
        console.log(`PASS: ${testName}`);
      } else {
        console.log(`FAIL: ${testName} — expected ${expected}, got ${actual}`);
      }
    }

    // Test 1: Home screen is active by default - tests whether the home div has the 'active' class when the page loads
    showScreen('home');
    assertEqual(document.getElementById('home').classList.contains('active'), true, 'home screen is active by default');

    // Test 2: Switching to a valid screen activates it - tests whether the birak div has the 'active' class after calling showScreen('birak')
    showScreen('birak');
    assertEqual(document.getElementById('birak').classList.contains('active'), true, 'birak becomes active when selected');

    // Test 3: Switching away removes the old active class - tests whether the birak div loses the 'active' class after switching to kambarang
    showScreen('kambarang');
    assertEqual(document.getElementById('birak').classList.contains('active'), false, 'birak loses active when switching to kambarang');

    // Test 4: Only one screen is ever active at a time - tests whether only one div has the 'active' class after switching to makuru
    showScreen('makuru');
    const activeScreens = document.querySelectorAll('.screen.active');
    assertEqual(activeScreens.length, 1, 'exactly one screen is active at a time');

    // Test 5: An invalid season id doesn't crash the app - tests whether calling showScreen with an invalid id throws an error or not
    try {
    showScreen('doesnotexist');
    assertEqual(true, true, 'invalid id does not crash the app');
    } catch (e) {
    assertEqual(false, true, 'invalid id does not crash the app');
    }

    showScreen('home'); // reset back to home after testing

    # Test 6: Birak filter only includes Dec/Jan rows - checks that the birak_data DataFrame only contains rows where the Month is either 12 (December) or 1 (January)
    birak_data = data[data["Month"].isin([12, 1])]
    only_birak_months = birak_data["Month"].isin([12, 1]).all()
    assert_equal(only_birak_months, True, "Birak filter only contains Dec/Jan rows")

    # Test 7: Season_Year correctly pairs Dec with the following Jan - shows that the Season_Year for December 1994 is the same as for January 1995, confirming that the season year is correctly assigned across the year boundary
    dec_1994_year = data[(data["Year"] == 1994) & (data["Month"] == 12)]["Season_Year"].iloc[0]
    jan_1995_year = data[(data["Year"] == 1995) & (data["Month"] == 1)]["Season_Year"].iloc[0]
    assert_equal(dec_1994_year, jan_1995_year, "Dec 1994 and Jan 1995 share the same Season_Year")

    # Test 8: Averaging calculation matches a hand-checked value - checks that the average of 20 and 30 is correctly calculated as 25 by the average_metric function, so that we know the function is working correctly
    sample_data = pd.DataFrame({"Temperature": [20, 30]})
    assert_equal(average_metric(sample_data, "Temperature"), 25, "average_metric() correctly averages 20 and 30 to 25")

    # Test 9: Color list length always matches bar count - checks that the length of the colors list is equal to the number of months (12), ensuring that there is a color assigned for each month in the chart
    month_names = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    season_lookup = data.groupby("Month")["Season"].first()
    colors = ["#BBBBBB" if season_lookup[m] == "Other" else "#23406B" for m in range(1, 13)]
    assert_equal(len(colors), len(month_names), "color list has exactly one entry per month")

    # Test 10: Filtering for a season that doesn't exist returns empty, doesn't crash - checks that filtering the data for a season name that doesn't exist ("NotARealSeason") returns an empty DataFrame, confirming that the filtering logic handles invalid season names gracefully without crashing
    missing_season_data = data[data["Season"] == "NotARealSeason"]
    assert_equal(len(missing_season_data), 0, "filtering an invalid season name returns an empty result, not a crash")