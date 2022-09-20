speed_entered_by_the_user = float(input())

if speed_entered_by_the_user <= 10:
    print('slow')
elif speed_entered_by_the_user <= 50:
    print('average')
elif speed_entered_by_the_user <= 150:
    print('fast')
elif speed_entered_by_the_user <= 1000:
    print('ultra fast')
elif speed_entered_by_the_user > 1000:
    print('extremely fast')