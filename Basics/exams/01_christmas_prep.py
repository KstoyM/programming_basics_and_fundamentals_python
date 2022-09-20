qty_paper = int(input())
qty_linen = int(input())
liters_of_glue = float(input())
discount = int(input())

total_sum = qty_paper * 5.8 + qty_linen * 7.2 + liters_of_glue * 1.2
total_sum -= total_sum * discount / 100

print(f'{total_sum:.3f}')