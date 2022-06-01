#697
#l - длина
#w - ширина
#h - высота
l, w, h = map(int, input("Please, enter your values: ").split())
s = 2*l*h + 2*w*h
if s%16 == 0:
  print(s//16)
else:
  print(s//16 + 1) 
