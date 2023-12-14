import csv

filenames = ['CSV1.csv', 'CSV2.csv', 'CSV3.csv', 'CSV4.csv']
text = []
for filename in filenames:
    with open(filename, 'r') as file:
        csvreader = csv.reader(file)
        next(csvreader)
        for row in csvreader:
            text.append(row[2])
    
with open('new_file.txt', 'w') as file:
    for i in text:
        file.write(i)
        file.write("\n")