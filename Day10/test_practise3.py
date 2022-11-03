
for i in range(0,5):
    print(i*i)
    # print(int(math.sqrt(i)))

# if n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 2 to 6, print Weird
# If n is even and greater than 20, print Not Weirdi

n = 3
# for i in range(0, 4):
if n%2 == 0:
    print('notweird')
else:
    print('weird')

for n in range(2, 5):
    if n%2 == 0:
        print('not weird')
for n in range(2, 6):
    if n%2 == 0:
        print('weird')

n = 24
if n%2 == 0:
    if n>20:
        print('weird')

#def is leap year
def is_leap(year):
    if year%4 == 0:
        return True
    else:
        return False
res=is_leap(2011)
print(res)

arr = []
for i in range(1,4,1):
    arr.append(i)
print(arr)


string = 'leetcode'

freq={}
for i in string:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
    for i in string:
        if freq[i]==1:
            print (string.index(i))
        print -1
		


