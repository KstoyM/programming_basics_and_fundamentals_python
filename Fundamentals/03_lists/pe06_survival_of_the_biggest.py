number_list = input().split()
numbers_to_remove = int(input())
number_list_as_digit = []
number_list_as_string = []
final_numbers = ''

for element in number_list:
    number_list_as_digit.append(int(element))

for number_index in range(numbers_to_remove):
    number_list_as_digit.remove(min(number_list_as_digit))

for element in number_list_as_digit:
    number_list_as_string.append(str(element))

for number in range(len(number_list_as_string)):
    final_numbers += number_list_as_string[number]
    if number < len(number_list_as_string) - 1:
        final_numbers += ', '

print(final_numbers)

# better solution >>
# numbers_str = input().split()
# numbers = []
#
# for num in numbers_str:
#     numbers.append(int(num))
#
# remover = int(input())
#
# for _ in range(remover):
#     numbers.remove(min(numbers))
#
# print(*numbers, sep=", ")