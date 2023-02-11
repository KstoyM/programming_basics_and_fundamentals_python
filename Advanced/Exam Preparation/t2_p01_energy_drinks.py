from collections import deque

milligrams_of_caffeine = list(map(int, input().split(", ")))
energy_drinks = deque(map(int, input().split(", ")))

MAX_CAFFEINE = 300
caffeine_tracker = 0

while milligrams_of_caffeine and energy_drinks:

    curr_energy_drink = energy_drinks.popleft()
    current_caffeine_dose = milligrams_of_caffeine.pop() * curr_energy_drink

    if current_caffeine_dose + caffeine_tracker <= MAX_CAFFEINE:
        caffeine_tracker += current_caffeine_dose
    else:
        energy_drinks.append(curr_energy_drink)
        if caffeine_tracker - 30 > 0:
            caffeine_tracker -= 30
        else:
            caffeine_tracker = 0

if energy_drinks:
    drinks_to_str = f'{", ".join(str(en) for en in energy_drinks)}'
    print(f'Drinks left: {drinks_to_str}')
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {caffeine_tracker} mg caffeine.")