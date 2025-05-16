import pandas as pd
from matplotlib import pyplot as plt

df_sales = pd.read_excel("linechart.xlsx")
df_sales.head()

plt.figure(figsize=(12,4))
plt.plot(df_sales["Quarter"], df_sales["Fridge"], color="blue", label="Fridge")
plt.plot(df_sales["Quarter"], df_sales["Dishwasher"], color="orange", label="Dishwasher")
plt.plot(df_sales["Quarter"], df_sales["Washing Machine"], color="green", label="Washing Machine")

plt.title("Product Sales")
plt.xlabel("Quarter")
plt.ylabel("Million $")

plt.legend()

plt.show()

total_sales = df_sales[["Fridge","Dishwasher","Washing Machine"]].sum()
total_sales

plt.pie(total_sales, labels=total_sales.index, autopct='%1.1f%%', startangle=140, explode=(0.1,0,0), shadow=True)
plt.show()