input_string = input()
result_string = ''

for char in input_string:
    result_string += chr(ord(char) + 3)

print(result_string)