import pyttsx3
import datetime
engine=pyttsx3.init()

engine.say('''Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the trav'ller in the dark,
Thanks you for your tiny spark,
He could not see which way to go,
If you did not twinkle so.

In the dark blue sky you keep,
And often thro' my curtains peep,
For you never shut your eye,
Till the sun is in the sky.

'Tis your bright and tiny spark,
Lights the trav'ller in the dark:
Tho' I know not what you are,
Twinkle, twinkle, little star.''')
# engine.runAndWait()


# a=10;
# b=11
# c=int(input("enter no. c"))
# d=int(input("enter no. d"))
# print(type(a))

# #chapter2
# #1
# print(a+b)
# #2
# print(b%a)
# #3
# print(type(c))
# #4
# print(a>b)
# #5
# avg=(c+d)/2
# print(avg)
# #6
# print(a*a)

#chapter 3 1. Write a python program to display a user entered name followed by Good
# Afternoon using input () function.
# 2. Write a program to fill in a letter template given below with name and date.
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''
# 3. Write a program to detect double space in a string.
# 4. Replace the double space from problem 3 with single spaces.
# 5. Write a program to format the following letter using escape sequence
# characters.
# letter = "Dear Harry, this python course is nice. Thanks!"

#1
str=input("enter name")
print(str)

#2
letter = f'''
 Dear {str},
 You are selected!
 {datetime.datetime.now()}'''

print(letter)

#3
def detect_double_space(input_string):
    # Check if there are any double spaces in the string
    if ' ' in input_string:
        return "single space detected!"
    else:
        return "No single spaces detected."

# Example usage
input_string = input("Enter a string: ")
result = detect_double_space(input_string)
print(result)
#5
letter = "Dear Harry, this python course is nice. Thanks!"

# Using escape sequences to format the letter
formatted_letter = "Dear Harry,\n\tThis python course is nice.\n\tThanks!"

# Print the formatted letter
print(formatted_letter)