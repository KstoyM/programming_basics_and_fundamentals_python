# 1 - iterates through numbers for each value (slower than the second solution)
# numbers = tuple(map(float, input().split(" ")))
# counter = {value:  numbers.count(value) for value in numbers}
#
# for k, v in counter.items():
#     print(f"{k} - {v} times")

# 2 - optimized solution
numbers = tuple(map(float, input().split(" ")))
counter = {}

for number in numbers:
    if number not in counter:
        counter[number] = 0
    counter[number] += 1

for k, v in counter.items():
    print(f"{k} - {v} times")