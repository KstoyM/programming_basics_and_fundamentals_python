input_str = input()

for index in range(len(input_str)):
    if input_str[index] == ":":
        print(f":{input_str[index + 1]}")
