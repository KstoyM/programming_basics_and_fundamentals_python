chat_lst = []

while True:
    command = input()

    if command == "end":
        break

    current_action = command.split()

    if current_action[0] == "Chat":
        chat_lst.append(current_action[1])

    elif current_action[0] == "Delete":
        if current_action[1] in chat_lst:
            chat_lst.remove(current_action[1])

    elif current_action[0] == "Edit":
        if current_action[1] in chat_lst:
            current_action_index = int(chat_lst.index(current_action[1]))
            chat_lst.remove(current_action[1])
            chat_lst.insert(current_action_index, current_action[2])

    elif current_action[0] == "Pin":
        if current_action[1] in chat_lst:
            chat_lst.remove(current_action[1])
            chat_lst.append(current_action[1])

    elif current_action[0] == "Spam":
        spam_list = [chat_lst.append(message) for message in current_action if message != "Spam"]

print(*chat_lst, sep="\n")
