import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Import the data from medical_examination.csv and assign it to the df variable.
df = pd.read_csv("medical_examination.csv")

# 2. Add an overweight column to the data.
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)

# 3. Normalize data by making 0 always good and 1 always bad.
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# 4. Draw the Categorical Plot in the draw_cat_plot function.
def draw_cat_plot():
    # 5. Create a DataFrame for the cat plot using pd.melt.
    df_cat = pd.melt(
        df,
        id_vars=['cardio'],
        value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    )

    # 6. Group and reformat the data in df_cat to split it by cardio.
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index=False).size()

    # 7. Convert the data into long format and create a chart using sns.catplot().
    fig = sns.catplot(
        x='variable',
        y='size',
        hue='value',
        col='cardio',
        data=df_cat,
        kind='bar'
    ).fig

    # 8. Get the figure for the output and store it in the fig variable.
    return fig

# 9. Draw the Heat Map in the draw_heat_map function.
def draw_heat_map():
    # 10. Clean the data in the df_heat variable.
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 11. Calculate the correlation matrix and store it in the corr variable.
    corr = df_heat.corr()

    # 12. Generate a mask for the upper triangle.
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 13. Set up the matplotlib figure.
    fig, ax = plt.subplots(figsize=(12, 10))

    # 14. Plot the correlation matrix using sns.heatmap().
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt=".1f",
        linewidths=0.5,
        center=0,
        cbar_kws={"shrink": 0.5},
        square=True
    )

    # 15. Return the figure for the output.
    return fig

# Do not modify the next two lines.
if __name__ == "__main__":
    draw_cat_plot().savefig('catplot.png')
    draw_heat_map().savefig('heatmap.png')