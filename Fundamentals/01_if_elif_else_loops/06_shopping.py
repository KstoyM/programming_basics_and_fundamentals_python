budget = int(input())

curr_command = input()
while curr_command != 'End':
    prod_price = int(curr_command)
    budget -= prod_price

    if budget < 0:
        print('You went in overdraft!')
        break
    else:
        curr_command = input()

if curr_command == 'End':
    print('You bought everything needed.')