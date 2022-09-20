price_of_kg_veggies = float(input())
price_of_kg_fruits = float(input())
total_kg_veggies = int(input())
total_kg_fruits = int(input())

total_income = (price_of_kg_veggies * total_kg_veggies + price_of_kg_fruits * total_kg_fruits) / 1.94

print(f'{total_income:.2f}')