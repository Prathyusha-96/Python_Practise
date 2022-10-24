import csv
html_output = []
names = []
my_data = []
with open('main.csv', 'r') as new_file:
    # csv_file = csv.DictReader(new_file)
    csv_file = csv.reader(new_file)
    next(csv_file)
    # next(csv_file)
    
    for line in csv_file:
        my_data.append(line)
        # print(type(line))
        my_data.append(line.split(','))
        if line[0] == 'NO reward':
            continue
        names.append(f"{line[0]}, {line[1]}")
    for name in names:
        print(name)

html_output = '\n<ul>'
for name in names:
    html_output += f'\n<li>{name}</li>'
html_output += '\n<ul>'
print(html_output)

#write operation

with open('new_main.csv', 'w') as write_file:
    csv_writer = csv.writer(write_file, delimiter = '-')
    csv_writer.writerows(my_data)



        
        
    

    