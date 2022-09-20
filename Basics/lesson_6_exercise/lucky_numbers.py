number = int(input())

for n in range(1, number + 1):
    for n2 in range(1, number + 1):
        for n3 in range(1, number + 1):
            for n4 in range(1, number + 1):
                if n + n2 == n3 + n4 and number % (n + n2) == 0:
                    print(f'{n}{n2}{n3}{n4}', end=' ')