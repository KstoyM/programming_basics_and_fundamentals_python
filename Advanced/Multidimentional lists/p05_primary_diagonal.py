matrix = [list(map(int, input().split())) for col in range(int(input()))]
primary_dgn_sum = 0

for row in range(len(matrix)):
    primary_dgn_sum += matrix[row][row]

print(primary_dgn_sum)
