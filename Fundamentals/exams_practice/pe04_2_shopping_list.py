def urgent_func(lst, item):
    if item not in lst:
        lst.insert(0, item)
    return lst


def unnecessary_func(lst, item):
    if item in lst:
        lst.remove(item)
    return lst


def correct_func(lst, old_item, new_item):
    if old_item in lst:
        old_item_index = lst.index(old_item)
        lst.remove(old_item)
        lst.insert(old_item_index, new_item)
    return lst


def rearrange_func(lst, item):
    if item in lst:
        lst.remove(item)
        lst.append(item)
    return lst


initial_list = input().split("!")

while True:

    command = input()

    if command == "Go Shopping!":
        break

    action = command.split()

    if action[0] == "Urgent":
        initial_list = urgent_func(initial_list, action[1])

    elif action[0] == "Unnecessary":
        initial_list = unnecessary_func(initial_list, action[1])

    elif action[0] == "Correct":
        initial_list = correct_func(initial_list, action[1], action[2])

    elif action[0] == "Rearrange":
        initial_list = rearrange_func(initial_list, action[1])

print(f"{', '.join(initial_list)}")
