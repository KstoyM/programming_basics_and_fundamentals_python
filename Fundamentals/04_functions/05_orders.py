def price_list(drink_type, quantity_of_drinks):
    total_price = 1
    if drink_type == 'coffee':
        total_price = (total_price + 0.5) * quantity_of_drinks
    elif drink_type == 'water':
        total_price *= quantity_of_drinks
    elif drink_type == 'coke':
        total_price = (total_price + 0.4) * quantity_of_drinks
    else:
        total_price = (total_price + 1) * quantity_of_drinks
    return total_price


beverage = input()
quant = int(input())

print(f'{price_list(beverage, quant):.2f}')
