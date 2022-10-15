list_len = int(input())
number_list = []

COMMAND_EVEN = 'even'
COMMAND_ODD = 'odd'
COMMAND_NEGATIVE = 'negative'
COMMAND_POSITIVE = 'positive'

for index in range(list_len):
    number_list.append(int(input()))

command = input()
filtered_numbers = []

for number in number_list:
    filtered_passes = (
        (command == COMMAND_EVEN and number % 2 == 0) or
        (command == COMMAND_ODD and number % 2 != 0) or
        (command == COMMAND_NEGATIVE and number < 0) or
        (command == COMMAND_POSITIVE and number >= 0)
        )
    if filtered_passes:
        filtered_numbers.append(number)

print(filtered_numbers)