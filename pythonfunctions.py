# Python Functions
# Functions in Python are blocks of reusable code that perform a specific task. They help in organizing code, making it more readable, and avoiding repetition.

# Types of Functions in Python
# Built-in Functions – Predefined functions in Python like print(), len(), sum(), etc.

# User-defined Functions – Functions created by the user.

# Lambda Functions – Anonymous functions using the lambda keyword.

# Recursive Functions – Functions that call themselves.

# 1. Creating a User-Defined Function

def greet():
    print("Hello, welcome to Python!")

greet()  # Output: Hello, welcome to Python!


# 2. Function with Parameters


def add(a, b):
    return a + b

result = add(5, 3)
print("Sum:", result)  # Output: Sum: 8

# 3. Function with Default Parameters

def greet(name="Guest"):
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!
greet()         # Output: Hello, Guest!


# 4. Function with Return Value

def multiply(x, y):
    return x * y

result = multiply(4, 5)
print("Multiplication:", result)  # Output: Multiplication: 20

# 5. Function with Variable-Length Arguments (*args and **kwargs)

#Example: Using *args

def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1, 2, 3, 4))  # Output: 10

#Example: Using **kwargs

def user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

user_info(name="Alice", age=25, city="New York")
# Output:
# name: Alice
# age: 25
# city: New York

# 6. Lambda Function (Anonymous Function)


#Example: Lambda Function
square = lambda x: x * x
print(square(5))  # Output: 25

#Example: Lambda with Multiple Arguments
add = lambda a, b: a + b
print(add(3, 7))  # Output: 10

# 7. Recursive Function

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120

