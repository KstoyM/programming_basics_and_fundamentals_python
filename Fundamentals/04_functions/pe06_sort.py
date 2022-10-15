input_list = input().split()
list_as_digits = []

for element in input_list:
    list_as_digits.append(int(element))

print(sorted(list_as_digits))
