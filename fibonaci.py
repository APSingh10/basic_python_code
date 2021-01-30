f1=0
f2=0
fibo=0
num=int(input("enter the numer of fibonaci series:"))
for i in range(0,num+1):
    f2=f1+i
    #print(f2,end="")
    f1=f2
    f2=i
    f2=f1+f2
    #f2=i
    #f2=f1+f2
    print(f2)
