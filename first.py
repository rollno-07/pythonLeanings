#1. Printing Output Use the print() function to display output
#The print() function is used to display text or other data on the screen. It is one of the most common and essential functions in Python.

print("Hello, World!")


#rinting Multiple Values
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


#####Python input() Function – User Input in Python
name = input("Enter your name: ")
print("Hello,", name)

#Converting Input Data Type:
age = int(input("Enter your age: "))
print(f"You are {age} years old.")

# Prompt Message:
language = input("What is your favorite programming language? ")
print(f"Nice choice! {language} is awesome.")


