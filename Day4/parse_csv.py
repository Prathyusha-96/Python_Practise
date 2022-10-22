import csv

with open('csv.txt', 'r') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter='\t')
	for line in csv_reader:
		print(line)
#dictonary reader
with open('csv.txt', 'r') as csv_file:

    csv_reader = csv.DictReader(csv_file)
    for line in csv_reader:
    	print(line['email'])

    

with open('new_csv.txt', 'w') as new_file:

    fieldnames = ['first_name', 'last_name', 'email']

    csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='-')
    
    csv_writer.writeheader()

    # for line in csv_reader:
    # 	csv_writer.writerow(line)
    	
	
    	
    
