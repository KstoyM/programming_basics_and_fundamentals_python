string1, string2 = input().split(" ")

total_sum = 0

if len(string1) > len(string2):
    for index in range(len(string2)):
        total_sum += ord(string1[index]) * ord(string2[index])
    for index in range(len(string2), len(string1)):
        total_sum += ord(string1[index])
elif len(string2) > len(string1):
    for index in range(len(string1)):
        total_sum += ord(string2[index]) * ord(string1[index])
    for index in range(len(string1), len(string2)):
        total_sum += ord(string2[index])
else:
    for index in range(len(string1)):
        total_sum += ord(string2[index]) * ord(string1[index])

print(total_sum)