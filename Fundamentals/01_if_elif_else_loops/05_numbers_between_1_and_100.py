curr_num = float(input())

while True:
    if 1 <= curr_num <= 100:
        print(f'The number {curr_num} is between 1 and 100')
        break
    else:
        curr_num = float(input())