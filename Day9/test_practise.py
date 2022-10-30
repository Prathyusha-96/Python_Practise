nums = [2, 7, 8, 10]
target = 9
if nums[0]+nums[1] == target:
    print([nums.index(2), nums.index(7)])

n = len(nums)
for i in range(n):
    for j in range(i + 1, n):
        if nums[i] + nums[j] == target:
            print(i, j)



nums = [3,2,4]
target = 6
n = len(nums)
for i in range(n):
    for j in range(i + 1, n):
        if nums[i] + nums[j] == target:
            print(i, j)

#palindrome
x = 121
num = x
reverse_num = 0
while x > 0:
    remainder = x % 10
    reverse_num = (reverse_num * 10) + remainder
    x = x // 10
    print(reverse_num)
    if num == reverse_num:
        print('True')
    else:
        print('False')
    
#another solution
reverse_num = int(str(x)[::-1])
print(reverse_num)
if x == reverse_num:
    print('True')
else:
    print('False')


#merge the two lists 
list1 = [1, 2, 4]
list2 = [1, 3, 4]
list1.extend(list2)
s_li = sorted(list1)
print(s_li)


#length of the last word
s = "Hello World"
new_s = s.split(" ")
print(len(new_s[-1]))

#ex2
s = "   fly me   to   the moon  "
new_str = s.split(" ")
print(new_str)
print(len(new_str[-3]))

#ex3
s = "luffy is still joyboy"
new_str = s.split(" ")
print(new_str)
print(len(new_str[-1]))

#add strings
num1 = "11"
n1 = int(num1)
print(n1)
num2 = "123"
n2 = int(num2)
print(n2)
print(str(n1 +n2))

#ex2
num1 = "456"
n1 = int(num1)
num2 = "77"
n2 = int(num2)
print(n1 + n2)

#third max number
nums = [3,2,1]
print(min(nums))

nums = [1,2]
print(max(nums))

nums = [2,2,3,1]
print(min(nums))

#fizzbuzz

list1 = []
for i in range(1, 4):
    # list1.append(i)
    if i % 3 == 0:
        list1.append('fizz')
    else:
        list1.append(i)
    # print(str(i))
    
print(list1)
