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

