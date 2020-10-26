# PYTHON BOOLEANS
# print(9 > 10)
# print(9 == 10)
# print(9 < 10)

# a = 33
# b = 393
# if a > b:
#     print("a is greater than b")
# else:
#     print("b is greater tha a")

# the bool() allows you to evaluate any value and give you a true and false value in return
# print(bool("Hello"))
# print(bool(0))
# print(bool(21))

# x = "a"
# y = 1
# print(bool(x))
# print(bool(y))

# MOST VALUES ARE TRUE
# Almost any value is evaluated to True if it has some sort of content.
# Any string is True, except empty strings.
# Any number is True, except 0.
# Any list, tuple, set, and dictionary are True, except empty ones.
# print(bool("abc"))
# print(bool(123))
# print(bool(["apple", "cherry", "banana"]))

# SOME VALUES ARE FALSE
# In fact, there are not many values that evaluates to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.
# print(bool(None))
# print(bool(0))
# print(bool(""))
# print(bool(()))
# print(bool([]))
# print(bool({}))

# FUNCTIONS CAN RETURN BOOLEANS
# def myfunc():
#     return True

# print(myfunc())

# def myfunc():
#     return True


# if myfunc():
#     print("true")
# else:
#     print("false")

# Python has many built in functions that can be used to return a boolean value , like this isinstance() function,which can be used to determine if an object is of a certain datatype:
# x = 200
# print(isinstance(x, int))

# PYTHON OPERATORS
# Operators are used to perform operations on variables and values.

# Python divides the operators in the following groups:

# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators

# +	Addition	x + y
# -	Subtraction	x - y
# *	Multiplication	x * y
# /	Division	x / y
# %	Modulus	x % y
# ** Exponentiation x ** y
# x = 2
# y = 5
# print(x**y)
# // Floor division x // y
# x = 10
# y = 8
# print(x//y)

# PYTHON ASSIGNMENT OPERATORS
# =	x = 5	x = 5
# += x += 3 x = x + 3
# -= x -= 3 x = x - 3
# *= x *= 3 x = x * 3
# /= x /= 3 x = x / 3
# %= x %= 3 x = x % 3
# //= x //= 3 x = x // 3
# **= x **= 3 x = x ** 3
# &= x &= 3 x = x & 3
# |= x |= 3 x = x | 3
# ^= x ^= 3 x = x ^ 3
# >>= |   x >>= 3 x = x >> 3  returns x with bits shifted to the right by y places
# <<= |   x <<= 3 x = x << 3  return x with the bits shifted to the left by x places

# PYTHON COMPARISON OPERATORS
# == Equal x == y
# != Not equal x != y
# >	Greater than	x > y
# <	Less than	x < y
# >= Greater than or equal to x >= y
# <= Less than or equal to x <= y

# PYTHON LOGICAL OPERATORS
# and Returns True if both statements are true	x < 5 and x < 10
# or Returns True if one of the statements is true	x < 5 or x < 4
# not Reverse the result, returns False if the result is true not(x < 5 and x < 10)

# PYTHON IDENTITY OPERATORS
# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
# is Returns True if both variables are the same object	x is y
# a = ["apple", "banana"]
# b = ["apple", "banana"]
# print(a is b)
# is not Returns True if both variables are not the same object	x is not y
# a = ["apple", "banana"]
# z = a
# print(a is z)
# print(a is not z)

# PYTHON MEMBERSHIP OPERATORS
# in Returns True if a sequence with the specified value is present in the object	x in y
# a = ["apple", "banana"]
# print("banana" in a)
# not in Returns True if a sequence with the specified value is not present in the object	x not in y
# a = ["apple", "banana"]
# print("orange" not in a)

# PYTHON BITWISE OPERATOR
# & 	AND	Sets each bit to 1 if both bits are 1
# |	OR	Sets each bit to 1 if one of two bits is 1
# ^	XOR	Sets each bit to 1 if only one of two bits is 1
# ~ 	NOT	Inverts all the bits
# << Zero fill left shift Shift left by pushing zeros in from the right and let the leftmost bits fall off
# >> Signed right shift Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off


# PYTHON LISTS
# python collections(arrays)
# There are 4 types of data types in python programming language.
# List: List is a collection which is ordered and changeable , allows duplicate members.(mutable)
# Tuple:Tuple is a collection which is ordered and unchangeable ,allows duplicate members.(unmutable)
# Set:Set is a collection which is unordered and unindexed , No duplicate members.
# Dictionary:Dictionary is a collection which is unordered , changeable and indexed . No duplicate members.
# When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.

# list
# lists are written with square brackets.
# thisisalist = ["banana", "apple", "cherry"]
# print(thisisalist)

# Acess items in a list
# You can access items in a list by referring to the index number
# thisisalist = ["banana", "apple", "cherry"]
# print(thisisalist[1])

# Negative Indexing
# Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.
# thisisalist = ["banana", "apple", "cherry"]
# print(thisisalist[-1])

# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new list with the specified items.
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])

# by leaving out the start value the range will start at the 1st value
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[:5])

# by leaving out the end value the range will go on till the end of the list
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:])

# Range of Negative Indexes
# Specify negative indexes if you want to start the search from the end of the list:
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[-4:-1])

# To change item value
# refer to the index of the specific value
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# thislist[2] = "blackcurrant"
# print(thislist)

# Loop through a list
# You can loop through the items of a list using the for loop
# thislist = ["apple", "cherry", "banana"]
# for fruit in thislist:
#     print(fruit)

# list length
# thislist = ["apple", "banana", "cherry"]
# print(len(thislist))

# Add Items
# To add an item to the end of the list, use the append() method:
# thislist = ["apple", "banana ", "cherry"]
# thislist.append("orange")
# print(thislist)

# To add an item at the specified index, use the insert() method:
# thislist = ["apple", "banana ", "cherry"]
# thislist.insert(1, "orange")
# print(thislist)

# Remove Item
# There are several methods to remove items from a list:
# The remove() method removes the specified item:

# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)

# The pop() method removes the specified index, (or the last item if index is not specified):
# thislist = ["apple", "banana", "cherry"]
# thislist.pop()
# print(thislist)

# The del keyword removes the specified index:
# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)

# the del keyword can also remove the complete list
# thislist = ["apple", "banana", "cherry"]
# del thislist

# The clear() method empties the list:
# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)

# Copy a list
# Make a copy of a list with the copy() method:
# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# print(mylist)

# another way to make a copy is using the built in list
# Make a copy of a list with the list() method:
# thislist = ["apple", "banana", "cherry"]
# mylist = list(thislist)
# print(mylist)

# Join two lists
# l1 = ["a", "b", "v"]
# l2 = [1, 2, 3]
# l3 = l1+l2
# print(l3)

# another way to join list is by appending list 2 to list 1  one by one
# l1 = ["a", "b", "c"]
# l2 = [1, 2, 3]
# for i in l2:
#     l1.append(i)

# print(l1)

# Or you can use the extend() method, which purpose is to add elements from one list to another list:
# l1 = ["a", "b", "c"]
# l2 = [1, 2, 3]
# l1.extend(l2)
# print(l1)

# list constructor
# It is also possible to use the list() constructor to make a new list.
# thislist = list(("apple", "banana", "cherry"))  # note the double bracket
# print(thislist)


# TUPLES
# A tuple is a collection which is oredered and unchangeable .In python tuples ae written with round brackets.
# thistuple = ("apple", "banana", "cherry")
# print(thistuple)

# Access Tuple Items
# You can access tuple items by referring to the index number, inside square brackets:
# thistuple = ("apple", "banana", "cherry")
# print(thistuple[0])

# Negative Indexing
# Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.
# thistuple = ("apple", "banana", "cherry")
# print(thistuple[-1])

# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new tuple with the specified items.
# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[2:5])

# Range of Negative Indexes
# Specify negative indexes if you want to start the search from the end of the tuple:
# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[-5:-2])

# Change Tuple Values
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple
# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y[0] = "orange"
# x = tuple(y)
# print(x)

# Loop Through a Tuple
# You can loop through the tuple items by using a for loop.
# thistuple = ("apple", "banana", "cherry")
# for i in thistuple:
#     print(i)

# Check if Item Exists
# To determine if a specified item is present in a tuple use the in keyword:
# thistuple = ("apple", "banana", "cherry")
# if "apple" in thistuple:
#     print("present")
# thistuple = ("apple", "banana", "cherry")
# if "apple" not in thistuple:
#     print("present")

# Tuple Length
# To determine how many items a tuple has, use the len() method:
# thistuple = ("apple", "banana", "cherry")
# print(len(thistuple))

# Create Tuple With One Item
# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
# thistuple = ("apple",)
# print(type(thistuple))
# thistuple = ("apple")
# print(type(thistuple))

# Tuples are unchangeable, so you cannot remove items from it, but you can delete the tuple completely:
# thistuple = ("apple", "banana", "cherry")
# del thistuple
# print(thistuple) #an error will arise as this tuple no longer exists.

# Join two tuples
# l1 = ('a', 'b', 'c')
# l2 = (1, 2, 3)
# l3 = l1+l2
# print(l3)

# The tuple() Constructor
# It is also possible to use the tuple() constructor to make a tuple.
# it is also possible to make a tuple using the tuple constructor
# thistuple = (("apple", "banana", "cherry"))
# print(thistuple)
