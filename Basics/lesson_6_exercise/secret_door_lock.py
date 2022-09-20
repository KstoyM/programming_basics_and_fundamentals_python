hundreds = int(input())
tens = int(input())
ones = int(input())

for h in range(1, hundreds + 1):
    for t in range(1, tens + 1):
        for o in range(1, ones + 1):
            if h % 2 == 0 and o % 2 == 0:
                if t in [2, 3, 5, 7]:
                    print(f'{h} {t} {o}')