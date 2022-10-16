def positive(some_numbers):
    return [number for number in some_numbers if int(number) >= 0]


def negative(some_numbers):
    return [number for number in some_numbers if int(number) < 0]


def even(some_numbers):
    return [number for number in some_numbers if int(number) % 2 == 0]


def odd(some_numbers):
    return [number for number in some_numbers if int(number) % 2 != 0]


number_list = input().split(', ')

print(f'Positive: {", ".join(positive(number_list))}')
print(f'Negative: {", ".join(negative(number_list))}')
print(f'Even: {", ".join(even(number_list))}')
print(f'Odd: {", ".join(odd(number_list))}')
