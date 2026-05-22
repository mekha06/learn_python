#Print numbers from 1 to 10 using a loop.
def numbers():
  for i in range(1,11):
    print(i)
numbers()

""" ouput-correct
1
2
3
4
5
6
7
8
9
10
"""

def numbers():
  n=10
  for i in range(n):
     print(i)
numbers()
""" output-wrong
0
1
2
3
4
5
6
7
8
9
"""