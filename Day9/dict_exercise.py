#convert lists into dict
from unittest import result


keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dict1 = dict(zip( keys, values))
print(dict1)

#merge two dict into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict1.update(dict2)
print(dict1)

sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
print(sampleDict['class']['student']['marks']['history'])

#initialize dictionary with default values
#we can use the fromkeys() method
#returns a dictionary with the specified keys and the specified value.

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

result = dict.fromkeys(employees, defaults)
print(result)

# Create a dictionary by extracting the keys from a given dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}
keys = ["name", "salary"]
res = dict()
for k in keys:
    res.update({k: sample_dict[k]})
print(res)

#Delete a list of keys from a dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

keys = ["name", "salary"]
for k in keys:
    sample_dict.pop(k)
print(sample_dict)

#Check if a value exists in a dictionary
sample_dict = {'a': 100, 'b': 200, 'c': 300}
if 200 in sample_dict.values():
    print('200 is present in dict')

print(sample_dict.get('b'))


#Rename key of a dictionary
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
sample_dict["location"] = sample_dict.pop("city")

print(sample_dict)
