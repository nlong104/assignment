# what should be in the ai log
What you asked the AI to do
What it produced, and which tool you used
What you kept or changed
How you verified it, since the rubric asks for verification of AI output

## Entry 1: Automated tests
**Tool:** Claude
**Date:** 4 Oct 2026
**What I asked:** Help planning automated tests for the code that switches screens and the data processing.
**What the AI produced:** A set of 5 JavaScript tests and 4 Python tests, plus an `assertEqual` helper.
**What I used / changed:** Used the tests, replaced Test 9 (it tested color logic that didn't end up in the final chart), and added Test 10 for invalid input.
**How I verified it:** Ran `tests.html` and `test_data.py` and checked all tests passed. Found that Test 9 didn't match my code anymore and rewrote it to match the final version.

## Entry 2: Weather data loading and season summaries
**Tool:** Claude
**Date:** 26 Sep 2026
**What I asked:** Help writing code to load temperature and precipitation data from `combined_data.csv` and work out average values for each Nyoongar season.
**What the AI produced:** A Python script with code that loads the CSV, matches each month to a season, and calculates average temperature and precipitation for each season.
**What I used / changed:** Used the structure and functions, but changed the seasons to Kambarang, Makuru and Birak, and changed the column names to match my file (`Year`, `Month`, `Temperature`, `Precipitation`). 
**How I verified it:** Ran `python weather_data.py` and checked that the number of rows loaded matched the CSV file


# Entry 3: Creating charts
**Tool:** Claude
**Date:** 30 Sep 2026
**What I asked:** How how to fix problems with chart sizing and alignment, and how polish a simpel chart.
**What the AI produced:** The basic pandas and matplotlib approach (grouping the data by month, taking the mean, and plotting a line chart and a bar chart), plus labelling the months and positioning the plot area.
**What I wrote or changed myself:** Chose the colours and fonts so that the plots matched the application and blended seemlessly into the background, wrote the titles and axis labels, and adapted the code to the `combined_data.py` dataset.
**Problem found and fixed:** The two charts didn't line up when shown side by side. Using `tight_layout()` together with `subplots_adjust()` overrode my manual margins, so I removed `tight_layout()` and kept the fixed margins.
**How I verified it:** I opened the saved images to check all 12 months appeared and the axes were labelled correctly, and checked they displayed side by side in the app. Test 9 in `test_data.py` also confirms the monthly grouping produces exactly 12 entries.

# Entry 4: Combining CSV data
**Tool:** Claude 
**Date:** 25 Sep 2026
**What I asked"** How to combine two datasets with the same headings into on dataset.
**What the AI produced:** Code used to combine two datasets, code to check it has combined correctly and to created a CSV file called `combined_data.py`.
**How I verified it:** Checked that the combined data lined up with the each of the individual sets to know that it was combined correctly.




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

