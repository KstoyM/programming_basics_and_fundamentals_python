start = int(input())
end = int(input())
magic_number = int(input())
counter = 0
flag = False

for x1 in range(start, end + 1):
    for x2 in range(start, end + 1):
        counter += 1
        if x1 + x2 == magic_number:
            flag = True
            break
    if flag:
        break

if not flag:
    print(f"{counter} combinations - neither equals {magic_number}")
else:
    print(f'Combination N:{counter} ({x1} + {x2} = {magic_number})')