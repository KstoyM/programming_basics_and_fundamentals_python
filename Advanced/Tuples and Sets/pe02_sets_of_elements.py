len_first_set, len_second_set = input().split(" ")

set_one = set(input() for _ in range(int(len_first_set)))
set_two = set(input() for _ in range(int(len_second_set)))

intersection = set_one.intersection(set_two)

print(*intersection, sep="\n")