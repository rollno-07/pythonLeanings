# What is Scope in Python?
# Scope refers to the region where a variable can be accessed. Python has different scopes for variables to determine their visibility.

# Types of Variable Scope in Python
# Local Scope – Variables declared inside a function.

# Global Scope – Variables declared outside a function.

# Enclosing (Nonlocal) Scope – Variables in nested functions.

# Built-in Scope – Predefined Python functions and keywords.

# 1. Local Scope

def my_function():
    x = 10  # Local variable
    print("Inside function:", x)

my_function()
# print(x)  # This will cause an error because x is not defined outside the function.
# 2. Global Scope

x = 20  # Global variable

def my_function():
    print("Inside function:", x)

my_function()
print("Outside function:", x)  # Global variable accessible outside
# 3. Modifying Global Variables Inside a Function

x = 5  # Global variable

def modify_global():
    global x
    x = 10  # Modifying global variable
    print("Inside function:", x)

modify_global()
print("Outside function:", x)  # Output: 10
# 4. Enclosing Scope (nonlocal Keyword)


def outer():
    x = 5  # Enclosing variable

    def inner():
        nonlocal x
        x = 10  # Modifying enclosing variable
        print("Inside inner function:", x)

    inner()
    print("Inside outer function:", x)

outer()
# 5. Built-in Scope


# Example: Built-in Scope

print(len("Python"))  # `len` is a built-in function

