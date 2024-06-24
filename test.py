import csv
import randomtimestamp

csv_file = '/Users/vishv/Documents/DjangoProject/DjangoProject2/mysite/laptops_extended.csv'
output_csv_file = '/Users/vishv/Documents/DjangoProject/DjangoProject2/mysite/Laptops_extended_timestamps.csv'

data = []
with open(csv_file, 'r', newline='') as file:
    reader = csv.DictReader(file)

    for row in reader:
        # Add a created_at timestamp
        row['created_at'] = randomtimestamp.randomtimestamp(start_year=2021, text=True, pattern='%Y-%m-%d %H:%M:%S')

        # Remove commas from the price field and convert to float
        # if row['price']:
        #     row['price'] = float(row['price'].replace(',', ''))
        # else:
        #     row['price'] = None
        # Append the modified row to the data list
        data.append(row)

# Get fieldnames from the first row
fieldnames = data[0].keys()

# Write the modified data to the output CSV file
with open(output_csv_file, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)
