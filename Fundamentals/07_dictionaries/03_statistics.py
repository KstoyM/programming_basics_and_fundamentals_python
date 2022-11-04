products = {}

while True:

    command = input()

    if command == "statistics":
        break

    key, value = command.split(": ")

    if key not in products:
        products[key] = 0
    products[key] += int(value)

print("Products in stock:")
for product, quantity in products.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(products.keys())}")
print(f"Total Quantity: {sum(products.values())}")


