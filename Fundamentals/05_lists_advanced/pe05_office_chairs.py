rooms = int(input())
free_chairs = 0
are_chairs_needed = False

for room in range(1, rooms + 1):
    chairs, visitors = input().split()
    if len(chairs) < int(visitors):
        print(f'{int(visitors) - len(chairs)} more chairs needed in room {room}')
        are_chairs_needed = True
    else:
        free_chairs += len(chairs) - int(visitors)

if not are_chairs_needed:
    print(f"Game On, {free_chairs} free chairs left")