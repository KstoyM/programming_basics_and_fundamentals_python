def odd_or_even(number):
    even_sum = 0
    odd_sum = 0
    for index in number:
        digit_index = int(index)
        if digit_index % 2 == 0:
            even_sum += digit_index
        else:
            odd_sum += digit_index
    return even_sum, odd_sum


input_number = input()
sum_of_even_digits, sum_of_odd_digits = odd_or_even(input_number)

print(f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}")