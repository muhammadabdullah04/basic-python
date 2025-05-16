import pandas as pd

df = pd.read_csv('fruits_data.csv')

print("Shape (Rows, Columns):", df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nDataframe:")
print(df)

new_df = df.fillna(-1)

print(new_df)


new_df = df.copy()

# Fill with mean values
new_df['apple(1kg)'] = new_df['apple(1kg)'].fillna(new_df['apple(1kg)'].mean())
new_df['banana(1 dozen)'] = new_df['banana(1 dozen)'].fillna(new_df['banana(1 dozen)'].mean())

# Fill with median values
new_df['grapes(1kg)'] = new_df['grapes(1kg)'].fillna(new_df['grapes(1kg)'].median())
new_df['mango(1kg)'] = new_df['mango(1kg)'].fillna(new_df['mango(1kg)'].median())

# Fill with string for Water Melons(1)
new_df['Water Melons(1)'] = new_df['Water Melons(1)'].fillna('Not Available')

# Show the new dataframe
print(new_df)