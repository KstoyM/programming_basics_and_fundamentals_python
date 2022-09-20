#Read Input

square_meters_nylon_needed = int(input())
liters_of_paint_needed = int(input())
liters_of_paint_thinner = int(input())
hours_needed_for_workers_to_finish_the_job = int(input())

#Process Input

sum_for_nylon = (square_meters_nylon_needed+2) * 1.5
sum_for_paint = (liters_of_paint_needed + (liters_of_paint_needed * 0.1)) * 14.5
sum_for_paint_thinner = liters_of_paint_thinner * 5
price_of_workers_per_hour = (sum_for_paint + sum_for_nylon + sum_for_paint_thinner + 0.4) * 0.3
total_price = sum_for_nylon + sum_for_paint + sum_for_paint_thinner + 0.4 + hours_needed_for_workers_to_finish_the_job*price_of_workers_per_hour

#Print
print(total_price)