from collections import deque

fireworks_effects = deque(map(int, input().split(", ")))
explosive_power = list(map(int, input().split(", ")))

fireworks_dict = {
    'Palm Fireworks': 0,
    'Willow Fireworks': 0,
    'Crossette Fireworks': 0
}

while fireworks_effects and explosive_power:

    if fireworks_dict['Palm Fireworks'] >= 3 and \
            fireworks_dict['Willow Fireworks'] >= 3 and fireworks_dict['Crossette Fireworks'] >= 3:
        break

    curr_firework = fireworks_effects.popleft()
    curr_explosive_power = explosive_power.pop()

    if 0 < curr_firework and 0 < curr_explosive_power:

        sum_vals = curr_firework + curr_explosive_power

    else:
        if curr_firework <= 0 and curr_explosive_power <= 0:
            continue
        elif curr_firework <= 0:
            explosive_power.append(curr_explosive_power)
            continue
        elif curr_explosive_power <= 0:
            fireworks_effects.appendleft(curr_firework)
            continue

    if sum_vals % 3 == 0 and sum_vals % 5 != 0:
        fireworks_dict['Palm Fireworks'] += 1
    elif sum_vals % 5 == 0 and sum_vals % 3 != 0:
        fireworks_dict['Willow Fireworks'] += 1
    elif sum_vals % 5 == 0 and sum_vals % 3 == 0:
        fireworks_dict['Crossette Fireworks'] += 1
    else:
        curr_firework -= 1
        fireworks_effects.append(curr_firework)
        explosive_power.append(curr_explosive_power)

if fireworks_dict['Palm Fireworks'] >= 3 and \
        fireworks_dict['Willow Fireworks'] >= 3 and fireworks_dict['Crossette Fireworks'] >= 3:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")
if fireworks_effects:
    print(f'Firework Effects left: {", ".join(str(fire) for fire in fireworks_effects)}')
if explosive_power:
    print(f'Explosive Power left: {", ".join(str(exp) for exp in explosive_power)}')
for k, v in fireworks_dict.items():
    print(f"{k}: {v}")
