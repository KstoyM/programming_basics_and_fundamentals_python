countries = input().split(", ")
capitals = input().split(", ")
result_dict = {countries[index]: capitals[index] for index in range(len(countries))}

for country, capital in result_dict.items():
    print(f"{country} -> {capital}")