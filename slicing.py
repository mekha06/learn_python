"""
You can return a range of characters by using the slice syntax.
Specify the start index and the end index, separated by a colon,
 to return a part of the string.
"""
s=input("enter the string value:")
print(s)
print(s[2:7])# slicing from 2nd position to 7th pos (7th pos not included) 
print(s[:7])# slicing from start position to 7th pos (7th pos not included)  
print(s[2:])# slicing from 2nd position to end pos ( 2nd pos inclusive)
print(s[-7:-2]) #negative slicing starts from the end of string,i.e d=0,l=-1,r=-2,o=-3,w=-4,""=-5,o=-6,l=-7,l=-8,e=-9,h=-10 in hello world
print(s[:9:2])# from start to till 9th pos but skipping a character between
print(s[2: :2])#from 2nd pos to end and skipping a character