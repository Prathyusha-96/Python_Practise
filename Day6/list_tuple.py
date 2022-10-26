fruits = ['cherry', 'kiwi', 'apple']
fruits.append('strawberry')
fruits[1] = 'blueberry'
print(fruits)

#swap
#List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
list = [23, 65, 19, 90]
num1 = list[0]
num2 = list[2]
list[0] = num2
list[2] = num1
print(list)

#method 2

list[0],list[2] = list[2],list[0]
print(list)

