from string import punctuation

with open("text.txt", 'r') as file:
    text = file.readlines()

output_file = open('output.txt', 'w')

for i in range(len(text)):
    row = text[i]

    letters = 0
    marks = 0

    for sym in row:
        if sym.isalpha():
            letters += 1
        elif sym in punctuation:
            marks += 1

    output_file.write(f"Line: {i + 1}: {''.join(row[:-1])} ({letters})({marks})\n")

output_file.close()
