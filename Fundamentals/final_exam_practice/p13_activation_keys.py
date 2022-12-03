def contains_func(key, substring):
    if substring in key:
        print(f"{key} contains {substring}")
    else:
        print("Substring not found!")


def flip_func(key, case, start_index, end_index):
    replace_string = key[start_index:end_index]
    if case == 'Upper':
        key = key.replace(replace_string, replace_string.upper())
    else:
        key = key.replace(replace_string, replace_string.lower())
    print(key)
    return key


def slice_func(key, start_index, end_index):
    replace_string = key[start_index:end_index]
    key = key.replace(replace_string, "")
    print(key)
    return key


raw_key = input()

while True:

    command = input().split(">>>")

    if command[0] == 'Generate':
        print(f"Your activation key is: {raw_key}")
        break

    action = command[0]

    if action == 'Contains':
        sub_str = command[1]
        contains_func(raw_key, sub_str)
    if action == 'Flip':
        casing = command[1]
        start_ind = int(command[2])
        end_ind = int(command[3])
        raw_key = flip_func(raw_key, casing, start_ind, end_ind)
    if action == 'Slice':
        start_ind = int(command[1])
        end_ind = int(command[2])
        raw_key = slice_func(raw_key, start_ind, end_ind)