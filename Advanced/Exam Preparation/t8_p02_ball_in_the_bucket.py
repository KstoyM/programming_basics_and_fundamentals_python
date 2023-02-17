SIZE = 6
board = []

total_points = 0

for i in range(SIZE):
    board.append(input().split(" "))

for turn in range(3):
    row, col = [int(x.strip("()")) for x in input().split(', ')]
    if 0 <= row < SIZE and 0 <= col < SIZE:
        if board[row][col] == 'B':
            board[row][col] = '0'
            for c in board:
                total_points += int(c[col])

if total_points >= 100:
    if total_points in range(100, 200):
        print(f"Good job! You scored {total_points} points, and you've won Football.")
    elif total_points in range(200, 300):
        print(f"Good job! You scored {total_points} points, and you've won Teddy Bear.")
    elif total_points > 299:
        print(f"Good job! You scored {total_points} points, and you've won Lego Construction Set.")
else:
    print(f"Sorry! You need {100 - total_points} points more to win a prize.")