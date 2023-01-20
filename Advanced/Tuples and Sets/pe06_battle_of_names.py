odd_set = set()
even_set = set()

for line in range(1, int(input()) + 1):
    name_sum = sum(ord(letter) for letter in input()) // line
    if name_sum % 2 == 0:
        even_set.add(name_sum)
    else:
        odd_set.add(name_sum)

if sum(odd_set) == sum(even_set):
    print(odd_set.union(even_set))
elif sum(odd_set) > sum(even_set):
    print(f"{', '.join([str(v) for v in odd_set.difference(even_set)])}")
else:
    print(f"{', '.join([str(v) for v in odd_set.symmetric_difference(even_set)])}")