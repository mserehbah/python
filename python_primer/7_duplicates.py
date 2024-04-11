#remove all duplicates in a list

data = [1,2,3,4,3,5,6,1,2,1,1,1]

cleaned_data = []

def remove_duplicates():

    for item in data:
        count = data.count(item)
        count2 = cleaned_data.count(item)
        #print(count, count2)
        if(count >= 1 and count2 == 0):
            cleaned_data.append(item)

    return print(cleaned_data)


remove_duplicates()