one_lv_coins = int(input())
two_lv_coins = int(input())
five_lv_bills = int(input())
sum_to_pay = int(input())

for o in range(0, one_lv_coins + 1):
    for t in range(0, two_lv_coins + 1):
        for f in range(0, five_lv_bills + 1):
            if (o * 1) + (t * 2) + (f * 5) == sum_to_pay:
                print(f'{o} * 1 lv. + {t} * 2 lv. + {f} * 5 lv. = {sum_to_pay} lv.')