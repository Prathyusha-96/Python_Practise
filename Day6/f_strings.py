#f strings
first_name = 'John'
last_name = 'Deo'

#string format
sentence = 'My name is {} {}'.format(first_name, last_name)
print(sentence)

#f string(formatted string)
sentence = f'My Name is {first_name} {last_name}'
print(sentence)

person = {'name': 'Cris', 'age': 25}
result = 'My Name is {name} and I am {age} years old'.format(**person)
print(result)

#f string
result = f"My name is {'name'} and iam {'age'} years old"
print(result)

#calculation
calculation = f'7 times 8 is equal to {7*8}'
print(calculation)
a = 5
b = 9
add = f'the sum of 5 and 9 is {5 + 9}'
print(add)

for n in range(1,10):
    sentence = f'The value is {n:02}'
    print(sentence)

pi = 3.14159265
sentence = f'Pi is equal to {pi:.5f}'
print(sentence)

NAME = 1
Name = 2
name = 3
print(NAME)
print(name)
print(Name)
