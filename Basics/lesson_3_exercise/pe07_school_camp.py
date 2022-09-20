season = input()
type_of_group = input()
number_of_students = int(input())
number_of_nights_stay = int(input())
price_per_night = 0
type_of_sport = ''

if season == 'Winter':
    if type_of_group == 'boys' or type_of_group == 'girls':
        price_per_night = 9.6
    else:
        price_per_night = 10
elif season == 'Spring':
    if type_of_group == 'boys' or type_of_group == 'girls':
        price_per_night = 7.2
    else:
        price_per_night = 9.5
else:
    if type_of_group == 'boys' or type_of_group == 'girls':
        price_per_night = 15
    else:
        price_per_night = 20

total_price = price_per_night * number_of_nights_stay * number_of_students

if number_of_students >= 50:
    total_price *= 0.5
elif 50 > number_of_students >= 20:
    total_price -= total_price * 0.15
elif 20 > number_of_students >= 10:
    total_price -= total_price * 0.05

if season == 'Winter':
    if type_of_group == 'boys':
        type_of_sport = 'Judo'
    elif type_of_group == 'girls':
        type_of_sport = 'Gymnastics'
    else:
        type_of_sport = 'Ski'
elif season == 'Spring':
    if type_of_group == 'boys':
        type_of_sport = 'Tennis'
    elif type_of_group == 'girls':
        type_of_sport = 'Athletics'
    else:
        type_of_sport = 'Cycling'
else:
    if type_of_group == 'boys':
        type_of_sport = 'Football'
    elif type_of_group == 'girls':
        type_of_sport = 'Volleyball'
    else:
        type_of_sport = 'Swimming'

print(f'{type_of_sport} {total_price:.2f} lv.')