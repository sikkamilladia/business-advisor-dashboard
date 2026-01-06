# Explotatory Data Analysis (EDA) for the dataset
# Goals:
# 1. Looking structure and content of the dataset
# 2. Looking for missing values
# 3. Looking for duplicates
# 4. Descriptive statistics
# 5. Visualizing the first data (trends, the most sell products, etc.)

import pandas as pd

# Load the dataset (csv file)
df = pd.read_csv('business_data.csv')

# Showing the first 5 rows of the dataset
print(df.head())

# 2. Check the mandatory information
# Data structure
df.info()

# 3. Check for missing values
print(df.isnull().sum())

# 4. Descriptive statistics
print(df.describe())

# Unique and category checker:
print(df['Product'].unique())
print(df['Region'].value_counts())