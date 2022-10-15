budget = float(input())
flour_price = float(input())

price_of_eggs = flour_price * 0.75
price_of_milk = flour_price * 1.25 / 4
price_of_bread = price_of_eggs + price_of_milk + flour_price

colored_eggs = 0
bread_counter = 0

while budget >= price_of_bread:
    colored_eggs += 3
    bread_counter += 1
    budget -= price_of_bread

    if bread_counter % 3 == 0:
        colored_eggs -= bread_counter - 2

print(f"You made {bread_counter} loaves of Easter bread! Now you have "
      f"{colored_eggs} eggs and {budget:.2f}BGN left.")
