item_collection = input().split('|')
budget = float(input())
starting_budget = budget
list_of_purchases = []

for item in item_collection:
    split_string = item.split('->')
    if split_string[0] == 'Clothes' and float(split_string[1]) <= 50 and float(split_string[1]) <= budget:
        list_of_purchases.append(split_string[1])
        budget -= float(split_string[1])
    elif split_string[0] == 'Shoes' and float(split_string[1]) <= 35 and float(split_string[1]) <= budget:
        list_of_purchases.append(split_string[1])
        budget -= float(split_string[1])
    elif split_string[0] == 'Accessories' and float(split_string[1]) <= 20.5 and float(split_string[1]) <= budget:
        list_of_purchases.append(split_string[1])
        budget -= float(split_string[1])

for item in list_of_purchases:
    budget += float(item) * 1.4
    print(f'{float(item) * 1.4:.2f}', end=' ')

print()
print(f'Profit: {budget - starting_budget:.2f}', end='\n')

if budget > 150:
    print("Hello, France!")
else:
    print("Not enough money.")