age = input('enter your age: ')
if int(age) >= 18:
    print('you are eligible for voting')
else:
    print('not eligible')

for n in range(1500, 2700):
    if (n % 7 == 0)  and (n % 5 == 0):
        print(n)

for n in range(1, 10):
    if n % 2 == 0:
        print('even num is', n)
    else:
        print('odd num is', n)

name = 'john' 
print(type(name))
print(name.capitalize())
print(name[::-1])

my_list = ['cat', 'dog', 'rat']

for animal in my_list:
    if animal.startswith('c'):
        print('cat is eating')
    elif animal.startswith('r'):
        print('dog is slepping')
    else:
        print('rat is running')

name ='Prathyusha'
print(name.startswith('P'))

my_list = [1, 2, 3, 4, 5, 1, 2 ,5]
new_list = []
for n in my_list:
    new_list.append(n * 5)
print(new_list) 

count = 0
for n in my_list:
    if n == 2:
        count += 1
print(count)
print(my_list.count(2))

def my_func(mystr):
    return mystr.upper()
name = my_func('john')
print(name)

# my_list = [0, 1, 1, 2, 3, 5, 8, 13, 21] #fibonacci

a = 0
b = 1
list = []
list.append(a)
list.append(b)
for i in range(2, 10):

    list.append(a+b)
    a = list[-2]
    b = list[-1]
print(list)

my_list = [1, 2, 3, 4, 5, 6, 8, 9, 10]
i = 0
while i < len(my_list)+1:
    if i % 2 == 0:
        print('even no is', i)
    else:
        print('odd' , i)
    i += 1
      

        












  
    
    
    