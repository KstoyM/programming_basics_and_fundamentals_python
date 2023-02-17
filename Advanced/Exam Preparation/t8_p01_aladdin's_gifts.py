from collections import deque

materials = list(map(int, input().split()))
magic_level = deque(map(int, input().split()))

gemstone = [range(100, 200), 0]
porcelain_sculpture = [range(200, 300), 0]
gold = [range(300, 400), 0]
diamond_jewellery = [range(400, 500), 0]

while materials and magic_level:

    curr_mat = materials[-1]
    curr_magic = magic_level[0]
    curr_item_val = curr_magic + curr_mat

    if curr_item_val < 100:
        if curr_item_val % 2 == 0:
            curr_item_val = curr_mat * 2 + curr_magic * 3
        else:
            curr_item_val = curr_mat * 2 + curr_magic * 2

    elif curr_item_val > 499:
        curr_item_val = int(curr_item_val / 2)

    if curr_item_val in range(100, 501):
        curr_mat = materials.pop()
        curr_magic = magic_level.popleft()
        if curr_item_val in gemstone[0]:
            gemstone[1] += 1
        elif curr_item_val in porcelain_sculpture[0]:
            porcelain_sculpture[1] += 1
        elif curr_item_val in gold[0]:
            gold[1] += 1
        elif curr_item_val in diamond_jewellery[0]:
            diamond_jewellery[1] += 1

    else:
        curr_mat = materials.pop()
        curr_magic = magic_level.popleft()

if gemstone[1] + porcelain_sculpture[1] >= 2 or gold[1] + diamond_jewellery[1] >= 2:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f'Materials left: {", ".join(str(el) for el in materials)}')
if magic_level:
    print(f'Magic left: {", ".join(str(el) for el in magic_level)}')

if diamond_jewellery[1] > 0:
    print(f'Diamond Jewellery: {diamond_jewellery[1]}')
if gemstone[1] > 0:
    print(f'Gemstone: {gemstone[1]}')
if gold[1] > 0:
    print(f'Gold: {gold[1]}')
if porcelain_sculpture[1] > 0:
    print(f'Porcelain Sculpture: {porcelain_sculpture[1]}')