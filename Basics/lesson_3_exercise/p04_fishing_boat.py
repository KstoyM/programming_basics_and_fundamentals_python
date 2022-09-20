budget = int(input())
season_of_the_year = input()
number_of_fishermen = int(input())
price_of_boat = 0
discount = 0
additional_discount = 0
if season_of_the_year == 'Spring':
    price_of_boat = 3000
elif season_of_the_year == 'Summer' or season_of_the_year == 'Autumn':
    price_of_boat = 4200
elif season_of_the_year == 'Winter':
    price_of_boat = 2600

if number_of_fishermen <= 6:
    discount = price_of_boat * 0.1
elif 7 <= number_of_fishermen <= 11:
    discount = price_of_boat * 0.15
elif number_of_fishermen >= 12:
    discount = price_of_boat * 0.25

price_of_boat = price_of_boat - discount

if number_of_fishermen % 2 == 0 and season_of_the_year != 'Autumn':
    additional_discount = price_of_boat * 0.05

price_of_boat = price_of_boat - additional_discount
money_left = abs(price_of_boat - budget)

if budget >= price_of_boat:
    print(f'Yes! You have {money_left:.2f} leva left.')
else:
    print(f'Not enough money! You need {money_left:.2f} leva.')