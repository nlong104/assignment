import pandas as pd

data = pd.read_csv("combined_data.csv")
# Reusable assertion function for testing that compares actual and expected values and logs the result
def assert_equal(actual, expected, test_name):
    if actual == expected:
        print(f"PASS: {test_name}")
    else:
        print(f"FAIL: {test_name} — expected {expected}, got {actual}")

def average_metric(df, column):
    return df[column].mean()

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