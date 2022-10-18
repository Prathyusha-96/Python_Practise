def sum_function(a, b):
	print(a+b)
sum_function(2, 3)

def sub(a, b):
	print(a-b)
sub(5, 3)

def mul(a, b):
	print(a*b)
mul(5, 7)

#
dict = {'0':1, '1':2, '2':3}
x = '2'
if x in dict.keys():
	print(True)
else:
	print(False)
	

dict1 = {0:"value1", 1:"value2"}
for key,value in dict.items():
	print(f"value of key {key} is {value}")

dict2 = {0:'value 1', 1:'value 2', 2:'value 3'}
print(dict.keys())
print(dict.values())

dict_1 = {0:'Value 1', 1:'Value 2', 2:'Value 3'}
keys_to_remove = [0, 1]
print()

#Define a function that accepts roll number and returns whether the student is present or absent.

def detail(roll):
	x = [24, 32, 27, 25]
	if roll in x:
		print(f"roll number {roll} is present")
	else:
		print(f"roll number {roll} is absent")

roll = 28
detail(roll)

#Define a function in python that accepts 3 values and returns the maximum of three numbers.

def max(a, b, c):
	if a > b and a > c:
		print(f"{a} is the max num")
	elif b > c and b > a:
		print(f"{b} is the max num")
	else:
		print(f"{c} is the max num")
max(30, 25, 10)


def even_or_odd(a):
	if a % 2 == 0:
		print(f"{a} is even num")
	else:
		print(f"{a} is odd num")
even_or_odd(5)

#define a function which counts vowels and consonant in a word.
def func(word):
	vov = 0
	con = 0
	for i in range(len(word)):
		if word[i] in ['a', 'e', 'i', 'o', 'u']:
			vov = vov + 1
		else:
			con = con + 1
	print("count of vowel is", vov)
	print("count of con is", con)
x = 'prathyusha'
func(x)


#Define a function that returns Factorial of a number.
def factorial(a):
	fact = 1
	while a != 0:
		fact *= a
		a = a - 1
	print('factorial is', fact)
factorial(6)

#Define a function that accepts lowercase words and returns uppercase words.
def func(word):
	print(word.upper())
word = 'prathyusha'
func(word)

#Define a function that accepts radius and returns the area of a circle.
def area(radius):
	area = 3.14*radius*radius
	return area
radius = 4
print(area(radius))

#write a Python function to find the Max of three numbers.
def max_of_two(a,b):
	if a > b:
		print (a)
	else:
		print (b)
max_of_two(10, 5)

#write a programm to sum all the list
def sum_of_all(list):
	list = [8, 7, 0, 2, 3]
	print (sum(list))

sum_of_all(list)

#another solution

def sum(numbers):
	total = 0
	for x in numbers:
		total += x
	return total
print(sum((10, 2, 7, 3)))

#multiplication of all numbers
def mul(numbers):
	total = 1
	for x in numbers:
		total *= x
	return total
print(mul((10, 2, 7, 3)))

# write a programm to reverse a string
def reverse():
	str = '123abcd'
	print(str[::-1])
reverse()

#using forloop
def reverse_str():
	str = 'python12'
	for x in range(len(str) -1, -1, -1):
		print(str[x], end=' ')
reverse_str()
	
#Write a Python function that accepts a string and calculate 
#the number of upper case letters and lower case letters
def my_func():
	str = 'The quick Brow Fox'
	for x in range(len(str)):
		if x == str.upper():
			print("upper case letters are ", x)
my_func()



		