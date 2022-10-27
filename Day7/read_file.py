#Read files
file = open('file.txt', 'r')
f = file.readlines()
# print(f)
new_list = []
for line in f:
    if line[-1] == '\n':
        new_list.append(line[:-1])
    else:
        new_list.append(line)
print(new_list)

#simply we can use .strip()
for line in f:
    new_list.append(line.strip())
print(new_list)

#writing the file
file = open('file.txt', 'w')
#\n escape chracter
file.write('hello\n')
file.write('iam learning python')
file.close()

