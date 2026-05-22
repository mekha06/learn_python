
print("Hello, world!")
#print() displays output on the screen.

name = "Alice"
age = 25
height = 5.6
#No need to declare types
#Python figures it out automatically

x = 10          # int
y = 3.14        # float
name = "John"   # string
is_student = True  # boolean

#Basic Operators
a = 10
b = 3

print(a + b)  # addition
print(a - b)  # subtraction
print(a * b)  # multiplication
print(a / b)  # division
print(a % b)  # remainder
print(a ** b) # exponentiation

#Conditional Statements
age = 18
if age >= 18:
    print("Adult")
else:
    print("Minor")

#Loops
for i in range(5):
    print(i)

count = 0
while count < 5:
    print(count)
    count += 1

#Lists
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Accessing elements  
fruits.append("orange")  # Adding an element
print(fruits)

#Functions
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Calling the function               

#user input
name = input("Enter your name: ")
print(f"Hello, {name}!")        

---------------------------------------------------------------------------------

#Dictionaries
#Dictionaries store key-value pairs. They are unordered, mutable, and indexed by keys.

person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}           
print(person["name"])  # Accessing values
person["age"] = 26  # Modifying values  
print(person.get("age"))  # 26
print(person)
person.pop("grade")   # removes "grade" 
for key, value in person.items(): # looping through dictionary items
    print(key, value)

--------------------------------------------------------------------------------------
#Sets
#Sets are unordered collections of unique elements. They are mutable and do not allow duplicate values.
numbers = {1, 2, 3, 3, 4}
print(numbers)  # {1, 2, 3, 4}
numbers.add(5)  # Adding an element
print(numbers)  # {1, 2, 3, 4, 5}
numbers.remove(2)  # Removing an element
print(numbers)  # {1, 3, 4, 5}
numbers.remove(2)   # error if not found
numbers.discard(10) # no error if not found
# Looping through set
for n in numbers:
    print(n)
# Set operations
A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)  # union → {1,2,3,4,5}
print(A & B)  # intersection → {3}
print(A - B)  # difference → {1,2}
print(B - A)  # difference → {4,5}

#| Feature    | Dictionary            | Set           |
#| ---------- | --------------------- | ------------- |
#| Structure  | key → value           | just values   |
#| Duplicates | keys unique           | no duplicates |
#| Order      | ordered (Python 3.7+) | unordered     |
#| Example    | {"a": 1}              | {1, 2, 3}     |

#Use dictionary when:
#You need to store related data
#👉 e.g., student info, user profiles
#Use set when:
#You need unique values only
#Fast membership checking
#👉 e.g., removing duplicates
-----------------------------------------------------------------------
#tuples
#Tuples are ordered, immutable collections of elements. They can contain duplicate values and are indexed by position.
numbers = (1, 2, 3)
names = ("Alice", "Bob", "Charlie")
print(numbers[0])   # 1
print(numbers[-1])  # 3
numbers = (1, 2, 3)
numbers[0] = 10   # ❌ Error!
#👉 You cannot modify a tuple after creation.
#📌 Single-element tuple (common mistake)
single = (5)    # This is just an integer, not a tuple
print(type(single))  # <class 'int'>
single_tuple = (5,)  # This is a single-element tuple
print(type(single_tuple))  # <class 'tuple'>

#🔁 Looping through tuple
for num in numbers:
    print(num)

#🔄 Tuple unpacking (very useful)
person = ("Alice", 25)

name, age = person

print(name)  # Alice
print(age)   # 25

#Common tuple methods
t = (1, 2, 3, 2)

print(len(t))      # 4
print(t.count(2))  # 2
print(t.index(3))  # 2

# Nested tuples
data = ((1, 2), (3, 4))

print(data[0])      # (1, 2)
print(data[0][1])   # 2
#| Feature    | Tuple       | List            |
#| ---------- | ----------- | --------------- |
#| Mutability | ❌ Immutable | ✅ Mutable    |
#| Speed      | Faster      | Slightly slower |
#| Syntax     | ( )         | [ ]             |

#Use tuples when:
#You want an ordered collection of items
#The data should not change (immutability)  
#👉 e.g., coordinates, RGB value
# Use lists when:
#You need a mutable collection of items
#👉 e.g., to-do list, shopping car
def reverse(string):
