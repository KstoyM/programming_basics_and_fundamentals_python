products_dict = {}

while True:

    command = input()

    if command == "buy":
        break

    product, price, quantity = command.split(" ")

    if product not in products_dict:
        products_dict[product] = [0, 0]
    products_dict[product][0] = price
    products_dict[product][1] += int(quantity)

for key, value in products_dict.items():
    price = float(value[0])
    quant = value[1]
    print(f"{key} -> {price * quant:.2f}")