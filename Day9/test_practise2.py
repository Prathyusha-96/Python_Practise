#plus one
list1 = [1, 2, 3] 
list2 = []
s = [str(i) for i in list1]
res = int("".join(s))
list2.append(res+1)
print(list2)

#ex2
# digits = [4, 3, 2, 1]
# digits[-1] = digits[-1] + 1
# print(digits)

#ex3
# digits = [9]


#print single number
n = [2,2,1]
print(sum(list(set(n))*2)-sum(n))


nums = [4,1,2,1,2]
print(sum(list(set(nums))*2)-sum(nums))

#sqrt
import math
x = 4
print(math.sqrt(x))

x = 8
print(math.sqrt(x))

