import csv
import pandas as pd

import sys

# input number you want to search
result_file = csv.reader(open('/Users/pengyuzhou/Downloads/Asvdplusplus.csv', "r"))
result_id_list = []
result_item_list = []
result_rating_list = []
for row in result_file:
    if int(row[1]) == 3:
        result_id_list.append(row[0])
        result_item_list.append(row[1])
        result_rating_list.append(row[2])

result_id_list = list(result_id_list)
result_item_list = list(result_item_list)
result_rating_list = list(result_rating_list)

# read csv, and split on "," the line
csv_file = csv.reader(open('/Users/pengyuzhou/Downloads/user-item-cf/train_output_cf_account_manager.csv', "r"))
train_id_list = []
train_item_list = []
train_rating_list = []
for row in csv_file:
    if int(row[1]) == 3:
        train_id_list.append(row[0])
        train_item_list.append(row[1])
        train_rating_list.append(row[2])
true_pos = 0
false_pos = 0
j = 0
# loop through csv list
for i in range(len(result_id_list)):

    # if current rows 2nd value is equal to input, print that row
    for j in range(len(train_id_list)):
        if result_id_list[i] == train_id_list[j]:
            test1 = result_id_list[i]
            test2 = train_id_list[i]
            if float(result_rating_list[i]) >= 1.5 and train_rating_list[j] == '2':
                true_pos = true_pos + 1
            if float(result_rating_list[i]) < 1 and train_rating_list[j] == '1':
                false_pos = false_pos + 1
            if float(result_rating_list[i]) < 1.5 and train_rating_list[j] == '2':
                false_pos = false_pos + 1
            if float(result_rating_list[i]) >= 1 and float(result_rating_list[i])<1.5 and train_rating_list[j] == '1':
                true_pos = true_pos + 1


print('The precision value is {}'.format(float(true_pos) / (true_pos + false_pos)))

