def change_func(message, old_letter, new_letter):
    message = message.replace(old_letter, new_letter)
    return message


def move_func(message, step_cnt):
    start_str = ''
    end_str = ''
    for index_letter in range(len(message)):
        if index_letter < int(step_cnt):
            end_str += message[index_letter]
        else:
            start_str += message[index_letter]
    message = start_str + end_str
    return message


def insert_func(message, ins_index, letter):
    message = message[:int(ins_index)] + letter + message[int(ins_index):]
    return message


encrypted_message = input()

while True:

    curr_command = input()

    if curr_command == 'Decode':
        break

    command = curr_command.split('|')

    action = command[0]
    if action == 'Move':
        steps = command[1]
        encrypted_message = move_func(encrypted_message, steps)

    if action == 'Insert':
        index = command[1]
        ins_letter = command[2]
        encrypted_message = insert_func(encrypted_message, index, ins_letter)

    if action == 'ChangeAll':
        rep_old = command[1]
        rep_new = command[2]
        encrypted_message = change_func(encrypted_message, rep_old, rep_new)

print(f'The decrypted message is: {encrypted_message}')