number_of_strings = int(input())

for cnt_string in range(number_of_strings):
    curr_string = input()
    if "," in curr_string or '.' in curr_string or "_" in curr_string:
        print(f'{curr_string} is not pure!')
    else:
        print(f'{curr_string} is pure.')