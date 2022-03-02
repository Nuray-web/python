f = open('input_file.txt', 'r')
res = []
for line in f.readlines():
  a = line.replace('\n','').split('    ')
  s = str(a[1] + a[0] + a[2])
  result = eval(s)
  res.append(result)

print(','.join([str(x) for x in res]))
