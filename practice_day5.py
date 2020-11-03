# # Scope
# # The variable is only available from inside the region from where it is created.This is called as scope.

# # Local Scope
# # A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

# # def myfunc():
# #     x = 300
# #     print(x)

# # myfunc()

# # Function Inside Function
# # As explained in the example above, the variable x is not available outside the function, but it is available for any function inside the function:

# # def myfunc():
# #     x = 20

# #     def myfunc2():
# #         print(x)
# #     return myfunc2()


# # myfunc()

# # Global Scope
# # A variable created in the main body of the Python code is a global variable and belongs to the global scope.

# # Global variables are available from within any scope, global and local.
# # x = 300


# # def myfunc():
# #     print(x)


# # myfunc()

# # print(x)

# # Naming Variables
# # If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables, one available in the global scope (outside the function) and one available in the local scope (inside the function):
# # x = 300


# # def myfunc():
# #     x = 200
# #     print(x)


# # myfunc()

# # print(x)

# # Global Keyword
# # If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.

# # The global keyword makes the variable global.

# # def myfunc():
# #     global x
# #     x = 300
# #     print(x)


# # myfunc()

# # print(x)

# # Also, use the global keyword if you want to make a change to a global variable inside a function.
# # x = 200


# # def myfunc():
# #     global x
# #     x = 100
# #     print(x)


# # myfunc()
# # print(x)


# # What is a Module?
# # Consider a module to be the same as a code library.

# # A file containing a set of functions you want to include in your application.

# # Create a Module
# # To create a module just save the code you want in a file with the file extension .py:
# # Example
# # Save this code in a file named mymodule.py


# # def greeting(name):
# #   print("Hello, " + name)

# # import mymodule
# # Use a Module
# # Now we can use the module we just created, by using the import statement:

# # Example
# # Import the module named mymodule, and call the greeting function:


# # mymodule.greeting("Jonathan")

# # Variables in Module
# # The module can contain functions, as already described, but also variables of all types(arrays, dictionaries, objects etc):

# # Example
# # Save this code in the file mymodule.py

# # person1 = {
# #     "name": "John",
# #     "age": 36,
# #     "country": "Norway"
# # }
# # Example
# # Import the module named mymodule, and access the person1 dictionary:


# # a = mymodule.person1["age"]
# # print(a)

# # Naming a Module
# # You can name the module file whatever you like, but it must have the file extension .py

# # Re-naming a Module
# # You can create an alias when you import a module, by using the as keyword:

# # Example
# # Create an alias for mymodule called mx:


# # a = mx.person1["age"]
# # print(a)

# # Built-in Modules
# # There are several built-in modules in Python, which you can import whenever you like.

# # Example
# # Import and use the platform module:

# # import platform

# # x = platform.system()
# # print(x)

# # Using the dir() Function
# # There is a built-in function to list all the function names (or variable names) in a module. The dir() function:
# # import platform
# # x = dir(platform)
# # print(x)

# # Import From Module
# # You can choose to import only parts from a module, by using the from keyword.

# # Example
# # The module named mymodule has one function and one dictionary:

# # def greeting(name):
# #   print("Hello, " + name)

# # person1 = {
# #   "name": "John",
# #   "age": 36,
# #   "country": "Norway"
# # }
# # Example
# # Import only the person1 dictionary from the module:

# # from mymodule import person1

# # print (person1["age"])

# # Note: When importing using the from keyword, do not use the module name when referring to elements in the module. Example: person1["age"], not mymodule.person1["age"]


# # Python Dates
# # A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.

# # import datetime
# # x = datetime.datetime.now()
# # print(x)

# # Date Output
# # When we execute the code from the example above the result will be:

# # 2020-11-03 20:59:19.961373
# # The date contains year, month, day, hour, minute, second, and microsecond.

# # The datetime module has many methods to return information about the date object.

# # Here are a few examples, you will learn more about them later in this chapter:

# # import datetime
# # x = datetime.datetime.now()
# # print(x.second)

# # Creating Date Objects
# # To create a date, we can use the datetime() class (constructor) of the datetime module.

# # The datetime() class requires three parameters to create a date: year, month, day.
# # import datetime
# # x = datetime.datetime(2020, 5, 17)
# # print(x)

# # The datetime() class also takes parameters for time and timezone(hour, minute, second, microsecond, tzone), but they are optional, and has a default value of 0, (None for timezone).

# # The strftime() Method
# # The datetime object has a method for formatting date objects into readable strings.

# # The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:

# # Example
# # Display the name of the month:

# # import datetime

# # x = datetime.datetime(2018, 6, 1)

# # print(x.strftime("%B"))

# # Directive	Description	                                                       Example
# # %a	        Weekday, short version	                                           Wed
# # %A	        Weekday, full version	                                           Wednesday
# # %w	        Weekday as a number 0-6, 0 is Sunday	                           3
# # %d	        Day of month 01-31	                                               31
# # %b	        Month name, short version	                                       Dec
# # %B	        Month name, full version	                                       December
# # %m	        Month as a number 01-12	                                           12
# # %y	        Year, short version, without century	                           18
# # %Y	        Year, full version	                                               2018
# # %H	        Hour 00-23	                                                       17
# # %I	        Hour 00-12	                                                       05
# # %p	        AM/PM	                                                           PM
# # %M	        Minute 00-59	                                                   41
# # %S	        Second 00-59	                                                   08
# # %f	        Microsecond 000000-999999	                                       548513
# # %z	        UTC offset                                                         + 0100
# # %Z	        Timezone	                                                       CST
# # %j	        Day number of year 001-366	                                       365
# # %U	        Week number of year, Sunday as the first day of week, 00-53	       52
# # %W	        Week number of year, Monday as the first day of week, 00-53	       52
# # %c	        Local version of date and time	                                   Mon Dec 31 17: 41: 00 2018
# # %x	        Local version of date	                                           12/31/18
# # %X	        Local version of time	                                           17: 41: 00
# # % %         A % character                                                        %

# # Python Math
# # Python has a set of built-in math functions, including an extensive math module, that allows you to perform mathematical tasks on numbers.
# # Built-in Math Functions
# # The min() and max() functions can be used to find the lowest or highest value in an iterable:
# # x = min(5, 10, 25)
# # y = max(5, 10, 25)
# # print(x)
# # print(y)

# # The abs() function returns the absolute (positive) value of the specified number:
# # x = abs(-7.25)
# # print(x)

# # The pow(x, y) function returns the value of x to the power of y (xy).
# # x = pow(4, 3)
# # print(x)

# # The Math Module
# # Python has also a built-in module called math, which extends the list of mathematical functions.

# # To use it, you must import the math module:

# # import math

# # When you have imported the math module, you can start using methods and constants of the module.

# # The math.sqrt() method for example, returns the square root of a number:

# # import math
# # x = math.sqrt(64)
# # print(x)

# # The math.ceil() method rounds a number upwards to its nearest integer, and the math.floor() method rounds a number downwards to its nearest integer, and returns the result:
# # import math
# # x = math.ceil(1.4)
# # y = math.floor(1.4)

# # print(x, y)

# # The math.pi constant, returns the value of PI(3.14...):

# # import math

# # x = math.pi
# # print(x)


# # PYTHON JSON
# # JSON is a syntax for storing and exchanging data.
# # JSON is text, written with JavaScript object notation.

# # JSON in Python
# # Python has a built-in package called json, which can be used to work with JSON data.

# # import json

# # Parse Json - Convert from JSON to python

# # import json

# # # some JSON
# # x = '{"name":"Aman","age":30,"city":"Newyork"}'

# # # parse JSON
# # y = json.loads(x)

# # print(y["age"])

# # Convert from Python to JSON
# # If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

# # import json
# # x = {
# #     "name": "aman",
# #     "age": 30,
# #     "city": "New York",
# # }
# # y = json.dumps(x)
# # print(y)

# # You can convert Python objects of the following types, into JSON strings:

# # dict
# # list
# # tuple
# # string
# # int
# # float
# # True
# # False
# # None

# # import json

# # print(json.dumps({"name": "John", "age": 30}))
# # print(json.dumps(["apple", "bananas"]))
# # print(json.dumps(("apple", "bananas")))
# # print(json.dumps("hello"))
# # print(json.dumps(42))
# # print(json.dumps(31.76))
# # print(json.dumps(True))
# # print(json.dumps(False))
# # print(json.dumps(None))

# # When you convert from Python to JSON, Python objects are converted into the JSON(JavaScript) equivalent:

# # Python	JSON
# # dict	Object
# # list	Array
# # tuple	Array
# # str	    String
# # int	    Number
# # float	Number
# # True	true
# # False	false
# # None	null

# # import json

# # x = {
# #     "name": "John",
# #     "age": 30,
# #     "married": True,
# #     "divorced": False,
# #     "children": ("Ann", "Billy"),
# #     "pets": None,
# #     "cars": [
# #         {"model": "BMW 230", "mpg": 27.5},
# #         {"model": "Ford Edge", "mpg": 24.1}
# #     ]
# # }

# #  print(json.dumps(x))

# # Format the Result
# # The example above prints a JSON string, but it is not very easy to read, with no indentations and line breaks.

# # The json.dumps() method has parameters to make it easier to read the result:

# import json
# x = {
#     "name": "John",
#     "age": 30,
#     "married": True,
#     "divorced": False,
#     "children": ("Ann", "Billy"),
#     "pets": None,
#     "cars": [
#         {"model": "BMW 230", "mpg": 27.5},
#         {"model": "Ford Edge", "mpg": 24.1}
#     ]
# }

# # print(json.dumps(x, indent=4))
# # You can also define the separators, default value is (", ", ": "), which means using a comma and a space to separate each object, and a colon and a space to separate keys from values:
# # json.dumps(x, indent=4, separators=(". ", " = "))
# # Order the Result
# # The json.dumps() method has parameters to order the keys in the result:
# print(json.dumps(x, indent=4, sort_keys=True))
