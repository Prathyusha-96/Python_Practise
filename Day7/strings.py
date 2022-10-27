# string methods
mystr = "    john  "

# #it can remove the spaces
print(mystr.strip())

# #len
mystr = 'prathyusha'
print(len(mystr))
# #lower
mystr = 'pRAThyusha'
print(mystr.lower())

# #upper
mystr = 'johnDeo'
print(mystr.upper())

#CAPITALIZE
mystr = 'john'
print(mystr.capitalize())

# #split
mystr = 'tim john deo cris'
print(mystr.split(' '))

#slice operators
#[start:stop:step]

name = 'Prathyusha'
print(name[0:-1])
# #reverse string
print(name[::-1])

fruits = ['apple', 'pears', 'strawberry']
# #insert another fruit
fruits[0:0] = 'b'
print(fruits)


# we can use these methods in strings and lists
#find

string = 'prathyusha'
print(string.find('y'))

#count
print(string.count('t'))

list = [1, 2, 5, 4, 2, 3, 1]
print(list.count(1))

string1 = 'hello'
if string1.count('-')>0:
    print('not good')
else:
    print('good')

