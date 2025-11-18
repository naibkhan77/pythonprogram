# Tuples // A tuple is an ordered collection of items in Python, just like a list, but immutable (cannot be changed after creation).

# Key Features of Tuples
# Ordered → Elements keep the order you put them in.
# Allow duplicates → Same value can appear multiple times.
# Immutable → Once created, you cannot change, add, or remove elements.
# Heterogeneous → Can store mixed data types (int, string, bool, etc).


# my_tuples = (1, 2, 3, "ali", True)
# print(my_tuples)


# Accessing tuple elements
# Just like lists (using indexes):

# my_tuples = ("apple", "banana", "cherry")
# print(my_tuples[0]) # apple
# print(my_tuples[-1]) # cherry   


# my_tuples = (1, 2, 3)
# my_tuples[1] = 99  # ❌ Error: 'tuple' object does not support item assignment
# print(my_tuples)

# Special cases
# A tuple with one element needs a comma:

# t = (4,)
# print(type(t)) # <class 'tuple'>


# Without the comma, it’s just an integer:

# t = (4)
# print(type(t)) # <class 'int'>



















