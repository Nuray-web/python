#504
k = int(input("Please enter the value: "))
#GCV - 1  VCG - 4  GCV - 7
#GVC - 2  CVG - 5  GVC - 8
#VGC - 3  CGV - 6  ...
f = 'GCV'
fl = list(f)
for i in range(k):
    a = fl[1]
    fl[1] = fl[2]
    fl[2] = a
    a = fl[1]
    fl[1] = fl[0]
    fl[0] = a
    i += 1
print(str(fl))
