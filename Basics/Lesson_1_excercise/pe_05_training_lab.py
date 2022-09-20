length_in_meters = float(input())
width_in_meters = float(input())


number_of_desks_width = (width_in_meters * 100 - 100) / 70
blabla = (width_in_meters * 100 - 100) / 70 - (width_in_meters * 100 - 100) % 70
print(blabla)
number_of_desks_length = (length_in_meters * 100) // 120

number_of_desks_total = number_of_desks_width * number_of_desks_length - 3

print(number_of_desks_total)