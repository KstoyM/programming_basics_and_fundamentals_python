def get_info(**kwargs):
    sentence = ''
    for k, v in kwargs.items():
        if k == 'name':
            sentence += f"This is {v} "
        elif k == 'town':
            sentence += f'from {v} '
        else:
            sentence += f'and he is {v} years old'
    return sentence


print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))
