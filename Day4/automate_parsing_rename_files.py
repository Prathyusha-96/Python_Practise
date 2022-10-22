# automate parsing and rename files
import os

os.chdir('/Users/Lenovo/Desktop/my_folder')

#change the file extension
for f in os.listdir():
	# print(f)
	# print(os.path.splitext(f))
	f_name, f_ext = os.path.splitext(f)

	f_title, f_proff= f_name.split('-')

	f_title = f_title.strip()
	f_proff = f_proff.strip()
	# f_num = f_num.strip()

#usng string formatting method
	print('{}-{}-{}'.format(f_title, f_proff, f_ext))

	
# new_name = '{}-{}-{}'.format(f_title, f_proff, f_ext)
# os.rename(f, new_name)