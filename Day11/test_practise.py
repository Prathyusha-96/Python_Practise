#area of triangle
# s = (a+b+c)/2
# area = √(s(s-a)*(s-b)*(s-c))

a= 5
b = 6
c =7
s = (a+b+c)/2
# print(s)
area = (s*(s-a)*(s-b)*(s-c))**0.5
print(area)

# Python program to swap two variables
x = 5
y = 10
temp = x
x = y
y = temp
print(x, y)

#Python Program to Generate a Random Number
import random
list1 = [2, 4, 5, 6, 8]

print(random.choice(list1))
print(random.randint(1,2))

#Python Program to Check if a Number is Positive, Negative or 0
num = 0

if num > 0:
    print('positive number')
elif num == 0:
    print('Zero')
else:
    print('negative number')

#Python Program to Check if a Number is Odd or Even3

num = 24
if num%2 == 0:
    print('even number')
else:
    print('odd number')

#Python Program to Check Leap Year
year = 2002
if year%4 == 0:
    print('leap year')
else:
    print('not a leap year')

# Python program to find the largest number among the three input numbers
a = 20
b = 100
c = 80
if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)


#prime number or not

num = 12
if num > 1:
    for i in range(2, num):
        if(num%i) == 0:
            print(num, 'is not a prime number')
            break
        else:
            print(num, 'is prime number')
else:
    print(num, 'is not a prime number')

#Python Program to Find the Factorial of a Number
import math
n = 6
print(math.factorial(n))

#another solution
n = 5
factorial = 1
for i in range(2, n+1):
    factorial = factorial*i
    print(factorial)

#multiplication table
num = 12
for i in range(1, num+1):
    print(num, 'x', i, '=', num*i)

#fibonacci series
nterms = 10
n1 = 0
n2 = 1
count = 0
list1 = []
while count < nterms:
    print(n1)
    n3 = n1 +n2
    n1 = n2
    n2 = n3
    count = count+1
    list1.append(count)
print(list1)
# Python program to display all the prime numbers within an interval
a = 100
b = 200
for num in range(a, b+1):
    if num > 1:
        for i in range(2, num):
            if num%i == 0:
                break
        else:
            print(num)

#sum of natural numbers
n = 16
if num < 0:
    print('enter positive number')
else:
    sum = 0
    while num>0:
        sum += num
        num -= 1
    print(sum)

