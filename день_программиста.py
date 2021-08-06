#550
n = int(input())
if n%400 == 0 or (n%100!=0 and n%4==0): 
    if n < 10:
            print("12/09/000")
    else:
        if n<100:
            print("12/09/00" + str(n))
        else:
            if n<1000:
                print("12/09/0"+ str(n))
            else:
                print("12/09/"+ str(n))
else:
    if n < 10:
            print("13/09/000"+ str(n))
    else:
        if n<100:
            print("13/09/00"+ str(n))
        else:
            if n<1000:
                print("13/09/0"+ str(n))
            else:
                print("13/09/"+ str(n))
