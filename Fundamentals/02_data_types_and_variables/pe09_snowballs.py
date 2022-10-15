number_of_snowballs = int(input())

max_weight = 0
max_time = 0
max_quality = 0
max_value = 0

for ball in range(number_of_snowballs):
    weight_of_snowball = int(input())
    time_needed = int(input())
    quality_of_snowball = int(input())
    value_of_snowball = (weight_of_snowball / time_needed) ** quality_of_snowball

    if value_of_snowball > max_value:
        max_weight = weight_of_snowball
        max_time = time_needed
        max_quality = quality_of_snowball
        max_value = value_of_snowball

print(f'{max_weight} : {max_time} = {int(max_value)} ({max_quality})')
