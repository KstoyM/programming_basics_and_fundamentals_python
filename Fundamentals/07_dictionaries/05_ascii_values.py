lst_of_chars = input().split(", ")
result_dict = {key: ord(key) for key in lst_of_chars}
print(result_dict)