def insert_space_func(message, curr_index):
    message = message[:curr_index] + ' ' + message[curr_index:]
    print(message)
    return message


def reverse_func(message, new_string):
    if new_string in message:
        message = message.replace(new_string, '', 1)
        message = message + new_string[::-1]
        print(message)
    else:
        print('error')
    return message


def change_all_func(message, old_string, new_string):
    if old_string in message:
        message = message.replace(old_string, new_string)
    print(message)
    return message


concealed_message = input()

while True:

    command = input().split(':|:')

    if command[0] == 'Reveal':
        print(f"You have a new text message: {concealed_message}")
        break

    action = command[0]

    if action == 'InsertSpace':
        index = int(command[1])
        concealed_message = insert_space_func(concealed_message, index)
    if action == 'Reverse':
        substring = command[1]
        concealed_message = reverse_func(concealed_message, substring)
    if action == 'ChangeAll':
        substring = command[1]
        replacement_str = command[2]
        concealed_message = change_all_func(concealed_message, substring, replacement_str)
