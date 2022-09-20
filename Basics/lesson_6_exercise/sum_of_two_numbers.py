start_int = int(input())
end_int = int(input())
magic_number = int(input())

counter = 0
flag = False

for n1 in range(start_int, end_int + 1):
    for n2 in range(start_int, end_int + 1):
        counter += 1
        if n1 + n2 == magic_number:
            flag = True
            print(f'Combination N:{counter} ({n1} + {n2} = {n1 + n2})')
            break
    if flag:
        break

if not flag:
    print(f'{counter} combinations - neither equals {magic_number}')
