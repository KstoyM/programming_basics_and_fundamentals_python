def create_matrix(rows: int, cols: int):
    matrix = []

    for _ in range(rows):
        matrix.append([0] * cols)

    return matrix


def player_choice(player):
    choice = int(input(f"Player {player}, please choose a column: \n"))

    return choice - 1


def implement_player_data_to_main_logic(playground, player_index, player):
    start_row_index = 0

    while start_row_index < len(playground) and playground[start_row_index][player_index] == 0:
        start_row_index += 1

    playground[start_row_index - 1][player_index] = player

    return start_row_index - 1, player_index


def check_win_condition(playground, row_index, column_index, win_counter):
    def check_right_win_condition(playground, row_index, column_index, max_column_index):
        right_values = [playground[row_index][i] for i in range(column_index, max_column_index)]
        return right_values

    def check_left_win_condition(playground, row_index, column_index, min_column_index):
        left_values = [playground[row_index][i] for i in range(column_index, min_column_index, -1)]
        return left_values

    def check_up_win_condition(playground, row_index, column_index, min_row_index):
        up_values = [playground[i][column_index] for i in range(row_index, min_row_index, -1)]
        return up_values

    def check_down_win_condition(playground, row_index, column_index, max_row_index):
        down_values = [playground[i][column_index] for i in range(row_index, max_row_index)]
        return down_values

    def check_down_right_win_condition(playground, row_index, column_index, max_row_index, max_column_index):
        diagonal_index = min(max_row_index - row_index, max_column_index - column_index)
        down_right_values = [playground[row_index + i][column_index + i] for i in range(diagonal_index)]
        return down_right_values

    def check_down_left_win_condition(playground, row_index, column_index, max_row_index, min_column_index):
        diagonal_index = min(max_row_index - row_index, abs(min_column_index - column_index))
        down_left_values = [playground[row_index + i][column_index - i] for i in range(diagonal_index)]
        return down_left_values

    def check_up_right_win_condition(playground, row_index, column_index, min_row_index, max_column_index):
        diagonal_index = min(abs(min_row_index - row_index), max_column_index - column_index)
        up_right_values = [playground[row_index - i][column_index + i] for i in range(diagonal_index)]
        return up_right_values

    def check_up_left_win_condition(playground, row_index, column_index, min_row_index, min_column_index):
        diagonal_index = min(abs(min_row_index - row_index), abs(min_column_index - column_index))
        up_left_values = [playground[row_index - i][column_index - i] for i in range(diagonal_index)]
        return up_left_values

    # indexes
    max_column_index = min(column_index + win_counter, len(playground[column_index]))
    min_column_index = max(-1, column_index - win_counter)
    max_row_index = min(row_index + win_counter, len(playground))
    min_row_index = max(-1, row_index - win_counter)

    # left, right, up, down
    right_win_condition_values = check_right_win_condition(playground, row_index, column_index, max_column_index)
    left_win_condition_values = check_left_win_condition(playground, row_index, column_index, min_column_index)
    up_win_condition_values = check_up_win_condition(playground, row_index, column_index, min_row_index)
    down_win_condition_values = check_down_win_condition(playground, row_index, column_index, max_row_index)

    # diagonals
    down_right_win_condition_values = check_down_right_win_condition(playground, row_index, column_index, max_row_index,
                                                                     max_column_index)
    down_left_win_condition_values = check_down_left_win_condition(playground, row_index, column_index, max_row_index,
                                                                   min_column_index)
    up_right_win_condition_values = check_up_right_win_condition(playground, row_index, column_index, min_row_index,
                                                                 max_column_index)
    up_left_win_condition_values = check_up_left_win_condition(playground, row_index, column_index, min_row_index,
                                                               min_column_index)

    possible_winner_checker = [
        right_win_condition_values,
        left_win_condition_values,
        up_win_condition_values,
        down_win_condition_values,
        down_right_win_condition_values,
        down_left_win_condition_values,
        up_right_win_condition_values,
    ]

    return any(len(current_list) == win_counter and len(set(current_list)) == 1 for current_list in possible_winner_checker)


def game_play_func(playground, win_counter):
    current_player, second_player = 1, 2

    while True:
        current_player_choice = player_choice(current_player)
        row_index, column_index = implement_player_data_to_main_logic(playground, current_player_choice, current_player)
        print_func(playground)

        if check_win_condition(playground, row_index, column_index, win_counter):
            print(f"The winner is player {current_player}")
            break

        current_player, second_player = second_player, current_player


def print_func(playground):
    for row in playground:
        print(row)


rows = int(input('Enter the number of rows: '))
cols = int(input('Enter the number of columns: '))
win_condition = int(input('Enter count for win combination: '))
playground = create_matrix(rows, cols)
game_play_func(playground, win_condition)
