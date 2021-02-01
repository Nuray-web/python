#692
n = int(input("Введите ваше число: "))

def binary(n):
   if (n == 0):
      return False
   while (n != 1):
      if (n % 2 != 0):
         return False
      n = n // 2
   return True

if binary(n):
   print('Yes')
else:
   print('No')
