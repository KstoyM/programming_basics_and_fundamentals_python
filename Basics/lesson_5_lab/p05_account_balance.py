total_amt = 0

while True:
    amt_deposit = input()

    if amt_deposit == 'NoMoreMoney':
        break

    amt_deposit = float(amt_deposit)

    if amt_deposit >= 0:
        total_amt += amt_deposit
        print(f'Increase: {amt_deposit:.2f}')
    else:
        print(f'Invalid operation!')
        break

print(f'Total: {total_amt:.2f}')