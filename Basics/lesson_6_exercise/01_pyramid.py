num = int(input())

counter = 1
is_counter_bigger_than_num = False

for row in range(1, num + 1):
    for col in range(1, row + 1):
        if counter > num:
            is_counter_bigger_than_num = True
            break
        print(f'{counter} ', end='')
        counter += 1
    if is_counter_bigger_than_num:
        break
    print()