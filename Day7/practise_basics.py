string = 'twinkle twinkle little start'
print('twinkle, \n\ttwinkle, \n\t little, \n\tstar')

import sys

from isort import file
print(sys.version)

import datetime
tday = datetime.date.today()
print(tday)

now = datetime.datetime.now()
print(now)

#area of circle
import math
r = 4
area_of_circle = math.pi*r*r
print(area_of_circle)

first_name = 'john'
last_name = 'deo'
print(last_name + ' ' + first_name)

# data = int(input('enter values'))
# list = data.split(',')
# tuple = tuple(list)
# print(list)
# print(tuple)

file_name = 'abc.java'
file_exten = file_name.split('.')
print(repr(file_exten[-1]))
# f_extns = file_name.split(".")
# print ("The extension of the file is : " + repr(f_extns[-1]))

color_list = ['red', 'green', 'blue', 'black']
# print(color_list[0::3])
print('%s, %s'%(color_list[0], color_list[-1]))

exam_date = (26, 10, 2022)

print('exams will start from: ' "%i/%i/%i"%exam_date )

#print calender
import calendar
y = 2022
m = 10
print(calendar.month(y, m))

import datetime
date1 = datetime.date(2014, 7, 2)
date2 = datetime.date(2014, 7, 11)
result = date2 - date1
print(result)

n = 20
if n <= 17:
    print((n - 17)*2)
else:
    print(n -17)

a = 5
b = 15
c = 25
result = a+b+c
# print(result)
if a == b == c:
    print(result)
else:
    print('not match')

x = [2, 3, 4, 5, 6]
for i in range(len(x)):
	y = x[i]*x[i]
	print(y, end = '')

def my_func():
	str = 'The quick Brow Fox'
	for x in range(len(str)):
		if x == str.upper():
			print("upper case letters are ", x)
		# else:
		# 	print('lowercase letters are', x)
my_func()

