floors = int(input())
apartments = int(input())

apt_name = ''
apt_number = 0

for floor in range(floors, 0, -1):
    for flat in range(apartments):
        apt_number = floor * 10 + flat

        if floor == floors:
            apt_name = f'L{apt_number}'
        elif floor % 2 != 0:
            apt_name = f'A{apt_number}'
        else:
            apt_name = f'O{apt_number}'

        print(f'{apt_name}', end=' ')
    print()