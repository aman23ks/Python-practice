
# PRINTING A STATEMENT IN PYTHON
# print("Hello world")

# INDENTATION
# Indentation is very important in python
# if(5 > 2):
# Point 1: (number of spaces in print upto the programmer but it should be atleast one)
# print("Five is greater than two")

# if(5 > 2):
#     # Point 2 : You have to use the same number of spaces in the block of code otherwise python will give you an error.
#     print("Five is greater than 2")
#     print("Five")


# VARIABLES
# Declaring a variable
# Python has no command for declaring a variable
# x = 9
# y = "Hello world"

# COMMENTS IN PYTHON
# there are two ways comment code in python using '#' and using " '''3 colons before and after mainly used in multiline commenting''' "

# CREATING A VARIABLE
# Point 1: A variable is created the moment you assign a value to it
# x = 5
# y = "John"
# print(x)
# print(y)

# Point 2: Variables don't need to be created with a paricular type, and can even change type after they have been set
# x = 5
# x = "Sally"
# print(x)

# Point 3: String variables can be created by either single or double quotes
# x = "John"
# x = 'John'

# Point 4: Variable names
# A variable can have a short name(like x and y) or a more descriptive name(age, carname, total_volume). Rules for Python variables:
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores(A-z, 0-9, and _)
# Variable names are case-sensitive(age, Age and AGE are three different variables)
# Legal variable names:
# myvar = "John"
# my_var = "John"
# _my_var = "John"
# myVar = "John"
# MYVAR = "John"
# myvar2 = "John"

# Illegal variable names:
# 2myvar = "John"
# my-var = "John"
# my var = "John"

# Point 5: Python allows you to assign multiple values to variables in a single line.
# x, y, z = "Orange", "Banana", "Cherry"
# print(x)
# print(y)
# print(z)

# x = y = z = "Orange"
# print(x)
# print(y)
# print(z)

# OUTPUT VARIABLES
# The Python print statement is often used to output variables.To combine both text and a variable, Python uses the + character:
# x = "awesome"
# print("Python is " + x)

# You can also use the + character to add a variable to another variable
# x = "Hello "
# y = "World"
# z = x + y
# print(z)

# For number + character works as a mathematical operator
# x = 5
# y = 7
# print(x+y)

# GLOBAL VARIABLES
# Point 1: Variables that are created outside a function are known as global variables . Global variables can be used by everyone both inside and outside of functions.
# x = "awesome"


# def myfun():
#     print("python is " + x)


# myfun()

# Point 2: If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.
# x = "awesome"


# def myfunc():
#     x = "fantastic"
#     print("Python is " + x)


# myfunc()

# print("Python is " + x)

# THE GLOBAL KEYWORD
# Point 1: When you create a variable inside a function, that variable is local and can only be used inside that function.To create a global variable inside a function you can use the global keyword.


# def myfunc():
#     global x
#     x = "fantastic"


# myfunc()

# print("Python is " + x)

# Pont 2:  Also, use the global keyword if you want to change a global variable inside a function.
# x = "awesome"


# def myfunc():

#     global x
#     x = "fantastic"


# myfunc()

# print("Python is " + x)

# DATA TYPES
# In programming, data type is an important concept.

# Variables can store data of different types, and different types can do different things.

# Python has the following data types built-in by default, in these categories:

# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview

# GETTING THE DATA TYPE
# You can get the data type using the tpye()
# x = 5
# print(type(x))


# x = "Hello World"	: str
# x = 20:	int
# x = 20.5	: float
# x = 1j	: complex
# x = ["apple", "banana", "cherry"]	: list
# x = ("apple", "banana", "cherry")	: tuple
# x = range(6)	: range
# x = {"name": "John", "age": 36}	: dict
# x = {"apple", "banana", "cherry"}	: set
# x = frozenset({"apple", "banana", "cherry"})	: frozenset
# x = True	: bool
# x = b"Hello"	: bytes
# x = bytearray(5)	: bytearray
# x = memoryview(bytes(5))	: memoryview

# PYTHON NUMBERS
# There are three numeric types in Python:

# int
# float
# complex

# x = 1    # int
# y = 2.8  # float
# z = 1j   # complex

# print(type(x))
# print(type(y))
# print(type(z))

# x = 1
# y = 35656222554887711
# z = -3255522

# print(type(x))
# print(type(y))
# print(type(z))

# x = 1.10
# y = 1.0
# z = -35.59

# print(type(x))
# print(type(y))
# print(type(z))


# Floats can also be used with an 'e' to indicate the power of 10
# x = 35e3
# y = 12E4
# z = -87.7e100
# print(type(x))
# print(type(y))
# print(type(z))

# Complex numbers are written with a j as the imaginary part
# x = 3+5j
# y = 5j
# z = -5j
# print(type(x))
# print(type(y))
# print(type(z))

# TYPE CONVERSION
# you can convert from one type to another with int(), float(), complex()
# x = 1
# y = 2.8
# z = 1j
# a = float(x)
# b = int(y)
# c = complex(x)

# print(a)
# print(b)

# print(c)

# print(type(a))
# print(type(b))
# print(type(c))


# RANDOM NUMBER
# import random
# print(random.randrange(1, 10))

# PYTHON CASTING
# int() - constructs an integer number from an integer literal, a float literal(by rounding down to the previous whole number), or a string literal(providing the string represents a whole number)
# float() - constructs a float number from an integer literal, a float literal or a string literal(providing the string represents a float or an integer)
# str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals

# STRING LITERALS
# Strings can be represented using either single quotes or double quotes
# print("Hello")
# print('Hello')

# Assign string to a variable
# a = "Hello"
# print(a)

# Multiline Strings
# Multiline strings can be represented using 3 double quotes / single quotes

# a = """nsfnbnbjsnbnbwibnpibn
# ainvabvnavbpibnpibnib
# bnaobaljbabnablbnlb"""
# print(a)

# a = '''nsfnbnbjsnbnbwibnpibn
# ainvabvnavbpibnpibnib
# bnaobaljbabnablbnlb'''
# print(a)

# STRINGS ARE ARRAYS
# Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
# However, Python does not have a character data type, a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string.

# a = "Hello, World!"
# print(a[1])

# SLICING
# You can return a range of characters by using the slice index.Specify the start index and the end index, seperated by a colon, to return a part of the string .
# b = "Hello, World!"
# print(b[2:5])  # character from position 2 to 4(one position before 5) are printed

# Negative Indexing
# b = "Hello, World!"
# print(b[-5:-2])

# String Length
# To get the len() of the string use len() function
# a = "Hello, World!"
# print(len(a))

# String Methods
# The strip method removes any  whitespaces from the beginning or the end
# a = " Hello, World! "
# print(a.strip())

# The lower method returns the string in lower case:
# a = "Hello, World!"
# print(a.lower())

# The upper method return the string in upper case:
# a = "Hello, World!"
# print(a.upper())

# The replace() method replaces a string with another string:
# a = "Hello, World!"
# print(a.replace("H", "J"))

# The split() method splits the string into substrings if it finds instances of a seperator
# a = "Hello, World!"
# print(a.split(","))

# Check String
# To check phrase if a certain phrase or character is present in a string, we can use the keywords 'in' or ' not in '
# txt = "The rain in Spain stays mainly in the plain"
# x = "ain" in txt
# print(x)

# txt = "The rain in Spain stays mainly in the plain"
# x = "ain" not in txt
# print(x)

# String Concatenation
# To concatenate the string you can use the + operator
# a = "Hello"
# b = "World"
# c = a+b
# print(c)

# a = "Hello"
# b = "World"
# c = a+" "+b
# print(c)

# STRING FORMAT
# We can't concatenate strings and numebers.
# But we can combine strings and numbers by using the format() method!
# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:
# age = 36
# txt = "My name is John, I am {}"
# print(txt.format(age))

# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want {} pieces of item {} for {} dollars."
# print(myorder.format(quantity, itemno, price))

# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
# print(myorder.format(quantity, itemno, price))

# ESCAPE CHARACTER
# To insert characters that are illegal in a string, use an escape character.
# An escape character is a backslash \ followed by the character you want to insert.
# An example of an illegal character is a double quote inside a string that is surrounded by double quotes:
# txt = "We are the so-called \"Vikings\" from the north."
# print(txt)
