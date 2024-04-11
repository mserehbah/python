#function that takes 3 boolean variables and returns true if atleast two of the variables are true, otherwise false

x = True
y = False
z = False

def check_variables(x, y, z):
    if((x & y) | (x & z) | (y & z)):
        return print(True)
    else:
        return print(False)


check_variables(x, y, z)