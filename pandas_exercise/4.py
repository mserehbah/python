import pandas as pd

pd.options.display.max_rows = 9999

data = pd.read_csv("D:/vscode/python/pandas_exercise/data.csv")

# get info about data / csv file

print(data.info())