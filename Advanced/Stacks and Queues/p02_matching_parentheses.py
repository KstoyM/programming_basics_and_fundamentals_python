stack = input()
indexes = []

for i in range(len(stack)):
    ch = stack[i]

    if ch == "(":
        indexes.append(i)
    elif ch == ")":
        left_p = indexes.pop()
        print(stack[left_p:i + 1])