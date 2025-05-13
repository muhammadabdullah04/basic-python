import pandas as pd

df = pd.read_csv("retail_sale_dataset.csv")

print("🔹 First 5 Rows:\n", df.head())
# Revenue by branch and city
print("\n🔹 Revenue by Branch:\n", df.groupby('Branch')['Total'].sum())
print("\n🔹 Revenue by City:\n", df.groupby('City')['Total'].sum())

# Average spending by gender and customer type
print("\n🔹 Avg Spending by Gender:\n", df.groupby('Gender')['Total'].mean())
print("\n🔹 Avg Spending by Customer Type:\n", df.groupby('Customer type')['Total'].mean())


# Busiest shopping days
print("\n🔹 Busiest Shopping Days:\n", df['Date'].value_counts().sort_index())

# Average rating per branch
print("\n🔹 Avg Customer Rating per Branch:\n", df.groupby('Branch')['Rating'].mean())