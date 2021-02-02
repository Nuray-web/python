#854
tr, tc = map(int, input("Please, enter your values: ").split())
n = str(input("Please, enter cond status: "))
if n == 'freeze':
  print(min(tr, tc))
elif n == 'heat':
  print(max(tr, tc))
elif n == 'auto':
  print(tc)
elif n == 'fan':
  print(tr)
else:
  print("ERROR")
