# encoding: utf-8
import csv
import numpy as np

def read_csv(filename):
    res = []
    with open(filename, 'r') as f:
        f_csv = csv.DictReader(f)
        for row in f_csv:
            res.append(format(dict(row)))
    return res

def format(row):
    for key in row.keys():
        if key in ['Survived', 'Age', 'SibSp', 'Parch', 'Fare']:
            row[key] = str_to_float(row[key])
        elif key == 'Ticket':
            row[key] = format_ticket(row[key])
        elif key == 'Pclass':
            # row[key] = row[key]
            row[key] = np.eye(3)[int(row[key])-1]  # OneHotEncoder
        elif key == 'Embarked':
            # row[key] = ['S','C','Q', ''].index(row[key])
            row[key] = np.eye(4)[['S','C','Q', ''].index(row[key])-1]  # OneHotEncoder
        elif key == 'Sex':
            row[key] = (1 if row[key] == 'male' else 0)
            row[key] = np.eye(2)[row[key]-1]       # OneHotEncoder
    return row

def str_to_float(str):
    return 0.0 if str == '' else float('0' + str)

def format_ticket(str):
    numbers = [int(s) for s in str.split() if s.isdigit()]
    if len(numbers) > 0:
        return numbers[0]
    else:
        return 0

# read_csv('train.csv')
