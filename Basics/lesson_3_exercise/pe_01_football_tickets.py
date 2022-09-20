budget = float(input())
ticket_category = input()
number_of_people = int(input())

travel_expenses = 0

if number_of_people <= 4:
    travel_expenses = budget * 0.75
elif number_of_people <= 9:
    travel_expenses = budget * 0.6
elif number_of_people <= 24:
    travel_expenses = budget * 0.5
elif number_of_people <= 49:
    travel_expenses = budget * 0.4
else:
    travel_expenses = budget * 0.25

if ticket_category == 'VIP':
    price_of_ticket = 499.99
else:
    price_of_ticket = 249.99

money_left = abs(budget - travel_expenses - number_of_people * price_of_ticket)
if budget > travel_expenses + number_of_people * price_of_ticket:
    print(f'Yes! You have {money_left:.2f} leva left.')
else:
    print(f'Not enough money! You need {money_left:.2f} leva.')