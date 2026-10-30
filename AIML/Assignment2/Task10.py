# check no. is prime
n=int(input("Enter a number: "))
c=0
for i in range(2,n//2):
    if n%i==0:
        c+=1
if c==0:
    print(n," is a Prime number")
else:
    print(n," is not a Prime number")