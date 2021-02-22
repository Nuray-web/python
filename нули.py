#043
#прям питоновский ответ
#print(len(max(input("Please, enter your binary code here: ").split('1'), key = len)))
s = str(input("Please, neter your binary code here: "))
a = 0
b = 0
i = 0
while len(s)>i:
  if s[i] == '0':
    a+=1
    if a>b:
      b = a
  if s[i] == '1':
      a = 0
  i+=1
print(b) 
