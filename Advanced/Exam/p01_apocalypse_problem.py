from collections import deque

textiles = deque(map(int, input().split(" ")))
medicaments = list(map(int, input().split(" ")))

patch = [30, 0]
bandage = [40, 0]
medkit = [100, 0]

prods_dict = {'Patch': 0, 'Bandage': 0, 'MedKit':0}

while textiles and medicaments:

    curr_textile = textiles.popleft()
    curr_med = medicaments.pop()
    curr_sum = curr_textile + curr_med

    if curr_sum == patch[0]:
        prods_dict['Patch'] += 1
    elif curr_sum == bandage[0]:
        prods_dict['Bandage'] += 1
    elif curr_sum == medkit[0]:
        prods_dict['MedKit'] += 1

    elif curr_sum > medkit[0]:
        prods_dict['MedKit'] += 1
        curr_sum -= medkit[0]
        med = medicaments.pop()
        med = med + curr_sum
        medicaments.append(med)

    else:
        curr_med += 10
        medicaments.append(curr_med)

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
elif not medicaments:
    print("Medicaments are empty.")

for k, v in sorted(prods_dict.items(),key= lambda x: (-x[1], x[0])):
    if v > 0:
        print(f'{k} - {v}')

if medicaments:
    print(f'Medicaments left: {", ".join(str(m) for m in (medicaments[::-1]))}')
if textiles:
    print(f'Textiles left: {", ".join(str(t) for t in textiles)}')