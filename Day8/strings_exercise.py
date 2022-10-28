#reverse words

# string = 'i am learning python'
# s = string.split()[::-1]
# l = []
# for i in s:
#     l.append(i)
# print(" ".join(l))

#remove ith character
# test_str = "Prathyusha"
# new_str = test_str[:2] + test_str[3:]
# print(new_str)

#find even length of words
# words = "iam in hyd city"
# s = words.split(' ')
# for i in s:
#     if len(i) % 2 == 0:
#         print(i)

#upperhalfcase
# string = "prathyusha"
# print(string[0:3] + string.upper()[3:])

#capitalize the first and last
my_str = "iam learning python"
s = my_str.split()
#["iam", "learning", "python"]
a = []
for word in s:
    x=word[0].upper()+word[1:-1]+word[-1].upper()
    a.append(x)
a = " ".join(a)
print(a)

#contains all vowels


# str1 = 'james'
# print(str1[0:-1])
# str1 = "JhonDipPeta"
# print(str1[4:7])
# str2 = "JaSonAy"
# print(str2[2:5])

#remove ith character from the string

my_str = 'Prathyusha'
print(my_str[0] + my_str[2:])

my_str = 'james'
# result = ""
# for i in range(len(my_str)):
#     if i%2 == 0:
#         result =result + my_str[i]
# print(result)
print(my_str[0:len(my_str):2])
#strat:end:
list1 = []

for i in range(4, 30, 2):
    list1.append(i)
print(list1)

list1 = [12, 15, 46, 84]
print(list1[::-1])

number = 789456
print(str(number)[::-1])






