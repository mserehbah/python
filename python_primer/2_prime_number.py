#check a prime number

print("Enter your number: ")
num = int(input())


def is_prime(num):
    if num <= 1:
        return False
    
    for i in range(2, int((num ** 0.5))+1):
        if(num % i == 0):
            return False
    return True


if is_prime(num):
     print("Number is a prime number")
else:
    print("Number is not a prime number")     