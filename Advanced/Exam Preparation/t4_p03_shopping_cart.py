def shopping_cart(*args):
    meals = {'Soup': [], 'Pizza': [], 'Dessert': []}
    meals_boundary = {'Soup': 3, 'Pizza': 4, 'Dessert': 2}
    result = []

    for item in args:
        if 'Stop' in item:
            break
        if len(meals[item[0]]) < meals_boundary[item[0]] and item[1] not in meals[item[0]]:
            meals[item[0]].append(item[1])

    for k, v in sorted(meals.items(), key=lambda x: (-len(x[1]), x[0])):
        result.append(f"{k}:")
        for value in sorted(v):
            result.append(f' - {value}')

    are_there_any_meals = bool(sum([len(v) for v in meals.values()]))

    if are_there_any_meals:
        return "\n".join(result)
    else:
        return f"No products in the cart!"


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))