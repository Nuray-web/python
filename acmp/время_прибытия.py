#331
hh, mm = map(int, input("Пожалуйста, введите время прибытия: ").split(':'))
h, m = map(int, input("Пожалуйста, введите нужное количество времени: ").split())
hh += h
mm += m
hh += mm//60
mm %= 60
hh %= 24
if hh<10 and mm<10:
  print('0' + str(hh)+ ":" + '0'+str(mm))
elif hh>10 and mm<10:
  print(str(hh)+ ":" + '0'+str(mm))
elif hh<10 and mm>10:
  print('0' + str(hh)+ ":" + str(mm))
else:
  print(str(hh) + ":" + str(mm))
