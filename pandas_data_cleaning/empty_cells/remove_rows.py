import pandas as pd

pd.options.display.max_rows = 9999

raw_df = pd.read_csv('D:/vscode/python/pandas_data_cleaning/data.csv')

# The raw data set contains some empty cells ("Date" in row 22, and "Calories" in row 18 and 28).
print(raw_df)

#clean data (rows with empty cells removed)

cleaned_df = raw_df.dropna() # By default, the dropna() method returns a new DataFrame, and will not change the original.
print(cleaned_df)

# To change the original # use the inplace argument and set it to true

raw_df.dropna(inplace=True)

print(raw_df)