import os

os.system("cls")

data_1:str = list(input("data 1: "))
data_2:str = list(input("data 2: "))
same_data_dict = {}
same_data_list = []

for i in data_1:
    same_data_dict[i] = data_2.count(i)

print(same_data_dict)

"""
for each item in dict
if item.key >= 1
copy item to list
"""
items = same_data_dict.items() # [(key, value), (key, value), (key, value)]

for i in items: # i = (key, value)
    if i[1] >= 1: # i[1] = value
        same_data_list.append(i[0]) # append(key); i[0] = key 

for i in same_data_list:
    print(i)