def iseven(number):
    if number % 2 == 0:
        return True
    return False


input_number = input().split()
digit_list = []

for element in input_number:
    digit_list.append(int(element))

filtered = filter(iseven, digit_list)
even_numbers = list(filtered)

print(even_numbers)