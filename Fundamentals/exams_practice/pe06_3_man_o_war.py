pirate_ship_status = list(map(int, input().split(">")))
warship_status = list(map(int, input().split(">")))

max_health = int(input())
has_a_ship_sunk = False

while True:

    command = input()

    if command == "Retire":
        break

    action = command.split()

    if action[0] == 'Fire':
        fire_section = int(action[1])
        damage = int(action[2])
        if 0 <= fire_section < len(warship_status):
            warship_status[fire_section] -= damage
            if warship_status[fire_section] <= 0:
                print("You won! The enemy ship has sunken.")
                has_a_ship_sunk = True
                break

    elif action[0] == 'Defend':
        fire_section_start = int(action[1])
        fire_section_end = int(action[2])
        damage = int(action[3])

        if 0 <= fire_section_start < len(pirate_ship_status) and \
                fire_section_start < fire_section_end < len(pirate_ship_status):
            for section in range(fire_section_start, fire_section_end + 1):
                pirate_ship_status[section] -= damage
                if pirate_ship_status[section] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    has_a_ship_sunk = True
                    break

    elif action[0] == "Repair":
        repair_index = int(action[1])
        repair_amount = int(action[2])
        if 0 <= repair_index < len(pirate_ship_status):
            if pirate_ship_status[repair_index] + repair_amount <= max_health:
                pirate_ship_status[repair_index] += repair_amount
            else:
                pirate_ship_status[repair_index] = max_health

    elif action[0] == "Status":
        need_repair_amount = max_health * 0.2
        need_repair_count = len([section for section in pirate_ship_status if int(section) < need_repair_amount])
        print(f"{need_repair_count} sections need repair.")

if not has_a_ship_sunk:
    print(f"Pirate ship status: {sum(pirate_ship_status)}")
    print(f"Warship status: {sum(warship_status)}")