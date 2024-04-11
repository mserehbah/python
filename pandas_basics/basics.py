import pandas as pd

# A Pandas Series is like a column in a table.

#list
a = [1,2,3,4]

col1 = pd.Series(a, index=["a","b","c", "d"])

print(col1)

#access item by ref. index
print(col1["a"])

#dictionary
items = {"one":123,"two":124,"three":432, "four":412,"five":222}

col2 = pd.Series(items)

print(col2)

#access item by ref. index
print(col2["five"])

#specify items you want to include in the series
col2 = pd.Series(items, index=["one", "two"])

print(col2)

#NB:
# Series is like a column, a DataFrame is the whole table.

#Dataframes

data = {
    "calories":[420, 380, 390],
    "duration":[50,45,40]
}

table1 = pd.DataFrame(data)

print(table1)

#locate a row(s) using index

print(table1.loc[0])

print(table1.loc[[0,1]])   # Note: When using [], the result is a Pandas DataFrame.

# named indexes

table1 = pd.DataFrame(data, index=["a","b","c"])

print(table1)

print(table1.loc["c"])

print(table1.loc[["c"]])
