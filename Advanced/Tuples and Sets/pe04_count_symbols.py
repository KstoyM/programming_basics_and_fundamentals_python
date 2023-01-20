symbols_dict = {}

for el in input():
    if el not in symbols_dict:
        symbols_dict[el] = 0
    symbols_dict[el] += 1

for k, v in sorted(symbols_dict.items()):
    print(f"{k}: {v} time/s")
