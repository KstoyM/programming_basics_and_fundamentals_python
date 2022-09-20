degrees_outside = int(input())
time_of_the_day = input()
outfit = ''
shoes = ''

if time_of_the_day == 'Morning':
    if 10 <= degrees_outside <= 18:
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
    elif 18 < degrees_outside <= 24:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif degrees_outside >= 25:
        outfit = 'T-Shirt'
        shoes = 'Sandals'

if time_of_the_day == 'Afternoon':
    if 10 <= degrees_outside <= 18:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif 18 < degrees_outside <= 24:
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    elif degrees_outside >= 25:
        outfit = 'Swim Suit'
        shoes = 'Barefoot'

if time_of_the_day == 'Evening':
    if 10 <= degrees_outside <= 18:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif 18 < degrees_outside <= 24:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif degrees_outside >= 25:
        outfit = 'Shirt'
        shoes = 'Moccasins'

print(f"It's {degrees_outside} degrees, get your {outfit} and {shoes}.")