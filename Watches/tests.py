import csv

upload_file='/Users/vishv/Documents/DjangoProject/DjangoProject2/mysite/watches_with_timestamps.csv'
with open(upload_file) as file:
    reader = csv.DictReader(file)
    print(reader.fieldnames)
    for row in reader:
        print(row['price'].replace(',',''))