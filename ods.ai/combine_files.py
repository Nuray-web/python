f1 = open('import_file_2_1.txt', 'r')
f2 = open('import_file_2_2.txt', 'r')

a = []
b = []
for line in f1.readlines():
    line = line.replace('\n','')
    a.append(line)
    
for line in f2.readlines():    
    line = line.replace('\n','')
    b.append(line)
    
all = dict(zip(a, b))

res = []
for key in all:
    n = all[key].split(' ')
    result = key[int(n[0]):int(n[1])]
    res.append(result)

print(' '.join([str(x) for x in res]))
