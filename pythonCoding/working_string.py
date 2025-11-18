#  Rules no 1 Variable 

# name = "Alice"      #string
# age = 25            #integer
# height = 5.6        #float   
# is_student = true   # boolean 

# 

# Rules no 2 

# Must start with a letter or underscore(_) 
# Can contain letters, number, and underscores. 
# Case-sensitive (Age and age are different). 
# Cannot start with a number or use reserved keywords (class, def, etc) 

# my_name "naib"
# _age = 23
# age 30

# Invalid: 

# 2name = "Tom" # starts with number
# class = "A"   # reserved keyword

# 

# 3. Data Types in Python

# 1.integer 

# x = 10; 
# y = -50; 
# print(type(x))  # output -> <class 'int'>

# 2.Float (float) -> Decimal numbers 

# pi = 3.14159
# temp = -12.5
# print(type(pi))  # <class 'float'>

# 3.String (str) → Text enclosed in quotes.

# message = "Hello World"
# print(type(message)) # <class 'str'>

# 4.Boolean (bool) → True or False.

# is_active = true
# is_admin = False 
# print(type(is_active)) # <class 'bool'>

#  

# Collection Data Types
# List (list) → Ordered, changeable, allows duplicates.

# fruits = ['apple', 'banana', 'cherry'] 

# print(fruits[0]) # apple 
# fruits.append('orange') #add new item 
# print(fruits)  # 'apple', 'banana', 'cherry' 'orange'

# Tuple (tuple) → Ordered, unchangeable (immutable).

# color = ['red', 'green', 'blue']
# print(color); 
# print(color[1]) # 'green' 


# Set (set) → Unordered, unique elements.

# number = {1, 2, 3, 3, 4}
# print(number) # {1, 2, 3, 4} (duplicates removed)


# Dictionary (dict) → Key-value pairs.

# student = {'name': 'Alice', 'age': 22, 'grade': 'A'}
# print(student['name'], student['age'])


# Special Data Type
# NoneType (None) → Represents nothing or absence of value.

# x = None 
# print(type(x)) # <class "NonoeType"

# 4. Type conversion 

# x = '100'
# y = float(x)
# z = int(x)
# print(y, z) 

# 

# 5. Multiple Assignment


# a, b, c, = 10, 20, 30
# print(a, b, c) # 10 20 30 

# 

# Or same value to multiple variables:

# x = y = z = 5 

# print(x, y, z) # 5 5 5

# 

# Variable & data type

# charater_name = "john"
# charater_age = "45"
# is_male = True

# print("There once was a man named " + charater_name + ", ")
# print("he was " +  charater_age + ",  years old. ")

# charater_name = "Mike"
# print("He really liked the name " + charater_name + ", ")
# print("but didn't like being " +  charater_age + ", ")

# 

# working with String 

# print("this is \n python")  # start with new line 
# print("Hello \" World") # cotation marks // Hello " World

# 
# concatination 

# prase = "this is about python" 
# print(prase + " is to easy") 


# prase = "This is Naib & You" 
# print(prase.lower())
# print(prase.upper())


# prase = "hello world"
# print(prase.isupper()) # False
# print(prase.islower())   # True
# print(prase.upper().isupper()) # True
# print(len(prase)) # 11
# print(prase[0]) # h
# print(prase.index("w")) # index 6
# print(prase.replace("hello" , "hi")) # hi world