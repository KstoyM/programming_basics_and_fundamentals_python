tail = input()
body = input()
head = input()

meerkat_body = [tail, body, head]

meerkat_body[0], meerkat_body[2] = meerkat_body[2], meerkat_body[0]

print(meerkat_body)