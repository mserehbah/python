import pandas as pd

pd.options.display.max_rows = 9999

df = pd.read_csv('D:/vscode/python/pandas_basics/data.csv')

#print(df.to_string()) #  use to_string() to print the entire DataFrame.

print(df)

# check your system's maximum returned rows

print('max rows: ', pd.options.display.max_rows) # 60

# max rows my system can display is 60, if dataframe is more than 60 rows-
# only the first 5 and last 5 rows are displayed

# Increase the maximum number of rows to display the entire DataFrame: 
    #pd.options.display.max_rows = 9999