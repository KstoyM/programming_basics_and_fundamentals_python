price_of_mackerel_kg = float(input())
price_of_sprat_kg = float(input())
weight_kg_bonito = float(input())
weight_kg_scad = float(input())
weight_kg_mussels = float(input())

price_of_bonito_kg = price_of_mackerel_kg * 1.6
price_of_scad_kg = price_of_sprat_kg * 1.8

price_of_mussels_total = 7.5 * weight_kg_mussels

price_of_all_products = price_of_bonito_kg * weight_kg_bonito + price_of_scad_kg * weight_kg_scad + price_of_mussels_total

print(f'{price_of_all_products:.2f}')