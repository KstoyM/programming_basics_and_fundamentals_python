def rate_func(curr_dict, curr_plant, curr_rating):
    if curr_plant in curr_dict:
        curr_dict[curr_plant].append(curr_rating)
    else:
        print('error')
    return curr_dict


def update_func(curr_dict, curr_plant, curr_rarity):
    if curr_plant in curr_dict:
        old_rarity = curr_dict[curr_plant][0]
        curr_dict[curr_plant].remove(old_rarity)
        curr_dict[curr_plant].insert(0, curr_rarity)
    else:
        print('error')
    return curr_dict


def reset_func(curr_dict, curr_plant):
    if curr_plant in curr_dict:
        rarity = curr_dict[curr_plant].pop(0)
        curr_dict[curr_plant].clear()
        curr_dict[curr_plant].append(rarity)
    else:
        print('error')
    return curr_dict


number_of_plants = int(input())
plants_dict = {}

for _ in range(number_of_plants):
    plant_name, plant_rarity = input().split('<->')
    plants_dict[plant_name] = [int(plant_rarity)]

while True:

    command = input().split(': ')

    if command[0] == 'Exhibition':
        break

    action = command[0]

    if action == 'Rate':
        curr_command = command[1].split(" - ")
        plant_name = curr_command[0]
        plant_rating = float(curr_command[1])
        plants_dict = rate_func(plants_dict, plant_name, plant_rating)
    elif action == 'Update':
        curr_command = command[1].split(" - ")
        plant_name = curr_command[0]
        new_rarity = int(curr_command[1])
        plants_dict = update_func(plants_dict, plant_name, new_rarity)
    elif action == 'Reset':
        plant_name = command[1]
        plants_dict = reset_func(plants_dict, plant_name)

print('Plants for the exhibition:')

for plant in plants_dict.items():
    plant_name = plant[0]
    plant_rarity = plant[1][0]
    if len(plant[1]) > 1:
        average_rating = (sum(plant[1]) - plant[1][0]) / (len(plant[1]) - 1)
    else:
        average_rating = 0.00
    print(f"- {plant_name}; Rarity: {plant_rarity}; Rating: {average_rating:.2f}")