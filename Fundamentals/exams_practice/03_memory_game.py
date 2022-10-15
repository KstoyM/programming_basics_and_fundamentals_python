sequence = [str(string) for string in input().split()]

command = input().split()
moves = 0

while command[0] != 'end':
    current_command = [int(string1) for string1 in command]

    moves += 1

    if current_command[0] == current_command[1] or 0 > current_command[0] or current_command[0] >= len(sequence) \
            or 0 > current_command[1] or current_command[1] >= len(sequence):
        middle_of_sequence = len(sequence) // 2
        string_to_insert = str(-moves) + 'a'
        sequence.insert(middle_of_sequence, string_to_insert)
        sequence.insert(middle_of_sequence, string_to_insert)
        print('Invalid input! Adding additional elements to the board')
        command = input().split()
        continue

    elif sequence[current_command[0]] == sequence[current_command[1]]:
        x = sequence.pop(current_command[0])
        sequence.remove(x)
        print(f"Congrats! You have found matching elements - {x}!")

    else:
        print('Try again!')

    if len(sequence) == 0:
        # is_game_over = True
        print(f"You have won in {moves} turns!")
        break

    command = input().split()

if command[0] == 'end':
    print('Sorry you lose :(')
    print(*sequence)