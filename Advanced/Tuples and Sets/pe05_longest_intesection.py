iterations = int(input())

intersections = dict()

for iteration in range(iterations):
    rng_one, rng_two = [el.split(",") for el in input().split("-")]

    set_one = list(range(int(rng_one[0]), int(rng_one[1]) + 1))
    set_two = list(range(int(rng_two[0]), int(rng_two[1]) + 1))

    intersection = set(set_one).intersection(set(set_two))
    intersections[iteration + 1] = [el for el in intersection]

longest_intersection_len = max(len(el) for el in intersections.values())
longest_intersection = max(intersections.values(), key=len)
print(f"Longest intersection is {longest_intersection} with length {longest_intersection_len}")