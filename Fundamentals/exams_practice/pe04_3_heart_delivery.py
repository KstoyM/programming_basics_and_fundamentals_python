neighborhood = list(map(int, input().split("@")))

current_index = 0

while True:

    command = input()

    already_had_valentines_day = False

    if command == "Love!":
        break

    jump, jump_index = command.split()
    jump_index = int(jump_index)

    current_index += jump_index

    if current_index >= len(neighborhood):
        current_index = 0
        if neighborhood[current_index] > 0:
            neighborhood[current_index] -= 2
        else:
            print(f"Place {current_index} already had Valentine's day.")
            already_had_valentines_day = True
    else:
        if neighborhood[current_index] > 0:
            neighborhood[current_index] -= 2
        else:
            print(f"Place {current_index} already had Valentine's day.")
            already_had_valentines_day = True

    if neighborhood[current_index] == 0 and not already_had_valentines_day:
        print(f"Place {current_index} has Valentine's day.")

print(f"Cupid's last position was {current_index}.")

result_list = [i for i in neighborhood if i > 0]

if len(result_list) == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(result_list)} places.")