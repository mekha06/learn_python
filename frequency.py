# Word frequency (dictionary)
n=int(input("enter the number of words:"))
w={}
for i in range(n):
    words=input("enter the words:")
    if words in w:
        w[words]+=1
    else:
        w[words]=1
for key,value in w.items():
    print(f"{key}:{value}")

"""
---------------------OUTPUT--------------------------------------
enter the number of words:6
enter the words:me
enter the words:he
enter the words:me
enter the words:she
enter the words:she
enter the words:me
me:3
he:1
she:2
"""