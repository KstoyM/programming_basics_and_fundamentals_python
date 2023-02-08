battlefield = [[*input()] for _ in range(int(input()))]

COMMANDS = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}

sub_pos = []
mines_hit = 0
cruisers = 0

for row in range(len(battlefield)):

    if 'S' in battlefield[row]:
        sub_pos = [row, battlefield[row].index("S")]
        battlefield[sub_pos[0]][sub_pos[1]] = "-"

    for el in battlefield[row]:
        if el == "C":
            cruisers += 1

command = input()

while mines_hit != 3 and cruisers > 0:

    row = int(sub_pos[0]) + COMMANDS[command][0]
    col = int(sub_pos[1]) + COMMANDS[command][1]

    sub_pos = [row, col]
    mark_on_position = battlefield[row][col]
    battlefield[row][col] = '-'

    if mark_on_position == '*':
        mines_hit += 1

    elif mark_on_position == 'C':
        cruisers -= 1

    command = input()

battlefield[sub_pos[0]][sub_pos[1]] = 'S'

if mines_hit == 3:
    print(f"Mission failed, U-9 disappeared! Last known coordinates {sub_pos}!")
else:
    print(f'Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!')

for row in battlefield:
    print("".join(row))