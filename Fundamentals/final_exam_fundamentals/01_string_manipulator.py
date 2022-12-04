input_str = input()

while True:
    command = input().split()

    if command[0] == 'End':
        break

    action = command[0]

    if action == 'Translate':
        char = command[1]
        replacement = command[2]
        input_str = input_str.replace(char, replacement)
        print(input_str)
    elif action == 'Includes':
        substring = command[1]
        if substring in input_str:
            print('True')
        else:
            print('False')
    elif action == 'Start':
        substring = command[1]
        substring_len = len(substring)
        if input_str[:substring_len] == substring:
            print('True')
        else:
            print('False')
    elif action == 'Lowercase':
        input_str = input_str.lower()
        print(input_str)
    elif action == 'FindIndex':
        char = command[1]
        for i in range(len(input_str) - 1, -1, -1):
            if char == input_str[i]:
                print(i)
                break
    elif action == 'Remove':
        start_index = int(command[1])
        count = int(command[2])
        input_str = input_str[:start_index] + input_str[start_index + count:]
        print(input_str)