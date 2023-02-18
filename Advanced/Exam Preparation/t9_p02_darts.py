SIZE = 7
players = input().split(", ")
board = [input().split(" ") for _ in range(SIZE)]

scores = [501, 501]
shots_made = [0, 0]

while scores[1] > 0:

    current_player = players[0]
    shots_made[0] += 1

    shots = eval(input())
    shot_r, shot_c = int(shots[0]), int(shots[1])

    if 0 <= shot_r < SIZE and 0 <= shot_c < SIZE:
        target_shot = board[shot_r][shot_c]
        if target_shot == 'B':
            print(f'{current_player} won the game with {shots_made[0]} throws!')
            break

        elif target_shot == 'D' or target_shot == 'T':
            shot_sum = int(board[shot_r][0]) + int(board[shot_r][-1]) + int(board[0][shot_c]) + int(board[-1][shot_c])

            if target_shot == 'D':
                scores[0] -= shot_sum * 2
            else:
                scores[0] -= shot_sum * 3

        else:
            scores[0] -= int(board[shot_r][shot_c])

    players[0], players[1] = players[1], players[0]
    scores[0], scores[1] = scores[1], scores[0]
    shots_made[0], shots_made[1] = shots_made[1], shots_made[0]

if scores[1] <= 0:
    print(f'{players[1]} won the game with {shots_made[1]} throws!')
