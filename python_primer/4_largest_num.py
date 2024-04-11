# find and print largest number in a list


grades = [10, 20, 30, 5, 80]
#print(max(grades))

def getLargestNum():
    max_grade = grades[0]

    for grade in grades:
        if grade > max_grade:
         max_grade = grade

    return max_grade


print(getLargestNum())