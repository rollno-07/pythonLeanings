# 1. Printing Output Use the print() function to display output
# The print() function is used to display text or other data on the screen. It is one of the most common and essential functions in Python.

print("Hello, World!")


# rinting Multiple Values
name="Alice"
age=25
print("Name:",name,"Age:",age)

# Using f-strings for Formatting
print(f"Name: {name}, Age: {age}")

# Adding Newlines and Special Characters
print("Line 1\nLine 2\nLine 3")
print("Hello\tWorld") # Tab space


# Controlling End Parameter
print("Hello", end=" ")
print("World!")

# Customizing Separators
print("Python", "is", "awesome", sep=" - ")


##### Python input() Function – User Input in Python
name = input("Enter your name: ")
print("Hello,", name)

# Converting Input Data Type:
age = int(input("Enter your age: "))
print(f"You are {age} years old.")

# Prompt Message:
language = input("What is your favorite programming language? ")
print(f"Nice choice! {language} is awesome.")

# What are Variables in Python?

# In Python, a variable is used to store data. It acts as a container that holds information which can be used later.

name = "Alice"
age = 30
print(name, age)

# Python Data Types with Examples

# Python supports multiple data types for handling various forms of data:

# int: Integer values for whole numbers.

x = 5
y = -10
print(x, y)

# float: Decimal values for precise calculations.

pi = 3.14
temp = -2.5
print(pi, temp)

# str: Strings for text data.

greeting = "Hello"
name = 'Python'
print(greeting, name)

# bool: Boolean values for true/false logic.

is_active = True
is_admin = False
print(is_active, is_admin)

# list: Ordered, mutable collections.

fruits = ["apple", "banana", "cherry"]
print(fruits)

# tuple: Ordered, immutable collections.

colors = ("red", "green", "blue")
print(colors)

# dict: Key-value pairs for structured data.

person = {"name": "Alice", "age": 30}
print(person["name"], person["age"])

# set: Unordered collections of unique values.

unique_numbers = {1, 2, 3, 3, 4}
print(unique_numbers)  # Output: {1, 2, 3, 4}

Dynamic Typing & Type Conversion

# Python uses dynamic typing, allowing variables to change types at runtime.

x = 10      # x is an int
x = "Python"  # x is now a string

# To convert data types, use functions like int(), float(), or str():

num = "25"
num = int(num)  # Now 'num' is an integer

# Python Lists – The Power of Ordered Collections

# What are Lists in Python?

# Lists are ordered, mutable collections that can hold multiple items in a single variable.

# Creating, Accessing, and Modifying Lists

my_list = [1, 2, 3, 4, 5]
print(my_list[0])  # Accessing first element
my_list[2] = 99    # Modifying an element
print(my_list)

# List Methods

# append(): Adds an item to the end of the list
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)

# extend(): Adds multiple items to the end of the list

fruits.extend(["orange", "grape"])
print(fruits)

# pop(): Removes and returns the last element (or specified index)

fruits.pop()  # Removes 'grape'
print(fruits)

# remove(): Removes the first matching element

fruits.remove("banana")
print(fruits)

# List Comprehensions for Efficient Coding

squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]

# Sorting, Reversing, and Slicing Lists

# sort(): Sorts the list in place

numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)

# reverse(): Reverses the order of the list

numbers.reverse()
print(numbers)

# Slicing: Extracts a subset of the list

print(numbers[1:3])  # Output: [2, 3]

# Python Dictionaries – Key-Value Pair Collections

# What are Dictionaries in Python?

# Dictionaries are unordered, mutable collections that store data in key-value pairs.

# Creating and Accessing Dictionaries

person = {"name": "Alice", "age": 30, "city": "New York"}
print(person["name"])  # Accessing a value

# Dictionary Methods

# get(): Safely retrieves a value for a key

print(person.get("age"))  # Output: 30
print(person.get("gender", "Not specified"))  # Default value if key not found

# update(): Updates the dictionary with new key-value pairs

person.update({"age": 31, "job": "Engineer"})
print(person)

# pop(): Removes and returns a key's value

person.pop("city")
print(person)

# keys() and values(): Return keys and values separately

print(person.keys())    # Output: dict_keys(['name', 'age', 'job'])
print(person.values())  # Output: dict_values(['Alice', 31, 'Engineer'])

# items(): Returns key-value pairs as tuples

print(list(person.items()))

# Python Casting (Type Conversion)
Python casting refers to converting one data type into another. Python provides several built-in functions for explicit type conversion:

int() — Converts to an integer

float() — Converts to a floating-point number

str() — Converts to a string

list() — Converts to a list

tuple() — Converts to a tuple

set() — Converts to a set

dict() — Converts to a dictionary

# Examples of Python Casting
Integer Conversion (int())
# Converting string to integer
x = int("10")    
print(x, type(x))  # Output: 10 <class 'int'>

# Converting float to integer (truncates decimals)
y = int(5.9)      
print(y)  # Output: 5

# Float Conversion (float())
# String to float
x = float("3.14")
print(x, type(x))  # Output: 3.14 <class 'float'>

# Integer to float
y = float(10)
print(y)  # Output: 10.0

# String Conversion (str())
# Integer to string
x = str(100)
print(x, type(x))  # Output: "100" <class 'str'>

# Float to string
y = str(3.14)
print(y)  # Output: "3.14"

# List Conversion (list())

# Tuple to list
x = list((1, 2, 3))
print(x, type(x))  # Output: [1, 2, 3] <class 'list'>

# String to list
y = list("Python")
print(y)  # Output: ['P', 'y', 't', 'h', 'o', 'n']

# Tuple Conversion (tuple())

# List to tuple
x = tuple([1, 2, 3])
print(x, type(x))  # Output: (1, 2, 3) <class 'tuple'>

# Set Conversion (set())
x = set([1, 2, 3, 3])
print(x)  # Output: {1, 2, 3} (removes duplicates)

# Dictionary Conversion (dict())
# List of tuples to dictionary
x = dict([("name", "Alice"), ("age", 30)])
print(x)  # Output: {'name': 'Alice', 'age': 30}

# Important Notes:
Casting must be valid. For instance, int("3.14") will raise an error since "3.14" is not a valid integer.

When converting from float to int, Python truncates the decimal part (it does not round).


# Python Functions
Functions in Python are blocks of reusable code that perform a specific task. They help in organizing code, making it more readable, and avoiding repetition.

# Types of Functions in Python
Built-in Functions – Predefined functions in Python like print(), len(), sum(), etc.

User-defined Functions – Functions created by the user.

Lambda Functions – Anonymous functions using the lambda keyword.

Recursive Functions – Functions that call themselves.

# 1. Creating a User-Defined Function
A function is defined using the def keyword.

 Example: Simple Function
 def greet():
    print("Hello, welcome to Python!")

greet()  # Output: Hello, welcome to Python!


# 2. Function with Parameters
Parameters allow functions to accept input values.

Example: Function with Parameters

def add(a, b):
    return a + b

result = add(5, 3)
print("Sum:", result)  # Output: Sum: 8

# 3. Function with Default Parameters
If no value is passed, the default value is used.

 Example: Function with Default Parameter

 def greet(name="Guest"):
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!
greet()         # Output: Hello, Guest!


# 4. Function with Return Value
A function can return a value using the return statement.

Example: Function Returning a Value
def multiply(x, y):
    return x * y

result = multiply(4, 5)
print("Multiplication:", result)  # Output: Multiplication: 20

# 5. Function with Variable-Length Arguments (*args and **kwargs)
*args – Allows passing multiple positional arguments as a tuple.

**kwargs – Allows passing multiple keyword arguments as a dictionary.

Example: Using *args

def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1, 2, 3, 4))  # Output: 10

Example: Using **kwargs

def user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

user_info(name="Alice", age=25, city="New York")
# Output:
# name: Alice
# age: 25
# city: New York

# 6. Lambda Function (Anonymous Function)
A lambda function is a small, one-line function without a name.

Example: Lambda Function
square = lambda x: x * x
print(square(5))  # Output: 25

Example: Lambda with Multiple Arguments
add = lambda a, b: a + b
print(add(3, 7))  # Output: 10

# 7. Recursive Function
A recursive function calls itself until a condition is met.

Example: Factorial using Recursion

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120

# Key Takeaways
Functions make code reusable and organized.

Use return to get output from a function.

*args handles multiple positional arguments, while **kwargs handles multiple keyword arguments.

Lambda functions are useful for short, one-line functions.

Recursive functions call themselves for solving problems like factorial or Fibonacci series.

# What is Scope in Python?
Scope refers to the region where a variable can be accessed. Python has different scopes for variables to determine their visibility.

Types of Variable Scope in Python
Local Scope – Variables declared inside a function.

Global Scope – Variables declared outside a function.

Enclosing (Nonlocal) Scope – Variables in nested functions.

Built-in Scope – Predefined Python functions and keywords.

1. Local Scope
A variable inside a function is local to that function and cannot be accessed outside.

Example: Local Variable

def my_function():
    x = 10  # Local variable
    print("Inside function:", x)

my_function()
# print(x)  # This will cause an error because x is not defined outside the function.
2. Global Scope
A variable declared outside any function is a global variable and can be accessed anywhere in the code.

Example: Global Variable

x = 20  # Global variable

def my_function():
    print("Inside function:", x)

my_function()
print("Outside function:", x)  # Global variable accessible outside
3. Modifying Global Variables Inside a Function
To modify a global variable inside a function, use the global keyword.

Example: Using global Keyword

x = 5  # Global variable

def modify_global():
    global x
    x = 10  # Modifying global variable
    print("Inside function:", x)

modify_global()
print("Outside function:", x)  # Output: 10
4. Enclosing Scope (nonlocal Keyword)
Enclosing (or nonlocal) scope applies to variables in a nested function (a function inside another function). Use nonlocal to modify them.

Example: Using nonlocal Keyword

def outer():
    x = 5  # Enclosing variable

    def inner():
        nonlocal x
        x = 10  # Modifying enclosing variable
        print("Inside inner function:", x)

    inner()
    print("Inside outer function:", x)

outer()
5. Built-in Scope
Python has built-in functions and keywords that are available everywhere.

Example: Built-in Scope

print(len("Python"))  # `len` is a built-in function
Summary
Local Scope: Variables inside a function, accessible only there.

Global Scope: Variables outside functions, accessible anywhere.

Enclosing Scope: Variables in outer functions, modified using nonlocal.

Built-in Scope: Predefined Python functions and keywords.

