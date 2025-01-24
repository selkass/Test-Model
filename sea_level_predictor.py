import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# 1. Use Pandas to import the data from epa-sea-level.csv.
df = pd.read_csv("epa-sea-level.csv")

# 2. Use matplotlib to create a scatter plot.
plt.figure(figsize=(10, 6))
plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], color="blue", label="Data Points")

# 3. Use linregress to get the slope and y-intercept of the line of best fit.
res = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
years_extended = range(1880, 2051)  # Extend the x-axis to 2050
plt.plot(
    years_extended,
    res.intercept + res.slope * years_extended,
    color="red",
    label="Best Fit Line (1880-2013)"
)

# 4. Plot a new line of best fit using data from year 2000 onwards.
df_recent = df[df["Year"] >= 2000]
res_recent = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
plt.plot(
    years_extended,
    res_recent.intercept + res_recent.slope * years_extended,
    color="green",
    label="Best Fit Line (2000-2013)"
)

# 5. Add labels and title.
plt.xlabel("Year")
plt.ylabel("Sea Level (inches)")
plt.title("Rise in Sea Level")
plt.legend()

# 6. Save and return the image.
plt.savefig("sea_level_plot.png")
plt.show()