rows, cols = [int(x) for x in input().split()]

matrix = [input().split() for _ in range(rows)]
valid_index_rows = range(rows)
valid_index_cols = range(cols)

while True:

    command, *info = [int(x) if x.isdigit() else x for x in input().split()]

    if command == 'END':
        break

    elif command == 'swap':

        row_el_one, col_el_one, row_el_two, col_el_two = \
            info[0], info[1], info[2], info[3]

        if row_el_one in valid_index_rows and row_el_two in valid_index_rows and col_el_one in \
                valid_index_cols and col_el_two in valid_index_cols and len(command) == 4:

            matrix[row_el_one][col_el_one], matrix[row_el_two][col_el_two] = \
                matrix[row_el_two][col_el_two], matrix[row_el_one][col_el_one]

            [print(*el) for el in matrix]

        else:
            print('Invalid input!')

    else:
        print('Invalid input!')
        continue
