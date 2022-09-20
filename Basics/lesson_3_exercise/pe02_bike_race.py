cnt_of_junior_bikers = int(input())
cnt_of_senior_bikers = int(input())
trace_type = input()
price_of_entry = 0
price_of_entry_juniors = 0
price_of_entry_seniors = 0

if trace_type == 'trail':
    price_of_entry_juniors = 5.5
    price_of_entry_seniors = 7
elif trace_type == 'cross-country':
    price_of_entry_juniors = 8
    price_of_entry_seniors = 9.5
elif trace_type == 'downhill':
    price_of_entry_juniors = 12.25
    price_of_entry_seniors = 13.75
elif trace_type == 'road':
    price_of_entry_juniors = 20
    price_of_entry_seniors = 21.5

price_of_entry = price_of_entry_seniors * cnt_of_senior_bikers + price_of_entry_juniors * cnt_of_junior_bikers

if trace_type == 'cross-country' and cnt_of_senior_bikers + cnt_of_junior_bikers >= 50:
    price_of_entry -= price_of_entry * 0.25

tax_for_organisers = price_of_entry * 0.05

print(f'{price_of_entry - tax_for_organisers:.2f}')