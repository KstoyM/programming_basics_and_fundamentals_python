lst = input().split("|")

for el in lst[::-1]:
    [print(x, end=" ") for x in el.split(" ") if x.isdigit()]
