import csv

# csv.reader(file, delimiter = ',')

with open('test.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row[0], row[1])
