gifts = input().split()
final_list = list(gifts)

command = input().split()

while True:
    if command[0] == 'OutOfStock':
        while command[1] in final_list:
            final_list.remove(command[1])
    elif command[0] == 'Required':
        if int(command[2]) < len(gifts):
            word_to_remove = gifts.pop(int(command[2]))
            if word_to_remove in final_list:
                final_list.insert(final_list.index(word_to_remove), command[1])
                final_list.remove(word_to_remove)
            else:
                final_list.insert(int(command[2]), command[1])
    elif command[0] == 'JustInCase':
        if gifts[-1] != final_list[-1]:
            final_list.append(command[1])
        else:
            final_list[-1], command[1] = command[1], final_list[-1]
    else:
        break
    command = input().split()
print(*final_list)
