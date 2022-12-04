def print_func(zoo):
    print("Animals:")
    for current_animal in zoo.items():
        print(f"{current_animal[0]} -> {current_animal[1][0]}g")
    areas_with_hungry_animals = {}
    for animal_values in zoo.values():
        curr_area = animal_values[1]
        if animal_values[0] > 0:
            if curr_area not in areas_with_hungry_animals:
                areas_with_hungry_animals[curr_area] = 1
            else:
                areas_with_hungry_animals[curr_area] += 1
    print("Areas with hungry animals:")
    for location in areas_with_hungry_animals.items():
        print(f' {location[0]}: {location[1]}')


zoo_dict = {}

while True:
    command = input().split(':')

    if command[0] == "EndDay":
        print_func(zoo_dict)
        break

    if command[0] == 'Add':
        animal, needed_food_quant, area = command[1].split('-')

        if animal not in zoo_dict:
            zoo_dict[animal] = [int(needed_food_quant), area]
        else:
            zoo_dict[animal][0] += int(needed_food_quant)
    else:
        animal, food_quant = command[1].split('-')
        if animal in zoo_dict:
            zoo_dict[animal][0] -= int(food_quant)
            if zoo_dict[animal][0] <= 0:
                del zoo_dict[animal]
                print(f'{animal} was successfully fed')
