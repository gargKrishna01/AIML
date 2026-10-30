# count no. of digits
n=int(input("Enter a number: "))
a=n
c=0
while n>0:
    n//=10
    c+=1
print("Number of digits in",a,"is :",c)