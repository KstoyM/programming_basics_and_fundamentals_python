given_number = int(input())
string_given_number = str(given_number)
number_list = list(string_given_number)

largest_number = ''

for iteration in range(len(str(given_number))):
    largest_number += max(number_list)
    number_list.remove(max(number_list))

print(largest_number)