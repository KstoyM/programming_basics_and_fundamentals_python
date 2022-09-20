command = input()

total_steps = 0

while command != 'Going home':
    steps_walked = int(command)
    total_steps += steps_walked

    if total_steps >= 10000:
        break

    command = input()

if command == 'Going home':
    command = int(input())
    total_steps += command

if total_steps > 10000:
    print(f'Goal reached! Good job!')
    print(f'{total_steps - 10000} steps over the goal!')
else:
    print(f'{abs(10000 - total_steps)} more steps to reach goal.')