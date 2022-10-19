#LEGB
#Local, Enclosing, Global, Built - in

#local scope
# a variable created inside function belongs to the local scope of that function, and can only be used inside that function

def my_func():
	x = 100
	print(x)
my_func()

#function inside function
def test_func():
	x = 'local x'
	def test():
		x = 'loacl y'
		print(x)
	test()
	print(x)
test_func()

#Global scope 
# a Variable created in tha main body of the python code belongs to the global variable
# global varibleas are available from any global or local scope

x = 400

def my_func():
	print(x)
my_func()
print(x)

#global keyword

# If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.

# The global keyword makes the variable global.

def my_func():
	global z
	z = 'hello'
	y = 'world'
	print(y)
  
my_func()
print(z)

# Also, use the global keyword if you want to make a change to a global variable inside a function.
x = 200
def myfunc():
	global x
	x = 500
myfunc()
print(x)



