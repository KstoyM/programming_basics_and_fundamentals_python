import os

directory = input()
files = {}

for filename in os.listdir(directory):
    extension = filename.split(".")[-1]
    if extension not in files:
        files[extension] = []
    files[extension].append(filename)

    with open('report.txt', 'w') as file:
        for key, values in sorted(files.items()):
            values_joined = "\n".join(f'- - - {v}' for v in values)
            file.write(f'.{key}\n{values_joined}\n')
