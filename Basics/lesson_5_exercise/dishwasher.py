detergent = int(input())

number_of_plates_current = 0
number_of_plates_total = 0
number_of_pots_current = 0
number_of_pots_total = 0
total_detergent = detergent * 750
total_detergent_left = total_detergent
counter = 0
things_for_washing = 0

curr_command = input()
while curr_command != 'End':
    things_for_washing = int(curr_command)
    counter += 1
    number_of_pots_current = 0
    number_of_plates_current = 0

    if counter % 3 == 0:
        number_of_pots_current += things_for_washing
        number_of_pots_total += things_for_washing
        total_detergent_left -= number_of_pots_current * 15
    else:
        number_of_plates_current += things_for_washing
        number_of_plates_total += things_for_washing
        total_detergent_left -= number_of_plates_current * 5

    if total_detergent_left < 0:
        break

    curr_command = input()

if total_detergent_left >= 0:
    print(f'Detergent was enough!')
    print(f'{number_of_plates_total} dishes and {number_of_pots_total} pots were washed.')
    print(f'Leftover detergent {total_detergent - (number_of_plates_total * 5 + number_of_pots_total * 15)} ml.')
else:
    print(f'Not enough detergent, {abs(total_detergent_left)} ml. more necessary!')