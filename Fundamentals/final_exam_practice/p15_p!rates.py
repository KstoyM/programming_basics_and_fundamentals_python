def plunder_func(cities_d, town, people, gold):
    cities_d[town][1] -= gold
    cities_d[town][0] -= people
    print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
    if cities_d[town][1] == 0 or cities_d[town][0] == 0:
        del cities_d[town]
        print(f"{town} has been wiped off the map!")
    return cities_d


def prosper_func(cities_d, town, gold):
    if gold < 0:
        print("Gold added cannot be a negative number!")
    else:
        cities_d[town][1] += gold
        print(f"{gold} gold added to the city treasury. {town} now has {cities_d[town][1]} gold.")
    return cities_d


def print_func(cities_d):
    if cities_d:
        print(f"Ahoy, Captain! There are {len(cities_d)} wealthy settlements to go to:")
        for town in cities_d:
            print(f'{town} -> Population: {cities_d[town][0]} citizens, Gold: {cities_d[town][1]} kg')
    else:
        print("Ahoy, Captain! All targets have been plundered and destroyed!")


cities_dict = {}

while True:
    city_input = input().split("||")

    if city_input[0] == "Sail":
        break

    city, population, money = city_input
    if city not in cities_dict:
        cities_dict[city] = [int(population), int(money)]
    else:
        cities_dict[city][0] += int(population)
        cities_dict[city][1] += int(money)

while True:
    command = input().split("=>")

    if command[0] == "End":
        print_func(cities_dict)
        break

    action = command[0]

    if action == "Plunder":
        town_plundered = command[1]
        people_plundered = int(command[2])
        gold_plundered = int(command[3])
        cities_dict = plunder_func(cities_dict, town_plundered, people_plundered, gold_plundered)
    elif action == "Prosper":
        town_plundered = command[1]
        gold_plundered = int(command[2])
        cities_dict = prosper_func(cities_dict, town_plundered, gold_plundered)
