def shopping_list(budget, **products):
    bought_items = []
    max_len = 10
    result = []

    if budget >= 100:
        for item_name, item_specs in products.items():
            item_price, item_quant = item_specs
            item_total_price = item_price * item_quant

            if item_total_price <= budget and len(bought_items) < max_len:
                bought_items.append(item_name)
                bought_items.append(item_total_price)
                budget -= item_total_price

        for index in range(0, len(bought_items), 2):

            if index + 1 <= len(bought_items):
                result.append(f'You bought {bought_items[index]} for ')
                result.append(f'{bought_items[index + 1]:.2f} leva.\n')

        return ''.join(result)

    else:
        return f'You do not have enough budget.'


print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))