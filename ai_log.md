# What should be in the ai log
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


## Entry 3: Creating charts
**Tool:** Claude
**Date:** 30 Sep 2026
**What I asked:** How how to fix problems with chart sizing and alignment, and how polish a simpel chart.
**What the AI produced:** The basic pandas and matplotlib approach (grouping the data by month, taking the mean, and plotting a line chart and a bar chart), plus labelling the months and positioning the plot area.
**What I wrote or changed myself:** Chose the colours and fonts so that the plots matched the application and blended seemlessly into the background, wrote the titles and axis labels, and adapted the code to the `combined_data.py` dataset.
**Problem found and fixed:** The two charts didn't line up when shown side by side. Using `tight_layout()` together with `subplots_adjust()` overrode my manual margins, so I removed `tight_layout()` and kept the fixed margins.
**How I verified it:** I opened the saved images to check all 12 months appeared and the axes were labelled correctly, and checked they displayed side by side in the app. Test 9 in `test_data.py` also confirms the monthly grouping produces exactly 12 entries.


## Entry 4: Combining CSV data
**Tool:** Claude 
**Date:** 25 Sep 2026
**What I asked"** How to combine two datasets with the same headings into on dataset.
**What the AI produced:** Code used to combine two datasets, code to check it has combined correctly and to created a CSV file called `combined_data.py`.
**How I verified it:** Checked that the combined data lined up with the each of the individual sets to know that it was combined correctly.


## Entry 5: Add images to the border of the whole application
**Tool:** ChatGPT
**Date:** 29 Sep 2026
**What I Asked:** Write code that puts images on the edge left and right border of the website page that goes from top to bottom. I want it to stay the same size no matter the size of the window.
**What the AI Produced:** a Python script that added in the images and gave code about where they should be placed on the page. 
**What I used/changed:** I added the code and then saw how it looked in the app. I then changed the width of the image to how i wanted it. 
**How i verified it:** I ran it and checked that it used the correct image and was in the correct spot on the application. 


## Entry 6: Map inclusion in the home page
**Tool:** VS Code AI
**Date:** 4 Oct 2026
**What i asked:** I want to add images underneath the graphs on the homeage, where is the right place to add this in
**What the AI produced:** It told me exactly where to start writing the code needed to add the images in. (Immediately after the graphs' closing </div>, and before the "How would you rate this site" section in frontend.html) Add a <section> there with the image and text.
**What i used/changed:** I added in some text of my own underneath this section, and the AI was correct in where to put it. I did not need to change anything, and i used this suggestion.
**How i verified it:** After putting the images in, i checked to make sure they appeared where i wanted on the homepage. 


## Entry 7: Automated tests 
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

## Entry 8: User site rating buttons
**Tool:** VS Code AI
**Date:** 1 Oct 2026
**What I asked:** I want to create a code for user output on the main screen, with a scale with a range of faces from sad to happy, asking "how would you rate this site". The user should be able to click on the face that aligns with their thoughts, and this record will be stored.
**What the AI Produced:** It produced code that initially did not work. After changing the port that Flask was running on to 8000, the code worked. It produced code that showed 5 faces from Very Unhappy to Very Happy, that appeared on the bottom of the home page as asked. It also created a CSV file to store this data, and automatically recorded the selection of these results in that CSV file
**What i used/changed:** I changed the text and the way the area looked slightly. I changed the colours of the button's borders to match the rest of the site. I also made another section that showed the user when the rating was saved after clicking it. 
**How i verified it:** I made sure the code worked, and ran it a few times to check. I clicked the buttons and made sure that it was recorded properly in the CSV file. 


## Entry 9: Create a "my account" section
**Tool:** VS Code AI
**Date:** 1 Oct 2026
**What i asked:** how can we make another screen that is accessed by button, to allow a user to make or create an account using a username and password, or login to an existing account and enter their existing username and password, to access a page where a record is kept of all things they have done from the website, recorded by clicking the activitiy they did
**What the AI produced:** It made basic code for an activity screen with a login or sign in page 
**What i used/changed:** I used this page, and then also asked the AI to separate the login information and secure it. I also asked it to include the parameters that the username and password needed when creating an account on the screen
**What the AI produced:** It made a file to securely store the login info. It included the parameters on the login page needed to make an account.
**How i verified it:** I checked every step of the way to make sure the code made sense and that it worked on the application. When it did not work, or missed something that i wanted included, i got AI to go through the code again and fix it. 
**What i added:** I then asked the ai to change the way activities were marked as done, making sure that you can check and uncheck the black point next to the activity.
**What the AI produced:** it did this, changing from the initial selection of the whole line of text, to just the black dot at the start of the activity
**How i verified it:** I checked that it worked, and that when you added an activity it was recorded on your profile. I then checked to make sure that when you unchecked the acitivity, that it was then unrecorded form your profile. 
