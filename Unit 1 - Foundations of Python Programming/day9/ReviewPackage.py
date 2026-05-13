# TOPIC 1
# Q1 - The purpose of the print() function is to output values or things stored in variable
# Q2 - Displaying text and variables
x = 5
print(x)

# Q3 - Print using multiple variables and strings
x = 6
y = 9
sum = x + y

print(x, "+", y, "is equal to", sum)

# Q4 - Formatted Output
a = 5
b = 10
product = a * b

print(f"{a} multiplied by {b} is equal to {product}\n\n")

# TOPIC 2
# Q1 - Variables are used to store data in short form, such that you don't need to rewrite long lines of codes multiple times
# Q2 - The different data types are boolean, ints, floats, and strings. 
# Ints and floats store numbers, floats having decimals, 
# booleans storing true or false, 
# and strings storing characters and text.
# Q3 - Declaring variables
variable = "value" # Write variable name (variable), then add assignment operator (=) and then assign your value (data type)

# Q4 - Type casting is used when you want to convert a data type into another. For example
num = 5
stringNum = (str)(num)

print(num + num)
print(stringNum + stringNum + "\n\n") 
# Notice how the first adds them together, whereas this prints the string twice. 
# This is because it is now a string, not and int.

# Q5 - Different data types
x = 5 # You first assign a name, followed by the assignment operator, and then the value (data types)
y = 5.6 # Floats have decimal places
hi = "hello" # Assign string values using quotes
true = True # Assign booleans using True or False
false = False

# Q6 - If you don't pick a clear variable name (ex: picking x for storing a name), your code might be unclear and you might get confused

# TOPIC 3
# Q1 - f strings allow for easier formatting in python, and allow you to easily convert data types into strings
# Q2 - Creating f strings
print(f"") # f before quotes

# Q3 - Embedding variables
number = 5
number2 = 9

print(f"{number} + {number2} is equal to", number + number2)

num1 = 12.12345678
# print(f"num is {num1:>12.2f}")
round_num = round(num1, 2)
print(round_num)

num = int("42")
print(num)