import pandas as pd

pd.options.display.max_rows = 9999

""" If you take a look at our data set, you can see that in row 7, 
the duration is 450, but for all the other rows the duration is between 30 and 60."""

data = pd.read_csv("D:/vscode/python/pandas_data_cleaning/data.csv")

print(data)

# One way to fix wrong values is to replace them with something else.
#data.loc[7, "Duration"] = 45

# for large datasets, the above might not be the best option, takes time, painstaking, prone to error due to parallax
# instead loop through the dataset, define conditions to replace in the best way
for i in data.index:
    if(data.loc[i, "Duration"] > 60):
        data.loc[i, "Duration"] = 60

print(data)