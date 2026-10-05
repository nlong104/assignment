import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("combined_data.csv")

# Chart 1 - average temperature 
monthly_avg = data.groupby("Month")["Temperature"].mean()

plt.figure(figsize=(6,5), facecolor="#fdd8e8") # sets background colour of chart 
monthly_avg.plot(kind="line", marker="o", color="#7B3039") # marker="o" just draws a small dot at each actual data point on top of the line, which makes it easier to read exact values.
plt.gca().set_facecolor("#fdd8e8") # sets background colour of chart - colours inner plot area specifically

plt.title("Average Monthly Maximum Temperature in Perth from 1994 - 2026", fontsize=11)
plt.xlabel("Month")
plt.ylabel("Average Monthly Maximum Temperature (°C)")
plt.xticks(range(1, 13), labels=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]) # makes sure all 12 months show up on the x-axis
plt.subplots_adjust(left=0.15, right=0.95, top=0.9, bottom=0.15) # making the charts centred in the image
plt.savefig("average_monthly_maximum_temperature.png", facecolor="#fdd8e8") # saves the chart to a file, and sets the background colour of the saved image

# Chart 2 - average precipitation
monthly_avg_precip = data.groupby("Month")["Precipitation"].mean()

plt.figure(figsize=(6,5), facecolor="#fdd8e8") # sets background colour of chart 
monthly_avg_precip.plot(kind="bar", color="#7B3039") # bar chart with different colours for each month
plt.gca().set_facecolor("#fdd8e8") # sets background colour of chart - colours inner plot area specifically

plt.title("Average Monthly Precipitation in Perth from 1994 - 2026")
plt.xlabel("Month")
plt.ylabel("Average Monthly Precipitation (mm)")
plt.xticks(range(0, 12), labels=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]) # makes sure all 12 months show up on the x-axis
plt.subplots_adjust(left=0.15, right=0.95, top=0.9, bottom=0.15) # making the charts centred in the image
plt.savefig("average_monthly_precipitation.png", facecolor="#fdd8e8") # saves the chart to a file, and sets the background colour of the saved image


print("Saved charts")