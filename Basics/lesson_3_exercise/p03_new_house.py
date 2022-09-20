type_of_flowers = input()
amount_of_flowers = int(input())
budget = int(input())
total_price = 0
discount = 0
price_increase = 0

if type_of_flowers == 'Roses':
    total_price = amount_of_flowers * 5
    if amount_of_flowers > 80:
        discount = total_price * 0.1
elif type_of_flowers == "Dahlias":
    total_price = amount_of_flowers * 3.8
    if amount_of_flowers > 90:
        discount = total_price * 0.15
elif type_of_flowers == 'Tulips':
    total_price = amount_of_flowers * 2.8
    if amount_of_flowers > 80:
        discount = total_price * 0.15
elif type_of_flowers == "Narcissus":
    total_price = amount_of_flowers * 3
    if amount_of_flowers < 120:
        price_increase = total_price * 0.15
elif type_of_flowers == "Gladiolus":
    total_price = amount_of_flowers * 2.5
    if amount_of_flowers < 80:
        price_increase = total_price * 0.2

total_price -= discount
total_price += price_increase
money_left = abs(budget - total_price)

if budget >= total_price:
    print(f'Hey, you have a great garden with {amount_of_flowers} {type_of_flowers} and {money_left:.2f} leva left.')
else:
    print(f'Not enough money, you need {money_left:.2f} leva more.')
