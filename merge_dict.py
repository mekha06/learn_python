# Merge two dictionaries
d1={}
n=int(input("enter the no of pairs:"))
for i in range(n):
    key,value=input("enter key and its value:").split()
    d1[key]=value
print(d1)

d2={}
n=int(input("enter the no of pairs:"))
for i in range(n):
    key,value=input("enter key and its value:").split()
    d2[key]=value
print(d2)
print("the merged dictionary is:")
d3=d1 | d2
print(d3)

"""
--------------------------------Output------------------------------------------------------
enter the no of pairs:2
enter key and its value:a 1
enter key and its value:b 3
{'a': '1', 'b': '3'}
enter the no of pairs:2 
enter key and its value:c 4
enter key and its value:d 3
{'c': '4', 'd': '3'}
the merged dictionary is 
{'a': '1', 'b': '3', 'c': '4', 'd': '3'}

"""

def input_dict():
    d={}
    n=int(input("enter the no of pairs:"))
    for i in range(n):
        key,value=input("enter the key and value:").split()
        d[key]=int(value)
    return d
d1=input_dict()
d2=input_dict()

d3=d1.copy() #creates a copy of dictionary d1 without altering d1
for key, value in d2.items(): #iterating through d2 dictionary using d2.items() function 
    d3[key]=d3.get(key,0) + value # d3 already contains d1 now it adds d2 items too by checking if same key exists and adds them or else just the value + 0  
print("The merged dictionary is:", d3)

"""
---------------------------Output-----------------------------------------------------
enter the no of pairs:2
enter the key and value:a 1
enter the key and value:b 2
enter the no of pairs:2
enter the key and value:a 3
enter the key and value:c 4
The merged dictionary is: {'a': 4, 'b': 2, 'c': 4}
"""
