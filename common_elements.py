#  Find common elements (set)
x=list(map(int,input("enter the elements of x:").split()))
y=list(map(int,input("enter the elements of y:").split()))

x_set=set(x)
y_set=set(y)
z=x_set & y_set
print("The common elements are:", z)

"""
-----------------------------------output------------------------------------------------------
enter the elements of x:1 2 3 4
enter the elements of y:3 4 5 6
The common elements are: {3, 4}

"""