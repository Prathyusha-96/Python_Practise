#list in comprehensions


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# i want 'n' for each 'n'in nums

my_list = []
for n in nums:
	my_list.append(n)
print(my_list)

#using comprehension

my_list = [n for n in nums]
print(my_list)

#n*n for each n in nums

my_list = [n*n for n in nums]
print(my_list)

#map: everything in the list through a certain function
#lambda is a anonymous function

my_list = map(lambda n: n*n, nums)
print(my_list)

#'n' for each 'n' in nums if 'n' is even

my_list = []
for n in nums:
	if n%2 == 0:
		my_list.append(n)
print(my_list)

#comprehension list
my_list = [n for n in nums if n%2 == 0]
print(my_list)

#using filter
my_list = filter(lambda n: n%2 == 0, nums)
print(my_list)

#I want a(letter, num)pair of each letter in 'abcd' and each number in '0123'
my_list = []
for letter in 'abcd':
	for num in range(4):
		my_list.append((letter, num))
print(my_list)

#using comprehension
my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
print(my_list)

'''
DICTIONARY COMPREHENSIONS
'''
name = ['python', 'javascript', 'html', 'css', 'react']
rating = [5, 6, 5, 8, 9]
print (zip(name, rating))

#using loop
my_dict = {}
for name, rating in zip(name, rating):
	my_dict[name] = rating
print(my_dict)

# using dict comprehension
# my_dict = {name: rating for name, rating in zip(name, rating) if name != 'css'}
# print(my_dict)

#set comprehension
nums = [1, 1, 2, 5, 8, 6, 7, 4, 4, 3, 5]
my_set = set()
for n in nums:
	my_set.add(n)
print(my_set)

#using comprehension
my_set = {n for n in nums}
print(my_set)

#GENERATOR EXPRESSIONS
#i want to yield n*n for n in each nums
nums = [1, 2, 3, 4, 5, 6]
def gen_func(nums):
	for n in nums:
		yield n*n
		
my_gen = gen_func(nums)
for i in my_gen:
	print (i)

#using comprehension
my_gen = (n*n for n in nums)
for i in my_gen:
	print (i)