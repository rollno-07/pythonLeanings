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