import pandas as pd

pd.options.display.max_rows = 9999

# create table / dataframe

# 1. using dictionary

students = {
    "names":["Momodou", "Musa", "John", "Amie", "Binta","Zakariya"],
    "mat#":[123,321,231,456,564,980 ],

}

df = pd.DataFrame(students)

print(df)

# 2. using csv
df = pd.read_csv("D:/vscode/python/pandas_exercise/data.csv")

print(df)