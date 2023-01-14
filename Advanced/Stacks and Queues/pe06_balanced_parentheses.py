from collections import deque

parentheses = deque([sym for sym in input()])
left_part = deque()
right_index = 0

while parentheses:
    left_parentheses = parentheses.popleft()

    if left_parentheses in "{[(":
        left_part.append(left_parentheses)
    elif not left_part:
        print("NO")
        break
    else:
        if f"{left_part.pop() + left_parentheses}" not in "{}[]()":
            print("NO")
            break
else:
    print('YES')
