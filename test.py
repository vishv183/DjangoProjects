import csv
from datetime import datetime, time
from random import random


def random_date(seed):
    random.seed(seed)
    d = random.randint(1, int(time.time()))
    return datetime.fromtimestamp(d).strftime('%Y-%m-%d')

random_date()

print(f'random date and time  = {datetime}')
file_csv = '/Users/vishv/Documents/DjangoProject/DjangoProject2/mysite/watches.csv'
with open(file_csv) as file:
    read = csv.reader(file)
    for line in read:
        print(line[-1])
        for row in line:
            pass
