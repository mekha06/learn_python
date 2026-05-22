# Recursive factorial  
def fact(n):
    if n<=1:
        return n
    return n*fact(n-1)
n=int(input("enter the number:"))
print(fact(n))


"""
-----------------------output---------------------------------------
PS C:\python basics> & C:/Python314/python.exe "c:/python basics/factorial.py"
enter the number:7
5040
PS C:\python basics> & C:/Python314/python.exe "c:/python basics/factorial.py"
enter the number:5
120
"""

# non recursive version using loop
n=int(input("enter the number:"))
fact=1
for i in range(1,n+1):
    fact=i*fact
print(fact)

"""
--------------------------------output of non recursive code------------------------------
PS C:\python basics> python factorial.py                                      
enter the number:4
24
PS C:\python basics> python factorial.py                                      
enter the number:7
5040
"""

