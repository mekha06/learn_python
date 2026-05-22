# Reverse a string
#  Input: "hello"
# Output: "olleh"
string=input("enter the string value:")
l=len(string)-1
rev=[]
for i in range(l,-1,-1):
    rev.append(string[i])
print("".join(rev))

"""
---------------output------------------------------------
enter the string value:hello
['o', 'l', 'l', 'e', 'h']
enter the string value:hello
olleh
"""

string = input("enter the string value:")
print(string[::-1])
"""
------------------output using slicing technique-------------------------------
enter the string value:hello
olleh
"""

