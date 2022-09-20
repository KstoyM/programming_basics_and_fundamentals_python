# плод	banana	apple	orange	grapefruit	kiwi	pineapple	grapes
# цена	2.70	1.25	0.90	1.60	3.00	5.60	4.20

type_of_fruit = input()
day_of_week = input()
volume = float(input())
price = 0

if day_of_week in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
    if type_of_fruit == 'banana':
        price = 2.5
    elif type_of_fruit == 'apple':
        price = 1.2
    elif type_of_fruit == 'orange':
        price = 0.85
    elif type_of_fruit == 'grapefruit':
        price = 1.45
    elif type_of_fruit == 'kiwi':
        price = 2.7
    elif type_of_fruit == 'pineapple':
        price = 5.5
    elif type_of_fruit == 'grapes':
        price = 3.85
elif day_of_week in ['Saturday', 'Sunday']:
    if type_of_fruit == 'banana':
        price = 2.7
    elif type_of_fruit == 'apple':
        price = 1.25
    elif type_of_fruit == 'orange':
        price = 0.9
    elif type_of_fruit == 'grapefruit':
        price = 1.60
    elif type_of_fruit == 'kiwi':
        price = 3
    elif type_of_fruit == 'pineapple':
        price = 5.6
    elif type_of_fruit == 'grapes':
        price = 4.2

if price == 0:
    print('error')
else:
    print(f'{price * volume:.2f}')