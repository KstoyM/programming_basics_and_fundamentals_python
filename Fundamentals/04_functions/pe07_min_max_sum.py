input_list = input().split()
list_as_digit = []

for element in input_list:
    list_as_digit.append(int(element))

print(f'The minimum number is {min(list_as_digit)}')
print(f'The maximum number is {max(list_as_digit)}')
print(f'The sum number is: {sum(list_as_digit)}')