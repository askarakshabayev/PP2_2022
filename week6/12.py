import csv

# csv.writer
# writerow

with open('test1.csv', mode='w') as test1:
    test_writer = csv.writer(test1, delimiter=',')
    test_writer.writerow(['line1', 'line1_1', 'line1_2'])
    test_writer.writerow(['line2', 'line2_1', 'line2_2'])
    test_writer.writerow(['line3', 'line3_1', 'line3_2'])
    test_writer.writerow(['line4', 'line4_1', 'line4_2'])
