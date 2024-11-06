#prime numbers
n=int(input("enter no "))
flag=False
for i in range(2,n):
    if n%i==0:
     flag=True
     break
if flag:
    print(n," is not prime ")
else:
   print(n," is prime ")
