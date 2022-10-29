#plindrome check on string
new_str = "wov"
reverse_str = new_str[::-1]
print(reverse_str)
if new_str == reverse_str:
    print("True")
else:
    print("False")

l = []
for n in range(2000, 3200):
    if (n%7 == 0) and (n%5 != 0):
        l.append(str(n))
print(l,end=',')

import math
n = 8
print(math.factorial(n), end=',')

my_string = "python"
x = 0
for i in my_string:
    x = x + 1
    print(my_string[0:x])
for i in my_string:
    x = x-1
    print(my_string[0:x])

#i*i
d = dict()
for i in range(1, 9):
    d[i] = i*i
print(d)

new_list = 34,24,52,62,75
l = []
l.append(new_list)
print(l)

values= 34,12,52,62,75
l=values.split(",")
t=tuple(l)
print (l)
print (t)

#sort
str1 = 'without', 'hello', 'bag', 'dies'
for items in str1:
   items.sort()
print(','.join(items))