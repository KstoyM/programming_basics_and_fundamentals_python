#Read Input

number_of_chicken_menus = int(input())
number_of_fish_menus = int(input())
number_of_veggie_menus = int(input())

#Processing Input

price_of_desert = (number_of_chicken_menus * 10.35 + number_of_fish_menus * 12.4 + number_of_veggie_menus * 8.15) * 0.2
total_price = round((number_of_chicken_menus * 10.35 + number_of_fish_menus * 12.4 + number_of_veggie_menus * 8.15 + \
              price_of_desert + 2.5), 2)

#Print Output
print(total_price)
