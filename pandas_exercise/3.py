import pandas as pd

pd.options.display.max_rows = 9999

vendors = {
    "name":["Marie","Musu","Alagie","Kemo","Badjie"],
    "product":["pepper","tomato","salt","barley","oil"]
}

vendors_data = pd.DataFrame(vendors)

#print(vendors_data)

# access specific col / series

products = vendors_data["name"]

print(products)

# access specific row
row1 = vendors_data.loc[[0]]

print(row1)