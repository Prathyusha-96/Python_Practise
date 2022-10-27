#functions
# def add(a,b):
#     return (a+b) ** 2
# print(add(5,6))

# def printString(string):
#     print(string)
# printString('HII')

# def myFunc():
#     print('hello')
# myFunc()

#optional parameters
def myFunc(x=7, y=2):
    print(x)
    print(y)
    # if y == 1:
    #     print('y is not 1')
    # else:
    #     print('y is  1')
myFunc()

#try and except
text = 'prathyusha'
# number = int(text) #giving an error
# print(text)
try:
    number = int(text)
    print(text)
except:
    print('error occured')

#global and local

var = 9

def func():
    global var
    var = 50
    x = 10
    print(x)  
def func2():
    y = 25
    print(y)
     
func2()

func()
    
print(var)