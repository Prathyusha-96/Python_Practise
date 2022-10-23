#File Objexts
'''
read (r), write(w), append(a)
the files'''


# f = open('test.txt', 'r')
# print(f.name)
# f.close()
with open('test.txt', 'r') as  f:
	f_contents = f.read()
	print(f_contents, end='')

	# f_contents = f.readline()
	# print(f_contents, end='')

	# f_contents = f.readline()
	# print(f_contents, end='')

	# size_to_read = 5

	# f_contents = f.read(size_to_read)

	# print(f.tell())

	# while len(f_contents) > 0:
	# 	print(f_contents, end='*')
	# 	f_contents = f.read(size_to_read)

 #    