def myfunc(name, age):
    print(name, age)
myfunc('john', 25)

#variable length
def func1(*args):
    for i in args:
        print(i)

func1(30, 20, 42)

#calculation
def add_sub(a,b):
    return a+b , a-b
res = add_sub(40, 10)
print(res)

def myfunc(name, salary='19000'):
    print(name, salary)
myfunc('john')

def outer(a, b):
    
    def inner():
        return a+b
    inner()
outer(2, 3)

#recursive func
def addition(num):
    if num:
        return num + addition(num -1)
    else:
        return 0
res = addition(10)
print(res)

def student(name, age):
    print(name, age)
student('deo', '35')
student_new = student
student_new('deo', '35')

print(list(range(4, 30, 2)))
