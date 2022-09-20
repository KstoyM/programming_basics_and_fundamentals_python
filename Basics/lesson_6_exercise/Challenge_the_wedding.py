amt_of_men = int(input())
amt_of_women = int(input())
number_of_tables = int(input())

used_tables = 0
no_more_tables = False

for partner_one in range(1, amt_of_men + 1):
    for partner_two in range(1, amt_of_women + 1):
        used_tables += 1
        print(f'({partner_one} <-> {partner_two})', end=' ')
        if used_tables >= number_of_tables:
            no_more_tables = True
            break
    if no_more_tables:
        break