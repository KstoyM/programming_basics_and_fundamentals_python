fuel_type = input()
fuel_amount = float(input())
club_card = input()
gasoline_price = 2.22
diesel_price = 2.33
gas_price = 0.93

if club_card == 'No':
    if fuel_type == 'Gas' and 25 >= fuel_amount >= 20:
        print(f'{(gas_price * fuel_amount) - gas_price * fuel_amount * 0.08:.2f} lv.')
    elif fuel_type == 'Gas' and fuel_amount > 25:
        print(f'{(gas_price * fuel_amount) - gas_price * fuel_amount * 0.1:.2f} lv.')
    elif fuel_type == 'Diesel' and 25 >= fuel_amount >= 20:
        print(f'{(diesel_price * fuel_amount) - diesel_price * fuel_amount * 0.08:.2f} lv.')
    elif fuel_type == 'Diesel' and fuel_amount > 25:
        print(f'{(diesel_price * fuel_amount) - diesel_price * fuel_amount * 0.1:.2f} lv.')
    elif fuel_type == 'Gasoline' and 25 >= fuel_amount >= 20:
        print(f'{(gasoline_price * fuel_amount) - gasoline_price * fuel_amount * 0.08:.2f} lv.')
    elif fuel_type == 'Gasoline' and fuel_amount > 25:
        print(f'{(gasoline_price * fuel_amount) - gasoline_price * fuel_amount * 0.1:.2f} lv.')
    elif fuel_type == 'Gas':
        print(f'{gas_price * fuel_amount:.2f} lv.')
    elif fuel_type == 'Diesel':
        print(f'{diesel_price * fuel_amount:.2f} lv.')
    elif fuel_type == 'Gasoline':
        print(f'{gasoline_price * fuel_amount:.2f} lv.')

if club_card == 'Yes':
    gasoline_price = 2.22 - 0.18
    diesel_price = 2.33 - 0.12
    gas_price = 0.93 - 0.08
    if fuel_type == 'Gas' and 25 >= fuel_amount >= 20:
        print(f'{(gas_price * fuel_amount) - gas_price * fuel_amount * 0.08:.2f} lv.')
    elif fuel_type == 'Gas' and fuel_amount > 25:
        print(f'{(gas_price * fuel_amount) - gas_price * fuel_amount * 0.1:.2f} lv.')
    elif fuel_type == 'Diesel' and 25 >= fuel_amount >= 20:
        print(f'{(diesel_price * fuel_amount) - diesel_price * fuel_amount * 0.08:.2f} lv.')
    elif fuel_type == 'Diesel' and fuel_amount > 25:
        print(f'{(diesel_price * fuel_amount) - diesel_price * fuel_amount * 0.1:.2f} lv.')
    elif fuel_type == 'Gasoline' and 25 >= fuel_amount >= 20:
        print(f'{(gasoline_price * fuel_amount) - gasoline_price * fuel_amount * 0.08:.2f} lv.')
    elif fuel_type == 'Gasoline' and fuel_amount > 25:
        print(f'{(gasoline_price * fuel_amount) - gasoline_price * fuel_amount * 0.1:.2f} lv.')
    elif fuel_type == 'Gas':
        print(f'{gas_price * fuel_amount:.2f} lv.')
    elif fuel_type == 'Diesel':
        print(f'{diesel_price * fuel_amount:.2f} lv.')
    elif fuel_type == 'Gasoline':
        print(f'{gasoline_price * fuel_amount:.2f} lv.')