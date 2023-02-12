# this task was done after drinking 0.5l of rakia  kekw

def words_sorting(*args):
    dick = {}
    result = []
    for word in args:
        sum_word = 0
        if word not in dick:
            dick[word] = []
        for v in word:
            sum_word = ord(v)
            dick[word].append(sum_word)

    values_sum = sum(sum(s for s in v) for v in dick.values())

    if values_sum % 2 != 0:
        for k, v in sorted(dick.items(), key=lambda x: -sum(x[1])):
            result.append(f'{k} - {sum(v)}')
    else:
        for k, v in sorted(dick.items(), key=lambda x: x[0]):
            result.append(f'{k} - {sum(v)}')

    return '\n'.join(result)


print(
    words_sorting(
        'cacophony',
        'accolade'
  ))