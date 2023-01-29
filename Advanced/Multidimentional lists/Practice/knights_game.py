size = int(input())
board = [list(input()) for _ in range(size)]

removed_knights = 0

positions = (
    (-2, -1),
    (-2, 1),
    (-1, -2),
    (-1, 2),
    (2, -1),
    (2, 1),
    (1, 2),
    (1, -2)
)

while True:
    max_attacks = 0
    knight_with_max_attacks_pos = []

    for row in range(size):
        for col in range(size):
            attacks = 0

            if board[row][col] == "K":

                for pos in positions:
                    pos_row = row + pos[0]
                    pos_col = col + pos[1]

                    if 0 <= pos_row < size and 0 <= pos_col < size:
                        if board[pos_row][pos_col] == "K":
                            attacks += 1

            if attacks > max_attacks:
                max_attacks = attacks
                knight_with_max_attacks_pos = [row, col]

    if knight_with_max_attacks_pos:
        board[knight_with_max_attacks_pos[0]][knight_with_max_attacks_pos[1]] = "0"
        removed_knights += 1
    else:
        break

print(removed_knights)
