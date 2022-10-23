import csv
data = []

with open('csv.txt', 'r') as file:
	csv_reader = file.readlines()
	for line in csv_reader:
		data.append(line.split(','))

#dictonary reader
# with open('csv.txt', 'r') as csv_file:

#     csv_reader = csv.DictReader(csv_file)
#     for line in csv_reader:
#     	print(line['email'])

fieldnames = ['first_name', 'last_name', 'email']


with open('new_csv.csv', 'w') as new_file:
	csv_writer = csv.writer(new_file, delimiter='-')
	# csv_writer.writerow(fieldnames)
	# csv_writer.writerows(data)
	# csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='-')
	# csv_writer.writeheader()
	csv_writer.writerows(data)
    	

    

    

    
    
    
    
# importing the csv module
# import csv
	
# # my data rows as dictionary objects
# mydict =[{'branch': 'COE', 'cgpa': '9.0', 'name': 'Nikhil', 'year': '2'},
# 		{'branch': 'COE', 'cgpa': '9.1', 'name': 'Sanchit', 'year': '2'},
# 		{'branch': 'IT', 'cgpa': '9.3', 'name': 'Aditya', 'year': '2'},
# 		{'branch': 'SE', 'cgpa': '9.5', 'name': 'Sagar', 'year': '1'},
# 		{'branch': 'MCE', 'cgpa': '7.8', 'name': 'Prateek', 'year': '3'},
# 		{'branch': 'EP', 'cgpa': '9.1', 'name': 'Sahil', 'year': '2'}]
	
# # field names
# fields = ['name', 'branch', 'year', 'cgpa']
	
# # name of csv file
# filename = "university_records.csv"
	
# # writing to csv file
# with open(filename, 'w') as csvfile:
# 	# creating a csv dict writer object
# 	writer = csv.DictWriter(csvfile, fieldnames = fields)
		
# 	# writing headers (field names)
# 	writer.writeheader()
		
# 	# writing data rows
# 	# writer.writerows(mydict)

	
    	
    
