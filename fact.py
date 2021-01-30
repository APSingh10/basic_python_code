while 1>0:
    try:
        num=int(input("enter the number:"))
        fact=1
        for n in range(1,num+1):
            fact*=n
        print(fact)
            
    except:
        print("invalid")

    x=int(input("press 2 for next factorial:"))
    if x==2:
        print("")
    else:
        print("Exit")
        break
