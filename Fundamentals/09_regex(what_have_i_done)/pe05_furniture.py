import re

bought_furniture = []
total_money_spent = 0
pattern = r'>>([A-Za-z]+)<<(\d+[.\d]*)!(\d+)\b'

while True:

    command = input()

    if command == 'Purchase':
        break

    matches = re.search(pattern, command)
    if matches:
        furniture, price, quantity = matches.groups()
        bought_furniture.append(furniture)
        total_money_spent += float(price) * int(quantity)

print('Bought furniture:')
for furniture in bought_furniture:
    print(furniture)
print(f'Total money spend: {total_money_spent:.2f}')