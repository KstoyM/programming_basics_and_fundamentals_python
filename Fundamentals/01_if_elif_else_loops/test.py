input_str = input()
indexes_list = []
for i in range(len(input_str)):
    if input_str[i] == input_str[i].capitalize():
        indexes_list.append(i)
print(indexes_list)