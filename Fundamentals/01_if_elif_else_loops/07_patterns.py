number = int(input())

for n in range(1, number+1):
    for i in range(0, n):
        print('*',  end='')
    print()
for n in range(number-1, 0, -1):
    for i in range(0, n):
        print('*', end='')
    print()