from math import ceil

budget = float(input())
number_of_students = int(input())
price_of_flour = float(input())
price_of_single_egg = float(input())
price_of_single_apron = float(input())

total_cost = 0
total_flour_needed = 0
total_eggs_needed = 0
total_aprons_needed = 0

for student in range(1, number_of_students +1):

    total_flour_needed += 1
    total_eggs_needed += 10
    total_aprons_needed += 1

    if student % 5 == 0:
        total_flour_needed -= 1

total_aprons_needed += ceil(total_aprons_needed * 0.2)
total_cost = total_flour_needed * price_of_flour + total_eggs_needed * \
             price_of_single_egg + total_aprons_needed * price_of_single_apron

if budget < total_cost:
    print(f"{total_cost - budget:.2f}$ more needed.")
else:
    print(f"Items purchased for {total_cost:.2f}$.")