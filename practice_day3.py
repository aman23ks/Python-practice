# Sets
# A set is a collection which is unordered and unindexed .In Python , sets are written with curly brackets.
# thisset = {"apple", "banana", "cherry"}
# print(thisset)

# Access Items
# You cannot access items in a set by referring to an index or a key.
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
# thisset = {"apple", "banana", "cherry"}
# for x in thisset:
#     print(x)

# thisset = {"apple", "banana", "cherry"}
# print("banana" in thisset)

# Change Items:
# Once a set is created you cannot change it items , but you can add new items.

# to add one item use the add() method:
# thisset = {"apple", "banana", "cherry"}
# thisset.add("orange")
# print(thisset)

# Add multiple items to a set use the update() method.
# thisset = {"apple", "banana", "cherry"}
# thisset.update(["orange", "mango", "grapes"])
# print(thisset)

# Length
# To determine how many items a set has , use the len() method
# thisset = {"apple", "banana", "cherry"}
# print(len(thisset))

# Remove Item
# To remove an item in a set , use the remove(),or the discard() method
# thisset = {"apple", "banana", "cherry"}
# thisset.remove("banana")
# print(thisset)

# thisset = {"apple", "banana", "cherry"}
# thisset.discard("banana")
# print(thisset)

# You can also use the pop(), method to remove an item, but this method will remove the last item. Remember that sets are unordered, so you will not know what item that gets removed.
# The return value of the pop() method is the removed item.

# thisset = {"apple", "banana", "cherry"}
# x = thisset.pop()
# print(thisset)

# Sets are unordered so when using pop() you will not know which item gets removed.
# thisset = {"apple", "banana", "cherry"}
# thisset.clear()
# print(thisset)

# The del keyword will delete the set completely:
# thisset = {"apple", "banana", "cherry"}
# del thisset
# print(thisset)

# Join Two Sets
# There are several ways to join two or more sets in Python.
# You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another:
# set1 = {"A", "B", "C"}
# set2 = {1, 2, 3}
# set3 = set1.union(set2)
# print(set3)

# set1 = {"A", "B", "C"}
# set2 = {1, 2, 3}
# set1.update(set2)
# print(set1)

# The set() Constructor
# It is also possible to use the set() constructor to make a set.

# thisset = set(("apple", "banana", "cherry"))  # note the double round brackets.
# print(thisset)


# Method	             Description
# add()	                 Adds an element to the set
# clear()	             Removes all the elements from the set
# copy()	             Returns a copy of the set
# difference()	         Returns a set containing the difference between two or more sets
# difference_update()	 Removes the items in this set that are also included in another, specified set
# discard()	             Remove the specified item
# intersection()	     Returns a set, that is the intersection of two other sets
# intersection_update()	 Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	         Returns whether two sets have a intersection or not
# issubset()	         Returns whether another set contains this set or not
# issuperset()	         Returns whether this set contains another set or not
# pop()	                 Removes an element from the set
# remove()	             Removes the specified element
# symmetric_difference() Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	inserts the symmetric differences from this set and another
# union()	             Return a set containing the union of sets
# update()	             Update the set with the union of this set and others


# Python Dictionaries
# A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": "1964"
# }
# print(thisdict)

# Accessing Items
# You can access the items of a dictionary by referring to its key name, inside square brackets:
# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": "1964"
# }
# x = thisdict["model"]
# print(x)
# x = thisdict.get("brand")
# print(x)

# Change values
# You can change the value of a specific item by reffering to its key name:

# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }

# thisdict["year"] = 2018
# print(thisdict)

# Loop through a dictionary
# You can loop through a dictionary by using a for loop.
# When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.
# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# for x in thisdict:
#     print(x)

# To print all the values in the dictionary one by one
# for x in thisdict:
#     print(thisdict[x])

# you can also use the values method to return the values in the dictionary:
# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# for x in thisdict.values():
#     print(x)

# Loop through both keys and values , by using items() method:
# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# for x, y in thisdict.items():
#     print(x, y)

# Check if Key Exists
# To determine if a specified key is present in a dictionary use the in keyword:
# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# if "model" in thisdict:
#     print("Present")

# Dictionary length
# To determine how many items a dictionary has , use the len() function.
# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# print(len(thisdict))

# Adding Items
# Adding an item to the dictionary is done by using a new index key and assigning a value to it:
# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# thisdict["color"] = "red"
# print(thisdict)

# Removing Items
# The pop() method removes the item with the specified key name:
# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# thisdict.pop("model")
# print(thisdict)

# The popitem() removes the last inserted item.
# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# thisdict.popitem()
# print(thisdict)

# the del keyword removes the item with the specified key name:
# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# del thisdict["model"]
# print(thisdict)
# the del keyword can also remove the dictionary completely :
# this will cause an error because the "thisdict" no longer exists.

# Clear
# the clear() method empties the dictionary
# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# thisdict.clear()
# print(thisdict)

# Copy a dictionary
# You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.
# There are ways to make a copy, one way is to use the built-in Dictionary method copy().
# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }

# mydict = thisdict.copy()
# print(mydict)

# Another way to make a copy is to use the built-in function dict().
# Make a copy of the dictionary with the dict() function;
# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }

# mydict = dict(thisdict)
# print(mydict)

# Nested Dictionaries
# A dictionary can also contain many dictionaries, this is called nested dictionaries.
# myfamily = {
#     "child1": {
#         "name": "Emil",
#         "year": 2004
#     },
#     "child2": {
#         "name": "Tobias",
#         "year": 2007
#     },
#     "child3": {
#         "name": "Linus",
#         "year": 2011
#     }
# }
# print(myfamily)

# Or, if you want to nest three dictionaries that already exists as dictionaries:
# child1 = {
#     "name": "Emil",
#     "year": 2004
# }
# child2 = {
#     "name": "Tobias",
#     "year": 2007
# }
# child3 = {
#     "name": "Linus",
#     "year": 2011
# }

# myfamily = {
#     "child": child1,
#     "child2": child2,
#     "child3": child3
# }

# print(myfamily)

# The dict() constructor
# it is also possible to use the dict() constructor to make a new dictionary:
# thisdict = dict(brand="Ford", model="Mustang", year=194)
# # note that keywords are not string literals
# # note the use of equals rather than colon for the assignment
# print(thisdict)


# Python If..else:
# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

# An if statement is written using the 'if' keyword.
# a = 33
# b = 200
# if b > a:
#     print("b is greater than a")

# Elif:
# the elif keyword is pythons way of saying "if the previous conditions were not true then try these conditions"
# a = 33
# b = 33
# if b > a:
#     print('b is greater than a')
# elif a == b:
#     print("a and b are equal")

# Else
# The else keyword catches anything which isn't caught by the preceding conditions.
# a = 200
# b = 33
# if b > a:
#     print("b is greater than a")
# elif a == b:
#     print("a and b are equal")
# else:
#     print("a is greater than b")

# You can also have else without elif
# a = 200
# b = 33
# if b > a:
#     print("b is greater than a ")
# else:
#     print("b is not greater than a")

# Short hand If
# if you have only one line to execute you can put it on the same line as the if statement
# a = 200
# b = 33
# if a > b: print("a is greater than b")

# Short hand If...Else
# a = 2
# b = 330
# print("A") if a > b else print("B")


# This technique is known as Ternary Operators, or Conditional Expressions.
# You can also have multiple else statements on the same line:
# one line if else statements with 3 conditions
# a = 330
# b = 330
# print("A") if a > b else print("=") if a == b else print("B")

# And
# The and keyword is a logical operator, and is used to combine conditional statements:
# a = 200
# b = 33
# c = 500
# if a > b and c > a:
#     print("Both conditions are true")

# Or
# The or keyword is a logical operator, and is used to combine conditional statements:

# a = 200
# b = 33
# c = 500
# if a > b or a > c:
#     print("At least one of the conditions is True")

# Nested If
# You can have if statements inside if statements,this is called nested if statements.
# x = 41
# if x > 10:
#     print("Above ten,")
#     if x > 20:
#         print("and also above 20!")
#     else:
#         print("but not above 20.")

# The pass Statement
# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
# a = 33
# b = 200
# if b > a:
#     pass

# The While Loop
# with the while loop we can execute a statements as long as the condition is true.
# i = 1
# while i < 6:
#     print(i)
#     i += 1

# The break Statement
# With the break statement we can stop the loop even if the while condition s true:
# i = 1
# while i < 6:
#     print(i)
#     if(i == 3):
#         break
#     i += 1

# The continue Statement
# With the continue statement we can stop the current iteration, and continue with the next:
# i = 0
# while i < 6:
#     i += 1
#     if i == 3:
#         continue
#     print(i)#note 3 is missing from the iteration

# The else Statement
# With the else statement we can run a block of code once when the condition no longer is true:
# i = 1
# while i < 6:
#     print(i)
#     i += 1
# else:
#     print("i is no longer less than 6")
