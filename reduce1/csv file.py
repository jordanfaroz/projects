import csv
with open('C:/test.csv.csv','r') as file:
    x = csv.reader(file)
    for line in x:
        print(line)