def take_odd_func(string):
    new_string = ''
    for index in range(len(string)):
        if index % 2 != 0:
            new_string += string[index]
    print(new_string)
    return new_string


def cut_func(string, index, length):
    substring = string[index: index + length]
    string = string.replace(substring, '', 1)
    print(string)
    return string


def substitute_func(string, sub_str, new_str):
    if sub_str in string:
        string = string.replace(sub_str, new_str)
        print(string)
    else:
        print("Nothing to replace!")
    return string


data = input()

while True:

    command = input().split(" ")
    action = command[0]

    if action == "Done":
        print(f"Your password is: {data}")
        break

    elif action == 'TakeOdd':
        data = take_odd_func(data)
    elif action == 'Cut':
        cut_index = int(command[1])
        cut_length = int(command[2])
        data = cut_func(data, cut_index, cut_length)
    elif action == 'Substitute':
        sub_string = command[1]
        substitute = command[2]
        data = substitute_func(data, sub_string, substitute)
