
# Check palindrome
w=input("enter the string:")
n=len(w)
i=n//2-1
j=n//2+1
is_palindrome=True
while i>=0 and j<=n-1:
    if w[i]!=w[j]:
        is_palindrome=False
        break
    else:
        i-=1
        j+=1
if is_palindrome:
    print(f"{w} is a palindrome")
else:
    print(f"{w} is not a palindrome")

"""
----------------------------OUTPUT--------------------------------------------
PS C:\python basics> & C:/Python314/python.exe "c:/python basics/palindrome.py"
enter the string:hello
hello is not a palindrome
PS C:\python basics> & C:/Python314/python.exe "c:/python basics/palindrome.py"
enter the string:malayalam
malayalam is a palindrome
PS C:\python basics> & C:/Python314/python.exe "c:/python basics/palindrome.py"
enter the string:python
python is not a palindrome

"""
"""
---------------------------------- Shorter version---------------------------------------

w = input("enter the string: ")

i = 0
j = len(w) - 1

is_palindrome = True

while i < j:
    if w[i] != w[j]:
        is_palindrome = False
        break
    i += 1
    j -= 1

if is_palindrome:
    print("Palindrome")
else:
    print("Not Palindrome")

"""