import pandas as pd


pd.options.display.max_rows = 9999


data = pd.read_csv("D:/vscode/python/pandas_data_cleaning/data.csv")
# row 26 is containing data in the wrong format # date is not in quotes
# row 22's date is NaN

date_col = data['Date']

print(data)

def format_date(date_col):
    #data["Date"] = pd.to_datetime(arg=data["Date"])

    #format date
    data['Date'] = pd.to_datetime(date_col, format='mixed')

    # remove rows with Nat Date
    data.dropna(subset=["Date"], inplace=True)

    print(data)


format_date(date_col)