#685
a1, a2, a3, b1, b2, b3 = map(int, input("Please enter your values: ").split())
if a1 < a2:
  c = a1
  a1 = a2
  a2 = c
if a2 < a3:
  c = a2
  a2 = a3
  a3 = c
if a1 < a2:
  c = a1
  a1 = a2
  a2 = c
if b1 < b2:
  c = b1
  b1 = b2
  b2 = c
if b2 < b3:
  c = b2
  b2 = b3
  b3 = c
if b1 < b2:
  c = b1
  b1 = b2
  b2 = c
print(a1 * b1 + a2 * b2 + a3 * b3)
