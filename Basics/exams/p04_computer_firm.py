number_of_pcs = int(input())

rating_of_curr_pc = 0
total_rating = 0
possible_sales = 0
sales_made = 0

for pc in range(1, number_of_pcs + 1):
    curr_rating = input()
    possible_sales += int(curr_rating) // 10
    rating_of_curr_pc += int(curr_rating) % 10
    total_rating += rating_of_curr_pc
    if rating_of_curr_pc == 2:
        sales_made += 0
    elif rating_of_curr_pc == 3:
        sales_made += possible_sales / 2
    elif rating_of_curr_pc == 4:
        sales_made += possible_sales * 0.7
    elif rating_of_curr_pc == 5:
        sales_made += possible_sales * 0.85
    elif rating_of_curr_pc == 6:
        sales_made += possible_sales
    rating_of_curr_pc = 0
    possible_sales = 0

print(f'{sales_made:.2f}')
print(f'{total_rating / number_of_pcs:.2f}')