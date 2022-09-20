amount_necessary = int(input())

counter = 0
sum_of_cash = 0
count_of_cash = 0
sum_of_cc = 0
count_of_cc = 0

curr_command = input()
while curr_command != 'End':
    price_of_product = int(curr_command)
    counter += 1

    if counter % 2 != 0 and price_of_product <= 100:
        sum_of_cash += price_of_product
        count_of_cash += 1
        print('Product sold!')
    elif counter % 2 != 0 and price_of_product > 100:
        print('Error in transaction!')
    elif counter % 2 == 0 and price_of_product >= 10:
        sum_of_cc += price_of_product
        count_of_cc += 1
        print('Product sold!')
    elif counter % 2 == 0 and price_of_product < 10:
        print('Error in transaction!')

    if sum_of_cash + sum_of_cc >= amount_necessary:
        print(f'Average CS: {sum_of_cash / count_of_cash:.2f}')
        print(f'Average CC: {sum_of_cc / count_of_cc:.2f}')
        break

    curr_command = input()

if curr_command == 'End':
    print('Failed to collect required money for charity.')
