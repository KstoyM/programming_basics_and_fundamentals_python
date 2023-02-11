names = input().split(", ")
size = 6
matrix = []

locked_player_one = False
locked_player_two = False

for row in range(size):
    matrix.append(input().split())

while True:

    player_one = names[0]
    p_row, p_col = [int(x) for x in input() if x.isdigit()]

    if not locked_player_one:

        if matrix[p_row][p_col] == 'E':
            print(f"{player_one} found the Exit and wins the game!")
            break

        elif matrix[p_row][p_col] == 'T':
            names.remove(player_one)
            player_who_won = ''.join(names)
            print(f"{player_one} is out of the game! The winner is {player_who_won}.")
            break

        elif matrix[p_row][p_col] == 'W':
            print(f"{player_one} hits a wall and needs to rest.")
            locked_player_one = True

    else:
        locked_player_one = False

    player_two = names[1]
    p_row, p_col = [int(x) for x in input() if x.isdigit()]

    if not locked_player_two:

        if matrix[p_row][p_col] == 'E':
            print(f"{player_two} found the Exit and wins the game!")
            break

        elif matrix[p_row][p_col] == 'T':
            names.remove(player_two)
            player_who_won = ''.join(names)
            print(f"{player_two} is out of the game! The winner is {player_who_won}.")
            break

        elif matrix[p_row][p_col] == 'W':
            print(f"{player_two} hits a wall and needs to rest.")
            locked_player_two = True

    else:
        locked_player_two = False



