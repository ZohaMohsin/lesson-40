#sum of whole numbers
n=int(input("enter no"))
sum1=0
for i in range(n):
    sum1=sum1+i
print(sum1)
total_sum=sum(range(n))
print(" total sum is ",total_sum)