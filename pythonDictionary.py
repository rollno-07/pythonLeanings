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
