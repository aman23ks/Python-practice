# For loops
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     print(x)

# Looping through a string
# for x in "banana":
#     print(x)

# break Statement
# with the break statement we can stop the loop before it has looped through all the items.
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     print(x)
#     if x == "banana":
#         break

# The continue statement
# with the continue statement we can stop the current iteration of the loop and continue with the next iteration.
# fruits = ["apple", "banana", "cherry"]

# for x in fruits:
#     if x == "banana":
#         continue
#     print(x)

# The range() Function
# To loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
# for x in range(6):
#     print(x)

# The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):
# for x in range(2, 6):
#     print(x)

# The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):
# for x in range(2, 30, 3):
#     print(x)

# Else in For Loop
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
# for x in range(6):
#     print(x)
# else:
#     print("Finally Finished!")

# Nested Loops
# A nested loop is a loop inside a loop.
# The "inner loop" will be executed one time for each iteration of the "outer loop":
# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#     for y in fruits:
#         print(x, y)

# The pass Statement
# for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
# for x in [0, 1, 2]:
#     pass

# Python Functions
# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

# def my_function():
#     print("Hello from a function")

# Calling a function
# To call a function, use the function name followed by parenthesis:
# def my_function():
#     print("Hello from a function")


# my_function()


# Arguments
# Information can be passed into functions as arguments.
# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
# The following example has a function with one argument(fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:

# def my_function(fname):
#     print(fname + " Refsnes")


# my_function("Email")
# my_function("Tobias")
# my_function("Linus")

# Parameters or Arguments?
# The terms parameter and argument can be used for the same thing: information that are passed into a function.
# From a function's perspective:
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.

# Number of Arguments
# By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.
# def my_function(fname, lname):
#     print(fname + " " + lname)


# my_function("Email", "Refsnes")

# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly:
# def my_function(*kids):
#     print("The youngest child is " + kids[2])

# my_function("Email", "Tobias", "Linus")

# Keyword Arguments
# You can also send arguments with the key = value syntax.
# This way the order of the arguments does not matter.
# def my_function(child3, child2, child1):
#     print("The youngest child is " + child3)


# my_function(child1="Email", child2="Tobias", child3="Linus")

# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments, and can access the items accordingly:
# def my_function(**kid):
#     print("His last name is " + kid["lname"])


# my_function(fname="Tobias", lname="Refsnes")

# Default Parameter Value
# The following example shows how to use a default parameter value.
# If we call the function without argument, it uses the default value:
# def my_function(country="Norway"):
#     print("I am from " + country)

# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")

# Passing a List as an Argument
# You can send any data types of argument to a function(string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
# E.g. if you send a List as an argument, it will still be a List when it reaches the function:
# def my_function(food):
#     for x in food:
#         print(x)


# fruits = ["apple", "banana", "cherry"]
# my_function(fruits)

# Return Values
# To let a function return a value, use the return statement:

# def my_function(x):
#     return 5*x


# print(my_function(3))
# print(my_function(5))
# print(my_function(9))


# The pass Statement
# function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.

# def my_function():
#     pass

# Recursion
# Python also accepts function recursion, which means a defined function can call itself.
# Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.
# The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.
# In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). We use the k variable as the data, which decrements (-1) every time we recurse. The recursion ends when the condition is not greater than 0 (i.e. when it is 0).
# To a new developer it can take some time to work out how exactly this works, best way to find out is by testing and modifying it.

# def tri_recursion(k):
#     if k > 0:
#         result = k + tri_recursion(k-3)
#         print(result)
#     else:
#         result = 0
#     return result


# print("\n\nRecursion example results")
# tri_recursion(6)

# Python Lambda
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# Add 10 to argument a , and return the result :
# x = lambda a: a + 10
# print(x(5))

# Lamda functions can take any number of arguments
# x=lambda a,b: a*b
# print(x(5,6))

# x = lambda a, b, c: a+b+c
# print(x(1, 2, 3))

# Why Use Lambda Functions?
# The power of lambda is better shown when you use them as an anonymous function inside another function.
# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:
# def myfunc(n):
#     return lambda a: a*n


# Use that function definition to make a function that always doubles the number you send in:
# mydoubler = myfunc(2)

# print(mydoubler(11))
# Or, use the same function definition to make a function that always triples the number you send in:
# mytripler = myfunc(3)
# print(mytripler(4))

# Or use the same function definition to make both funtions
# mydoubler = myfunc(2)
# print(mydoubler(11))
# mytripler = myfunc(3)
# print(mytripler(4))

# print(mydoubler(11))
# print(mytripler(4))

# Python arrays
# Python does not have built-in support for Arrays, but Python Lists can be used instead.
# This page shows you how to use LISTS as ARRAYS, however, to work with arrays in Python you will have to import a library, like the NumPy library.
# everthing is same as in lists

# Classes and Objects
# Python Classes/Objects
# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.

# Create a Class
# To create a class, use the keyword class:
# class myClass:
#     x=5

# Create Object
# Now we can use the class named MyClass to create objects:
# class myClass:
#     x = 5
# p1 = myClass()
# print(p1.x)

# The __init__() Function
# The examples above are classes and objects in their simplest form, and are not really useful in real life applications.
# To understand the meaning of classes we have to understand the built-in __init__() function.
# All classes have a function called __init__(), which is always executed when the class is being initiated.
# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# p1 = Person("John", 36)
# print(p1.name)
# print(p1.age)

# Object Methods
# Objects can also contain methods. Methods in objects are functions that belong to the object.
# Let us create a method in the Person class:

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def myfunc(self):
#         print("Hello my name is " + self.name)


# p1 = Person("John", 36)
# p1.myfunc()

# The self Parameter
# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:
# class Person:
#     def __init__(mysillyobject, name, age):
#         mysillyobject.name = name
#         mysillyobject.age = age

#      def myfunc(abc):
#         print("Hello my name is " + abc.name)


# p1 = Person("John", 36)
# p1.myfunc()


# Modify Object Properties
# You can modify properties on objects like this:
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def myfunc(self):
#         print("Hello my name is " + self.name)


# p1 = Person("John", 36)
# p1.myfunc()
# p1.age = 40
# print(p1.age)

# # del object properties using del keyword
# del p1.age
# print(p1.age)  # you'll get an error because its already deleted

# # delete objects
# del p1
# print(p1)  # you'll get an error

# The pass Statement
# class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.
# class Person:
#     pass


# Python Inheritance
# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.

# Create a Parent Class
# Any class can be a parent class, so the syntax is the same as creating any other class:
# Create a class named Person, with firstname and lastname properties, and a printname method:

# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname

#     def printname(self):
#         print(self.firstname, self.lastname)

# Use the Person class to create an object, and then execute the printname method:


# x = Person("John", "Doe")
# x.printname()

# Create a class named Student, which will inherit the properties and methods from the Person class:


# class Student(Person):
#     #     pass

# Use the pass keyword when you do not want to add any other properties or methods to the class.
# x = Student("Mike", "Olsen")
# print(x.firstname)

# Add the __init__() Function
# So far we have created a child class that inherits the properties and methods from its parent.

# We want to add the __init__() function to the child class (instead of the pass keyword).
# The __init__() function is called automatically every time the class is being used to create a new object.


# class Student(Person):
#     def __init__(self, fname, lname)
# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.


# Note: The child's __init__() function overrides the inheritance of th
# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
# class Student(Person):
#     def __init__(self, fname, lname):
#         Person.__init__(self, fname, lname)

# Use the super() Function
# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:


# class Student(Person):
#     def __init__(self, fname, lname):
#         super().__init__(fname, lname)


# By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.

# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname

#     def printname(self):
#         print(self.firstname, self.lastname)

# Use the Person class to create an object, and then execute the printname method:


# x = Person("John", "Doe")
# x.printname()
# Add a property called graduationyear to the Student class:


# class Student(Person):
#     def __init__(self, fname, lname, year):
#         super().__init__(fname, lname)
#         self.graduationyear = year


# # In the example below, the year 2019 should be a variable, and passed into the Student class when creating student objects. To do so, add another parameter in the __init__() function:
# x = Student("Mike", "Olsen", 2019)

# dd a method called welcome to the Student class:

# class Student(Person):
#   def __init__(self, fname, lname, year):
#     super().__init__(fname, lname)
#     self.graduationyear = year

#   def welcome(self):
#     print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

# Python Iterators
# An iterator is an object that contains a countable number of values.
# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
# Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().

# Iterator vs Iterable
# Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.
# All these objects have a iter() method which is used to get an iterator:
# mytuple = ("apple", "banana", "cherry")
# myit = iter(mytuple)
# print(next(myit))
# print(next(myit))
# print(next(myit))

# Even strings are iterable objects, and can return an iterator:
# mystr = "banana"
# myit = iter(mystr)

# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))

# Looping Through an Iterator
# We can also use a for loop to iterate through an iterable object:
# mytuple = ("apple", "banana", "cherry")
# for x in mytuple:
#     print(x)

# Create an Iterator
# To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.
# As you have learned in the Python Classes/Objects chapter, all classes have a function called __init__(), which allows you to do some initializing when the object is being created.
# The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.
# The __next__() method also allows you to do operations, and must return the next item in the sequence.
# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self

#     def __next__(self):
#         x = self.a
#         self.a += 1
#         return x


# myclass = MyNumbers()
# myiter = iter(myclass)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

# StopIteration
# The example above would continue forever if you had enough next() statements, or if it was used in a for loop.
# To prevent the iteration to go on forever, we can use the StopIteration statement.
# In the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified number of times:
# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self

#     def __next__(self):
#         if self.a <= 20:
#             x = self.a
#             self.a += 1
#             return x
#         else:
#             raise StopIteration


# myclass = MyNumbers()
# myiter = iter(myclass)

# for x in myiter:
#     print(x)
