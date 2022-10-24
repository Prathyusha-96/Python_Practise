#duck typing and easier to ask forgiveness than permission (EAFP)
class Duck:

    def quack(self):
        print('Quack,quack')
    def fly(self):
        print('Flap, flap')
class Person:

    def quack(self):
        print("I'am quacking like a duck")
    def fly(self):
        print("I'am flapping like a duck")

def quack_and_fly(thing):
    #non-duck-typed(non-pythonic)
    if isinstance(thing, Duck):
        thing.quack()
        thing.fly()
    else:
        print('This has to be duck')
    thing.quack()
    thing.fly()
    
    #LBYL(Look before you leap)(non-pythonic)
    if hasattr(thing, 'quack'):
        if callable(thing.quack):
            thing.quack()
    if hasattr(thing, 'fly'):
        if callable(thing.fly):
            thing.fly()
    #EAPF (Pythonic)
    try:
        thing.quack()
        thing.fly()
        thing.bark()
    except AttributeError as e:
        print(e)
    print()
d = Duck()
quack_and_fly(d)
p = Person()
quack_and_fly(p)

#Example1
person = {'name': 'john', 'age': 25, 'job': 'programmer'}
person = {'name': 'john', 'age': 25}

#LBYL (non pythonic)
if 'name' in person and 'age' in person and 'job' in person:
    print("I'm {name}, I'm {age} years old and I am a {job}".format(**person))
else:
    print('missing some keys')

#EAPF (PYTHONIC)
try:
    print("I'm {name}, I'm {age} years old and I am a {job}".format(**person))
except KeyError as e:
    print("missing {} key".format(e))

# Example2
my_list = [1, 2, 3, 4, 5, 6, 7]

#lbyl
if len(my_list) > 6:
    print(my_list[6])
else:
    print('that index does not exist')

# pythonic
try:
    print(my_list[7])
except IndexError:
    print('that index does not exist')

#example 3
import os
my_file = 'demo_file.txt'

#Race condition
if os.access(my_file, os.R_OK):
    with open(my_file) as f:
        print(f.read())
else:
    print('file can not be accessed')
#No Race condition
try:
    f = open(my_file)
except IOError as e:
    print('file can not be accesed')
else:
    with f:
        print(f.read())

