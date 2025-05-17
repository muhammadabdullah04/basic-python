import pandas as pd

# Read movies.csv into df_movies
df_movies = pd.read_csv("movies.csv")
print("Movies - Top 3 rows:")
print(df_movies.head(3))

# Read financials.csv into df_financials
df_financials = pd.read_csv("financials.csv")
print("\nFinancials - Top 3 rows:")
print(df_financials.head(3))

# Read languages.csv into df_languages
df_languages = pd.read_csv("languages.csv")
print("\nLanguages - Top 3 rows:")
print(df_languages.head(3))
