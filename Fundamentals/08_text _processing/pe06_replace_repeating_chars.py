input_str = input()
result_string = ''
previous_char = ''

for char in input_str:
    if char != previous_char:
        result_string += char
    previous_char = char

print(result_string)