import pandas as pd

pd.options.display.max_rows = 9999

# The fillna() method allows us to replace empty cells with a value.


raw_df = pd.read_csv("D:/vscode/python/pandas_data_cleaning/data.csv")

print(raw_df)

#raw_df.fillna("NA", inplace=True)

# To only replace empty values for one column, specify the column name for the DataFrame:
raw_df["Calories"].fillna("NA", inplace=True)

print(raw_df)