# sum of digits of a no.
n=int(input("Enter a number: "))
a=n
s=0
while n>0:
    s+=n%10
    n//=10
print("Sum of digits of",a,"is",s)