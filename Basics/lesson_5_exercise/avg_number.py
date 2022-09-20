iterations = int(input())

total_sum = 0

for n in range(iterations):
    curr_num = int(input())
    total_sum += curr_num

print(f'{total_sum / iterations:.2f}')