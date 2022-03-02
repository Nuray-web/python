import json

f3 = open('import_file_3.txt', 'r')
periodic_table = json.load(open('periodic_table.json', encoding='utf-8'))

import re
#re.findall('|'.join(map(re.escape, periodic_table.keys())), f3.readline())
all = re.findall('[A-Z][a-z]*\\d*|\\([^)]+\\)\\d*', f3.readline())

all = filter(lambda x: x != "", all)

res = []
for i in all:
    s = periodic_table[i]
    res.append(s)

''.join(res)
