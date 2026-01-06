# Explotatory Data Analysis (EDA) for the dataset
# Goals:
# 1. Looking structure and content of the dataset
# 2. Looking for missing values
# 3. Looking for duplicates
# 4. Descriptive statistics
# 5. Visualizing the first data (trends, the most sell products, etc.)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(path='data/business_data.csv'):
    df = pd.read_csv(path)                      # Load the dataset
    df.drop_duplicates(inplace=True)            # remove duplicates
    df.dropna(inplace=True)                     # remove rows with missing values
    df['Date'] = pd.to_datetime(df['Date'])     # convert to datetime
    return df

def data_summary(df):
    print("Data Info")
    print(df.info())
    print("\n Missing Values:")
    print(df.isnull().sum())
    print("\n Descriptive Statistics:")
    print(df.describe())
    print("\n Unique Values:")
    print("Products:", df['Product'].unique())
    print("Regions:", df['Region'].value_counts())

def plot_revenue_by_product(df):
    product_revenue = df.groupby('Product')['Revenue'].sum().sort_values(ascending=False)

    plt.figure(figsize=(8,5))
    sns.barplot(x=product_revenue.index, y=product_revenue.values, palette='viridis', hue=product_revenue.index, legend=False)
    plt.title('Total Revenue per Product')
    plt.ylabel('Revenue')
    plt.xlabel('Product')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_revenue_trend(df):
    daily_revenue = df.groupby('Date')['Revenue'].sum()

    plt.figure(figsize=(10,4))
    daily_revenue.plot(marker='o')
    plt.title('Revenue Trend Over Time')
    plt.ylabel('Revenue')
    plt.xlabel('Date')
    plt.grid(True)
    plt.tight_layout()
    plt.show()