# notes = []
#
# while True:
#     command = input()
#     if command == "End":
#         break
#
#     current_action = command.split("-")
#     action_importance = int(current_action[0]) - 1
#     action = current_action[1]
#
#     notes.append((action_importance, action))
#
# sorted_notes = [note[1] for note in sorted(notes)]
# print(sorted_notes)

list_of_actions = [0] * 10

while True:
    command = input()

    if command == 'End':
        break

    current_action = command.split("-")
    action_importance = int(current_action[0]) - 1
    action = current_action[1]

    list_of_actions.pop(action_importance)
    list_of_actions.insert(action_importance, action)

result = [element for element in list_of_actions if element != 0]
print(result)