dec=int(input("Enter the number: "))
binary=""
while(dec>0):
    rem=dec%2
    dec=dec//2
    #print(rem)
    binary=str(rem)+binary

print(binary)
