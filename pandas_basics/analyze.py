import pandas as pd

pd.options.display.max_rows = 9999

df = pd.read_csv('D:/vscode/python/pandas_basics/data.csv')

# viewing the data

#get quick overview by viewing the first 10 rows
print(df.head(10))

#get quick overview by viewing the last 10 rows
print(df.tail(10))

#get quick overview by viewing the first 5 rows
print(df.head())

#NB: ******************************************
    # by default, head() and tail() gives an overview of the first and last five rows respectively when arguments are not supplied

# info about the data

print(df.info()) # this gives info about:

# no. of entries/rows
# no. of columns
# column info: name of each column with data type and non-null values in each column
# data types used
# memory usage

