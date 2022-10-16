input_version = [int(version) for version in input().split(".")]

input_version[2] += 1

if input_version[2] == 10:
    input_version[2] = 0
    input_version[1] += 1
    if input_version[1] == 10:
        input_version[1] = 0
        input_version[0] += 1

result = map(str, input_version)
print('.'.join(result))