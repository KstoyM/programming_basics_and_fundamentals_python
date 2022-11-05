synonyms = {}
iterations = int(input())

for _ in range(iterations):
    key = input()
    synonym = input()
    if key not in synonyms:
        synonyms[key] = []
    synonyms[key].append(synonym)

for key, value in synonyms.items():
    print(f"{key} - {', '.join(value)}")