x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())

point_location = ''

if x1 < x < x2 and y1 < y < y2:
    point_location = 'Inside / Outside'
elif x > x2:
    point_location = 'Inside / Outside'
elif y > y2:
    point_location = 'Inside / Outside'
elif x < x1:
    point_location = 'Inside / Outside'
elif y < y1:
    point_location = 'Inside / Outside'
else:
    point_location = 'Border'

print(point_location)