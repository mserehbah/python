# calculate the sum of all numbers from 1 to N using a loop

print("Enter your number: ")
num = int(input())

def sum(num):
   items = range(1, num)
   ans = 0
   for n in items:
      ans = ans + n
      #print(n+1)

   return print(ans)   

sum(num)
