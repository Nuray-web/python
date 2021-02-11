#08
a = list(map(int, input("Please enter some integers: ").split()))  
n = int(input("Please enter the position: ")) #position index
i = 0
pos = a[i] #just index to identify
ind = i
shift = (ind - n) % len(a)
while shift != i:
   a[ind] = a[shift]
   ind = shift
   shift = (ind - n) % len(a)
a[ind] = pos
print(*a)
