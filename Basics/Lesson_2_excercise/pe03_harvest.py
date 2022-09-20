from math import floor
from math import ceil
square_meters_for_harvesting = int(input())
grapes_per_square_meter = float(input())
liters_of_wine_needed = int(input())
number_of_workers = int(input())

square_meters_harvest_for_wine = square_meters_for_harvesting * 0.4
grapes_harvested_in_kg = square_meters_harvest_for_wine * grapes_per_square_meter
wine_harvested_in_liters = grapes_harvested_in_kg / 2.5
remaining_wine_for_workers = wine_harvested_in_liters - liters_of_wine_needed

if wine_harvested_in_liters < liters_of_wine_needed:
    print(f'It will be a tough winter! More {floor(liters_of_wine_needed - wine_harvested_in_liters)} '
          f'liters wine needed.')
else:
    print(f'Good harvest this year! Total wine: {floor(wine_harvested_in_liters)} liters.')
    print(f'{ceil(remaining_wine_for_workers)} liters left -> '
          f'{ceil(remaining_wine_for_workers / number_of_workers)} liters per person.')