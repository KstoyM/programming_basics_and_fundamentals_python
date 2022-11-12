# word = input()
# digits = ''
# letters = ''
# other = ''
#
# for char in word:
#     if char.isdigit():
#         digits += char
#     elif char.isalpha():
#         letters += char
#     else:
#         other += char
#
# print(f"{digits}\n{letters}\n{other}")

word = input()
all_dict = {'digits': '', 'letters': '', 'other': ''}

for char in word:
    if char.isdigit():
        all_dict['digits'] += char
    elif char.isalpha():
        all_dict['letters'] += char
    else:
        all_dict['other'] += char

for value in all_dict.values():
    print(value)