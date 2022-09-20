number_entered_by_user = int(input())

if number_entered_by_user < 100:
    print(f'Less than 100')
elif number_entered_by_user <= 200:
    print(f'Between 100 and 200')
elif number_entered_by_user > 200:
    print(f'Greater than 200')