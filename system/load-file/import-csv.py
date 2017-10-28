import csv

# Open csv and save into 
with open('data.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    data = list(reader)
    
print data