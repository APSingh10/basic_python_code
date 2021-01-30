while True:

    
    num=int(input("enter the number:"))
    a=num//2
    for i in range(2,a+1):
        if(num%i==0):
            print("not a prime number")
            break
        else:
            if(i==a):
                print("is a prime number")        
