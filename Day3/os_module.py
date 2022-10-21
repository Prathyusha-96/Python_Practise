import os
from datetime import datetime

# print(os.getcwd()) #current working dir(directory)

#change dir

# os.chdir(':\Users\Lenovo\Desktop\Python_Practise\Day3\')
# print(os.chdir())

#to create directory
# os.mkdir('newdir')
# os.makedirs('newdir/subdir')
# print(os.listdir())

#to delete directory
# os.rmdir('newdir')
os.removedirs('newdir/subdir')
print(os.listdir())

#renaming files
# os.rename('module.py', 'os_module.py')
# print(os.listdir())

#to know the modified time
# mod_time = os.stat('module.py').st_mtime
# print(datetime.fromtimestamp(mod_time))

#to find all the files and folders  on the desktop
# for dirpath, dirname, filenames in os.walk('/Users/Lenovo/Desktop/'):
# 	print('current path:', dirpath)
# 	print('directories:', dirname)
# 	print('files:', filenames)
# 	print()

#os path
print(os.path.basename('/tmp/test.txt')) #print filename
print(os.path.dirname('/tmp/test.txt')) #print dirname
print(os.path.split('/tmp/test.txt'))   
print(os.path.exists('/tmp/test.txt')) #if it exists or not