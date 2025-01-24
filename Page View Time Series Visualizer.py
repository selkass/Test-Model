import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 1. Use Pandas to import the data from "fcc-forum-pageviews.csv". Set the index to the date column.
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"], index_col="date")

# 2. Clean the data by filtering out days when the page views were in the top 2.5% or bottom 2.5% of the dataset.
df_cleaned = df[
    (df["value"] >= df["value"].quantile(0.025)) &
    (df["value"] <= df["value"].quantile(0.975))
]

# 3. Create a draw_line_plot function that uses Matplotlib to draw a line chart.
def draw_line_plot():
    fig, ax = plt.subplots(figsize=(14, 6))
    ax.plot(df_cleaned.index, df_cleaned["value"], color="red")
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    plt.close()
    return fig

# 4. Create a draw_bar_plot function that draws a bar chart.
def draw_bar_plot():
    # Group by year and month, then calculate the average page views.
    df_bar = df_cleaned.copy()
    df_bar["year"] = df_bar.index.year
    df_bar["month"] = df_bar.index.month
    df_bar = df_bar.groupby(["year", "month"])["value"].mean().unstack()

    # Plot the bar chart.
    fig = df_bar.plot(kind="bar", figsize=(10, 6)).figure
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title="Months", labels=[
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ])
    plt.close()
    return fig

# 5. Create a draw_box_plot function that uses Seaborn to draw two adjacent box plots.
def draw_box_plot():
    # Prepare the data for box plots.
    df_box = df_cleaned.copy()
    df_box.reset_index(inplace=True)
    df_box["year"] = [d.year for d in df_box["date"]]
    df_box["month"] = [d.strftime("%b") for d in df_box["date"]]

    # Set up the matplotlib figure.
    fig, axes = plt.subplots(1, 2, figsize=(18, 6))

    # Year-wise box plot.
    sns.boxplot(x="year", y="value", data=df_box, ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    # Month-wise box plot.
    month_order = [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ]
    sns.boxplot(x="month", y="value", data=df_box, ax=axes[1], order=month_order)
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    plt.close()
    return fig

# Do not modify the next two lines.
if __name__ == "__main__":
    draw_line_plot().savefig("line_plot.png")
    draw_bar_plot().savefig("bar_plot.png")
    draw_box_plot().savefig("box_plot.png")