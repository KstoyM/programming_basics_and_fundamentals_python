elements = input().split()
stock = {}

for i in range(0, len(elements), 2):
    key = elements[i]
    value = int(elements[i + 1])
    stock[key] = value

search_products = input().split(" ")

for product in search_products:

    if product in stock.keys():
        print(f"We have {stock[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")

