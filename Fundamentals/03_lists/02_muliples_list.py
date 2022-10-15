factor = int(input())
count_of_numbers = int(input())

list_of_numbers = []

for number in range(1, count_of_numbers + 1):
    list_of_numbers.append(factor * number)

print(list_of_numbers)