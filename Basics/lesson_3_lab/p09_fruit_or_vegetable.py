type_of_product = input()

if type_of_product == 'banana' or type_of_product == 'apple' or type_of_product == 'kiwi'\
        or type_of_product == 'cherry' or type_of_product == 'lemon' or type_of_product == 'grapes':
    print('fruit')
elif type_of_product in ['tomato', 'cucumber', 'pepper', 'carrot']:
    print('vegetable')
else:
    print('unknown')