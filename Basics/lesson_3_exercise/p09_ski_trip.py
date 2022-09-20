days_of_stay = int(input())
type_of_room = input()
grade_of_stay = input()
price_of_room = 0
discount = 0
price_increase = 0
days_of_stay -= 1
price_of_stay_no_discount = 0

if type_of_room == 'room for one person':
    price_of_room = 18
    price_of_stay_no_discount = days_of_stay * price_of_room
elif type_of_room == 'apartment':
    price_of_room = 25
    price_of_stay_no_discount = days_of_stay * price_of_room
    if days_of_stay < 10:
        discount = price_of_stay_no_discount * 0.3
    elif 10 <= days_of_stay <= 15:
        discount = price_of_stay_no_discount * 0.35
    elif days_of_stay > 15:
        discount = price_of_stay_no_discount * 0.5
elif type_of_room == 'president apartment':
    price_of_room = 35
    price_of_stay_no_discount = days_of_stay * price_of_room
    if days_of_stay < 10:
        discount = price_of_stay_no_discount * 0.1
    elif 10 <= days_of_stay <= 15:
        discount = price_of_stay_no_discount * 0.15
    elif days_of_stay > 15:
        discount = price_of_stay_no_discount * 0.2

price_of_stay = price_of_stay_no_discount - discount

if grade_of_stay == 'positive':
    price_of_stay += price_of_stay * 0.25
else:
    price_of_stay -= price_of_stay * 0.1

print(f'{price_of_stay:.2f}')
