matrix = [[el for el in input()] for _ in range(int(input()))]
symbol = input()
flag = False

for row in range(len(matrix)):
    for col in range(len(matrix)):
        if symbol == matrix[row][col]:
            print(f'{(row, col)}')
            flag = True
            break
    if flag:
        break
if not flag:
    print(f'{symbol} does not occur in the matrix')