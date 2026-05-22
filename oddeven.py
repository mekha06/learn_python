# Take a number and print whether it is even or odd.
def oddeven():
    n=int(input("Enter the number:"))
    if(n%2==0):
        print(f"{n} is even")
    else:
        print(f"{n} is odd")
oddeven()
"""
-----output-----
Enter the number:4
4 is even
PS C:\python basics> python oddeven.py
Enter the number:5
5 is odd
PS C:\python basics> python oddeven.py
Enter the number:21
21 is odd
PS C:\python basics> python oddeven.py
Enter the number:36
36 is even
"""