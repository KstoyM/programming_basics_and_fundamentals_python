a = int(input())
b = int(input())
max_passwords = int(input())

time_to_break = False

for i in range(35, 56):
    if time_to_break:
        break
    for i2 in range(64, 97):
        if time_to_break:
            break
        for i3 in range(1, a + 1):
            if time_to_break:
                break
            for i4 in range(1, b + 1):
                max_passwords -= 1

                if i > 55:
                    i = 35
                if i2 > 96:
                    i2 = 64

                print(f'{chr(i)}{chr(i2)}{i3}{i4}{chr(i2)}{chr(i)}', end='|')

                i += 1
                i2 += 1

                if i3 == a and i4 == b:
                    time_to_break = True
                    break

                if max_passwords == 0:
                    time_to_break = True
                    break