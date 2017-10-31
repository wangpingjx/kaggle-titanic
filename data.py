import util
import numpy as np

def load_data():
    x_data, y_data = train()
    return [x_data[100:], y_data[100:]],[x_data[:100], y_data[:100]]

def train():
    data = util.read_csv('train.csv')
    return extract_data(data)

def load_age_data():
    x_data, y_data = age_train()
    return [x_data[100:], y_data[100:]],[x_data[:100], y_data[:100]]

def age_train():
    x_data, y_data = [], []
    for row in data:
        if empty(row['Age']):
            continue
        row_data = np.hstack([row[key] for key in row if key in ['SibSp', 'Parch']])
        x_data.append(row_data)
        y_data.append([row[key] for key in row if key in ['Age']])
    return np.array(x_data), np.array(y_data)

# def xtest():
#     data = util.read_csv('test.csv')
#     return extract_data(data)[0]
#
# def ytest():
#     data = util.read_csv('gender_submission.csv')
#     return extract_data(data)[1]

def extract_data(data):
    x_data, y_data = [], []
    for row in data:
        row_data = np.hstack([row[key] for key in row if key in ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch']])
        # ticket number count
        row_data = np.append(row_data, float(len([mem for mem in data if row['Ticket'] == mem['Ticket']])))

        x_data.append(row_data)

        y_data.append([row[key] for key in row if key in ['Survived']])

        # x_data.append([item for key in row for item in row[key] if key in ['Fare']])
        # x_data.append([item for key in row for item in row[key] if key in ['Pclass', 'Sex', 'Age', 'Family', 'Fare', 'Embarked']])
        # x_data.append([item for key in row for item in row[key] if key in ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']])
        # y_data.append([item for key in row for item in row[key] if key in ['Survived']])

    return np.array(x_data), np.array(y_data)

# watch()
