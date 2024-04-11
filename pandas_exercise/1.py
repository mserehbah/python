import pandas as pd

pd.options.display.max_rows = 9999

#create series / col

grades = [12,20,30,40,50]

col1 = pd.Series(grades, index=["a","b","c","d","e"])
print(col1)