
# workin with number 

# a = 10 
# b = 3

# Additon 
# print("a + b = ", a + b)

# # subtraction 
# print("a - b = ", a - b)

# # multiplication 
# print("a * b = ", a * b)

# # Divition 
# print("a / b = ", a / b)

# # Floor division (no decimal, just the whole number)
# print("a // b = ", a // b)

# Reminder Module
# print("a % b", a % b)

# Exponent (power) 
# print("a ** b", a ** b)

#  Example Output: 

# a + b = 13
# a - b = 7
# a * b = 30
# a / b = 3.3333333333333335
# a // b = 3
# a % b = 1
# a ** b = 1000

# //////////////////////////////////

# from math import *

# it means “import everything from the math module” into your program

# print(2.098)

# print(3 + 4.5) #  7.5

# print(3 * 4 + 5) # 17 

# print(3 * (4 + 5)) # 27 

# print(10 % 3) # reminder 1 

# my_num = 10 
# print(my_num) # 10
# print(str(my_num)) # now return string 10

# num = -5 
# print(abs(num))  # absolute value 5

# show power which is 27 
# print(pow(3, 3)) # 27

#  show heigh number which is 6 and min show low number 

# print(max(4, 6)) # 6

# print(round(5.7)) # 6

# print(floor(4.5))  # 4

# print(ceil(3.4)) # 4

# print(sqrt(36)) # 6.0

# print(sqrt(16))      # square root → 4.0
# print(floor(3.7))    # round down → 3
# print(ceil(3.7))     # round up → 4
# print(pow(2, 3))     # 2 to the power of 3 → 8
# print(pi)            # value of π → 3.141592653589793
# print(e)             # value of e → 2.718281828459045

# 

# Getting input from user 

# name = input("Enter Your name ")
# age = input("Enter Your age")   
# print("Hello " + name + "!", "Your age is " + age )

# 

# Build a basic calculator

# num1 = (input("Enter Your first number: "))
# num2 = (input("Enter Your second number: "))

# result = int(num1) + int(num2) # with out this int python treat number as a string 

# print(result)

# 

# num1 = (input("Enter Your first number: "))
# num2 = (input("Enter Your second number: "))

# result = float(num1) + float(num2)

# print(result) # 9.4

# /////////////

# Mad libs Game 

# color = input("Enter a color: ")
# plural_noun = input("Enter a plural noun: ")
# celebrity = input("Enter a celebrity: ")

# print("Roses are " + color)
# print(plural_noun + " are blue")
# print("I love " + celebrity)

# 

# In Python, all inputs from the user using input() are strings by default, so if you want a number, you need to convert it.

# Input as an integer

# num = float(input("Enter an integer: "))
# print(num) 
# print(type(num))

# 


# number = int(input("Enter an integer: ")) 
# print(number)
# print(type(number))

# 

# using float for calculation

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number"))
# print("sum", num1 + num2)

# 
# /////////

# try → “Try to run this code.
# except → “If there’s an error, do this instead.

# try: 
#     x = int(input("Enter a number: ")) 
#     y = int(input("Enter another number: ")) 
#     result = x / y 
#     print("Result is: ", result)
# except ZeroDivisionError: 
#     print("You connot divided by zero!") 
    

#

# in this why we use try and except 

# num1 = int(input("Enter you first number: ")) 
# num2 = int(input("Enter your second number: ")) 
# result = num1 / num2 

# print("Result is: ", result) 

# 
# in this example string is not allowed

# try: 
#     number = int(input("Enter a number: ")) 
#     print(number) 
# except: 
#     print("Invalid Input") 

# try: 
#     number = int(input("Enter a number: ")) 
#     print(number, "is print") 
# except: 
#     print("Invalid input: ")


# 

# Catch all errors (not recommended for everything)


# try: 
#     # some code that might fail 
#     num = int(input("Enter a number: ")) 
#     print(10 / num)
# except: 
#     print("Something went wrong!")

# 






    
    

 









