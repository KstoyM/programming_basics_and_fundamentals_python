SIZE = 8

board = []
pawn_positions = {
    'w': [[], [-1]],
    'b': [[], [1]]
}

validation = {
    'w': 0,
    'b': 7
}

positions = {
    'col': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
    'row': [8, 7, 6, 5, 4, 3, 2, 1]
}

for row in range(SIZE):
    board.append(input().split())

    if "w" in board[row]:
        pawn_positions['w'][0] = [row, board[row].index('w')]
    if "b" in board[row]:
        pawn_positions['b'][0] = [row, board[row].index('b')]

    white_pos = pawn_positions['w'][0]
    black_pos = pawn_positions['b'][0]

while True:

    if 'b' in board[white_pos[0]][white_pos[1] + 1] or 'b' in board[white_pos[0]][white_pos[1] - 1]:
        print(f"Game over! White win, capture on {positions['col'][black_pos[1]]}{positions['row'][black_pos[0] - 1]}.")
        break

    white_pos = [white_pos[0] - 1, white_pos[1]]


    if white_pos[0] == validation['w']:
        print(f"Game over! White pawn is promoted to a queen at "
              f"{positions['col'][white_pos[1]]}{positions['row'][white_pos[0]]}.")
        break

    if 'w' in board[black_pos[0]][black_pos[1] + 1] or 'b' in board[black_pos[0]][black_pos[1] - 1]:
        print(f"Game over! Black win, capture on {positions['col'][white_pos[1]]}{positions['row'][white_pos[0] + 1]}.")
        break

    black_pos = [black_pos[0] + 1, black_pos[1]]

    if black_pos[0] == validation['b']:
        print(f"Game over! Black pawn is promoted to a queen at "
              f"{positions['col'][black_pos[1]]}{positions['row'][black_pos[0]]}.")
        break
