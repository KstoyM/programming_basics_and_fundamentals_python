tank_capacity = 255
number_of_fills = int(input())

water_in_the_tank = 0

for fill in range(number_of_fills):
    current_water_input = int(input())
    if tank_capacity - current_water_input < 0:
        print('Insufficient capacity!')
        continue
    water_in_the_tank += current_water_input
    tank_capacity -= current_water_input
print(f'{water_in_the_tank}')