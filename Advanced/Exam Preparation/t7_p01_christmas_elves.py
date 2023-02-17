from collections import deque

elf_energy = deque(map(int, input().split()))
materials = list(map(int, input().split()))

total_energy_used = 0
total_toys_made = 0
que_counter = 1

while materials and elf_energy:

    current_elf = elf_energy.popleft()
    current_material = materials.pop()

    if current_elf < 5:
        materials.append(current_material)
        continue

    if que_counter % 3 == 0 and current_elf >= current_material * 2:
        if que_counter % 5 == 0:
            total_toys_made -= 2
        total_energy_used += current_material * 2
        total_toys_made += 2
        que_counter += 1
        current_elf += 1 - current_material * 2
        elf_energy.append(current_elf)
        continue

    elif que_counter % 5 == 0 and current_elf >= current_material:
        total_energy_used += current_material
        que_counter += 1
        current_elf -= current_material
        elf_energy.append(current_elf)

    elif current_elf >= current_material and not que_counter % 3 == 0:
        total_energy_used += current_material
        total_toys_made += 1
        que_counter += 1
        current_elf += 1 - current_material
        elf_energy.append(current_elf)

    else:
        current_elf *= 2
        que_counter += 1
        elf_energy.append(current_elf)
        materials.append(current_material)

print(f'Toys: {total_toys_made}')
print(f'Energy: {total_energy_used}')

if elf_energy:
    print(f'Elves left: {", ".join(str(elf) for elf in elf_energy)}')
if materials:
    print(f'Boxes left: {", ".join(str(box) for box in materials)}')
