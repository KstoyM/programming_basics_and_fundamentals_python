number_stack = [int(n) for n in input().split()]

for n in range(len(number_stack)):
    print(number_stack.pop(), end=' ')