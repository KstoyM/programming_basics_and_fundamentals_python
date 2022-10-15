divisor = int(input())
boundary = int(input())

for counter in range(boundary, divisor, -1):
    if counter % divisor == 0:
        print(counter)
        break