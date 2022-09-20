from math import floor
from math import ceil

number_of_magnolias = int(input())
number_of_hyacinths = int(input())
number_of_roses = int(input())
number_of_cactus = int(input())
price_of_the_present = float(input())

# Ако парите СА стигнали: "She is left with {останали} leva." – сумата трябва да е закръглена към по-малко цяло число (пр. 1.90 -> 1).
# Ако парите НЕ достигат: "She will have to borrow {останали} leva." – сумата трябва да е закръглена към по-голямо цяло число (пр. 1.10 -> 2).

price_of_flowers = number_of_magnolias * 3.25 + number_of_hyacinths * 4 + number_of_roses * 3.5 + number_of_cactus * 8
profit = price_of_flowers - price_of_flowers * 0.05

if price_of_the_present <= profit:
    print(f'She is left with {floor(profit - price_of_the_present)} leva.')
else:
    print(f'She will have to borrow {ceil(price_of_the_present - profit)} leva.')