#count even and odd numbers given a list

nums = [1,2,3,4,5,6,7,8,9,10,100,13,17]

even = []

odd = []

def count():
    for num in nums:
        if(num%2 == 0):
            even.append(num)
        else:
            odd.append(num)

    print('even',len(even))
    print('odd', len(odd))


count()