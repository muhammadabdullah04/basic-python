import pandas as pd

df = pd.read_csv("movies_data.csv")
print(df)

g = df.groupby('industry')
# 2. Get the size of each category
print("Size of each category:")
print(g.size())

# 3. Get all the data related to 'Bollywood'
print("\nData related to Bollywood:")
print(g.get_group('Bollywood'))

# Define the custom grouping function
def grouper(df, idx, col):
    rating = df.loc[idx, col]
    if 1 <= rating <= 3.9:
        return 'Poor'
    elif 4 <= rating <= 7.9:
        return 'Average'
    elif 8 <= rating <= 10:
        return 'Good'
    else:
        return 'Others'

# Apply custom grouping using groupby with a function
g = df.groupby(lambda idx: grouper(df, idx, 'imdb_rating'))

# Iterate through the groups and print them
for group_name, group_data in g:
    print(f"\nGroup: {group_name}")
    print(group_data)