import sys
import os
# Fix to let Python find the 'src' folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
from src import eda, insight

st.set_page_config(page_title="Business Advisor Dashboard", layout="wide")

# Load data
df = eda.load_data()
df = insight.add_profit_columns(df)

st.title("Business Advisor Dashboard")
st.markdown("Hello Cikaaa 🥺💖 Ini dashboardmu yang ciamik banget~ Let's analyze the biz 🔍")

# Sidebar filter
st.sidebar.header("Filter")
products = st.sidebar.multiselect("Choose the product:", df['Product'].unique(), default=df['Product'].unique())

filtered_df = df[df['Product'].isin(products)]

# Metrics
st.subheader("Business Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"${filtered_df['Revenue'].sum():,.0f}")
col2.metric("Total Profit", f"${filtered_df['Profit'].sum():,.0f}")
col3.metric("Average Margin", f"{filtered_df['Margin %'].mean():.2f}%")

# Trend chart
st.subheader("Daily Revenue Trend")
daily = filtered_df.groupby('Date')['Revenue'].sum()
st.line_chart(daily)

# Profit by Product
st.subheader("Profit per Product")
st.bar_chart(insight.profit_by_product(filtered_df))

# Revenue by Region
st.subheader("Revenue per Region")
st.bar_chart(insight.revenue_by_region(filtered_df))
