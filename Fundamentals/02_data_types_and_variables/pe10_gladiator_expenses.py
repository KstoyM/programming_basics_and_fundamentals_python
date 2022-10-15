lost_fights_count = int(input())
broken_helmets = lost_fights_count // 2
broken_swords = lost_fights_count // 3
broken_shields = lost_fights_count // 6
broken_armors = broken_shields // 2

helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

expenses = broken_helmets * helmet_price + broken_swords * sword_price + \
    broken_shields * shield_price + broken_armors * armor_price

print(f'Gladiator expenses: {expenses:.2f} aureus')