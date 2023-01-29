size = int(input())

territory = []
tea_bags = 0
alice_pos = []

move_commands = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(size):
    territory.append(input().split())

    if "A" in territory[row]:
        alice_pos = [row, territory[row].index("A")]
        territory[alice_pos[0]][alice_pos[1]] = '*'

while tea_bags < 10:

    command = input()

    alice_pos = [
        alice_pos[0] + move_commands[command][0],
        alice_pos[1] + move_commands[command][1]
    ]

    if not (0 <= alice_pos[0] < size and 0 <= alice_pos[1] < size):
        print("Alice didn't make it to the tea party.")
        break

    if territory[alice_pos[0]][alice_pos[1]] == 'R':
        print("Alice didn't make it to the tea party.")
        territory[alice_pos[0]][alice_pos[1]] = '*'
        break

    elif territory[alice_pos[0]][alice_pos[1]].isdigit():
        tea_bags += int(territory[alice_pos[0]][alice_pos[1]])
        territory[alice_pos[0]][alice_pos[1]] = '*'
    else:
        territory[alice_pos[0]][alice_pos[1]] = '*'

if tea_bags >= 10:
    print("She did it! She went to the party.")
[print(*r) for r in territory]
