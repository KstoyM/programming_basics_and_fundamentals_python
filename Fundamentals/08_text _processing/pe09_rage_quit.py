input_string = input()
current_string = ''
result_string = ''

for index in range(len(input_string)):
    if not input_string[index].isdigit():
        current_string += input_string[index].upper()
    else:
        if index < len(input_string) - 1:
            if input_string[index + 1].isdigit():
                result_string += current_string * int(input_string[index] + input_string[index + 1])
                current_string = ''
            else:
                result_string += current_string * int(input_string[index])
                current_string = ''
        else:
            result_string += current_string * int(input_string[index])
            current_string = ''

print(f"Unique symbols used: {len(set(result_string))}")
print(f"{result_string}")