import re

iterations = int(input())
pattern = r'(@)#+[A-Z][A-Za-z0-9]{4,}[A-Z]\1#+'
for _ in range(iterations):
    barcode = input()
    match = re.match(pattern, barcode)
    if match:
        product_group = re.findall('\d+', match.group())
        if len(product_group) == 0:
            print("Product group: 00")
        else:
            print(f"Product group: {''.join(product_group)}")
    else:
        print("Invalid barcode")