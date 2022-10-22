def collect_func(lst, coll_item):
    if coll_item not in lst:
        lst.append(coll_item)
    return lst


def drop_func(lst, drop_item):
    if drop_item in lst:
        lst.remove(drop_item)
    return lst


def combine_func(lst, comb_item):
    old_item, new_item = comb_item.split(":")
    if old_item in lst:
        old_item_index = lst.index(old_item)
        lst.insert(old_item_index + 1, new_item)
    return lst


def renew_func(lst, renew_item):
    if renew_item in items:
        lst.remove(renew_item)
        lst.append(renew_item)
    return lst


items = input().split(", ")

while True:

    command = input()

    if command == "Craft!":
        break

    action, item = command.split(" - ")

    if action == "Collect":
        items = collect_func(items, item)
    elif action == "Drop":
        items = drop_func(items, item)
    elif action == "Combine Items":
        items = combine_func(items, item)
    elif action == "Renew":
        items = renew_func(items, item)

print(f"{', '.join(items)}")
