from cgi import print_arguments
import csv
from operator import itemgetter

html_output = ''
names  = []
with open('test.csv', 'r') as data_file:
   csv_data = csv.reader(data_file)
   csv_data = csv.DictReader(data_file)
   for item in csv_data:
    print(item)
   
#    we dont want headers and unnecessiary bad data

   next(csv_data)
   next(csv_data)

   for line in csv_data:
    if line[0] == 'NO reward':
        break
    names.append(f"{line[0]}, {line[1]}")
for name in names:
    print(name)

    print(line)
print(list(csv_data)) 

html_output = f'<p>There are currently {len(names)} members in employe list.Thank you!</p>'
print(html_output)
# html unordered list
html_output = '\n<ul>'
for name in names:
    html_output += f'\n<li>{name}</li>'
html_output += '\n</ul>'
print(html_output)