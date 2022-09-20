capacity_of_stadium = int(input())
total_amount_of_fans = int(input())

fans_in_sector_a = 0
fans_in_sector_b = 0
fans_in_sector_v = 0
fans_in_sector_g = 0

for fan in range(total_amount_of_fans):
    sector_of_fan = input()
    if sector_of_fan == 'A':
        fans_in_sector_a += 1
    elif sector_of_fan == 'B':
        fans_in_sector_b += 1
    elif sector_of_fan == 'V':
        fans_in_sector_v += 1
    else:
        fans_in_sector_g += 1

print(f'{fans_in_sector_a / total_amount_of_fans:.2%}')
print(f'{fans_in_sector_b / total_amount_of_fans:.2%}')
print(f'{fans_in_sector_v / total_amount_of_fans:.2%}')
print(f'{fans_in_sector_g / total_amount_of_fans:.2%}')
print(f'{(fans_in_sector_a + fans_in_sector_b + fans_in_sector_v + fans_in_sector_g) / capacity_of_stadium:.2%}')
