first_num_max = int(input())
second_num_max = int(input())
third_num_max = int(input())

for n1 in range(1, first_num_max + 1):
    for n2 in range(2, second_num_max + 1):
        for n3 in range(1, third_num_max + 1):
            if n1 % 2 == 0 and n3 % 2 == 0 and n2 in [2, 3, 5, 7]:
                print(f'{n1} {n2} {n3}')