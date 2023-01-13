from collections import deque

kids_names = deque(input().split())

hot_index = int(input())
current_index = 0

while len(kids_names) > 0:

    current_kid = kids_names.popleft()
    current_index += 1

    if len(kids_names) == 0:
        print(f'Last is {current_kid}')

    else:
        if current_index == hot_index:
            current_index = 0
            print(f'Removed {current_kid}')
        else:
            kids_names.append(current_kid)
