# reverse a string

print("Enter your string: ")

string = input()

def revers(string):
    str_list = []

    for char in string:
        str_list.append(char)

    reversed_string_list = []
    for item in str_list:
        reversed_string_list.insert(0, item)

    print(reversed_string_list)

    str_list_length = len(str_list)
    reversed_string = ""
    for i in range(str_list_length):
        reversed_string = reversed_string + reversed_string_list[i]
    print(reversed_string)    

revers(string)
