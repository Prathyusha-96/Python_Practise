#Write a program to reverse a string in python.
str = 'python'
print(str[::-1])

##using forloop
for i in range(len(str) -1, -1, -1):
	print(str[i], end=' ')
print("\n")



#Write a program to count vowels and consonants in a string.
str = 'python'
vov = 0
con = 0
for i in range(len(str)):
	if str[i] in ['a', 'e', 'i', 'o', 'u']:
		vov = vov + 1
		print("vowels count is:", vov)
	else:
		con = con + 1
		print("consonents count is:", con)

#Write a program to remove duplicates in a string.
n = 'pythonlobby'
x = []
for i in range(len(n)):
	if n[i] not in x:
		x.append(n[i])
	else:
		pass
for i in range(len(x)):
	print(x[i], end=' ')

print(len(n))


#Python program to count the occurrence of each character in a word.
#Python program to convert lower letter to upper and upper letter to lower in a string.
num = 'ProGrAmm'
x = []
for i in range(len(num)):
	if num[i].islower():
		x.append(num[i].upper())
	elif num[i].isupper():
		x.append(num[i].lower())
for i in range(len(x)):
	print(x[i], end=' ')

#word search
str = 'Iam a boy'
word = 'boy'
if word in str:
	print(f"{word} exist in string")
else:
	print(f"{word} doesn't exist")
#Write a python program to sort letters of word by lower to upper case format.
strn = 'pythONLoBbY'
lower = []
upper = []
for i in range(len(strn)):
	if strn[i].islower():
		lower.append(strn[i])
	else:
		upper.append(strn[i])
result = ' '.join(lower+upper)
print(result)

#Write a program in Python to count lower, upper, numeric and special characters in a string.
n = '@pyThOnlobb!Y34'
numeric = 0
lower = 0
upper = 0
special = 0
for i in range(len(n)):
	if n[i].isnumeric():
		numeric = numeric + 1
	elif n[i].islower():
		lower = lower + 1
	elif n[i].isupper():
		upper = upper + 1
	else:
		special = special + 1
print('num is', numeric)
print('lower char is', lower)
print('upper char is', upper)
print('special char is', special)

#Write a program in Python to remove an empty character from a list sequence.
n = ['name', 'age', '', 'hello']
list1 = list(filter(None, n))
print(list1)

#Python program to convert all the starting letter of a word in upper case format or in the title format.
n = "hello this is pythonlobby"
new_str = n.title()
print(new_str)

for x in "banana":
	print(x)