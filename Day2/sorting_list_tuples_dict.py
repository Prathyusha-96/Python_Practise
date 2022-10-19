#sort method
#we have two methods to sort the lists
#using sort func

li = [5, 6, 8, 4, 2, 1, 9 ,3, 0]
s_li = sorted(li, reverse=True)
print(s_li)

#using sort method
li.sort()
print(li)

#for tuples and dict we have use only sort fun
tup = (2, 4, 8, 7, 10, 45)
s_tup = sorted(tup)
print(s_tup)

# dict = {'name': 'john', 'job': 'painter', 'age': 25, 'hobby': 'dancing'}
# s_dict = sorted(dict)
# print(s_dict)

#for negative values
li = [-5, -7, -8, 2, 4, 6]
s_li = sorted(li, key=abs) #using key parameter
print(s_li)

# question sortng employe name age salary
class Employee():
	def __init__(self, name, age, salary):
		self.name = name
		self.age = age
		self.salary = salary

	def __repr__(self):
		return '({}, {}, ${})'.format(self.name, self.age, self.salary)

e1 = Employee('john', 24, 10000)
e2 = Employee('deo', 30, 30000)
e3 = Employee('carl', 35, 20000)

def e_sort(emp):
	return emp.salary

employees = [e1, e2, e3]

# sl_employees = sorted(employees, key=e_sort)

sl_employees = sorted(employees, key=lambda e: e.name) #using lambda func

print(sl_employees)