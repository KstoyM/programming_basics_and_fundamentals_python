def forecast(*args):
    weather_dict = {'Sunny': [], 'Cloudy': [], 'Rainy': []}
    result = []

    for el in args:
        city, weather = el[0], el[1]

        weather_dict[weather].append(city)

    print(weather_dict)
    for k, v in weather_dict.items():
        for value in sorted(v):
            result.append(f'{value} - {k}')

    return "\n".join(result)

print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))
