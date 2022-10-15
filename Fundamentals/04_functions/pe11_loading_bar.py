def loading_status(number):
    if number == 100:
        return '100% Complete!\n[%%%%%%%%%%]'
    else:
        return f'{number}% [{(number // 10) * chr(37)}{(10 - number // 10) * chr(46)}]\nStill loading...'


input_number = int(input())

print(loading_status(input_number))
