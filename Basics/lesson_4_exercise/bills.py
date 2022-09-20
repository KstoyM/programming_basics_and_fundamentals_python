number_of_months = int(input())

water_price = 20
internet_price = 15
electricity_price = 0
other_price = 0

for month in range(number_of_months):
    el_price_for_month = float(input())
    electricity_price += el_price_for_month
    other_price += (el_price_for_month + water_price + internet_price) * 1.2

print(f'Electricity: {electricity_price:.2f} lv')
print(f'Water: {water_price * number_of_months:.2f} lv')
print(f'Internet: {internet_price * number_of_months:.2f} lv')
print(f'Other: {other_price:.2f} lv')
print(f'Average: {(electricity_price + other_price + water_price * number_of_months + internet_price * number_of_months) / number_of_months:.2f} lv')