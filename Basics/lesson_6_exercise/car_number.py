range_start = int(input())
range_end = int(input())

for n1 in range(range_start, range_end + 1):
    for n2 in range(range_start, range_end + 1):
        for n3 in range(range_start, range_end + 1):
            for n4 in range(range_start, range_end + 1):
                if n1 % 2 == 0 and n4 % 2 != 0 and n1 > n4 and (n2 + n3) % 2 == 0:
                    print(f'{n1}{n2}{n3}{n4}', end=' ')
                elif n4 % 2 == 0 and n1 % 2 != 0 and n1 > n4 and (n2 + n3) % 2 == 0:
                    print(f'{n1}{n2}{n3}{n4}', end=' ')
