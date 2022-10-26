#while loop
count  = 0
while(count < 3):
    count += 1
    print('hello')
    
a = [1, 2, 3, 4]
while a:
    print(a.pop())
Prints all letters except 'o' and 't'

#conditional statement
i = 0
a = 'python'
while i < len(a):
    if a[i] == 'o' or a[i] == 't':
        i += 1
        continue
    print('current letter is:', a[i])
    i += 1
n = 1
while n < 5:
    print('hello world')
    n += 1
#break
n = 1
while n < 5:
    print('prathyusha')
    n = n+1
    if n == 3:
        break
#continue
n = 1
while n < 5:
    print('prathyusha')
    n += 1
    if n == 3:
        continue
n = 1
while n < 6:
    if n == 2:
        n += 1
        continue
    print('python')
    n += 1

i = 1
while i < 6:
    print(i)
    i += 1

i = 1
while i < 5:
    print(i)
    if i == 3:
        break
    i += 1

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
    
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print('i is no longer than 6')

#if-elif-else in while loop
z = 0
while z < 3:
    if z == 0:
        print('z is', z)
        z += 1
    elif z == 1:
        print('z is', z)
        z += 1
    else:
        print('z is', z)
        z += 1

#adding elements to list using while loop
my_list = []
i = 0
while i < 5:
    my_list.append(i)
    i += 1
print(my_list)

#to print number series
n = 5
while n <= 15:
    print(n, end=',')
    n += 5


for i in range(5, 15):
    print(i, end=',')
    
my_tuple = (10, 20, 30, 40, 50, 60)
i = 0
while i < len(my_tuple):
    print(my_tuple[i])
    i += 1

for i in my_tuple:
    print(i)

my_list = [2,4,5,6,8]
adition = 0
i = 0
while i < len(my_list):
    adition += my_list[i]
    i += 1
print(adition)

#popping out using while  loop
fruits = ['apple', 'kiwi', 'cherry']
i = 0
while i < len(fruits):
    print(fruits.pop())
print(fruits)

#printing all letters except some using while loop
i = 0
word = 'Hello'
while i < len(word):
    if word[i] == 'e' or word[i] == 'o':
        i += 1
        continue
    print(word[i])
    i += 1

#factorial
n = 5
f = n
r = 1
while f != 0:
    r *= f
    f -= 1
print('factorial of n is:',r)

import math
n = 4
print(math.factorial(n))
