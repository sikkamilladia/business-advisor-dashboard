import eda
import insight

# Load and analyze
df = eda.load_data()
df = insight.add_profit_columns(df)

# Show insights
print("Profit by Product:")
print(insight.profit_by_product(df))

print("\nRevenue by Region:")
print(insight.reveneue_by_region(df))

print("\nRevenue by Day of Week:")
print(insight.revenue_by_day(df))

# Visualizations
insight.plot_margin_per_product(df)

eda.data_summary(df)
eda.plot_revenue_by_product(df)
eda.plot_revenue_trend(df)

#run pake ini: 
# cd ..
# python src/main.py