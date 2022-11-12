input_str = input()
explosion_strength = 0
result_str = ''

for index in range(len(input_str)):
    if explosion_strength == 0 and input_str[index] != ">":
        result_str += input_str[index]

    if explosion_strength > 0 and input_str[index] != ">":
        explosion_strength -= 1

    if input_str[index] == ">":
        explosion_strength += int(input_str[index + 1])
        result_str += ">"

print(result_str)

