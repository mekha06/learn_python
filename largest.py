#  Find largest number in a list
num=list(map(int,input("enter the numbers:").split()))
print(num)
n=len(num)
a=list(num)
for i in range(n):
    for j in range(i+1,n):
        if a[i]>a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print("the largest number is:",a[n-1])


    