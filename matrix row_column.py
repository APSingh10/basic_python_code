a=0
b=0
matrix=[]
col=[]
while 0<1:
    try:
        for i in range(a,3):
            
            for j in range(b,4):
                b=j
                a=i
                col.append((int(input("enter the row " +str(i)+ " And column " +str(j)+ "  :")) ))
                
            b=0
            matrix.append(col)
            col=[]
        
        for x in matrix:
            print(x)
        break
    except:
        print("invalid")
