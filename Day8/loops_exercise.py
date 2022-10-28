#print 10 numbers using while loop

n = 10
i = 0
while i < n:
    i += 1
    print(i)

s = 0
n = 10
for i in range(1, n+1, 1):
    s += i
print(s)

#multiplication of 2 table
n = 2
for i in range(2, 10):
    p = n*i
    print(p)
list1 = [10, 20, 30, 40, 50]
new_list = reversed(list1)
for item in new_list:
    print(item)

for n in range(-10, 0):
    print(n)

for i in range(5):
    print(i)
else:
    print('done')

#prime numbers

for num in range(25,50 +1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
            else:
                print(num)

#fibonacci series
num1 = 0
num2 = 1
for i in range(10):
    print(num1, end=' ')
    res = num1 + num2
    num1 = num2
    num2 = res

#factorial
import math
n=5
print(math.factorial(n))


list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for x in list1[1::2]:
    print(x, end=' ')



            
       
