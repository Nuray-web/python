#550
n = int(input("Please enter the value of year: "))
if n%400 == 0 or n%100!=0 and n%4==0: 
    print("12/09/"+str(n))
else:
    print("13/09/"+str(n))
