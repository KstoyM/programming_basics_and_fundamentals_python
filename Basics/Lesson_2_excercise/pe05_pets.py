from math import floor
from math import ceil

number_of_days_missing = int(input())
kg_food_left = int(input())
kg_food_for_dog_per_day = float(input())
kg_food_for_cat_per_day = float(input())
gr_food_for_turtle_per_day = float(input())

food_necessary = (kg_food_for_cat_per_day + kg_food_for_dog_per_day + gr_food_for_turtle_per_day / 1000) * \
                 number_of_days_missing

if kg_food_left >= food_necessary:
    print(f'{floor(kg_food_left - food_necessary)} kilos of food left.')
else:
    print(f'{ceil(food_necessary - kg_food_left)} more kilos of food are needed.')