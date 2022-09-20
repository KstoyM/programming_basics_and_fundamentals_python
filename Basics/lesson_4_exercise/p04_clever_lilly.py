lilly_age = int(input())
price_of_washing_machine = float(input())
price_of_toy = int(input())

money_saved = 0
toys_received = 0

for n in range(1, lilly_age + 1):
    if n % 2 == 0:
        money_saved += n * 5 - 1
    else:
        toys_received += 1

money_save_total = money_saved + toys_received * price_of_toy

if money_save_total >= price_of_washing_machine:
    print(f'Yes! {money_save_total - price_of_washing_machine:.2f}')
else:
    print(f'No! {price_of_washing_machine - money_save_total:.2f}')