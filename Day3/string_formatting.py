#string formatting operations for dicts, lists, numbers, dates

# using .format for  dicts
person = {'name': 'john', 'age': 25}

# using concatination'

# sentance = 'My name is ' + person['name'] + ' and I am ' + str(person['age']) + ' years old. '
# print(sentance)

# using .format method
# sentance = 'My name is {} and I am {} years old.' .format(person['name'], person['age'])
# print(sentance)

#placed index
sentance = 'My name is {0} and I am {1} years old.' .format(person['name'], person['age'])
print(sentance)

tag = 'h1'
text = 'THis is a headline'
sentance = '<{0}>{1}</{0}>'.format(tag, text)
print(sentance)

#usign list
li = ['jhon', 25]
sentance = 'My name is {0[0]} and I am {0[1]} years old.' .format(li)
print(sentance)

class person():
	def __init__(self, name, age):
		self.name = name
		self.age = age
p1 = person('jack', '29')

sentance = 'My name is {0.name} and I am {0.age} years old.'.format(p1)
print(sentance)

#passing some keywords into placeholders

sentance = 'My name is {name} and I am {age} years old.'.format(name='deo', age='33')
print(sentance)

#keyword arguments
person1 = {'name': 'Tom', 'age': 26}
sentence = 'My name is {name} and I am {age} years old.'.format(**person1)
print(sentence)

# using Numbers

for i in range(1, 11):
	sentence = 'The value is {:03}'.format(i) #digits
	print(sentence)

#decimals

pi = 3.14159265

sentence = 'pi is equal to {:.2f}'.format(pi) #decimal
print(sentence)

sentence = '1 Mb is equal to {:,.2f}'.format(1000**2)
print(sentence)

sentence = '1 Tb is eual to {:,.2f}'.format(1000**3)
print(sentence)

sentence = '1 GB is eual to {:,.2f}'.format(1000**5)
print(sentence)

# using dates
import datetime
my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)

# FORMATTING OPTIONS
# %B IS MONTH
# %d is day
# %Y IS YEAR
sentence = '{:%B %d, %Y}'.format(my_date)
print(sentence)