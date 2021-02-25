#294
k1, l1, m1 = map(int, input("Please, enter your values: ").split()) #болты
k2, l2, m2 = map(int, input("Please, enter your values: "). split()) #гайки
k11 = int(k1 - (k1*(l1/100)))
k22 = int(k2 - (k2*(l2/100)))
k = 0  
if k11>k22:
  k = (k11-k22)*m1
  k11 = k1*(l1/100)*m1
  k22 = k2*(l2/100)*m2
  print(int(k11+k22+k))
elif k11<k22:
  k = (k22-k11)*m2
  k11 = k1*(l1/100)*m1
  k22 = k2*(l2/100)*m2
  print(int(k11+k22+k))
else:
  k = 0
  k11 = k1*(l1/100)*m1
  k22 = k2*(l2/100)*m2
  print(int(k11+k22))
