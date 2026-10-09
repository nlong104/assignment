# What should be in the ai log
What you asked the AI to do
What it produced, and which tool you used
What you kept or changed
How you verified it, since the rubric asks for verification of AI output



## Entry 1: Combining CSV data
**Tool:** Claude 
**Date:** 25 Sep 2026
**What I asked"** How to combine two datasets with the same headings into on dataset.
**What the AI produced:** Code used to combine two datasets, code to check it has combined correctly and to created a CSV file called `combined_data.py`.
**How I verified it:** Checked that the combined data lined up with the each of the individual sets to know that it was combined correctly.

## Entry 2: Weather data loading and season summaries
**Tool:** Claude
**Date:** 26 Sep 2026
**What I asked:** Help writing code to load temperature and precipitation data from `combined_data.csv` and work out average values for each Nyoongar season.
**What the AI produced:** A Python script with code that loads the CSV, matches each month to a season, and calculates average temperature and precipitation for each season.
**What I used / changed:** Used the structure and functions, but changed the seasons to Kambarang, Makuru and Birak, and changed the column names to match my file (`Year`, `Month`, `Temperature`, `Precipitation`). 
**How I verified it:** Ran `python weather_data.py` and checked that the number of rows loaded matched the CSV file


# Entry 3: Creating/styling buttons 
**Tool:** Claude
**Date:** 27 Sep 2026
**What I asked:** How to create buttons from a python application that switch between screens.
**What the AI produced:** A general template for how to insert a button into the app, and how to add some styles to it.
**What I wrote or changed myself:** Added in the specific button names and screen names to that the buttons would work with this specific app, changed button style so that the font was the same as the rest of the app and that the buttons were centred on the screen. Then could use this template for all other buttons on the app.
**How I verified it:** Ran the code and opened the server to see whether the buttons were working correctly and had the correct styling.


## Entry 4: Add images to the border of the whole application
**Tool:** ChatGPT
**Date:** 29 Sep 2026
**What I Asked:** Write code that puts images on the edge left and right border of the website page that goes from top to bottom. I want it to stay the same size no matter the size of the window.
**What the AI Produced:** a Python script that added in the images and gave code about where they should be placed on the page. 
**What I used/changed:** I added the code and then saw how it looked in the app. I then changed the width of the image to how i wanted it. 
**How i verified it:** I ran it and checked that it used the correct image and was in the correct spot on the application. 


## Entry 5: Creating charts
**Tool:** Claude
**Date:** 30 Sep 2026
**What I asked:** How how to fix problems with chart sizing and alignment, and how polish a simpel chart.
**What the AI produced:** The basic pandas and matplotlib approach (grouping the data by month, taking the mean, and plotting a line chart and a bar chart), plus labelling the months and positioning the plot area.
**What I wrote or changed myself:** Chose the colours and fonts so that the plots matched the application and blended seemlessly into the background, wrote the titles and axis labels, and adapted the code to the `combined_data.py` dataset.
**Problem found and fixed:** The two charts didn't line up when shown side by side. Using `tight_layout()` together with `subplots_adjust()` overrode my manual margins, so I removed `tight_layout()` and kept the fixed margins.
**How I verified it:** I opened the saved images to check all 12 months appeared and the axes were labelled correctly, and checked they displayed side by side in the app. Test 9 in `test_data.py` also confirms the monthly grouping produces exactly 12 entries.


## Entry 6: User site rating buttons
**Tool:** VS Code AI
**Date:** 1 Oct 2026
**What I asked:** I want to create a code for user output on the main screen, with a scale with a range of faces from sad to happy, asking "how would you rate this site". The user should be able to click on the face that aligns with their thoughts, and this record will be stored.
**What the AI Produced:** It produced code that initially did not work. After changing the port that Flask was running on to 8000, the code worked. It produced code that showed 5 faces from Very Unhappy to Very Happy, that appeared on the bottom of the home page as asked. It also created a CSV file to store this data, and automatically recorded the selection of these results in that CSV file
**What i used/changed:** I changed the text and the way the area looked slightly. I changed the colours of the button's borders to match the rest of the site. I also made another section that showed the user when the rating was saved after clicking it. 
**How i verified it:** I made sure the code worked, and ran it a few times to check. I clicked the buttons and made sure that it was recorded properly in the CSV file. 


## Entry 7: Create a "my account" section
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

## Entry 8: Map inclusion in the home page
**Tool:** VS Code AI
**Date:** 4 Oct 2026
**What i asked:** I want to add images underneath the graphs on the homeage, where is the right place to add this in
**What the AI produced:** It told me exactly where to start writing the code needed to add the images in. (Immediately after the graphs' closing </div>, and before the "How would you rate this site" section in frontend.html) Add a <section> there with the image and text.
**What i used/changed:** I added in some text of my own underneath this section, and the AI was correct in where to put it. I did not need to change anything, and i used this suggestion.
**How i verified it:** After putting the images in, i checked to make sure they appeared where i wanted on the homepage. 


## Entry 9: Automated tests
**Tool:** Claude
**Date:** 4 Oct 2026
**What I asked:** Help planning automated tests for the code that switches screens and the data processing.
**What the AI produced:** A set of 5 JavaScript tests and 4 Python tests, plus an `assertEqual` helper.
**What I used / changed:** Used the tests, replaced Test 9 (it tested color logic that didn't end up in the final chart), and added Test 10 for invalid input.
**How I verified it:** Ran `tests.html` and `test_data.py` and checked all tests passed. Found that Test 9 didn't match my code anymore and rewrote it to match the final version.

# Entry 10: Activity images 
**Tool:** Claude
**Date:** 5 Oct 2026
**What I asked:** How to add multiple images in a row
**What the AI produced:** Code to allow the three images to be side by side on the screen.
**What I changed/wrote myself:** The images were not of equal dimensions so the images were then cropped so that they fit evenly on te screen.
**How I verified it:** Ran the code and opened to server to see whether the images fit the way they were intended to.


