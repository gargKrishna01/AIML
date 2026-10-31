num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
while True:
    print("Enter 1 to perform Addition")
    print("Enter 2 to perform Subtraction")
    print("Enter 3 to perform Multiplication")
    print("Enter 4 to perform Division")
    ch=int(input("Enter your choice: 3"))
    if ch==1:
        print(num1+num2)
    elif ch==2:
        print(num1-num2)
    elif ch==3:
        print(num1*num2)
    elif ch==4:
        print(num1/num2)
    else:
        print("Invalid input")
    break
