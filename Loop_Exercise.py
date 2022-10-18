import sys
print(sys.version)
print(sys.executable)


#ForLoop
numbers = [12, 75, 150, 180, 145, 525, 50]
 
for num in numbers:
	if num > 500:
		break
	elif num > 150:
		continue
	elif num % 5 == 0:

		print(num)
	

#count the number of digits

num = 7586925
counter = 0
while num != 0:
	num = num // 10
	counter = counter + 1
	print("total digits are:", counter)

#reverse number pattern

print("number pattern")
row = 5
for i in range(1, row+1):
	for j in range(1, i+1):
		print(j, end=' ')
	print("")

#Write a program to reverse a string in python.
str = 'python'
print(str[::-1])

##using forloop
for i in range(len(str) -1, -1, -1):
	print(str[i], end=' ')
print("\n")

