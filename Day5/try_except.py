# the try block  lets you test a block of code for errors.
try:
    print(x) #will generate an exception
except:
    print("An exception occured")
# #many expetions
try:
    print(x)
except NameError:
    print('variable x is not defined')
except:
    print("something went wrong")

try:
    f = open('demofile.txt')
    
except FileNotFoundError:
    print('sorry file does not exist')

except Exception as e:
    print(e)


#Else
#You can use the else keyword to define a block of code to be executed if no errors were raised:
try:
    print('hello')
except:
    print('something went wrong')
else:
    print('nothing went wrong')

try:
    f = open('demo_file.txt')
    # print(f.read())
    # f.close()
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print('executed ....')

#finally block if specified, will be executed regardless if the try block raises an error or not.
try:
    print(x)
except:
    print('something went wrong')
finally:
    print('Executed finally ....')


try:
  f = open("demo_file.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")

#raise exception
# to throw an exception if a condition occurs.
x = -1
if x < 0:
    raise Exception('error')
#You can define what kind of error to raise, and the text to print to the user.

x = 'helloo'

if not type(x) is int:
    raise TypeError('only integers are allowed')