def naughty_or_nice_list(kids, *commands, **kwargs):
    result_dict = {'Nice': [], 'Naughty': [], 'Not found': []}
    kids_dict = {}
    nice_list = ''
    naughty_list = ''
    not_found_list = ''

    for kid in kids:
        kid_value, kid_name = kid[0], kid[1]
        if kid_value not in kids_dict:
            kids_dict[kid_value] = []
        kids_dict[kid_value].append(kid_name)

    for command in commands:
        comm_value, command_status = command.split("-")
        if int(comm_value) in kids_dict:
            if len(kids_dict[int(comm_value)]) > 1:
                continue
            else:
                kid_name = kids_dict[int(comm_value)]
                result_dict[command_status].append(*kids_dict[int(comm_value)])
                kids_dict[int(comm_value)].remove(*kid_name)

    for name, status in kwargs.items():
        name_count = 0
        for value in kids_dict.values():
            if name in value:
                name_count += value.count(name)

        if name_count == 1:
            result_dict[status].append(name)
            for value in kids_dict.values():
                if name in value:
                    value.remove(name)

    if kids_dict.values():
        for value in kids_dict.values():
            if value:
                result_dict['Not found'].append(*value)

    for key in result_dict:
        if len(result_dict[key]) > 0:
            if key == 'Nice':
                nice_list += f'{key}: '
                for value in result_dict[key]:
                    nice_list += f'{value}, '
            elif key == 'Naughty':
                naughty_list += f'{key}: '
                for value in result_dict[key]:
                    naughty_list += f'{value}, '
            else:
                not_found_list += f'{key}: '
                for value in result_dict[key]:
                    not_found_list += f'{value}, '

    nice_list = nice_list.rstrip(" ,")
    naughty_list = naughty_list.rstrip(" ,")
    not_found_list = not_found_list.rstrip(" ,")
    final_result = ''
    if nice_list:
        final_result += f'{nice_list}\n'
    if naughty_list:
        final_result += f'{naughty_list}\n'
    if not_found_list:
        final_result += f'{not_found_list}\n'

    return final_result


print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
