# This program extracts the text from four csv files and saves to .txt file named new_file.txt

import csv # library to open .csv file

filenames = ['CSV1.csv', 'CSV2.csv', 'CSV3.csv', 'CSV4.csv']

with open('new_file.txt', 'w') as file1: 
    for filename in filenames: # iterate through all files
        with open(filename, 'r') as file2: # to open each .csv file
            csvreader = csv.reader(file2) # from csv library
            next(csvreader) # pointer points to first row

            for row in csvreader: # iterate through each row in file
                for column in row:
                    file1.write(column) # write text in each column to new file
                    file1.write("\n")