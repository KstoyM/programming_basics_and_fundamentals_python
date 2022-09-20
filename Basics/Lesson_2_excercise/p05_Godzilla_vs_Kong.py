movie_budget = float(input())
number_of_extras = int(input())
price_of_clothes_set = float(input())

decor = movie_budget * 0.1
total_price_of_clothes = number_of_extras * price_of_clothes_set

if number_of_extras > 150:
    total_price_of_clothes = total_price_of_clothes - (total_price_of_clothes * 0.1)

if decor + total_price_of_clothes > movie_budget:
    print(f"Not enough money!")
    print(f"Wingard needs {decor + total_price_of_clothes - movie_budget:.2f} leva more.")

if decor + total_price_of_clothes <= movie_budget:
    print(f"Action!")
    print(f"Wingard starts filming with {movie_budget - decor - total_price_of_clothes:.2f} leva left.")