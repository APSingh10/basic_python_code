def function_abc(a,b):
    if(a==0):
        print(b)
    else:
        b*=a
        a-=1
        function_abc(a,b)#0,15
    


x=int(input("enter the 1st number:"))
#y=int(input("enter the 2nd number:"))
function_abc(x,1)

