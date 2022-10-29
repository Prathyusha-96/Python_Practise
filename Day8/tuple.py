tuple1 = (10,20,30,40,50)
print(tuple1[::-1])

tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
print(tuple1[1][1])

tuple1 = (10, 20, 30, 40)
a, b, c, d = tuple1
print(a)
print(b)
print(c)
print(d)

tuple1 = (11, 22)
tuple2 = (99, 88)
tuple1, tuple2 = tuple2, tuple1
print(tuple1)
print(tuple2)

tuple1 = (11, 22, 33, 44, 55, 66)
tuple2 =tuple1[3:-1]
print(tuple2)

tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0] = 222
print(tuple1)

tuple1 = (50, 10, 60, 70, 50)
print(tuple1.count(50))

var= "James Bond"
print(var[2::-1])

var = "James" * 2  * 3
print(var)

x = 36 / 4 * (3 +  2) * 4 + 2
print(x)

my_list = ['john','apple', 'deo', 'cherry']
for i in my_list:
    if i == 'john':
        print('exist')

lst=[ 1, 6, 3, 5, 3, 4 ]
i=7
if i in lst:
    print('exist')
else:
    print('does not exist')

#while loop
i = 1
while i <= 10:
    print(i)
    i += 1

# #print pattern

rows = 5
for i in range(1, rows + 1):
    # print(i)
    for j in range(1, i +1):
        print(j , end=' ')
       
    print(' ')

s = 0
n = 10
for i in range(1, n + 1, 1):
    s += i
print(s)


#The number must be divisible by five
# If the number is greater than 150, then skip it and move to the next number
# If the number is greater than 500, then stop the loop

numbers = [12, 75, 150, 180, 145, 525, 50]
for i in numbers:
    if i % 5 == 0 and i < 150 and i < 500:
        print(i)

       


    
       

