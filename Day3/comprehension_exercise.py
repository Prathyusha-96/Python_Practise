# Find all of the numbers from 1-1000 that are divisible by 7
# my_list = [n for n in range(1, 1000) if n%7 == 0]
# print(my_list)

#Find all of the numbers from 1-1000 that have a 3 in them

my_list = [n for n in range(1, 100) if '3' in str(n)]
print(my_list)

# Count the number of spaces in a string

str = 'lerning python by watching the videos from corey'
my_str = [s for s in str if s == ' ']
print(len(my_str))

# Create a list of all the consonants in the string “Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams”

str = "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"
consonant_list = [letter for letter in str if letter not in 'a, e, i, o, u, " "']
print(consonant_list)

# Get the index and the value as a tuple for items in the list “hi”, 4, 8.99, ‘apple’, (‘t,b’,’n’). 
# Result would look like (index, value), (index, value)

items = ['hi', 4, 8.99, 'apple', ('t,b','n')]
result = [(index, items) for index, items in enumerate(items)]
print(result)

# Find the common numbers in two lists (without using a tuple or set) 
# list_a = 1, 2, 3, 4, list_b = 2, 3, 4, 5

list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]
common_num = [n for n in list_a if n in list_b ]
print(common_num)

# Get only the numbers in a sentence like ‘In 1984 there were 13 instances of a 
# protest with over 1000 people attending’

sentance = "In 1984 there were 13 instances of a protest with over 1000 people attending"
numbers = [int(letter) for letter in sentance if letter in ['1','2','3','4','5','6','7','8','9','0']]
print(numbers)

#

words = sentance.split()
result = [num for num in words if not num.isalpha()]
print(result)

# Find all of the words in a string that are less than 4 letters

str = "my name is pra thyusha pyt ram"
new_str = str.split()
result = [word for word in new_str if len(word) <= 4]
print(result)

list_a = [1, 2, 3,4,5,6,7,8,9]
list_b = [2, 7, 1, 12]
result = [(a, b) for a in list_a for b in list_b if a == b]
print(result)

result1 = [i for i in range(1, 1001) if i%8 == 0]
print(result1)

# result2 = [n for n in range(1, 1000) if '6' in str(n)]
# print(result2)

string = "Practice Problems to Drill List Comprehension in Your Head"
result = [s for s in string if s == ' ']
print(len(result))

remv_vowel = [letter for letter in string if letter != 'a,e,i,o,u']
print(remv_vowel)


