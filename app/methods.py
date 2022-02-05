import csv
import os
import config

def readdata():
    path = os.path.join(config.BASE_DIR,'app//data//random.csv')
    data = []
    with open(path) as f:
        reader = csv.DictReader(f, delimiter=';')
        for dict in reader:
            data.append(dict)
    return data