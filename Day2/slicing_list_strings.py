my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#          0  1  2  3  4  5  6  7  8  9
#         -10-9 -8 -7 -6 -5 -4 -3 -2 -1 

print(my_list[0:9])
print (my_list[2:-5:1])
print(my_list[0:-1])
print(my_list[-2:-9])
print(my_list[:-8])
print(my_list[::-1])


sample_str = 'Learning Python'

print(len(sample_str)) 
#reverse the str
print(sample_str[::-1])

#get the second word
print(sample_str[-6:])

#get the first word
print(sample_str[:-7]) #or [:8]

print(sample_str[1:9])

