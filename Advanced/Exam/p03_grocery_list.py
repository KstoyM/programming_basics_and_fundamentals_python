def shop_from_grocery_list(budget, products_to_buy, *price_list):

    for product in price_list:
        product_name = product[0]
        product_price = product[1]

        if product_name not in products_to_buy:
            continue
        elif product_price > budget:
            break
        else:
            budget -= product_price
            products_to_buy.remove(product_name)

    if products_to_buy:
        return f"You did not buy all the products. Missing products: {', '.join(p for p in products_to_buy)}."
    else:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))