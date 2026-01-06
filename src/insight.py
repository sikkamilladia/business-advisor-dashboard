# Generate insight from src import eda
# Goal:
# 1. Which product has the highest revenue?
# 2. What is the trend of revenue over time?
# 3. Which day has the highest/lowest revenue?

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Profit and margin analysis
def add_profit_columns(df):
    df['Profit'] = df['Revenue'] - df['Cost']
    df['Margin %'] = (df['Profit'] / df['Revenue']) * 100
    return df

def profit_by_product(df):
    return df.groupby('Product')['Profit'].sum().sort_values(ascending=False)

# 2. Top Region by Revenue:
def revenue_by_region(df):
    return df.groupby('Region')['Revenue'].sum().sort_values(ascending=False)

# 3. Highest and Lowest Revenue Days:
def revenue_by_day(df):
    df['Day of Week'] = df['Date'].dt.day_name()
    return df.groupby('Day of Week')['Revenue'].sum().sort_values(ascending=False)

# 4. Visualizing Profit Margin per Product:
def plot_margin_per_product(df):
    plt.figure(figsize=(8, 5))
    sns.barplot(x='Product', y='Margin %', data=df, errorbar=None, palette='magma', hue='Product', legend=False)
    plt.title('Margin Per Product')
    plt.ylabel('Margin %')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()