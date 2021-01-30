#program for the greatest  number
while True:
    try:
   
        num1=int(input("enter the number:"))
        num2=int(input("enter the number:"))
        num3=int(input("enter the number:"))
        num4=int(input("enter the number:"))
        Sum=num1+num2+num3+num4
        print("the Sum of the numbers is:",Sum)

        for i in range(Sum):
            if(num1==i or num2==i or num3==i or num4==i):
                largest=i
        print("the largest number is:",largest)

    except:
        print("invalid,not an integer value")
