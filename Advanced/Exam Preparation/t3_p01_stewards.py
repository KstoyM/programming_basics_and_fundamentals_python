from collections import deque

seats = input().split(", ")
first_seq = deque(input().split(", "))
second_seq = deque(input().split(","))
taken_seats = []
rotations = 0
matches = 0

while rotations < 10 and matches < 3:

    first_num = int(first_seq.popleft())
    sec_num = int(second_seq.pop())

    ascii_char = chr(first_num + sec_num)

    first_comb = f"{first_num}{ascii_char}"
    second_comb = f"{sec_num}{ascii_char}"

    rotations += 1

    if first_comb in seats:
        matches += 1
        taken_seats.append(first_comb)
        seats.remove(first_comb)
    elif second_comb in seats:
        matches += 1
        taken_seats.append(second_comb)
        seats.remove(second_comb)
    else:
        first_seq.append(str(first_num))
        second_seq.appendleft(str(sec_num))

print(f'Seat matches: {", ".join(taken_seats)}', end="")
print(f'\nRotations count: {rotations}')