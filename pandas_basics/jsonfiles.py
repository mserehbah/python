import pandas as pd

pd.options.display.max_rows = 9999

df = pd.read_json('D:/vscode/python/pandas_basics/data.json')

print(df)

dictionary = {
    "students":{
        "a":"Momodou",
        "b":"Yankuba",
        "c":'Aminata',
        "d":"Musa",
    },
    "fields":{
        "a":"ICT",
        "b":"BPA",
        "c":"SAS"
    }
}

print(pd.DataFrame(dictionary)) # python dictionary is similar to json