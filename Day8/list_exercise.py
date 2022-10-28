#Python program to interchange first and last elements in a list

list = [21, 25, 65, 70, 31]
# list[0] = num1
# list[4] = num2
num1 = list[0]
num2 = list[-1]
list[0] = num2
list[-1] = num1
print(list)

#swap twoelements in a list
list1 = [23, 20, 45, 52]
list1[0], list1[2] = list1[2], list1[0]
print(list1)

#ways to find length of lists
list2 = ['apple','banana','kiwi','cherry'] 
print(len(list2))

#using counter
count = 0
for i in list2:
    count += 1
print(count)

#max of two numbers

def max_of_two(a,b):
    if a > b:
        print(a)
    if b > a:
        print(b)
max_of_two(12, 25)
#min of two numbers

def min_of_two(a, b):
    if a < b:
        print(a)
    if b < a:
        print(b)
min_of_two(2, 4)

# element exist in list
# my_list = ['john','apple', 'deo', 'cherry']
# for i in my_list:
#     if i == 'john':
#         print('exist')
    
list4 = [1, 2, 3, 4, 5]
for i in list4:
    if i == 6:
        print('exist')
    # else:
    #     print('not exist')

list5 = [1, 2, 3, 4, 5]
i = 6
if i in list5:
    print('exist')
else:
    print('not exist')

#diff ways to clear a list 
mylist = [1, 5, 6, 4, 7]
# mylist.clear()
# print(mylist)

#reverse a list
mylist.reverse()
print(mylist[::-1])

#sum and average 
mylist1 = [1, 2, 3, 4, 5]
sum_of_list = sum(mylist1)
avg = sum_of_list/len(mylist1)

print(sum_of_list)
print(avg)

#multiply all numbers
import math
mylist2 = [1, 2, 3, 6, 8]
print(math.prod(mylist2))

# count even and odd no
list7 = [2, 5, 25, 65, 8, 6]
even_count = 0
odd_count = 0
for i in list7:
    if i%2 == 0:
        even_count += 1
    else:
        odd_count += 1
print('even no are: ', even_count)
print('odd no are: ', odd_count)

#find positive numbers
list8 = [5, -2, 6, -9, 7]
for num in list8:
    if num>=0:
        print('positive numbers are', num)
    elif num<0:
        print('negative numbers are',num)

#remove list of list 
list9 = [5, 6, [], 8, 9, []]
res = [ele for ele in list9 if ele != []]
print(str(res))
        
    