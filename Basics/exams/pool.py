from math import ceil

number_of_ppl = int(input())
entry_price = float(input())
price_per_chair = float(input())
price_per_umbrella = float(input())

entry_price = number_of_ppl * entry_price
price_per_chair = ceil(number_of_ppl * 0.75) * price_per_chair
price_per_umbrella = ceil(number_of_ppl / 2) * price_per_umbrella

total_price = entry_price + price_per_chair + price_per_umbrella

print(f'{total_price:.2f} lv.')