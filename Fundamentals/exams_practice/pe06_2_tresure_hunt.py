treasure_chest = input().split("|")

while True:

    command = input()

    if command == "Yohoho!":
        break

    action = command.split()

    if action[0] == "Loot":
        action.remove("Loot")
        for element in action:
            if element not in treasure_chest:
                treasure_chest.insert(0, element)

    elif action[0] == "Drop":
        drop_index = int(action[1])
        if 0 < drop_index < len(treasure_chest):
            dropped_item = treasure_chest.pop(drop_index)
            treasure_chest.append(dropped_item)

    elif action[0] == "Steal":
        steal_list = []
        stolen_items = int(action[1])
        if len(treasure_chest) > stolen_items > 0:
            for item in range(len(treasure_chest) - 1, len(treasure_chest) - 1 - stolen_items, -1):
                curr_remove_item = treasure_chest.pop(item)
                steal_list.insert(0, curr_remove_item)
        else:
            steal_list = [i for i in treasure_chest]
            treasure_chest.clear()
        print(f"{', '.join(steal_list)}")

if len(treasure_chest) == 0:
    print("Failed treasure hunt.")
else:
    len_of_items = sum([len(item) for item in treasure_chest])
    print(f"Average treasure gain: {len_of_items / len(treasure_chest):.2f} pirate credits.")
