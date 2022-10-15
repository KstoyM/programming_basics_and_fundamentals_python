decorations_to_buy = int(input())
days_until_christmas = int(input())

ornaments_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15

money_spent = 0
spirit = 0

for day in range(1, days_until_christmas + 1):
    if day % 11 == 0:
        decorations_to_buy += 2
    if day % 2 == 0:
        money_spent += decorations_to_buy * ornaments_price
        spirit += 5
    if day % 3 == 0:
        money_spent += decorations_to_buy * (tree_skirt_price + tree_garland_price)
        spirit += 13
    if day % 5 == 0:
        money_spent += decorations_to_buy * tree_lights_price
        spirit += 17
        if day % 3 == 0:
            spirit += 30
    if day % 10 == 0:
        spirit -= 20
        money_spent += tree_skirt_price + tree_garland_price + tree_lights_price

if days_until_christmas % 10 == 0:
    spirit -= 30

print(f"Total cost: {money_spent}")
print(f"Total spirit: {spirit}")
