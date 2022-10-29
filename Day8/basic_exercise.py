previous_num = 0
for i in range(10):
    x_sum = previous_num + i
    print("current num is ", i, "previous num is", previous_num, "sum is", x_sum)
    previous_num = i

#even characters
new_str = "pynative"
print(new_str[0::2])

#remove n characters
remove_str = "pynative"
n = 4
print(remove_str[n:])
print(remove_str[2:])
 

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

if numbers_x[0] == numbers_x[-1]:
    print('True')
else:
    print("False")

if numbers_y[0] == numbers_y[-1]:
    print("True")
else:
    print("False")

my_list = [10, 20, 33, 46, 55]
for x in my_list:
    if x%5 == 0:
        print(x)

str_x = "Emma is good painter, Emma is a write"
res = str_x.count("Emma")
print( res, "times appeared")

#print pattern
rows = 5
for i in range(rows + 1):
    for j in range(i):
        print(i , end=' ')
    print(' ')

#palindrome number
number = 121
original_num = number
reverse_num = 0
while number > 0:
    remainder = number % 10
    reverse_num = (reverse_num * 10) + remainder
    number = number // 10
    print(reverse_num)
if original_num == reverse_num:
    print('True')
else:
    print('False')


list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
list3 = []

for i in list1:
    if i%2 != 0:
        list3.append(i)
for i in list2:
    if i%2 == 0:
        list3.append(i)
print(list3)

num = 7632
# new_num = str(num)[::-1]
# print(new_num.strip(''))
while num > 0:
    digit = num % 10
    num = num // 10
    print(digit, end=' ')

# multiplication table from 1 to 10

for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end=" ")
    print("\t\t")
    


for i in range(6, 0, -1):
    for j in range(0, i-1):
        print('*' , end=' ')
    print(' ')

def exponent(base, exp):
    print(base ** exp)
exponent(5, 4)
        

