# lambda function
# it is anonymous function
# it can takes no.of arguments. but only have one expression

# syntax

x = lambda a: a +10
print(x(5))

a = 5
b = 8
x = lambda a, b: a*b
print(x(a, b))

#The power of lambda is better shown when you use them as an anonymous function inside another function.

def myfunc(n):
	return lambda a: a*n

my_num = myfunc(2)
my_doubler = myfunc(10)
print(my_doubler(20))
print(my_num(10))