# Print first n Fibonacci numbers.
n=int(input("enter the number:"))
a,b=0,1
for i in range(n):
    print(a)
    a,b=b,a+b

"""
--------------------------OUTPUT---------------------------------------    
enter the number:7 
0
1
1
2
3
5
8

"""
"""
------------------------------------Recursion call--------------------------------------------------
def fibo(n):
    if n<=1:
        return n
    return fibo(n-1)+fibo(n-2)
    
n=int(input("enter the number:"))
for i in range(n):
    print(fibo(i), end=" ")

"""