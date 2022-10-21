numbers = list(map(int, input().split()))

average_number = sum(numbers) / len(numbers)

max_number = max(numbers)
added_numbers = 0
result_list = []
flag = False

if max_number <= average_number:
    print('No')
    flag = True
else:
    while True:

        if added_numbers == 5 or max(numbers) <= average_number:
            break

        else:
            current_max = max(numbers)
            result_list.append(current_max)
            numbers.remove(current_max)
            added_numbers += 1

if not flag:
    print(*result_list)