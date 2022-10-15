command = input()
price_without_taxes = 0
price_without_disc = 0
total_price = 0

while True:
    if command not in ['special', 'regular']:
        part_price = float(command)
        if part_price < 0:
            print('Invalid price!')
            command = input()
            continue

        price_without_taxes += part_price
        price_without_disc += part_price * 1.2
        command = input()

    else:
        if command == 'special':
            total_price = price_without_disc - price_without_disc * 0.1
        else:
            total_price = price_without_disc
        if total_price == 0:
            print("Invalid order!")
            break
        print(f"Congratulations you've just bought a new computer!\n"
              f"Price without taxes: {price_without_taxes:.2f}$\n"
              f"Taxes: {price_without_disc - price_without_taxes:.2f}$\n"
              f"-----------\n"
              f"Total price: {total_price:.2f}$")
        break
