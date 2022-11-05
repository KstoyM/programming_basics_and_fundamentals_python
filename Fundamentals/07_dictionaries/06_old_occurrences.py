input_list = input().split(" ")
input_dict = {}

for key in input_list:
    if key.lower() not in input_dict:
        input_dict[key.lower()] = 1
    else:
        input_dict[key.lower()] += 1

for key, value in input_dict.items():
    if value % 2 != 0:
        print(key, end=' ')
