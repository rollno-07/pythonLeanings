# Python Casting (Type Conversion)
# Python casting refers to converting one data type into another. Python provides several built-in functions for explicit type conversion:

# int() — Converts to an integer

# float() — Converts to a floating-point number

# str() — Converts to a string

# list() — Converts to a list

# tuple() — Converts to a tuple

# set() — Converts to a set

# dict() — Converts to a dictionary

# Examples of Python Casting
# Integer Conversion (int())
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
# Casting must be valid. For instance, int("3.14") will raise an error since "3.14" is not a valid integer.

# When converting from float to int, Python truncates the decimal part (it does not round).
