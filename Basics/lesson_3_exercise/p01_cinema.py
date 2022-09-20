# ⦁	Premiere - премиерна прожекция, на цена 12.00 лева;
# ⦁	Normal - стандартна прожекция, на цена 7.50 лева;
# ⦁	Discount - прожекция за деца, ученици и студенти на намалена цена от 5.00 лева.

type_of_projection = input()
number_of_rows = int(input())
number_of_columns = int(input())
price = 0

if type_of_projection == 'Premiere':
    price = 12
elif type_of_projection == 'Normal':
    price = 7.5
elif type_of_projection == 'Discount':
    price = 5

total_income = price * number_of_columns * number_of_rows
print(f'{total_income:.2f} leva')