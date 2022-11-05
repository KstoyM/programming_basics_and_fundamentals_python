mine = {}

while True:

    command = input()

    if command == "stop":
        break

    material = command
    quantity = int(input())

    if material not in mine:
        mine[material] = 0
    mine[material] += quantity

for mat in mine.keys():
    print(f"{mat} -> {mine[mat]}")