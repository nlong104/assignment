import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("combined_data.csv")

# Average the Temperature column, grouped by Month (1-12), across all years
monthly_avg = data.groupby("Month")["Temperature"].mean()

monthly_avg.plot(kind="line", marker="o") # marker="o" just draws a small dot at each actual data point on top of the line, which makes it easier to read exact values.
plt.title("Average Monthly Temperature from 1994 - 2026")
plt.xlabel("Month")
plt.ylabel("Average Monthly Temperature (°C)")
plt.xticks(range(1, 13), labels=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]) # makes sure all 12 months show up on the x-axis
plt.savefig("average_monthly_temperature.png")

print("Average monthly temperature chart saved as 'average_monthly_temperature.png'")