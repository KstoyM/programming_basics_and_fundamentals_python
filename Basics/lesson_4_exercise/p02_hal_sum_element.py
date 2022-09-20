from sys import maxsize

iterations = int(input())
max_num = -maxsize
total_sum = 0

for _ in range(iterations):
    current_num = int(input())
    total_sum += current_num
    if current_num > max_num:
        max_num = current_num

if max_num == total_sum - max_num:
    print('Yes')
    print(f'Sum = {max_num}')
else:
    print('No')
    diff = abs(max_num - (total_sum - max_num))
    print(f'Diff = {diff}')