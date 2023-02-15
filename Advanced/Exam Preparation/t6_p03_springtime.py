def start_spring(**kwargs):
    fixed_dict = {}
    result = []
    for key, value in kwargs.items():
        if value not in fixed_dict:
            fixed_dict[value] = []
        fixed_dict[value].append(key)

    for key, value in sorted(fixed_dict.items(), key= lambda x: (-len(x[1]), x[0])):
        result.append(f'{key}:')
        for v in sorted(value):
            result.append(f'-{v}')

    return "\n".join(result)


example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))