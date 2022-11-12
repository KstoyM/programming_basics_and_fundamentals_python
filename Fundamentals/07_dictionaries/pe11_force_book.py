force_book = {}

while True:
    command = input()
    is_force_user_in_book = False

    if command == "Lumpawaroo":
        break

    if "|" in command:
        force_side, force_user = command.split(" | ")
        for user in force_book.values():
            if force_user in user:
                is_force_user_in_book = True
        if force_side not in force_book and not is_force_user_in_book:
            force_book[force_side] = []
            force_book[force_side].append(force_user)
        elif not is_force_user_in_book:
            force_book[force_side].append(force_user)

    if "->" in command:
        force_user, force_side = command.split(" -> ")
        for user in force_book.values():
            if force_user in user:
                is_force_user_in_book = True
        if force_side not in force_book.keys():
            force_book[force_side] = []
        if not is_force_user_in_book:
            force_book[force_side].append(force_user)
        else:
            for side, user in force_book.items():
                if force_user in force_book[side]:
                    force_book[side].remove(force_user)
            force_book[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")

for side, members in force_book.items():
    if len(force_book[side]) > 0:
        print(f"Side: {side}, Members: {len(force_book[side])}")
        for member in force_book[side]:
            print(f"! {member}")