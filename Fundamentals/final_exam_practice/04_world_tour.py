def add_stop_func(curr_stops, curr_index, curr_string):
    if 0 <= curr_index < len(curr_stops):
        curr_stops = curr_stops[:curr_index] + curr_string + curr_stops[curr_index:]
    return curr_stops


def remove_stop_func(curr_stops, s_index, e_index):
    if 0 <= s_index <= e_index < len(curr_stops):
        curr_stops = curr_stops[:s_index] + curr_stops[e_index + 1:]
    return curr_stops


def switch_func(curr_stops, o_string, n_string):
    if o_string in curr_stops:
        curr_stops = curr_stops.replace(o_string, n_string)
    return curr_stops


stops_str = input()

while True:

    command = input().split(":")

    if command[0] == 'Travel':
        break

    elif command[0] == 'Add Stop':
        index = int(command[1])
        string = command[2]
        stops_str = add_stop_func(stops_str, index, string)

    elif command[0] == 'Remove Stop':
        start_index = int(command[1])
        end_index = int(command[2])
        stops_str = remove_stop_func(stops_str, start_index, end_index)

    elif command[0] == 'Switch':
        old_string = command[1]
        new_string = command[2]
        stops_str = switch_func(stops_str, old_string, new_string)
    print(stops_str)
print(f"Ready for world tour! Planned stops: {stops_str}")