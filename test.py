from scipy.stats import kstest
import numpy as np
import util


data = util.read_csv('train.csv')

sibsp_group = {}
for row in data:
    if ticket_group.get(int(row['SibSp'])):
        ticket_group[str(row['SibSp'])].append(row)
    else:
        ticket_group[str(row['SibSp'])] = [row]

for sibsp_group, group in ticket_group.items():
    cnt    = len(group)
    sur = len([mem for mem in group if mem['Survived'] == 1.0])
    child = len([mem for mem in group if mem['Age'] < 20.0])
    sur_child = len([mem for mem in group if mem['Age'] < 20.0 and mem['Survived'] == 1.0])
    sur_adult = len([mem for mem in group if mem['Age'] >= 20.0 and mem['Survived'] == 1.0])
    # if cnt > 1 and len([mem for mem in group if mem['Survived'] > 0 and mem['Age'] > 20.0 and mem['Parch'] >= 1.0]):
    #     print('parent Survived')

    if cnt > 2:
        print('Count:',cnt, 'Survived count:', sur)
        print('Total survived: ', sur/cnt * 100)
        # if sur_adult:
        #     print('Survived adult:', sur_adult)
        # else:
        #     print('adult dead')
        #
        # if child > 0:
        #     print('Children survived: ', sur_child/child * 100)
        # else:
        #     print('No Child')
