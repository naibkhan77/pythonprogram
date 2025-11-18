
# Creating Your First Function
# In Python, we use the keyword def to define (make) a function.

# def greet():
#     print("Hello, welcome to python!")
# greet()

# 


# Functions with Parameters (Inputs)

# def greet(name): 
#     print("Hello", name)
# greet("Alice")

# 


# Functions with Return Values (Outputs)

# def add(a, b): 
#     return a + b
# result = add(5, 3)  
# print("The sum is: ", result)


# 

# Default Parameters // طے شدہ

# If you don’t give a value, Python can use a default.

# def greet(name="Feiend"):
#     print("Hello", name)
# greet("charlie")

# 

# Multiple Return Values
# A function can return more than one value (using tuples).

# def calculate(a, b): 
#     return a + b, a - b, a * b

# add, sub, mul = calculate(5, 2) 
# print("sum: ", add)
# print("difference: ", sub)
# print("Product: ", mul)


# 

# Keyword Arguments
# You can pass values using the parameter name (order doesn’t matter).
# f-string (formatted string) / in js we use ( `` ) this sine

# def introduce(name, age): 
#     print(f"my name is {name} and I am {age} year old. ")
# introduce(age=20, name="Alice")  


# def sayhi(name, age):
#     print("Hello " + name + ", Your are is " + str(age) + ", Year old ")
# sayhi("naib", 24)

# 

# //////////////////////////////////

# Exponent Function 
# An exponent means “raise a number to the power of another number.”

# print(2**3)

# print(pow(2, 3))

# 

# base = 4
# power = 2 
# result = base ** power 
# print(result) 


# 

#  Simple exponent function

# def raise_to_power(base, power): 
#     return base ** power 

# print(raise_to_power(2, 3)) 

# 

# Manual exponent using a loop


# def raise_to_power(base_num, pow_num): 
#     result = 1 
#     for index in range(pow_num): # this loop runs 4 times bc power is 4
#         result *= base_num 
#     return result 
# print(raise_to_power(3, 4))


# 

# 2D lis
# A 2D list is basically a list of lists. It’s like a table with rows and columns.

# number_grid = [
    
#     [1, 2, 3], 
#     [4, 5, 6], 
#     [7, 8, 9], 
#     [0]
# ]

# print(number_grid[0][0]) # output 1 
# print(number_grid[1][2]) # output 6

# 

# number_grid = [
    
#     [1, 2, 3], 
#     [4, 5, 6], 
#     [7, 8, 9], 
#     [0]
# ]

# for row in number_grid: 
#     for col in row: 
#         print(col)


# 



















