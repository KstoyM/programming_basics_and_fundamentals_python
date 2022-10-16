initial_array = input().split()
final_array = list(initial_array)


while True:

    command = input().split()
    if 'end' in command:
        break

    elif 'decrease' in command:
        final_array = [int(element) - 1 for element in final_array]
        continue

    action = command[0]
    first_index = int(command[1])
    second_index = int(command[2])

    if action == 'swap':
        final_array[first_index], final_array[second_index] = \
            final_array[second_index], final_array[first_index]

    elif action == 'multiply':
        element_to_add = final_array.pop(first_index)
        if first_index < second_index:
            element_amended = (int(element_to_add) * int(final_array[second_index - 1]))
        else:
            element_amended = (int(element_to_add) * int(final_array[second_index]))
        final_array.insert(first_index, element_amended)


print(*final_array, sep=', ')
