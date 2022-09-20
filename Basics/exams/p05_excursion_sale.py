amt_of_sea_excursions = int(input())
amt_of_mountain_excursions = int(input())

amount_collected = 0

while True:
    type_of_excursion = input()

    if type_of_excursion == 'Stop':
        print(f'Profit: {amount_collected} leva.')
        break

    if type_of_excursion == 'sea':
        if amt_of_sea_excursions == 0:
            continue
        else:
            amount_collected += 680
            amt_of_sea_excursions -= 1
    elif type_of_excursion == 'mountain':
        if amt_of_mountain_excursions == 0:
            continue
        else:
            amount_collected += 499
            amt_of_mountain_excursions -= 1

    if amt_of_mountain_excursions == 0 and amt_of_sea_excursions == 0:
        print(f'Good job! Everything is sold.')
        print(f'Profit: {amount_collected} leva.')
        break