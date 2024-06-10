import csv

file_csv = '/Users/vishv/Documents/DjangoProject/DjangoProject2/mysite/watches.csv'
with open(file_csv) as  file:
    read = csv.reader(file)
    for line in read:
        print(line)
        break