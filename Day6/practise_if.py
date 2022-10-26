

x = 2
y = 3
if x == y and x + y == 5:
    print('correct')
if x == y or x+y == 5:
    print('right')
sub1 = 90
sub2 = 85
sub3 = 75
average = (sub1+sub2+sub3)/3
print(average)
if average > 90:
    print('grade is: A')
elif average >= 80 and average < 90:
    print('grade is B')
elif average >= 70 and average < 80:
    print('grade is C')
elif average >= 60 and average < 70:
    print('grade is D')
else:
    print('grade is E')

age = input('enter your age')
if int(age)>=4 and int(age)<17:
    print('kid has access granted')
else:
    print('no access')

a = 10
b = 12
c = 20
if a>b and a>c:
    print(a)
elif b>c and b>a:
    print(b)
else:
    print(c)

name = 'prathyusha'
age = 20
score = 80
if (age >= 17 and age < 21 and score >= 80):
    
    print('you are eligible for loan')
else:
    print('not eligible')

char = 'P'
if char == char.upper():
    print('upper case letter')
else:
    print('lowercase letter')

char = 'a'
asscii_value = ord(char)
if asscii_value >= 65 and asscii_value <= 90:
    print('upper case letter')
elif asscii_value >= 97 and asscii_value <= 122:
    print('lowercase letter')
else:
    print('none')


a = 3
b = 2
c = 3
if (c==(a**2)+(b**2)**(1/2)):
    print('triangle is right angle')
elif (a==b or b==c or a==c):
    print("triangle is isoceless")
else:
    print('triangle is not of known type')

num = 6
n = 2
result = num**n

print(result)
if (result%2==0):
    print('n is even')
else:
    print('n is odd')

#prime numbers
x = 13
for i in range(2,x):
    if x % 2 == 0:
       print('prime number')
    
    else:
       print('not a prime number')
       break


