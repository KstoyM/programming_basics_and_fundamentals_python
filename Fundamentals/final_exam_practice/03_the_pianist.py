# My solution

def add_func(pieces_dict, curr_piece, curr_composer, curr_key):
    if curr_piece in pieces_dict:
        print(f"{curr_piece} is already in the collection!")
    else:
        pieces_dict[curr_piece] = [curr_composer, curr_key]
        print(f"{curr_piece} by {curr_composer} in {curr_key} added to the collection!")


def remove_func(pieces_dict, curr_piece):
    if curr_piece in pieces_dict:
        del pieces_dict[curr_piece]
        print(f"Successfully removed {curr_piece}!")

    else:
        print(f"Invalid operation! {curr_piece} does not exist in the collection.")


def change_key_func(pieces_dict, curr_piece, curr_key):
    if curr_piece in pieces_dict:
        pieces_dict[curr_piece].remove(pieces_dict[curr_piece][1])
        pieces_dict[curr_piece].append(curr_key)
        print(f"Changed the key of {curr_piece} to {curr_key}!")
    else:
        print(f"Invalid operation! {curr_piece} does not exist in the collection.")


def print_func(pieces_dict):
    for curr_piece in pieces_dict:
        composer_p = pieces_dict[curr_piece][0]
        key_p = pieces_dict[curr_piece][1]
        print(f"{curr_piece} -> Composer: {composer_p}, Key: {key_p}")


number_of_pieces = int(input())
pieces = {}

for index in range(number_of_pieces):
    piece = input().split("|")
    pieces[piece[0]] = [piece[1], piece[2]]

while True:

    command = input().split("|")

    if command[0] == 'Stop':
        print_func(pieces)
        break

    piece = command[1]

    if command[0] == 'Add':
        composer = command[2]
        key = command[3]
        add_func(pieces, piece, composer, key)

    elif command[0] == 'Remove':
        remove_func(pieces, piece)

    elif command[0] == 'ChangeKey':
        new_key = command[2]
        change_key_func(pieces, piece, new_key)


# Mario's solution

# def store_data_func(number):
#     data = {}
#     for _ in range(number):
#         current_data = input().split('|')
#         piece = current_data[0]
#         composer = current_data[1]
#         key = current_data[2]
#
#         data[piece] = [composer, key]
#
#     return data
#
#
# def add_command_function(piece, composer, key, data):
#     if piece not in data:
#         data[piece] = [composer, key]
#         print(f"{piece} by {composer} in {key} added to the collection!")
#     else:
#         print(f"{piece} is already in the collection!")
#
#
# def remove_function(piece, data):
#     if piece in data:
#         print(f"Successfully removed {piece}!")
#         del data[piece]
#     else:
#         print(f"Invalid operation! {piece} does not exist in the collection.")
#
#
# def change_key_function(piece, new_key, data):
#     if piece in data:
#         # Our dictionary for example ---> {'Fur Elise': ['Beethoven', 'A Minor']}
#         # At the index 0 in list is composer, at the index 1 is a specific key
#         data[piece][1] = new_key
#         print(f"Changed the key of {piece} to {new_key}!")
#     else:
#         print(f"Invalid operation! {piece} does not exist in the collection.")
#
#
# def print_function(data):
#     result = ''
#     for piece in data:
#         composer = data[piece][0]
#         key = data[piece][1]
#         result += f"{piece} -> Composer: {composer}, Key: {key}\n"
#
#     return result
#
#
# # Our core function that navigates our entire program. Each time in it
# # we will accept one element as a parameter -- > number of pieces
# def the_pianist_func(number):
#     # store_data_func returns a dictionary containing as key the name of
#     # pieces and as value containing a list of two elements. At index 0 in
#     # the list is the name of composer, and at the index 1 in the list is
#     # specific key
#     data = store_data_func(number)
#
#     while True:
#         command = input().split('|')
#
#         if command[0] == 'Stop':
#             print(print_function(data))
#             break
#
#         current_command = command[0]
#         piece = command[1]
#
#         if current_command == 'Add':
#             composer = command[2]
#             key = command[3]
#             add_command_function(piece, composer, key, data)
#
#         elif current_command == 'Remove':
#             remove_function(piece, data)
#
#         elif current_command == 'ChangeKey':
#             new_key = command[2]
#             change_key_function(piece, new_key, data)
#
#
# number_of_pieces = int(input())
# the_pianist_func(number_of_pieces)