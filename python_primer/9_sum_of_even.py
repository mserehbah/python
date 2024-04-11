#sum of even numbers in a dictionary

dictionary = []

for i in range(1, 26):
    dictionary.append(i)

even = []

for item in dictionary:
    if(item%2==0):
        even.append(item)


def sum_even():
    sum = 0
    for num in even:
        sum = sum + num

    return print(sum)


sum_even()