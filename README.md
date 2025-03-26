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