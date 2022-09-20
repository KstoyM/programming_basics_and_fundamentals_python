price_of_t_shirt = float(input())
target_sum = float(input())

price_of_shorts = price_of_t_shirt * 0.75
price_of_socks = price_of_shorts * 0.2
price_of_shoes = (price_of_t_shirt + price_of_shorts) * 2

total_sum = price_of_t_shirt + price_of_shorts + price_of_socks + price_of_shoes
total_sum -= total_sum * 0.15

if total_sum >= target_sum:
    print('Yes, he will earn the world-cup replica ball!')
    print(f'His sum is {total_sum:.2f} lv.')
else:
    print(f'No, he will not earn the world-cup replica ball.')
    print(f'He needs {target_sum - total_sum:.2f} lv. more.')