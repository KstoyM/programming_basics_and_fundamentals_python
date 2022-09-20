inheritance_amt = float(input())
year_of_death = int(input())
money_used = 0

for n in range(1800, year_of_death + 1):
    if n % 2 == 0:
        money_used += 12000
    else:
        money_used += 12000 + 50 * (n - 1800 + 18)

if inheritance_amt >= money_used:
    print(f"Yes! He will live a carefree life and will have {inheritance_amt - money_used:.2f} dollars left.")
else:
    print(f'He will need {money_used - inheritance_amt:.2f} dollars to survive.')