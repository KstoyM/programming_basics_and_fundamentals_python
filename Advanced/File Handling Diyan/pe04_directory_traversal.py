import os


def save_extensions(dir_name, first_level=False):
    for filename in os.listdir(dir_name):
        file = os.path.join(dir_name, filename)
        print(file)
        if os.path.isfile(filename):
            extension = filename.split(".")[-1]

            if extension not in extensions:
                extensions[extension] = []

            extensions[extension].append(filename)
        elif os.path.isdir(filename) and not first_level:
            save_extensions(dir_name + "/" + filename, first_level=True)


directory = input()
extensions = {}
result = []

save_extensions(directory)

extensions = sorted(extensions.items(), key=lambda x: x[0])

for extension, files in extensions:
    result.append(f".{extension}")

    for file in sorted(files):
        result.append(f"- - -{file}")

with open(f'report.txt', 'w') as file:

    file.write("\n".join(result))