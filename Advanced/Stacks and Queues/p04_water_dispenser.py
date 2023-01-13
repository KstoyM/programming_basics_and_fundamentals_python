from collections import deque


def start_func(people_que, water):
    while True:
        action = input().split()
        if action[0] == 'End':
            print(f'{water} liters left')
            break
        elif action[0] == 'refill':
            liters_to_refill = int(action[1])
            water += liters_to_refill
        else:
            necessary_water = int(action[0])
            current_person = people_que.popleft()
            if water - necessary_water >= 0:
                water -= necessary_water
                print(f'{current_person} got water')
            else:
                print(f'{current_person} must wait')


quantity_of_water = int(input())

people = deque()

while True:

    command = input()

    if command == 'Start':
        start_func(people, quantity_of_water)
        break

    else:
        people.append(command)