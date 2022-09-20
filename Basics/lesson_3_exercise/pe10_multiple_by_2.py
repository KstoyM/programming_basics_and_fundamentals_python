while True:
    number = float(input())
    if number >= 0:
        print(f'Result: {number * 2:.2f}')
    elif number < 0:
        print('Negative number!')
        break