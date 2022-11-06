result_dict = {"shards": 0, "fragments": 0, "motes": 0}

is_item_obtained = False

command = input().split(" ")

while not is_item_obtained:

    for index in range(0, len(command), 2):
        quantity = int(command[index])
        item = command[index + 1].lower()
        if item not in result_dict:
            result_dict[item] = 0
        result_dict[item] += quantity
        if result_dict["shards"] >= 250:
            print("Shadowmourne obtained!")
            is_item_obtained = True
            result_dict["shards"] -= 250
        elif result_dict["fragments"] >= 250:
            print("Valanyr obtained!")
            is_item_obtained = True
            result_dict["fragments"] -= 250
        elif result_dict["motes"] >= 250:
            print("Dragonwrath obtained!")
            is_item_obtained = True
            result_dict["motes"] -= 250
        if is_item_obtained:
            break
    if not is_item_obtained:
        command = input().split(" ")

for item, value in result_dict.items():
    print(f"{item}: {value}")