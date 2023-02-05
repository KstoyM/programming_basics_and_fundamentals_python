# За въпроси - дискорд K.Stoyanov#5887

def reverse_func(text):
    text_for_reversing = text.split(" ")
    reversed_text = " ".join(word[::-1] for word in text_for_reversing)
    return reversed_text


for_replace = ["-", ",", ".", "!", "?"]

with open('text.txt', 'r') as file:
    text = file.readlines()
    for line in range(len(text)):
        if line % 2 == 0:
            new_line = text[line][:-1]
            new_text = [''.join([el.replace(el, '@') if el in for_replace else el for el in line]) for line in new_line]
            new_text = "".join(word for word in new_text[::-1])

            print(reverse_func(new_text))
