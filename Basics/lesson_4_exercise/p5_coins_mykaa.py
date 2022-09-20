money_inserted = float(input())

money_inserted *= 100

money_left_in_200 = money_inserted // 200
money_left_in_100 = money_inserted // 100
money_left_in_50 = money_inserted // 50
money_left_in_20 = money_inserted // 20
money_left_in_10 = money_inserted // 10
money_left_in_5 = money_inserted // 5
money_left_in_2 = money_inserted // 2
money_left_in_1 = money_inserted // 1

amt_of_coins_in_100 = money_left_in_100 - money_left_in_200 * 2
amt_of_coins_in_50 = money_left_in_50 - money_left_in_100 * 2
amt_of_coins_in_20 = money_left_in_20 - money_left_in_50 * 2.5
amt_of_coins_in_10 = money_left_in_10 - money_left_in_20 * 2
amt_of_coins_in_5 = money_left_in_5 - money_left_in_10 * 2
amt_of_coins_in_2 = money_left_in_2 - money_left_in_5 * 2.5
amt_of_coins_in_1 = money_left_in_1 - money_left_in_2 * 2

total_coins = money_left_in_200 + amt_of_coins_in_100 + amt_of_coins_in_50 + amt_of_coins_in_20 + \
              amt_of_coins_in_10 + amt_of_coins_in_5 + amt_of_coins_in_2 + amt_of_coins_in_1

print(int(total_coins))