cake_length = int(input())
cake_height = int(input())

number_of_pieces = cake_length * cake_height
number_of_pieces_taken = 0

command = input()

while command != 'STOP':
    pieces_taken = int(command)
    number_of_pieces -= pieces_taken
    number_of_pieces_taken += pieces_taken

    if number_of_pieces <= 0:
        print(f'No more cake left! You need {number_of_pieces_taken - cake_height * cake_length} pieces more.')
        break
    else:
        command = input()

if command == 'STOP':
    print(f'{cake_height * cake_length - number_of_pieces_taken} pieces are left.')
