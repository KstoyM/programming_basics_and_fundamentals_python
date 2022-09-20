number_of_dog_food_packages = int(input())
number_of_cat_food_packages = int(input())
dog_food_total = float(number_of_dog_food_packages*2.5)
cat_food_total = float(number_of_cat_food_packages*4)
final_price=dog_food_total+cat_food_total
print(f"{final_price} lv.")
