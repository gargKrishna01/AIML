# reverse a number
n=int(input("Enter a number: "))
a=n
r=0
while n>0:
    r=r*10+n%10
    n//=10
print("Reverse of",a,"is:",r)