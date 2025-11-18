
#  Working with list chapter 4 

# names = ["alice", "david", "zain"]
# for name in names:
#     print(name)
    
    
# 

# line = ["alice", "david", "zain"]

# for student in line: 
#     print(f"{student.title()}, that was a great trick! ")
    
    
# 

# Doing Something After a for Loop

# line = ["alice", "david", "maxwell"]
# for student in line: 
#     print(f"{student.title()}, that was a great trick!")
#     print(f"I can't wait to see your next trick, {student.title()}")
    
# 

# Avoiding Indentation Errors
# Forgetting to Indent

# line = ["alice", "david", "caroline"]
# for student in line: 
# print(student) # IndentationError: expected an indented block after 'for' statement on line 33

# 

# Indenting Unnecessarily
# We don’t need to indent the print() call, because it isn’t part of a loop; 
# hence, Python reports that error:

# message = "Hello python world! "
# print(message)

# 

# Indenting Unnecessarily After the Loop

# line = ['alice', 'david', 'carolina']
# for student in line: 
#     print(f"{student.title()}, That was a great trick!")    
#     print(f"I can't wait to see your next trick, ")
    
#     print("thank you everyone that was a great magic show")
    

# 

#  TRY IT YOURSELF

#  4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these 
# pizza names in a list, and then use a for loop to print the name of each pizza.
#  • Modify your for loop to print a sentence using the name of the pizza, 
# instead of printing just the name of the pizza. For each pizza, you should 
# have one line of output containing a simple statement like I like pep
# peroni pizza.
#  • Add a line at the end of your program, outside the for loop, that states 
# how much you like pizza. The output should consist of three or more lines 
# about the kinds of pizza you like and then an additional sentence, such as 
# I really love pizza!


# pizza = ["Neapolitan", "Sicilian", "Roman style"]
# for person in pizza: 
#     print(f" My favorite pzza is {person.title()}, Roman style pizaa")
#     print("I love all type of pizza but the Roman style is too Yami ! ")


# 

# Making Numerical Lists

# Using the range() Function

# for value in range(1, 5): 
#     print(value)
    

# 

# Using range() to Make a List of Numbers

# numbers = list(range(1, 6))
# print(numbers)

# hello = list(str(f"hello naib"))
# print(hello)

# 

# Here we are using the range(start, stop, step) function.

# even_number = list(range(2, 11, 2))
# print(type(even_number))


# squares = [] 
# for value in range(1, 11): 
#     square = value ** 2
#     squares.append(square)
# print(squares)

# 

# squares = [] 
# for value in range(1, 11): 
#     squares.append(value**2)
# print(squares)


# 

# Simple Statistics with a List of Numbers

# digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# print(min(digits)) # 0 
# print(max(digits)) # 9
# print(sum(digits)) # 45

# 

#  List Comprehensions

# suquares = [value**2 for value in range(1, 11)]
# print(suquares)

# 

# Try It Yourself 

# Counting to Twenty: Use a for loop to print the numbers from 1 to 20, 
# inclusive.

# for number in range(1, 21):
#     print(number)   


# 

# Odd Numbers: Use the third argument of the range() function to make a list 
# of the odd numbers from 1 to 20. Use a for loop to print each number

# You can do this with the step argument in range(start, stop, step)

# for number in range(1, 21, 2):
#     print(number)

# 

#  Make a list of the multiples of 3, from 3 to 30. Use a for loop to 
# print the numbers in your list

# multiples_of_3 = [] 

# for number in range(3, 31, 3): 
#     multiples_of_3.append(number)
    
# for num in multiples_of_3: 
#     print(num)

# 

# Cubes: A number raised to the third power is called a cube. For example, 
# the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that 
# is, the cube of each integer from 1 through 10), and use a for loop to print out 
# the value of each cube

# cubes = [] 

# for number in range(1, 11): 
#     cubes.append(number ** 3)
    
# for cube in cubes: 
#     print(cube)


# ///////

# orking with Part of a List

#  Slicing a List
# Slicing lets you extract a portion (sub-list) from a list using the syntax:

# list[start:end:step]

# number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 

# print(number[2:6])  # [2, 3, 4, 5]  → from index 2 up to (but not including) 6
# print(number[:5])  # [0, 1, 2, 3, 4]  → start omitted = from beginning
# print(number[::2])  # [0, 2, 4, 6, 8]  → step 2 = every second element

# 

# players = ['charles', 'martina', 'michael', 'eli', 'florence']
# print(players[0:4]) 
# print(players[2:])
# print(players[-3])


# 

# Looping Through a Slice

# players = ['charles', 'martina', 'michael', 'eli', 'florence']

# print("Here are the first three players on my team:")
# for player in players[0:3]: 
#     print(player.title())


# 

# Copying a List

# my_foods = ['pizza', 'falafel', 'carrot cake']
# friend_foods = my_foods[:]
# print(f"\nMy favorite food are: ")
# print(friend_foods)


# 

# my_foods = ['pizza', 'falafel', 'carrot cake']

# my_foods.append('cannoil')
# print(my_foods)


# 

# ///////////// Tuples  ///////////////

# Lists work well for storing collections of items that can change throughout the 
# life of a program. 
# immutable list is called a tuple.
# That means once a tuple is created, you cannot change (add, remove, or update) its elements.

# 

# Example: List (mutable)

# fruits = ['apple', 'banana', 'cherry']
# fruits[1] = 'orange' 
# fruits.append("grape")
# print(fruits)

# # 

# # Example: Tuple (immutable)

# colors = ('red', 'green', 'blue')
# # colors[1] 'yellow' #  Error! Tupes can't be modified
# print(colors) # ('red', 'green', 'blue')


# 

# dimensions = (200, 50) 
# dimensions[0] = 250 
# print(dimensions) # TypeError: 'tuple' object does not support item assignment

# 

# Looping Through All Values in a Tuple

# dimensions = (200, 50) 
# for dimension in dimensions: 
#     print(dimension)


# 

# Writing Over a Tuple

# Try it Yourself
# A buffet-style restaurant offers only five basic foods. Think of five 
# simple foods, and store them in a tuple.
#  • Use a for loop to print each food the restaurant offers.
#  • Try to modify one of the items, and make sure that Python rejects the 
# change.

# restaurants = ('chawal', 'checken', 'sekhekababe', 'fish', 'khaleem')
# print('Original menu:')
# for restaurant in restaurants: 
#     print(restaurant)
# restaurants[1] = 'biryani' 
# print(restaurants)

# 

# The restaurant changes its menu, replacing two of the items with different 
# foods. Add a line that rewrites the tuple, and then use a for loop to print 
# each of the items on the revised menu.

# restaurants = ('chawal', 'biryani', 'burger', 'fish', 'khaleem')
# print('\n Revised menu:')
# for restaurant in restaurants: 
#     print(restaurant)

# 

# this is a list example 
# when we replace the value 

restaurants = ['chawal', 'cheken', 'sekhekababe', 'fish', 'khaleem']

restaurants[-1] = 'dal'
restaurants[-2] = 'lobya'
for i in restaurants: 
    print(i)
    

# 

# 







































    