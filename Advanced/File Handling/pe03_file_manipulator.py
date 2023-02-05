import os


def create_func(file_name):
    with open(file_name, 'w') as file:
        file.write("")


def add_func(file_name, content):
    with open(file_name, 'a') as file:
        file.write(f"{content}\n")


def replace_func(file_name, old_string, new_string):
    try:
        with open(file_name, 'r') as file:
            text = file.readlines()
            for i in range(len(text)):
                text[i] = text[i].replace(old_string, new_string)

        with open(file_name, 'w') as file:
            file.write("".join(text))

    except FileNotFoundError:
        print("An error occurred")


def delete_func(file_name):
    try:
        os.remove(*file_name)

    except FileNotFoundError:
        print("An error occurred")


command = input()

COMMANDS = {
    'Create': lambda x: create_func(*x),
    'Add': lambda x, y: add_func(x, y),
    'Replace': lambda x, y, z: replace_func(x, y, z),
    'Delete': lambda x: delete_func(x)
}

while command != 'End':
    action, *data = command.split("-")

    if len(data) == 1:
        COMMANDS[action](data)
    else:
        COMMANDS[action](*data)

    command = input()
