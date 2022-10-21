def shoot_func(lst, index, power):
    if 0 <= index < len(lst):
        if lst[index] - power <= 0:
            lst.pop(index)
        else:
            lst[index] -= power

    return lst


def add_func(lst, index, value):
    if 0 <= index < len(lst):
        lst.insert(index, value)
    else:
        print("Invalid placement!")

    return lst


def strike_func(lst, index, radius):
    validator_index = index - radius > 0 and index + radius < len(lst)
    if validator_index:
        start_index = index - radius
        end_index = index + radius
        lst = [lst[i] for i in range(len(lst)) if i < start_index or i > end_index]
    else:
        print("Strike missed!")

    return lst


target_sequence = list(map(int, input().split()))

command = input()

while True:

    if command == 'End':
        break

    action, value1, value2 = command.split()

    if action == 'Shoot':
        target_sequence = shoot_func(target_sequence, int(value1), int(value2))

    elif action == 'Add':
        target_sequence = add_func(target_sequence, int(value1), int(value2))

    elif action == 'Strike':
        target_sequence = strike_func(target_sequence, int(value1), int(value2))

    command = input()

result = '|'.join([str(element) for element in target_sequence])
print(result)
