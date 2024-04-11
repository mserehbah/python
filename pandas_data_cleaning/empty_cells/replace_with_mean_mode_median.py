import pandas as pd

pd.options.display.max_rows = 9999

data = pd.read_csv("D:/vscode/python/pandas_data_cleaning/data.csv")

# replace empty values with mean # Mean = the average value (the sum of all values divided by number of values).

calories_col_mean = data["Calories"].mean()

data["Calories"].fillna(calories_col_mean, inplace=True)

print(data)

# replace empty values with median # Median = the value in the middle, after you have sorted all values ascending.

calories_col_median = data["Calories"].median()

data["Calories"].fillna(calories_col_median, inplace=True)

print(data)

# replace empty values with mode # Mode = the value that appears most frequently.

calories_col_mode = data["Calories"].mode()

# new way of doing it compared to above method # pandas update 3.
data.fillna({"Calories":calories_col_mode}, inplace=True)

print(data)