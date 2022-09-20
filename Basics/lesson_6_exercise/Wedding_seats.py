sector = input()
rows_in_first_sector = int(input())
places_in_uneven_row = int(input())

cnt_of_places = 0

for index_of_sector in range(65, ord(sector) + 1):
    row = 1
    places_current = places_in_uneven_row
    if index_of_sector > 65:
        rows_in_first_sector += 1
    for row in range(1, rows_in_first_sector + 1):
        if row % 2 == 0:
            places_current += 2
        else:
            if row > 1:
                places_current -= 2
        for place in range(97, places_current + 97):
            cnt_of_places += 1
            print(f'{chr(index_of_sector)}{row}{chr(place)}')
print(f'{cnt_of_places}')
