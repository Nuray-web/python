#933
a, b, c, t = map(int, input("Please enter your values: ").split())
if a>t or a == t:
  print(a*b)
elif a<t:
  n = (t-a)*c
  print((a*b)+n)
